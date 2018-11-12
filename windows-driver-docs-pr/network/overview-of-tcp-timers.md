---
title: Overview of TCP Timers
description: Overview of TCP Timers
ms.assetid: d1190d9c-3a43-4373-8a5b-be8f20d41920
keywords:
- timers WDK TCP chimney offload , about TCP timers
- TCP timers WDK TCP chimney offload , about TCP timers
- timers WDK TCP chimney offload , types
- TCP timers WDK TCP chimney offload , types
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Overview of TCP Timers


\[The TCP chimney offload feature is deprecated and should not be used.\]

An offload target must maintain the following set of timers for each offloaded TCP connection:

-   Delayed Acknowledgement Timer (RFC 1122)

-   FIN\_WAIT\_2 Timer

-   Keep-alive Timer (RFC 1122)

-   Persist Timer

-   Push Timer

-   Retransmit Timer (RFC 2581)

An offload target can optionally maintain a Silly Window Syndrome (SWS) prevention timer (RFC 813) for each offloaded TCP connection.

The timer granularity of the offload target must be the granularity that is specified by the host stack in the **TicksPerSecond** member of the [**NDIS\_TASK\_TCP\_CONNECTION\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff567873) structure. The host stack supplies this structure when setting the [OID\_TCP\_TASK\_OFFLOAD](https://msdn.microsoft.com/library/windows/hardware/ff569815) OID. The host stack can specify a timer granularity of 10, 100, or 1000 ticks per second.

Each TCP timer must be large enough so that it takes at least several weeks of running time for the timer to wrap to zero.

If an offloaded connection enters the TIME\_WAIT state, the offload target should initiate termination of the offload of that connection (upload).

 

 





