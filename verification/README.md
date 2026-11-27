# Finite verification

Run the checks from the repository root with Python 3.11 or newer.

```bash
python -m pip install -r verification/requirements.txt
python verification/run_all.py
```

The verifier constructs the probe in the computational basis, traces out the indicated sensors and evaluates mixed-state QFI from the eigensystem of the actual output density matrix. A separate Dicke-basis calculation checks the random-count mixture and the untagged quadrature construction at larger sizes.

| Check | Range and expected result |
| --- | --- |
| Tagged probes | 62 physical partial traces for sensor counts 2 through 7, covering each nontrivial loss count and representative positions. The spectral QFI agrees with the fixed-count formula. |
| Independent loss | 27 combinations of array size and erasure rate. Optimizing the common variance and taking the weighted spectral QFI agrees with the random-count formula. |
| Constant-risk estimator | 29,326 population total, sample size and array size combinations. The risk is constant over all possible total charges at each size and count. |
| Untagged moment-matched probes | 180 sensors and loss counts 1 through 5. The rounded quadrature nodes remain separated, the fitted weights are positive, and the QFI matches the exact optimum. |
| Three-sensor memory examples | The dense untagged state gives QFI 2.25 for each single erasure. A probe with one protected qubit gives 1.774923787870 after averaging independent erasures of probability one half. |

The finite checks test the prepared states and formulas. General optimality follows from the [fixed-count proof](../science/optimal-probe.md), [random-count proof](../science/loss-distributions.md) and [memory converse](../science/memory.md).

