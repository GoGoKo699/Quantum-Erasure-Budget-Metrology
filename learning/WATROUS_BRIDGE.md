# From quantum channels to an erasure-tolerant phase measurement

One qubit disappears from a four-sensor array after all four have sensed the same phase. The receiver knows which qubit disappeared. A joint measurement on the three survivors can still attain local Fisher information four. The [worked example](WORKED_EXAMPLE.md) shows the state, the surviving measurement and the sensitivity in this case.

## Educational anchor

John Watrous, *The Theory of Quantum Information*, Cambridge University Press, 2018. The author's standard-layout manuscript gives the chapter and section numbering below. [Book and manuscript](https://cs.uwaterloo.ca/~watrous/TQI/)

| Read | Use in this project |
| --- | --- |
| §1.2.2, probability theory | Expectations and the law of a pair of random variables. The project develops the sampling and conditional-variance calculation. [Chapter 1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf) |
| §§2.1.2–2.1.3, quantum states, reductions and purifications | Write the sensor–reference state, expand it across the lost and retained registers, and trace out the lost register. Purification explains the reference allowed in the converse. [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) |
| §§2.2.1–2.2.2, channels and their representations | View phase encoding and discard as channels. Use the discarded register to express erasure as a sum of conditional branches. [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) |
| §§2.3.1–2.3.2, measurements and their probabilities | Convert output states to classical outcome probabilities with the Born rule. A projective measurement of a syndrome can preserve coherence within its eigenspace. [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) |
| §7.1.1, the subspace of permutation-invariant vectors | Build its qubit basis by normalizing sums of equal-weight computational strings. A Dicke basis vector is the qubit case of this symmetrization. [Chapter 7](https://cs.uwaterloo.ca/~watrous/TQI/TQI.7.pdf) |

## Translate the registers

| Object | Role |
| --- | --- |
| $`A`$ and $`A^c`$ | The erased and surviving site sets. The position flag identifies $`A`$. Taking the partial trace over $`A`$ gives the physical state for that flag. |
| $`G=\sum_i\lvert1\rangle\langle1\rvert_i`$ | The phase generator on the sensors. Its eigenvalue is the integer excitation count, also called Hamming weight. |
| $`W`$ and $`K`$ | The total excitation count and the count on $`A`$, as classical variables induced by measuring the input basis. The receiver can infer $`K`$ with the proposed measurement. |
| $`\lvert D_w^N\rangle`$ | The unit vector proportional to the sum of all $`N`$-qubit strings with weight $`w`$. |
| $`C`$ | An optional protected register that carries the input count modulo $`t+1`$ coherently. It has no phase coupling and survives erasure. |

## Follow the proof from the anchor

1. Apply Watrous's reduction rule to a pure sensor–reference state. Expanding in a basis of the erased sites gives a mixture of pure conditional survivors. For the upper bound, supply the missing basis outcome as a classical register. Forgetting that register recovers the physical experiment.
2. Turn the best local measurement into a variance calculation. A normalized pure branch evolving under $`G`$ has a tangent perpendicular to the state proportional to $`-i(G-\langle G\rangle)\lvert\psi\rangle`$. Measuring superpositions of the state and its normalized tangent attains four times the variance of $`G`$. The QFI rule and the local measurement follow from the pure-state calculation in §III, Eqs. (15)–(17). [Demkowicz-Dobrzański et al.](https://arxiv.org/abs/0904.0456)
3. Average over $`t`$-site erasure patterns. For an input string of fixed weight $`w`$, the lost count has a hypergeometric law. A bounded-loss converse follows by estimating $`w`$ with a single affine estimator that has the same squared risk for every $`w`$.
4. Use the qubit symmetric basis from §7.1.1 to choose amplitudes whose weight law is beta-binomial. Its posterior mean equals the affine estimator. Then realize access to the lost count by measuring the difference between the protected residue and the surviving count modulo $`t+1`$. This measurement separates the pure branches while retaining coherence within each branch.
5. For fixed $`t`$, support the state on separated weights and choose amplitudes by moment matching. The surviving count supports then distinguish the branches directly. The distributional proof and its memory conditions are part of the project's scientific account.

The [model](../science/model.md) fixes the single-exposure protocol, the position flag and the local objective. The [optimal probe](../science/optimal-probe.md) supplies the finite bound and its attaining measurement. The [milestone map](MILESTONES.md) follows these dependencies in order.

