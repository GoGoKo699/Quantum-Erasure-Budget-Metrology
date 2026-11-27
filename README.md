# Quantum Erasure Budget Metrology

**How much phase information survives the loss of any $`t`$ out of $`N`$ sensors?** A probe that superposes symmetric states of different excitation numbers reaches the exact local precision limit. A protected register stores only the excitation number modulo $`t+1`$. The receiver uses it to infer the erased excitation count without measuring the survivor count itself, then measures the surviving phase coherence.

For one parallel exposure to a common unknown phase, with erased positions announced, the optimal worst-pattern quantum Fisher information is

```math
F^*(N,t)=\frac{N^2}{\bigl(1+\sqrt{t(N-1)/(N-t)}\bigr)^2},
\qquad 1\le t\lt N.
```

For **30 sensors and three erasures**, the protocol with a four-level protected register achieves **115.20**. Independent Ramsey probes with 27 survivors achieve **27** under the same phase convention.

| Setting | Result |
| --- | --- |
| A fixed number of losses | One explicit preparation and readout attain the formula for every set of erased sites. |
| A known distribution of loss counts | One beta-binomial probe family is optimal. The best input is found by maximizing a concave function of the input charge variance. |
| No protected memory | A single erasure allows exact attainment for every array size. For any fixed loss count, separated excitation numbers attain the optimum at sufficiently large array size. |
| A fixed number of survivors | If at least two sensors survive, exact attainment requires a protected register whose dimension grows linearly with the initial sensor count. |
| Three sensors with independent erasures | At loss probability one half, one protected qubit is necessary and sufficient to attain the optimal QFI, approximately 1.77492. |

## Read the science

- [Model](science/model.md) defines the parallel phase exposure, location flag and local estimation criterion.
- [Optimal probe and readout](science/optimal-probe.md) connects a classical minimax sampling bound to a coherent receiver that attains it.
- [Random loss counts](science/loss-distributions.md) treats a known count distribution, including equal-rate independent erasures.
- [Protected memory](science/memory.md) gives a finite dimension bound and shows how an optimal measurement can work even when erasure sectors overlap.
- [Related work](references/RELATED_WORK.md) identifies the inherited statistical rule, the earlier optical bound and erasure-tolerant probe constructions.

## Learn the project

The learning route uses **John Watrous, *The Theory of Quantum Information* (2018)**. The [bridge](learning/WATROUS_BRIDGE.md) connects its treatment of states, measurements and channels to the sensing model. The [30 milestones](learning/MILESTONES.md) follow the argument from partial trace to the exact finite loss law. The [four-sensor example](learning/WORKED_EXAMPLE.md) works through preparation, erasure and a receiver with no protected register. The [reading guide](llms.txt) maps individual questions to proof locations.

## Reproduce the finite checks

From the repository root, run

```bash
python -m pip install -r verification/requirements.txt
python verification/run_all.py
```

The [verification guide](verification/README.md) records the test ranges, outputs and limits.

## Scope

The bound is for local estimation around a chosen nominal phase. It uses one exposure per sensor, a phase-independent erasure pattern, and ideal joint preparation and readout. For losses at arbitrary known positions, neither the content of the erased qubits nor a measurement of their environment is available.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

