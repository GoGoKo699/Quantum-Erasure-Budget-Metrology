# Optimal probes for a fixed erasure budget

Each of $`N`$ qubits acquires the phase $`|1\rangle\mapsto e^{-i\theta}|1\rangle`$ once, and the receiver learns the positions of any $`t`$ erased qubits. The receiver may jointly measure the survivors and a protected, signal-free register. The [model](model.md) specifies the timing and local estimation criterion. For $`1\le t\lt N`$, the optimal worst-pattern Fisher information is

```math
F^*_{N,t}=\frac{N^2}{(1+u_t)^2},\qquad
u_t=\sqrt{\frac{t(N-1)}{N-t}}.
```

A register with $`t+1`$ levels suffices. The converse permits a protected register of arbitrary size. For $`t=0`$, the two extreme charge states give $`F^*_{N,0}=N^2`$. For $`t=N`$, the phase is absent from the receiver's reduced state, so $`F^*_{N,N}=0`$.

## Converse

Purify an arbitrary input, retaining the purifying system as protected memory for an upper bound if necessary. For a fixed erased set $`A`$, expand the probe in the computational basis on $`A`$. Giving the receiver a classical copy of this basis string $`X_A`$ can only increase its quantum Fisher information. Each conditional state is pure. The generating charge on the survivors has the conditional law of $`W-|X_A|`$, where $`W`$ is the total excitation number in a computational-basis sample from the input. The probability of each branch is phase independent. The enlarged output therefore has QFI $`4\mathbb E[\operatorname{Var}(W\mid X_A,A)\mid A]`$.

The minimum over sets $`A`$ is bounded above by the mean over a uniform independent choice of $`A`$. Write $`K=|X_A|`$. Given $`W=w`$, the sampled count $`K`$ is hypergeometric. In particular, $`Y=NK/t`$ has conditional mean $`w`$ and variance $`w(N-w)/u_t^2`$. The estimator

```math
\delta(K)=\frac N2+\frac{u_t}{1+u_t}\left(\frac{NK}{t}-\frac N2\right)
```

has conditional squared error $`[w(N-w)+(w-N/2)^2]/(1+u_t)^2=N^2/[4(1+u_t)^2]`$ at every $`w`$. The conditional mean given $`(A,X_A)`$ minimizes squared error and can use this estimator. The upper bound follows without assuming any symmetry of the input. The estimator acts on a fictitious record in the converse. In the physical protocol the receiver obtains only the erasure locations and measures a collective syndrome on registers it holds.

## Probe and receiver

Let $`|D_w^N\rangle`$ denote the normalized symmetric state at charge $`w`$. For $`t\lt N-1`$, set

```math
\beta=\frac{Nu_t}{N-1-u_t},\qquad a=\frac\beta2,\qquad
q_w=\binom Nw\frac{\mathrm B(w+a,N-w+a)}{\mathrm B(a,a)}.
```

Use $`q_w=2^{-N}\binom Nw`$ when $`t=N-1`$, the $`a\to\infty`$ limit. Prepare

```math
|\Psi\rangle=\sum_{w=0}^N\sqrt{q_w}\,|D_w^N\rangle|w\bmod(t+1)\rangle_C.
```

The basis register $`C`$ stays coherent throughout the phase encoding. For any $`t`$ erased positions, the Dicke decomposition across the cut gives the erased-charge likelihood

```math
h_t(k\mid w)=\frac{\binom wk\binom{N-w}{t-k}}{\binom Nt}.
```

After tracing those positions, the joint state is a mixture of subnormalized vectors

```math
|\phi_k(\theta)\rangle
=\sum_{w=0}^N\sqrt{q_w h_t(k\mid w)}\,e^{-i\theta(w-k)}
   |D_{w-k}^{N-t}\rangle|w\bmod(t+1)\rangle_C,
\qquad k=0,\ldots,t,
```

with infeasible terms omitted. The phase $`e^{-i\theta k}`$ is common within each branch and has no observable effect. If $`J`$ is the surviving charge operator, the spectral projectors of $`(C-J)\bmod(t+1)`$ distinguish the branches for all phases. Here $`C`$ in the subtraction denotes the integer-valued register observable. A reversible modular subtraction into a measurement register implements this projective measurement without learning $`J`$ itself.

The distribution $`q`$ arises by drawing $`P\sim\mathrm{Beta}(a,a)`$ and then drawing $`N`$ independent bits conditionally on $`P`$. Consequently,

```math
\mathbb E[W\mid K=k]=k+(N-t)\frac{a+k}{2a+t}=\delta(k).
```

The last equality holds because both affine functions send $`t/2`$ to $`N/2`$ and have slope $`Nu_t/[t(1+u_t)]`$. For $`t=N-1`$ the posterior mean is $`k+1/2`$. Each branch contributes the pure-state information $`4\operatorname{Var}(W\mid K=k)`$, and the probability-weighted sum equals the bound. Permutation invariance gives this same performance for every erased set. The same probe guarantees at least this much information for every pattern of at most $`t`$ erasures, because the receiver with fewer erasures can discard additional qubits to reach $`t`$.

