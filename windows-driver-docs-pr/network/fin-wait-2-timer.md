---
title: FIN_WAIT_2 Timer
description: FIN_WAIT_2 Timer
ms.assetid: 912d30a7-5bd4-4460-8136-466f5ad84536
keywords:
- timers WDK TCP chimney offload , FIN_WAIT_2 timers
- TCP timers WDK TCP chimney offload , FIN_WAIT_2 timers
- FIN_WAIT_2 timers WDK TCP chimney offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# FIN\_WAIT\_2 Timer


\[The TCP chimney offload feature is deprecated and should not be used.\]

When an offloaded TCP connection enters the FIN\_WAIT\_2 state, the offload target starts the FIN\_WAIT\_2 timer for that connection. The [retransmit timer](retransmit-timer.md) for the connection acts as the FIN\_WAIT\_2 timer when the connection is in the FIN\_WAIT\_2 state. An offload target should use a value of 120 seconds as the initial value of the FIN\_WAIT\_2 timer.

If an acceptable TCP segment arrives on the connection before the FIN\_WAIT\_2 timer expires, the offload target restarts the FIN\_WAIT\_2 timer.

If the FIN\_WAIT\_2 timer expires before an acceptable TCP segment arrives on the connection, the offload target must call the [**NdisTcpOffloadEventHandler**](https://msdn.microsoft.com/library/windows/hardware/ff564595) function with the *EventType* parameter set to **TcpIndicateRetrieve** and the *EventSpecificInformation* parameter set to **TimeoutExpiration**. This call requests that the host stack terminate the offload of the connection.

When the FIN\_WAIT\_2 timer expires, the offload target should change its TCP state to CLOSED.

When offloading a TCP connection that is in the FIN\_WAIT\_2 state, the host stack passes the value of its FIN\_WAIT\_2 timer for the connection to the offload target. The host stack passes this value in the retransmit **TimeoutDelta** member of the [**TCP\_OFFLOAD\_STATE\_DELEGATED**](https://msdn.microsoft.com/library/windows/hardware/ff570939) structure. The offload target uses this value as the starting value for its FIN\_WAIT\_2 timer for the connection. If the host stack target was not running the FIN\_WAIT\_2 timer for the connection, it supplies a value of -1in the retransmit **TimeoutDelta** member.

Similarly, when terminating the offload of a TCP connection that is in the FIN\_WAIT\_2 state, an offload target passes the value of its FIN\_WAIT\_2 timer for the connection to the host stack. The offload target passes this value in the retransmit **TimeoutDelta** member of the TCP\_OFFLOAD\_STATE\_DELEGATED structure.The host stack uses this value as the starting value for its FIN\_WAIT\_2 timer for the connection. If the offload target was not running the FIN\_WAIT\_2 timer, it should supply a value of -1 in the retransmit **TimeoutDelta** member. If the offload target supplies a value of 0 in the retransmit **TimeoutDelta** member, the host stack assumes that the offload target's FIN\_WAIT\_2 timer was running, and the host stack's FIN\_WAIT\_2 timer expires immediately.

 

 





