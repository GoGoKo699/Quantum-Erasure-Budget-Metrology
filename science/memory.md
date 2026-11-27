# Protected memory at the exact optimum

Write $`M=N-t`$ for the number of survivors and $`D`$ for the Hilbert-space dimension of the protected register. The modular tag suffices with $`D=t+1`$. With $`1\le t\le N-2`$, exact attainment in the worst erasure pattern requires
```math
D\ge \left\lceil\frac{t+1}{2^M}\right\rceil .
```
For a permutation-symmetric sensor probe the bound improves to $`D\ge\lceil(t+1)/(M+1)\rceil`$. These statements cover mixed probes on the specified sensor and register spaces. They quantify exact equality with the unrestricted quantum Fisher information (QFI). Product Ramsey probes give $`M`$ QFI. At each fixed $`M\ge2`$, the unrestricted optimum tends to $`M`$ as $`N`$ grows, while exact attainment needs $`D=\Theta_M(N)`$.

## Equality conditions for the erasure refinement

At a fixed erasure pattern $`A`$, write the output of a pure probe as $`\rho(\theta)=\sum_x |u_x(\theta)\rangle\langle u_x(\theta)|`$, where $`x`$ is the erased computational string, and omit zero branches. The branch vectors include the protected register. Choose the branch phases so that the derivative at the measurement point is
```math
\dot u_x=-i(G-\mu_x)u_x,
\qquad
\mu_x=\frac{\langle u_x,G u_x\rangle}{\|u_x\|^2},
```
where $`G`$ is the survivor excitation number. Since the weights $`\|u_x\|^2`$ are constant in the phase, the refined QFI is $`4\sum_x\|\dot u_x\|^2`$.

For any Hermitian $`L`$, the SLD variational functional satisfies
```math
2\operatorname{Tr}(\dot\rho L)-\operatorname{Tr}(\rho L^2)
 =4\sum_x\|\dot u_x\|^2-\sum_x\|(L+2i(G-\mu_x))u_x\|^2 .
```
Its maximum is the unrefined QFI, attained by a symmetric logarithmic derivative (SLD). Equality with the refined QFI therefore holds precisely when a single Hermitian $`L`$ obeys
```math
L u_x=-2i(G-\mu_x)u_x
\quad\text{for all }x.
```
An equivalent criterion is
```math
\langle u_x,(2G-\mu_x-\mu_y)u_y\rangle=0
\quad\text{for every }x,y .
```
To see sufficiency, let $`U`$ have columns $`u_x`$ and $`V`$ have columns $`2\dot u_x`$. The pairwise criterion states $`U^\dagger V=V^\dagger U`$. If $`Uc=0`$, then $`U^\dagger Vc=0`$ and $`Vc=2iU\operatorname{diag}(\mu_x)c`$ lies in the span of $`U`$. Thus $`Vc=0`$. The assignment $`u_x\mapsto 2\dot u_x`$ is well defined and Hermitian as a compression on their span. On its orthogonal complement, take the adjoint of the off-diagonal block and choose the remaining diagonal block to be zero.

## An optimal probe has every erased charge at every cut

Let $`X_i`$ be the computational-basis bit at sensor $`i`$, with the law determined by the input's diagonal after tracing out the protected register. Let $`S=\sum_i X_i`$, $`K=\sum_{i\in A}X_i`$, and $`\gamma=\sqrt{tM/(N-1)}`$. Use $`a=N\gamma/[2(t+\gamma)]`$ and $`b=N/(t+\gamma)`$ so that the minimax estimator is $`\delta(k)=a+bk`$. Draw $`A`$ uniformly and independently of the input. The constant-risk argument bounds the average refined QFI by the optimum, while the worst QFI bounds the average unrefined QFI from below. If the worst QFI equals the optimum, every pattern has equality in the QFI refinement and the square-loss projection. In particular,
```math
\mathbb{E}[S\mid A,X_A]=a+bK
```
on its support. Conditional on $`S`$, the uniformly drawn subset makes $`K`$ hypergeometric even for a nonsymmetric input.

