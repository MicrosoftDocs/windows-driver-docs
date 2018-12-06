---
title: Generating and Using Timestamps
description: Generating and Using Timestamps
ms.assetid: a654a702-d01e-43d9-a0ef-7886ccfeb11d
keywords:
- TCP chimney offload WDK networking , timestamps
- chimney offload WDK networking , timestamps
- timestamps WDK TCP chimney offload
- TCP timestamps WDK TCP chimney offload
- timestamps WDK TCP chimney offload , about TCP timestamps
- TCP timestamps WDK TCP chimney offload , about TCP timestamps
- synchronization WDK TCP chimney offload
- target synchronization WDK TCP chimney offload
- calibrating timestamps WDK TCP chimney offload
- clocks WDK TCP chimney offload
- connection timestamps WDK TCP chimney offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Generating and Using Timestamps


\[The TCP chimney offload feature is deprecated and should not be used.\]

The host stack and offload target must synchronize the generation of TCP timestamps. This synchronization allows the host stack and offload target to generate timestamps that increase monotonically, even if the TCP connection is offloaded or the offload of the connection is terminated.

Note that the timer that is used for the timestamps should be calibrated to the granularity that is specified by the host stack in the **TicksPerSecond** member of the [**NDIS\_TASK\_TCP\_CONNECTION\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff567873) structure. The host stack supplies this structure when setting the [OID\_TCP\_TASK\_OFFLOAD](https://msdn.microsoft.com/library/windows/hardware/ff569815) OID. The host stack can specify a timer granularity of 10, 100, or 1000 ticks per second.

This section includes:

[Calculating the Timestamp Delta](calculating-the-timestamp-delta.md)

[Generating a Timestamp](generating-a-timestamp.md)

[Calculating the Merged Round-Trip Time](calculating-the-merged-round-trip-time.md)

[Examples of Timestamp Processing](examples-of-timestamp-processing.md)

 

 





