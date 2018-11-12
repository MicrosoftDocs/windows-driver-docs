---
title: Responding to a Disconnect Request
description: Responding to a Disconnect Request
ms.assetid: f812086e-a281-4738-ad10-42de64fb1ed2
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

# Responding to a Disconnect Request


\[The TCP chimney offload feature is deprecated and should not be used.\]

The host stack initiates the closing of an offloaded TCP connection by calling the [**NdisOffloadTcpDisconnect**](https://msdn.microsoft.com/library/windows/hardware/ff563696) function, which causes NDIS to call the offload target's [**MiniportTcpOffloadDisconnect**](https://msdn.microsoft.com/library/windows/hardware/ff559457) function.

If the *Flags* parameter of *MiniportTcpOffloadDisconnect* is set to **TCP\_DISCONNECT\_ABORTIVE\_CLOSE**, the offload target performs an abortive disconnect by sending an RST segment on the specified TCP connection.

If the *Flags* parameter of *MiniportTcpOffloadDisconnect* is set to **TCP\_DISCONNECT\_GRACEFUL\_CLOSE**, the offload target performs a graceful disconnect by sending a FIN segment on the specified TCP connection. In the disconnect request, the host stack can specify data that the offload target must send on the connection before sending the FIN segment.

From the perspective of the offload target, sending a FIN segment closes the send half of the connection but does not close the receive half of the connection. The remote host terminates the receive half of the connection by sending a FIN segment or an RST segment to the offload target.

The offload target must not free resources for the connection on which it has sent either a FIN or RST segment until the host stack terminates the offload of the connection.

For more information about responding to an abortive or graceful disconnect request, see [**MiniportTcpOffloadDisconnect**](https://msdn.microsoft.com/library/windows/hardware/ff559457) and [**NdisTcpOffloadDisconnectComplete**](https://msdn.microsoft.com/library/windows/hardware/ff564590).

 

 





