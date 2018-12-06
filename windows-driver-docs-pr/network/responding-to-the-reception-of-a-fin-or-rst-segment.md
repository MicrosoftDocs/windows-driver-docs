---
title: Responding to the Reception of a FIN or RST Segment
description: Responding to the Reception of a FIN or RST Segment
ms.assetid: 74807473-2d57-4f5b-bc7d-80165c4e18b9
keywords:
- connection closing WDK TCP chimney offload
- disconnections WDK TCP chimney offload
- RST segment WDK TCP chimney offload
- FIN segment WDK TCP chimney offload
- abortive disconnects WDK TCP chimney offload
- graceful disconnects WDK TCP chimney offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Responding to the Reception of a FIN or RST Segment


\[The TCP chimney offload feature is deprecated and should not be used.\]

A remote host issues a graceful disconnect on an offloaded TCP connection by sending a FIN segment. In response, an offload target must call the [**NdisTcpOffloadEventHandler**](https://msdn.microsoft.com/library/windows/hardware/ff564595) function with the *EventType* parameter set to **TcpIndicateDisconnect** after the offload target ensures that all received data on the connection has been consumed by the client application.

A remote host issues an abortive disconnect on an offloaded TCP connection by sending an RST segment. In response to receiving an acceptable RST segment, an offload target calls the [**NdisTcpOffloadEventHandler**](https://msdn.microsoft.com/library/windows/hardware/ff564595) function with the *EventType* parameter set to **TcpIndicateAbort**. The offload target completes all outstanding send requests, receive requests, and disconnect requests on the connection with **NDIS\_STATUS\_REQUEST\_ABORT**.

Note that a graceful disconnect shuts down only the receive half of the connection. It does not shut down the send half of the connection.

In response to either a FIN or RST segment, an offload target must not free the resources for the connection until the host stack terminates the offload of the connection.

If the offload target receives data on the connection when the connection is in the CLOSED state, it should forward such data to the host stack through the nonoffload NDIS interface by calling the [**NdisMIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff563598) function.

## Related topics


[*ProtocolTcpOffloadEvent*](https://msdn.microsoft.com/library/windows/hardware/ff570272)

[Indicating TCP Chimney-Specific Events](indicating-tcp-chimney-specific-events.md)

 

 