The resulting law of $`S`$ has the same factorial moments through order $`t+1`$ as the attaining beta-binomial prior. To prove this, let $`m_r=\mathbb E[(S)_r]`$, with $`(z)_r`$ denoting falling factorials. For $`0\le r\le t`$,
```math
\mathbb{E}[(K)_r\mid S]=\frac{(t)_r}{(N)_r}(S)_r .
```
Compute $`\mathbb E[S(K)_r]`$ using this identity and the conditional-mean formula given $`K`$. The relation $`z(z)_r=(z)_{r+1}+r(z)_r`$ gives
```math
\left(1-b\frac{t-r}{N-r}\right)m_{r+1}
   =[a+(b-1)r]m_r .
```
Its left coefficient is at least $`1-bt/N=\gamma/(t+\gamma)\gt 0`$, so $`m_0=1`$ fixes all these moments. Since the beta-binomial prior has the same conditional mean, its moments obey the same recurrence.

To pass from an average over cuts to each cut, fix $`B`$ with $`|B|\lt t`$ and any $`t`$-subset $`A`$ containing it. Put $`X_B=\prod_{i\in B}X_i`$. Multiplying the conditional mean by $`X_B`$ and averaging yields
```math
\mathbb{E}[S X_B]=a\mathbb{E}X_B+b\sum_{j\in A}\mathbb{E}[X_B X_j] .
```
Given distinct $`j,j'`$ outside $`B`$, choose two such $`A`$ differing only by swapping $`j`$ with $`j'`$. Hence $`\mathbb E X_{B\cup\{j\}}=\mathbb E X_{B\cup\{j'\}}`$. Repeated single-element exchanges connect all subsets of the same size. Every moment $`\mathbb E X_C`$ with $`|C|\le t`$ consequently depends only on $`|C|`$, and its value is $`m_{|C|}/(N)_{|C|}`$. Inclusion–exclusion now identifies the complete distribution of $`X_A`$ for each $`A`$ with the corresponding beta-binomial mixture of Bernoulli strings. The prior has a positive density on the open unit interval for $`t\le N-2`$. Every erased string, and thus every charge $`k\in\{0,\ldots,t\}`$, occurs with positive probability.

## Why exact attainment consumes memory

On every branch with charge $`k`$, the survivor generator mean is $`\mu_k=a+(b-1)k`$. Here $`M\gt \gamma`$ for $`M\ge2`$, so $`b-1\gt 0`$ and all $`t+1`$ means are distinct. The common SLD condition makes $`u_x`$ an eigenvector of the single operator $`G-iL/2`$ at eigenvalue $`\mu_k`$. Choosing one branch from each charge gives $`t+1`$ independent vectors. The output dimension $`2^M D`$ bounds their number. For permutation-symmetric sensor probes their vectors lie in the symmetric survivor subspace tensored with the register, and $`G`$ preserves that subspace. The SLD may be compressed to this subspace, so the same argument gives $`(M+1)D\ge t+1`$.

For a mixed optimal probe, choose any pure-state decomposition on the same input space. For each erasure pattern QFI is convex, and after averaging over patterns the QFI of every pure component is bounded by the same optimum. The optimal mixed probe has average equal to the optimum, so each positive-weight pure component also attains the average bound. The preceding proof used the worst-case hypothesis to deduce exactly this average equality. Every step thereafter applies to the pure components, giving the same dimension lower bound.

For example, when $`t=N-2`$ and $`N\ge6`$, even nonsymmetric untagged probes fail to attain the exact optimum. Keeping $`M\ge2`$ fixed yields $`D\ge\lceil (N-M+1)/2^M\rceil`$, matched in order by the tagged construction. The endpoint $`t=N-1`$ has $`b=1`$ and a single survivor-charge mean. Independent Ramsey probes attain $`F=1`$ there with $`D=1`$.

## One erasure needs no protected register

For $`t=1`$, the unrestricted optimum is $`N^2/4`$. At $`N=2`$ a product probe attains it. At $`N=3`$, use the symmetric state
```math
|\psi\rangle=
\sqrt{7/32}(|000\rangle+|111\rangle)
+\sqrt{3/32}\sum_{x:\,|x|=1,2}|x\rangle .
```
For either erased-bit value the branch probability is $`1/2`$. At the nominal phase zero, the survivor-charge means for bits 0 and 1 are $`3/4`$ and $`5/4`$. The conditional total-charge means are therefore $`3/4`$ and $`9/4`$, as required by $`\delta`$. In the common-SLD criterion, the weight-one contribution vanishes since $`\mu_0+\mu_1=2`$. Weight zero and weight two have equal branch-overlap magnitudes and opposite coefficients, so they cancel. The erased bits remain unobserved. The SLD readout on both survivors attains the refined QFI $`9/4`$.

