# A probe for a distribution of erasure counts

Suppose the number $`T`$ of erased probes has a known distribution $`p_t`$ independent of the probe and signal. The input is prepared before the count is known. The receiver observes the erased set, so the QFI of the full record is the probability-weighted sum of the pattern-specific QFIs. The result below applies when positions are uniformly random given the count, and to a worst-pattern guarantee in which positions can be chosen adversarially for each count. The same probe attains the optimum in both cases. Equal-rate independent erasures are one example.

For $`N\ge2`$, define

```math
r_t=\frac{t(N-1)}{N-t},\qquad
f_t(v)=\frac{v(1-v)}{1+(r_t-1)v}\quad (1\le t\lt N),
\qquad f_0(v)=v,\quad f_N(v)=0.
```

The optimum, permitting a protected register, is

```math
F^*(p)=N^2\max_{1/N\le v\le1}\sum_{t=0}^N p_t f_t(v).
```

The variable $`v`$ is the normalized pre-erasure charge variance $`4\mathrm{Var}(W)/N^2`$. Only one variance is selected, even when different counts favor different charge profiles.

## Upper bound at given charge variance

Use the erased-string refinement from the [fixed-count proof](optimal-probe.md#converse). Conditional on a count $`t\in\{1,\ldots,N-1\}`$, sample the erased set uniformly for this upper bound. Write $`K`$ for the erased charge, $`Y=NK/t`$, and $`V=\mathrm{Var}(W)`$. Hypergeometric sampling gives $`\mathbb E[Y\mid W]=W`$, hence $`\mathrm{Cov}(W,Y)=V`$. Its mean conditional sampling variance is

```math
B=\mathbb E[\mathrm{Var}(Y\mid W)]
  =\frac{N^2/4-V-(\mathbb E[W]-N/2)^2}{r_t}.
```

Linearly regressing $`W`$ against $`Y`$ gives mean squared error $`VB/(V+B)`$, interpreted as zero when both variances vanish. The conditional mean using the full erased-string refinement has at most this error. Replacing $`B`$ by $`(N^2/4-V)/r_t`$ only increases the estimate. Multiplying by four yields the upper bound $`N^2 f_t(v)`$ for the mean QFI at count $`t`$. The average bounds the worst pattern at that count. The same input variance gives the bounds $`N^2v`$ at $`t=0`$ and zero at $`t=N`$.

For $`1\le t\lt N`$, the derivative of $`f_t`$ vanishes at its unique maximizer $`1/(1+\sqrt{r_t})\ge 1/N`$, and $`f_t`$ is increasing to the left of this point. As $`f_0`$ is increasing and $`f_N`$ is constant, the scalar maximization can be restricted to $`[1/N,1]`$.

## One preparation attains all the conditional bounds

For a chosen interior variance $`1/N\lt v\lt 1`$, use the same beta-binomial charge law as in the [fixed-count probe](optimal-probe.md#probe-and-receiver), here with

```math
2a=\frac{N(1-v)}{Nv-1}.
```

The law has mean $`N/2`$ and normalized variance $`(N+2a)/(N(1+2a))=v`$. At $`v=1/N`$ take the fair binomial law, and at $`v=1`$ take the equally weighted endpoints $`0,N`$. If there is a positive-probability count strictly between zero and $`N`$, let $`t_{\max}`$ be the largest such count. Use a protected register with $`t_{\max}+1`$ levels to store the charge modulo $`t_{\max}+1`$ coherently. After observing $`T=t\lt N`$, the receiver uses the same modular subtraction and branch measurement. A count $`N`$ never contributes information and requires no receiver branch. A distribution supported entirely on $`0,N`$ requires no protected register.

For every supported count strictly between zero and $`N`$, the posterior mean $`\mathbb E[W\mid K=k]=k+(N-t)(a+k)/(2a+t)`$ is affine in $`k`$. Its fair-binomial and endpoint limits are also affine on the support. This posterior achieves the linear regression error at each count. The actual syndrome measurement realizes those pure branches from the surviving state, so the QFI at every pattern of each count equals $`N^2 f_t(v)`$. Selecting a maximizing $`v`$ therefore attains the stated optimum. For $`N=1`$, the single sensor gives $`F^*(p)=p_0`$.

If any $`p_t\gt 0`$ for $`1\le t\lt N`$, the objective is strictly concave because $`f_t''(v)=-2r_t/[1+(r_t-1)v]^3\lt 0`$. The one-dimensional optimum is an endpoint or the unique derivative root. In particular the two-extreme-charge probe is optimal exactly when $`p_0\ge\sum_{t=1}^{N-1}p_t/r_t`$, as follows from the left derivative at $`v=1`$. The formula includes failed shots through $`f_N=0`$ and charges all $`N`$ probes on every shot.