To attain the QFI locally, work at a chosen reference phase $`\theta_0`$. In a detected branch let $`|\psi\rangle`$ be its normalized state at $`\theta_0`$, and let $`|d\rangle=(J-\langle J\rangle)|\psi\rangle/\sqrt{\operatorname{Var}J}`$ if the variance is positive. Project onto $`(|\psi\rangle\pm i|d\rangle)/\sqrt 2`$ and their orthogonal complement. At $`\theta_0`$ the two probabilities are $`1/2`$ with slopes of magnitude $`\sqrt{\operatorname{Var}J}`$, giving Fisher information $`4\operatorname{Var}J`$. A zero-variance branch requires only a constant outcome. The bound concerns local estimation in this reference frame.

## Removing the protected register at fixed loss count

For $`t=1`$ and even $`N\ge4`$, use the known three-charge symmetric probe with probabilities $`(1/4,1/2,1/4)`$ on $`(0,N/2,N)`$. The two erased-charge branches have disjoint surviving weight supports. The prior is centered and has variance $`N^2/8`$, which fixes both components of the affine posterior mean for binary $`K`$ and gives the exact optimum $`N^2/4`$. For odd $`N\ge5`$ the same result follows by taking $`c=\lfloor N/2\rfloor`$, the charges $`(0,c,N)`$, and probabilities

```math
q_0=\frac{4c-N}{8c},\qquad q_c=\frac{N^2}{8c(N-c)},\qquad
q_N=\frac{3N-4c}{8(N-c)}.
```

For every fixed $`t\ge1`$, the protected register can be removed for all sufficiently large $`N`$. Let $`W_N`$ have the exact beta-binomial distribution above. As $`N\to\infty`$ with $`t`$ fixed, the moments of $`W_N/N`$ converge to those of $`\mathrm{Beta}(\sqrt t/2,\sqrt t/2)`$. This follows by conditioning on $`P`$: the $`N`$ independent bits give conditional variance at most $`1/(4N)`$ for their mean, and $`2a\to\sqrt t`$.

Choose $`t+2`$ distinct interior Gaussian quadrature nodes $`x_j`$ and their positive weights for this limiting beta distribution. Round $`Nx_j`$ to integers $`w_j`$. For sufficiently large $`N`$ the rounded weights are separated by at least $`t+1`$. Solve the square Vandermonde system for probabilities $`p_j`$,

```math
\sum_{j=1}^{t+2}p_j(w_j/N)^\ell=\mathbb E[(W_N/N)^\ell],
\qquad \ell=0,\ldots,t+1.
```

The solutions tend to the positive quadrature weights by continuity of the inverse Vandermonde matrix. The likelihood $`h_t(k\mid w)`$ is a polynomial in $`w`$ of degree at most $`t`$, and $`w h_t(k\mid w)`$ has degree at most $`t+1`$. Moment matching therefore preserves the branch probabilities, posterior means and unconditional second moment. It preserves the same optimal mean conditional variance.

Prepare $`\sum_j\sqrt{p_j}|D_{w_j}^N\rangle`$. For each allowed probe charge $`w_j`$, the possible survivor charges lie in $`[w_j-t,w_j]`$. These intervals are disjoint, and within an interval the survivor charge identifies $`k=w_j-J`$. The receiver measures the projectors onto the unions of survivor weight spaces belonging to the same $`k`$. Every branch remains coherent across different $`w_j`$, and the same two-outcome local measurement within each branch attains the bound.

## Scaling with the erasure budget

For fixed $`t`$ and growing $`N`$, the loss retains a fraction $`(1+\sqrt t)^{-2}`$ of the ideal $`N^2`$ information. If $`1\ll t\ll N`$, the optimal QFI is asymptotic to $`N^2/t`$. At a fixed loss fraction $`t/N\to\alpha\in(0,1)`$, it is asymptotic to $`N(1-\alpha)/\alpha`$.

Independent Ramsey probes give $`N-t`$ information for every pattern. At a fixed loss fraction the ratio of the two precisions in QFI units tends to $`1/\alpha`$. With a fixed number of survivors, that ratio tends to one even though the [protected memory needed for exact equality](memory.md#why-exact-attainment-consumes-memory) grows with the array size.

## Preparation and readout resources

An explicit state preparation loads the charge amplitudes into a binary count register of $`\lceil\log_2(N+1)\rceil`$ qubits and computes the protected modular label when used. To expand a count into symmetric qubits, at a step with $`m`$ unprepared qubits and $`j`$ excitations remaining, append $`\sqrt{(m-j)/m}|0\rangle+\sqrt{j/m}|1\rangle`$ controlled on $`j`$, then subtract the appended bit from the count. Induction gives the uniform Dicke amplitudes at a fixed initial charge, and the count returns to zero. This direct construction uses $`O(N^2)`$ count-selective rotations, reversible arithmetic, and $`\lceil\log_2(t+1)\rceil`$ persistent protected qubits in the general protocol. It assumes access to known rotations and joint readout.

At readout the inverse Dicke expansion compresses the surviving symmetric states to their count register. The syndrome can then be computed reversibly. Within a syndrome, the two specified measurement vectors live in a charge basis of at most $`N-t+1`$ states and can be rotated to computational-basis outcomes by finite two-level rotations. Approximate gate compilation, sensor layout and gate noise are separate implementation costs.
