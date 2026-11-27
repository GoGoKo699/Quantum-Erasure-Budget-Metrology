# Four sensors with one known erasure

All four qubits acquire the same phase $`\theta`$, with each $`\lvert1\rangle`$ contributing a factor $`e^{-i\theta}`$. Exactly one qubit is erased. The preparation below works for every location. The measurement is designed around a chosen nominal phase $`\theta_0`$.

## Prepare and expose the probe

Let $`\lvert D_w^n\rangle`$ be the uniform unit vector over $`n`$-bit strings with $`w`$ ones. Prepare

```math
\lvert\psi\rangle=
\tfrac12\lvert D^4_0\rangle+
\tfrac1{\sqrt2}\lvert D^4_2\rangle+
\tfrac12\lvert D^4_4\rangle.
```

For instance, $`\lvert D^4_2\rangle`$ has six terms. For any one selected qubit, three terms have that qubit in $`\lvert0\rangle`$ and the other three in $`\lvert1\rangle`$. Thus its expansion across the erased site and the rest is

```math
\lvert D^4_2\rangle=
\tfrac1{\sqrt2}\bigl(
\lvert0\rangle\lvert D^3_2\rangle+
\lvert1\rangle\lvert D^3_1\rangle
\bigr).
```

The sensor generator is diagonal in this basis, so the three terms of the prepared state acquire phases $`1,e^{-2i\theta},e^{-4i\theta}`$.

## Measure survivor parity

Tracing out the erased qubit gives two equally weighted pure branches. Each is supported on one parity of the surviving excitation count. In the odd branch we have dropped a phase common to both terms.

| Measured parity | Conditional survivor state |
| --- | --- |
| Even | $`(\lvert D^3_0\rangle+e^{-2i\theta}\lvert D^3_2\rangle)/\sqrt2`$ |
| Odd | $`(\lvert D^3_1\rangle+e^{-2i\theta}\lvert D^3_3\rangle)/\sqrt2`$ |

The parity outcome thus identifies the lost excitation count. The measurement resolves even versus odd and preserves the coherence between the two weights within the corresponding sector. Measuring the full surviving count would separate the two terms.

## Read the relative phase

Call the lower and higher weight states in the observed branch $`\lvert L\rangle`$ and $`\lvert H\rangle`$. Use the two measurement directions

```math
\lvert m_\pm\rangle
=\frac{\lvert L\rangle\pm i e^{-2i\theta_0}\lvert H\rangle}{\sqrt2}.
```

The probabilities are $`p_\pm(\theta)=[1\mp\sin(2(\theta-\theta_0))]/2`$. At $`\theta=\theta_0`$ they are both $`1/2`$ and their derivatives are $`-1`$ and $`+1`$. Consequently the conditional Fisher information is

```math
\sum_{\pm}\frac{[p_\pm'(\theta_0)]^2}{p_\pm(\theta_0)}=4.
```

Both parity outcomes are retained and their probabilities are phase independent, so the total Fisher information is also four. The four sensors undergo one exposure each. The measurement uses the three survivors jointly and requires no register protected during sensing. Three independent Ramsey survivors have local Fisher information three with the same per-qubit phase generator.

## Check the ceiling by counting

In the universal bound, grant the receiver the value $`K\in\{0,1\}`$ of the lost computational-basis bit, and average uniformly over the four possible lost sites. For an input string with weight $`W=w`$, the chance of $`K=1`$ is $`w/4`$. The estimator $`1+2K`$ of $`W`$ has squared risk one for every $`w`$. Therefore the optimal posterior squared risk can be at most one. Four times that risk bounds the Fisher information after loss, which gives four.

For this particular probe, condition on $`K=0`$ to obtain equal weights at $`W=0,2`$. Condition on $`K=1`$ to obtain equal weights at $`W=2,4`$. Their posterior means equal $`1+2K`$ and their variances are both one. The survivor-parity measurement realizes the same conditioning in the physical experiment. The [general proof and construction](../science/optimal-probe.md) extend this reasoning to larger erasure budgets.

