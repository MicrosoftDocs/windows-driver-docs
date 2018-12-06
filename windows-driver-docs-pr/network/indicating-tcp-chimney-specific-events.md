---
title: Indicating TCP Chimney-Specific Events
description: Indicating TCP Chimney-Specific Events
ms.assetid: 98b22b7f-8881-4029-9558-d5d94bb7878e
keywords:
- events WDK TCP chimney offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Indicating TCP Chimney-Specific Events


\[The TCP chimney offload feature is deprecated and should not be used.\]

An offload target calls the [**NdisTcpOffloadEventHandler**](https://msdn.microsoft.com/library/windows/hardware/ff564595) function to indicate the following TCP chimney-specific events to the host stack:

### Disconnects that are initiated by the remote host

To indicate that it has received a FIN segment from the remote host, an offload target calls the [**NdisTcpOffloadEventHandler**](https://msdn.microsoft.com/library/windows/hardware/ff564595) function with the *EventType* parameter set to **TcpIndicateDisconnect**.

To indicate that it has received an RST segment from the remote host, an offload target calls the [**NdisTcpOffloadEventHandler**](https://msdn.microsoft.com/library/windows/hardware/ff564595) function with the *EventType* parameter set to **TcpIndicateAbort**. For more information, see [Responding to the Reception of a FIN or RST Segment](responding-to-the-reception-of-a-fin-or-rst-segment.md).

### Requests to terminate the offload of a TCP connection

To request that the host stack terminate the offload of a TCP connection, an offload target calls the [**NdisTcpOffloadEventHandler**](https://msdn.microsoft.com/library/windows/hardware/ff564595) function with the *EventType* parameter set to **TcpIndicateRetrieve** and the *EventSpecificInformation* parameter set to a **TCP\_UPLOAD\_REASON** value that indicates the reason for the request.

### Changes in the preferred send backlog size

To indicate a change in the preferred send backlog size, an offload target calls the [**NdisTcpOffloadEventHandler**](https://msdn.microsoft.com/library/windows/hardware/ff564595) function with the *EventType* parameter set to **TcpIndicateSendBacklogChange** and the *EventSpecificInformation* parameter set to the optimum number of send data bytes that the host stack should have outstanding at the offload target.

## Related topics


[*ProtocolTcpOffloadEvent*](https://msdn.microsoft.com/library/windows/hardware/ff570272)

[Responding to the Reception of a FIN or RST Segment](responding-to-the-reception-of-a-fin-or-rst-segment.md)

 

 






