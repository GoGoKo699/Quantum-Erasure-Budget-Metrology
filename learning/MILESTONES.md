# Understanding map

The first 12 milestones connect state, channel, measurement and sampling concepts to the fixed-loss sensing model. The remaining 18 follow the converse through a matching probe, receiver and exact resource statements. Section numbers refer to the [Watrous bridge](WATROUS_BRIDGE.md).

## Background and preliminaries

| ID | Central question | Understanding target and connection | Dependencies | Source |
| --- | --- | --- | --- | --- |
| M01 | What physically acquires the unknown phase? | Identify the parallel exposure and explain why a one-qubit computational value sets its phase contribution. | — | [Model](../science/model.md) |
| M02 | How does the same phase accumulate on a multi-qubit string? | Use total excitation number as the generator eigenvalue and connect differences in weights to relative phase. | M01 | [Model](../science/model.md) |
| M03 | Which part of a superposition carries the signal? | Relate coherent amplitudes at different weights to a phase-dependent interference measurement. | M02 | [Example](WORKED_EXAMPLE.md) |
| M04 | How do we split the array into registers? | Form the tensor factors for erased sites, survivors and a possible reference. | M01 | Watrous §2.1.2 |
| M05 | What state is available after a site is erased? | Use partial trace to express the loss channel and interpret each conditional vector in an erased-basis expansion. | M03, M04 | Watrous §§2.1.3, 2.2.1–2.2.2 |
| M06 | How can a pure reference represent mixed input preparations? | Use purification to enlarge the comparison class for an upper bound on attainable information. | M04, M05 | Watrous §2.1.3 |
| M07 | How does a coarse projective measurement act on coherence? | Identify which amplitudes stay coherent under projection onto a sector; connect this to counting only parity. | M03, M05 | Watrous §§2.3.1–2.3.2; [Example](WORKED_EXAMPLE.md) |
| M08 | What sensitivity does one local measurement deliver? | Obtain local classical Fisher information from probabilities and their derivatives at the nominal phase. | M01, M07 | [Bridge](WATROUS_BRIDGE.md); [Example](WORKED_EXAMPLE.md) |
| M09 | Why does a pure phase branch have information four times a variance? | Resolve the tangent into its parallel and perpendicular parts and connect the perpendicular part to a two-direction readout. | M02, M08 | [Optimal probe](../science/optimal-probe.md) |
| M10 | How does permutation symmetry simplify the state? | Group computational amplitudes into normalized Dicke vectors and see why any loss set of a given size gives equivalent output statistics. | M02, M04 | Watrous §7.1.1; [Example](WORKED_EXAMPLE.md) |
| M11 | What can a random sample of erased sites reveal about weight? | Identify the hypergeometric law of the lost count at a fixed total and relate posterior squared error to conditional variance. | M02, M05 | Watrous §1.2.2; [Optimal probe](../science/optimal-probe.md) |
| M12 | What is the fixed-budget sensing objective? | Combine a fixed loss count, a known location flag, an unobserved lost input, all allowed readouts and the worst-pattern local objective. | M05, M06, M08, M11 | [Model](../science/model.md) |

## Narrative and innovation

| ID | Central question | Understanding target and connection | Dependencies | Source |
| --- | --- | --- | --- | --- |
| M13 | What extra record simplifies the converse? | Reveal the erased basis string in a mathematical refinement and use measurement simulation to compare it with the physical experiment. | M05, M06, M12 | [Optimal probe](../science/optimal-probe.md) |
| M14 | Why is there no information in the branch probabilities? | Use diagonality of phase encoding to identify phase-independent branch probabilities and additive information across branches. | M02, M09, M13 | [Optimal probe](../science/optimal-probe.md) |
| M15 | How does a worst pattern yield a sampling problem? | Average over uniformly chosen size-$`t`$ sets for an upper bound and express each refined contribution as a conditional variance of total weight. | M11–M14 | [Optimal probe](../science/optimal-probe.md) |
| M16 | What does an affine estimator trade against sampling noise? | Shrink the expanded sample count towards half the array and compare its squared bias with its sampling variance. | M11, M15 | [Optimal probe](../science/optimal-probe.md) |
| M17 | How does the estimator give an all-probe upper bound? | Balance the two errors to make squared risk constant across input weights and use the optimality of the posterior mean. | M15, M16 | [Optimal probe](../science/optimal-probe.md) |
| M18 | Which weight law has the needed posterior mean? | Form the symmetric beta-binomial input weight law and reason from its updated parameters to the posterior mean. | M11, M16 | [Optimal probe](../science/optimal-probe.md) |
| M19 | Why is a matching weight law alone insufficient? | Use the Dicke decomposition to see that different loss counts can share survivor basis states. Connect that overlap to the inaccessible record in M13. | M10, M13, M18 | [Optimal probe](../science/optimal-probe.md) |
| M20 | What should a protected quantum register remember? | Design a coherent residue of the total weight whose dimension depends on the loss count bound. Relate its readout to interference within a branch. | M07, M18, M19 | [Optimal probe](../science/optimal-probe.md) |
| M21 | How can the receiver read the lost count? | Compute the difference of the register label and surviving count modulo the register dimension, and explain why each possible loss count has a unique syndrome. | M07, M20 | [Optimal probe](../science/optimal-probe.md) |
| M22 | Which second measurement extracts the phase? | Apply the pure-state tangent readout after the syndrome, including zero-variance sectors and the weight of each outcome. | M09, M14, M21 | [Optimal probe](../science/optimal-probe.md) |
| M23 | What makes the finite guarantee sharp on each pattern? | Match posterior means and the constant-risk bound, and use symmetry for attainment independent of locations. | M10, M17, M18, M22 | [Optimal probe](../science/optimal-probe.md) |
| M24 | How can a probe distinguish branches without a protected register? | Relate spacing between occupied weights to disjoint survivor count supports, with one erased qubit as the concrete example. | M07, M19, M23 | [Example](WORKED_EXAMPLE.md); [Memory](../science/memory.md) |
| M25 | Which moments suffice for fixed-budget memory removal? | Use the degree of the hypergeometric likelihood to identify the moments that preserve posterior risk, and the spaced quadrature construction that matches them at large size. | M11, M18, M24 | [Optimal probe](../science/optimal-probe.md#removing-the-protected-register-at-fixed-loss-count) |
| M26 | What changes when the loss count itself is random? | Average the flagged Fisher information over a parameter-independent count law and distinguish one common preparation from one preparation per count. | M12, M14, M23 | [Loss distributions](../science/loss-distributions.md) |
| M27 | Why can one probe family handle every count? | Constrain the total-weight variance, bound each count using affine regression, and use simultaneous beta-binomial attainment to reduce preparation choice to one scalar. | M16, M18, M21, M26 | [Loss distributions](../science/loss-distributions.md) |
| M28 | When does loss change the scaling of precision? | Read fixed, growing and extensive loss regimes from the finite law and compare with independent Ramsey probes under the same phase generator. | M23 | [Model](../science/model.md); [Optimal probe](../science/optimal-probe.md) |
| M29 | When is protected memory required? | Connect the common SLD to the surviving Hilbert-space dimension. Explain why three independently erased sensors can require a protected qubit even though every single-erasure pattern alone can be handled without one. | M20–M27 | [Memory](../science/memory.md) |
| M30 | What complete capability does the theorem give? | Reconstruct the worst-pattern converse, matching physical readout, random-count extension and locality of the phase criterion. Place the result relative to known erasure-metrology and sampling arguments. | M12, M23, M27–M29 | [Overview](../README.md); [Related work](../references/RELATED_WORK.md) |

