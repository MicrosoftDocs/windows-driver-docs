---
title: Terminating a connection's offload due to resource constraints
description: Terminating the Offload of a Connection Because of Resource Constraints
ms.assetid: 3b2a9a87-8e2b-44cf-ad77-6d81822cb932
keywords:
- state offloading process WDK TCP chimney offload , resource contraints
- offloading state process WDK TCP chimney offload , resource contraints
- resource contraints WDK TCP chimney offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Terminating the Offload of a Connection Because of Resource Constraints


\[The TCP chimney offload feature is deprecated and should not be used.\]

After a TCP connection has been offloaded, an offload target might fail to allocate the necessary resources for the connection. For example, the offload target's call to [**NdisMAllocateNetBufferSGList**](https://msdn.microsoft.com/library/windows/hardware/ff562776) could fail. If this failure happens, the offload target should request that the host stack terminate the offload of the connection. The offload makes such a request by calling the [**NdisTcpOffloadEventHandler**](https://msdn.microsoft.com/library/windows/hardware/ff564595) function with the *EventType* parameter set to **TcpIndicateRetrieve** and the *EventSpecificInformation* parameter set to **UploadRequested**. If the offload target receives an I/O request (a call to the [**MiniportTcpOffloadDisconnect**](https://msdn.microsoft.com/library/windows/hardware/ff559457), [*MiniportTcpOffloadForward*](https://msdn.microsoft.com/library/windows/hardware/ff559458), [*MiniportTcpOffloadReceive*](https://msdn.microsoft.com/library/windows/hardware/ff559460), [*MiniportTcpOffloadReceiveReturn*](https://msdn.microsoft.com/library/windows/hardware/ff559462), or [*MiniportTcpOffloadSend*](https://msdn.microsoft.com/library/windows/hardware/ff559464) function) before the offload termination has completed, the offload target should complete such a request with NDIS\_STATUS\_UPLOAD\_IN\_PROGRESS.

 

 