For $`N\ge4`$, choose $`c=\lfloor N/2\rfloor`$ and the Dicke weights $`0,c,N`$ with respective probabilities
```math
\frac{4c-N}{8c},\qquad \frac{N^2}{8c(N-c)},\qquad \frac{3N-4c}{8(N-c)}.
```
They give $`\mathbb E S=N/2`$ and $`\operatorname{Var}S=N^2/8`$. These are the moments of the attaining prior through order two and fix the conditional means for $`t=1`$. The weights are separated by at least two, so the erased bit is determined by the survivor's charge support. An orthogonal syndrome measurement preserves superpositions within each support. For even $`N`$ the state is the corresponding three-weight gnu-code probe.

The dimension bounds leave finite intermediate regimes open. The common-SLD criterion allows overlapping branch supports and may help find further untagged probes even when a spaced Dicke state fails to exist.

## A finite gap for independent erasures

Three parallel sensors with independent loss probability $`1/2`$ already give a strict protected-memory advantage. Exactly one protected qubit suffices to attain the unrestricted optimum. The count probabilities for $`t=0,1,2,3`$ are $`(1,3,3,1)/8`$. The random-count theorem gives the optimum as $`9\max_{1/3\le v\le1}g(v)`$, where
```math
g(v)=\tfrac18 v+\tfrac38 v(1-v)+\tfrac38\frac{v(1-v)}{1+3v}.
```
Here $`v=4\operatorname{Var}(S)/9`$. Strict concavity and $`g'(1/3)=1/4`$, $`g'(1)=-11/32`$ place the unique maximizer $`v_*`$ in the interior. The modulo-three tag attains this optimum by the general construction. A two-level tag already suffices. Prepare the same beta-binomial Dicke amplitudes with the tag $`w\bmod 2`$ for excitation count $`w`$. At $`t=1`$ parity separates the two erased charges. For $`t=2`$, the two extreme charges $`k=0,2`$ share a parity sector, while $`k=1`$ has the opposite sector. By complement symmetry, $`\mu_0+\mu_2=1`$, and the overlaps of $`u_0`$ and $`u_2`$ in survivor-charge sectors zero and one have equal magnitudes and the same positive phase. Their terms cancel in the common-SLD criterion. The receiver can use a common SLD on the even sector and attain the same optimum with one protected qubit.

Any pure probe attaining this optimum must have mean $`\mathbb ES=3/2`$, because the affine-regression bound is strictly increasing in $`\operatorname{Var}(K)`$ at positive $`v`$ before enforcing that mean. The individual nonnegative regression and refinement gaps must all vanish since every erasure pattern has positive probability. The conditional mean of $`S`$ given each erased string of length $`t`$ must equal the affine regression function from the common attaining beta-binomial prior. For $`t=2`$, put $`\beta=3(1-v_*)/(3v_*-1)\gt 0`$. The slope is $`b=(3+\beta)/(2+\beta)`$, so $`b-1\gt 0`$ and $`1-2b/3\gt 0`$. The moment and subset-exchange argument above applies to these affine coefficients, showing that each two-erasure cut has all three erased charges in its support. Thus the single surviving qubit needs three independent eigenvectors of $`G-iL/2`$, which is impossible on its two-dimensional Hilbert space.

The mixed-probe argument again follows by convexity. For fixed register size the QFI of a state evolved by a fixed generator is continuous in the state. In its spectral expression the coefficient $`(\lambda-\lambda')^2/(\lambda+\lambda')`$ extends continuously at zero. Compactness then makes the dimension-one optimum strictly below the attainable tagged optimum. This is a finite-use statement for parallel protocols at fixed transmissivity. The asymptotic i.i.d. erasure bound and its unassisted attainability concern a different limit.
