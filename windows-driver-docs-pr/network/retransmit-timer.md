---
title: Retransmit Timer
description: Retransmit Timer
ms.assetid: 71a425cd-9335-4702-b0a3-fe3a1b996cb0
keywords:
- timers WDK TCP chimney offload , retransmit timers
- TCP timers WDK TCP chimney offload , retransmit timers
- retransmit timers WDK TCP chimney offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Retransmit Timer


\[The TCP chimney offload feature is deprecated and should not be used.\]

When setting [OID\_TCP\_TASK\_OFFLOAD](https://msdn.microsoft.com/library/windows/hardware/ff569815) during offload target initialization, the host stack supplies a value in the **TcpMaximumRetransmissions** member of the [**NDIS\_TASK\_TCP\_CONNECTION\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff567873) structure. **TcpMaximumRetransmissions** specifies the maximum number of times that the offload target should retransmit a segment on an offloaded TCP connection.

The host stack can override **TcpMaximumRetransmissions** on a per-connection basis by supplying a value in the **MaxRT** member of the [**TCP\_OFFLOAD\_STATE\_CACHED**](https://msdn.microsoft.com/library/windows/hardware/ff570937) structure during an initiate offload or update offload operation. The host stack sets the TCP\_FLAG\_MAX\_RT\_RESTART flag in the **Flags** member of the TCP\_OFFLOAD\_STATE\_CACHED structure to indicate that the value of **MaxRT** has changed and that the offload target should reset the **TotalRT** variable in the TCP delegated state for the connection. **TotalRT** indicates the total time, in clock ticks, that the offload target has spent retransmitting the current TCP segment.

The TCP delegated state for a connection contains values in the retransmit **Count** and **TimeoutDelta** members of the [**TCP\_OFFLOAD\_STATE\_DELEGATED**](https://msdn.microsoft.com/library/windows/hardware/ff570939) structure. The value of the retransmit **Count** specifies the number of retransmits that have been sent. The value of the retransmit **TimeoutDelta** specifies the time, in clock ticks, that remains until the next retransmit timeout.

When offloading a TCP connection, the host stack passes its current retransmit values for the connection to the offload target. The offload uses these values to resume retransmit processing on the offloaded connection. If the host stack target was not running the retransmit timer, it supplies a value of -1 in the **TimeoutDelta** member.

Similarly, when terminating the offload of a TCP connection, an offload target passes its current retransmit values for the connection to the host stack. The host stack uses these values to resume retransmit processing on the uploaded connection. If the offload target was not running the retransmit timer, it should supply a value of -1 in the **TimeoutDelta** member. If the offload target supplies a value of 0 in the **TimeoutDelta** member, the host stack assumes that the retransmit timer was running, and the host stack's retransmit timer expires immediately.

 

 





