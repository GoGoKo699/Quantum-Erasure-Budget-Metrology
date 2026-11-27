# Science

The problem is to estimate a common phase in one parallel interrogation after losing an arbitrary set of sensors. The receiver learns the erased locations. The erased excitation count affects the phase coherence of the survivors, so an optimal probe must control both how much charge the erasure reveals and how much coherence the receiver can use.

1. [Model](model.md) defines the flagged partial trace, local QFI, interrogation budget and protected register.
2. [Optimal probe and readout](optimal-probe.md) proves the sharp universal bound and constructs a single probe attaining it for every erasure set.
3. [Loss-count distributions](loss-distributions.md) gives one probe family that is optimal after averaging with a known law of loss counts.
4. [Protected memory](memory.md) proves when a growing protected register is necessary for exact optimality and gives examples where receiver-only readout attains the full information.

The [related-work account](../references/RELATED_WORK.md) traces the finite-population statistical ingredient, optical conditional-variance bounds, earlier erasure-tolerant probe families, and the closest exact phase-programming result. The [four-sensor example](../learning/WORKED_EXAMPLE.md) is a short route from loss to readout.

