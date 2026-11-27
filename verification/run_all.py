from itertools import combinations
from math import comb

import numpy as np
from scipy.linalg import eigh
from scipy.optimize import minimize_scalar
from scipy.special import roots_jacobi
from scipy.stats import betabinom, binom, hypergeom


def r_value(n, t):
    return t * (n - 1) / (n - t)


def fixed_loss_optimum(n, t):
    return (n / (1 + np.sqrt(r_value(n, t)))) ** 2


def curve(n, t, v):
    if t == 0:
        return v
    if t == n:
        return 0.0
    return v * (1 - v) / (1 + (r_value(n, t) - 1) * v)


def weight_probabilities(n, v):
    w = np.arange(n + 1)
    if abs(v - 1 / n) < 1e-14:
        return binom.pmf(w, n, 0.5)
    if abs(v - 1) < 1e-14:
        q = np.zeros(n + 1)
        q[[0, n]] = 0.5
        return q
    a = n * (1 - v) / (2 * (n * v - 1))
    return betabinom.pmf(w, n, a, a)


def full_probe(n, q, tag_size):
    probe = np.zeros((2,) * n + (tag_size,))
    for basis in np.ndindex((2,) * n):
        w = sum(basis)
        probe[basis + (w % tag_size,)] = np.sqrt(q[w] / comb(n, w))
    return probe


def spectral_qfi(probe, erased):
    n = probe.ndim - 1
    retained = tuple(i for i in range(n) if i not in erased)
    size = probe.shape[-1]
    amplitude = probe.transpose(erased + retained + (n,)).reshape(
        2 ** len(erased), 2 ** len(retained) * size
    )
    rho = amplitude.T @ amplitude
    charges = np.repeat([i.bit_count() for i in range(2 ** len(retained))], size)
    eigenvalues, eigenvectors = eigh(rho)
    generator = eigenvectors.T @ (charges[:, None] * eigenvectors)
    total = eigenvalues[:, None] + eigenvalues[None, :]
    difference = eigenvalues[:, None] - eigenvalues[None, :]
    ratio = np.divide(difference**2, total, out=np.zeros_like(total), where=total > 1e-12)
    return 2 * np.sum(ratio * abs(generator)**2)


def dicke_qfi(q, t, tag_size):
    n = len(q) - 1
    m = n - t
    amplitude = np.zeros((t + 1, (m + 1) * tag_size))
    for k in range(t + 1):
        for j in range(m + 1):
            w = k + j
            probability = q[w] * comb(t, k) * comb(m, j) / comb(n, w)
            amplitude[k, j * tag_size + w % tag_size] = np.sqrt(probability)
    rho = amplitude.T @ amplitude
    charges = np.repeat(np.arange(m + 1), tag_size)
    eig, vec = eigh(rho)
    g = vec.T @ (charges[:, None] * vec)
    total = eig[:, None] + eig[None, :]
    diff = eig[:, None] - eig[None, :]
    ratio = np.divide(diff**2, total, out=np.zeros_like(total), where=total > 1e-12)
    return 2 * np.sum(ratio * abs(g)**2)


worst_rel = 0
fixed_cases = 0
for n in range(2, 8):
    for t in range(1, n):
        v = 1 / (1 + np.sqrt(r_value(n, t)))
        probe = full_probe(n, weight_probabilities(n, v), t + 1)
        expected = fixed_loss_optimum(n, t)
        cases = list(combinations(range(n), t))
        for erased in {cases[0], cases[-1], cases[len(cases) // 2]}:
            observed = spectral_qfi(probe, erased)
            worst_rel = max(worst_rel, abs(observed / expected - 1))
            np.testing.assert_allclose(observed, expected, rtol=2e-10, atol=2e-10)
            fixed_cases += 1

mixture_cases = 0
for n in range(2, 11):
    for erasure_rate in (0.08, 0.35, 0.8):
        probs = binom.pmf(np.arange(n + 1), n, erasure_rate)
        obj = lambda v: sum(probs[t] * curve(n, t, v) for t in range(n + 1))
        opt = minimize_scalar(lambda v: -obj(v), bounds=(1 / n, 1), method="bounded")
        v = max((1 / n, opt.x, 1), key=obj)
        q = weight_probabilities(n, v)
        observed = sum(probs[t] * dicke_qfi(q, t, n) for t in range(n + 1))
        expected = n**2 * obj(v)
        np.testing.assert_allclose(observed, expected, rtol=2e-10, atol=2e-10)
        mixture_cases += 1

risk_cases = 0
for n in range(2, 45):
    for t in range(1, n):
        gamma = np.sqrt(t * (n - t) / (n - 1))
        sample = np.arange(t + 1)
        delta = n / 2 + n / (t + gamma) * (sample - t / 2)
        totals = np.arange(n + 1)[:, None]
        laws = hypergeom.pmf(sample, n, totals, t)
        risk = np.sum(laws * (delta - totals)**2, axis=1)
        np.testing.assert_allclose(risk, fixed_loss_optimum(n, t) / 4, rtol=2e-12)
        risk_cases += n + 1

quadrature_results = []
for t in range(1, 6):
    n = 180
    a_limit = np.sqrt(t) / 2
    nodes, _ = roots_jacobi(t + 2, a_limit - 1, a_limit - 1)
    supports = np.rint(n * (nodes + 1) / 2).astype(int)
    assert np.all(np.diff(supports) > t)
    v = 1 / (1 + np.sqrt(r_value(n, t)))
    full_q = weight_probabilities(n, v)
    moment_matrix = np.vander(np.arange(n + 1) / n, N=t + 2, increasing=True).T
    q = np.zeros(n + 1)
    weights = np.linalg.solve(moment_matrix[:, supports], moment_matrix @ full_q)
    assert np.all(weights > 0)
    q[supports] = weights
    observed = dicke_qfi(q, t, 1)
    expected = fixed_loss_optimum(n, t)
    np.testing.assert_allclose(observed, expected, rtol=2e-10, atol=2e-10)
    quadrature_results.append([t, supports.tolist(), float(min(weights))])

three_qubit_probe = full_probe(3, np.array([7, 9, 9, 7]) / 32, 1)
for site in range(3):
    np.testing.assert_allclose(spectral_qfi(three_qubit_probe, (site,)), 9 / 4)

count_probabilities = np.array([1, 3, 3, 1]) / 8


def three_sensor_objective(v):
    return sum(count_probabilities[t] * curve(3, t, v) for t in range(4))


opt = minimize_scalar(
    lambda v: -three_sensor_objective(v),
    bounds=(1 / 3, 1),
    method="bounded",
    options={"xatol": 1e-13},
)
assert opt.success
tagged_probe = full_probe(3, weight_probabilities(3, opt.x), 2)
iid_information = 0.0
for t in range(4):
    erased_sets = list(combinations(range(3), t))
    branch_values = [spectral_qfi(tagged_probe, erased) for erased in erased_sets]
    expected = 9 * curve(3, t, opt.x)
    np.testing.assert_allclose(branch_values, expected, rtol=2e-10, atol=2e-10)
    iid_information += count_probabilities[t] * np.mean(branch_values)
np.testing.assert_allclose(iid_information, 1.7749237878695032, rtol=2e-10)

print(f"Tagged physical reductions: {fixed_cases}, max relative error {worst_rel:.3g}")
print(f"Independent erasure model cases: {mixture_cases}")
print(f"Finite-population risk checks: {risk_cases}")
print(f"Ancilla-free N=180 checks [t, weight supports, min probability]: {quadrature_results}")
print(f"Three sensors: untagged one-erasure QFI 2.25; independent erasures with a protected qubit {iid_information:.12f}")

