# Parallel phase sensing with a hard erasure budget

A single interrogation applies the same phase rotation to each of $`N`$ two-level sensors. The parameter acts through the total excitation number

```math
G_N=\sum_{i=1}^{N}|1\rangle\langle 1|_i,\qquad U_\theta=\exp(-i\theta G_N).
```

The generator convention gives local quantum Fisher information (QFI) one for a single ideal Ramsey probe. The initial state may include a protected register $`R`$ of dimension $`D`$. This register experiences neither the phase nor loss. Its dimension counts quantum storage retained through the interrogation. The probe proof denotes this register by $`C`$ when it holds the charge residue.

## Erasure and readout

For an erased set $`A`$, the receiver gets $`A`$ as a classical location flag and holds the surviving sensors and $`R`$. The contents of the erased sites are traced out. For fixed $`A`$, the output is

```math
\rho_{\theta,A}=\mathrm{Tr}_{A}\bigl[(U_\theta\otimes I_R)\rho(U_\theta^\dagger\otimes I_R)\bigr].
```

The erasure choice carries no phase information. The model allows joint preparation, one parallel phase exposure per sensor, calibration at a nominal phase $`\theta_0`$, and a collective measurement that can use the erasure flag. No intermediate control, other signal calls, or observation of the erased contents enters the protocol. All measurement outcomes count.

We maximize the least local QFI over all sets of size $`t`$:

```math
F^*(N,t;D)=\sup_{\rho}\ \min_{|A|=t}F_Q(\rho_{\theta,A}),\qquad
F^*(N,t)=\sup_{D\ge1}F^*(N,t;D).
```

Local QFI is invariant along this unitary orbit. We specify a measurement attaining it at the chosen nominal phase. Its scale describes local phase discrimination or estimation around that point. Global accuracy over the full phase circle depends on additional features of the probe, including the spacing of its excitation numbers.

The same optimum applies to the budget “at most $`t`$,” since one can ignore additional survivors and loss is phase independent. For $`t=0`$, the GHZ probe attains $`N^2`$. When all sensors are erased, the reference marginal is phase independent and the information is zero. At $`t=N-1`$, product Ramsey probes attain one.

## What the receiver measures

The fixed-count protocol encodes the total excitation count modulo $`t+1`$ in the protected register. The receiver measures the difference between this residue and the survivor count modulo the same integer. This reads the erased excitation count as a syndrome and preserves the survivor superposition in that sector. A phase-sensitive measurement within the sector then uses the remaining coherence. The preparation and joint measurement use ideal parameter-independent gates; hardware noise and gate-depth optimization are separate questions.

When the loss count is random with a known phase-independent distribution, the receiver uses the count supplied by the location flag. The [random-count result](loss-distributions.md) covers uniform locations given each count and the worst pattern separately at each count. An erasure mechanism that measures the input and chooses locations from that outcome is a different channel.

