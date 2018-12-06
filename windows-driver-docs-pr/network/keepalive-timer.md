---
title: Keepalive Timer
description: Keepalive Timer
ms.assetid: 32c27ab0-b28b-47f6-a3cd-8c55b50f810b
keywords:
- timers WDK TCP chimney offload , keepalive timers
- TCP timers WDK TCP chimney offload , keepalive timers
- keepalive timers WDK TCP chimney offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Keepalive Timer


\[The TCP chimney offload feature is deprecated and should not be used.\]

During an offload or an update operation, the host stack can set the following information in the [**TCP\_OFFLOAD\_STATE\_CACHED**](https://msdn.microsoft.com/library/windows/hardware/ff570937) structure that is supplied for a TCP connection:

-   The TCP\_FLAG\_KEEP\_ALIVE\_ENABLED flag in the **Flags** member enables the keepalive option for a TCP connection. If the host stack does not set this flag, the keepalive option for a TCP connection is disabled.

-   The TCP\_FLAG\_KEEP\_ALIVE\_RESTART flag in the **Flags** member causes the offload target to restart its keepalive timer with a value of 0.

-   The **KaProbeCount** member specifies the maximum number of keepalive probes that the offload target can send to determine whether a TCP connection is intact.

-   The **KaTimeout** member specifies the timeout interval for inactivity before sending the first keepalive probe.

-   The **KaInterval** member specifies the timeout after which to retransmit a keepalive frame if no response is received to a keepalive probe.

The [**TCP\_OFFLOAD\_STATE\_DELEGATED**](https://msdn.microsoft.com/library/windows/hardware/ff570939) structure contains **ProbeCount** and **TimeoutDelta** members for the keepalive option. The value in the keepalive **ProbeCount** specifies the number of keepalive probes that have been sent that have not received a response. The value in the keepalive **TimeoutDelta** specifies the time remaining until the next keepalive timeout.

When offloading a TCP connection, the host stack passes its current keepalive values for the connection to the offload target. The offload uses these values to resume keepalive processing on the offloaded connection. If the host stack target was not running the keepalive timer, it supplies a value of -1 in the **TimeoutDelta** member.

Similarly, when terminating the offload of a TCP connection, an offload target passes its current keepalive values for the connection to the host stack. The host stack uses these values to resume keepalive processing on the uploaded connection. If the offload target was not running the keepalive timer, it should supply a value of -1 in the **TimeoutDelta** member. If the offload target supplies a value of 0 in the **TimeoutDelta** member, the host stack assumes that the keepalive timer was running, and the host stack's keepalive timer expires immediately.

 

 





