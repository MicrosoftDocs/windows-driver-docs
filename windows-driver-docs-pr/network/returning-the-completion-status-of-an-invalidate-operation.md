---
title: Returning the Completion Status of an Invalidate Operation
description: Returning the Completion Status of an Invalidate Operation
ms.assetid: f205ccd4-7b00-467e-950e-2601820d5275
keywords:
- invalidating offloaded state WDK TCP chimney offload , completion status
- completion status of invalidation WDK TCP chimney offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Returning the Completion Status of an Invalidate Operation


\[The TCP chimney offload feature is deprecated and should not be used.\]




Before calling the [**NdisMInvalidateOffloadComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563609) function, the offload target must write either of the following NDIS\_STATUS values to the **Status** member of each [**NDIS\_MINIPORT\_OFFLOAD\_BLOCK\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff566469) structure in the state tree:

<a href="" id="ndis-status-success"></a>NDIS\_STATUS\_SUCCESS  
The offload target successfully invalidated the state objects.

<a href="" id="ndis-status-failure"></a>NDIS\_STATUS\_FAILURE  
The invalidate operation did not succeed because the hardware state is corrupt.

If the hardware state is corrupt, the offload target must do the following:

1.  Call the **NdisMInvalidateOffloadComplete** function with a status value of NDIS\_STATUS\_FAILURE.

2.  Call the [**NdisTcpOffloadEventHandler**](https://msdn.microsoft.com/library/windows/hardware/ff564595) function with the *EventType* parameter set to **TcpIndicateRetrieve** and the *EventSpecificInformation* parameter set to **HardwareFailure**.

3.  Call the **NdisTcpOffloadEventHandler** function with the *EventType* parameter set to **TcpIndicateAbort**.

4.  When the host stack calls the [**MiniportTerminateOffload**](https://msdn.microsoft.com/library/windows/hardware/ff559468) function, complete any outstanding calls to the [*MiniportTcpOffloadSend*](https://msdn.microsoft.com/library/windows/hardware/ff559464) and [*MiniportTcpOffloadReceive*](https://msdn.microsoft.com/library/windows/hardware/ff559460) functions with a status value of NDIS\_STATUS\_REQUEST\_ABORTED in each NET\_BUFFER\_LIST structure.

5.  Call the [**NdisMTerminateOffloadComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563685) function.

 

 





