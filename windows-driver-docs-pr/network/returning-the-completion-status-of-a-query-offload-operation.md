---
title: Returning the Completion Status of a Query Offload Operation
description: Returning the Completion Status of a Query Offload Operation
ms.assetid: 9583279e-1f18-4753-a7fa-08947339553f
keywords:
- querying offloaded TCP chimney state, completion status
- completion status of querying WDK TCP chimney offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Returning the Completion Status of a Query Offload Operation


\[The TCP chimney offload feature is deprecated and should not be used.\]




Before calling the [**NdisMQueryOffloadStateComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563634) function, the offload target must write one of the following NDIS\_STATUS values to the **Status** member of each [**NDIS\_MINIPORT\_OFFLOAD\_BLOCK\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff566469) structure in the state tree:

<a href="" id="ndis-status-success"></a>NDIS\_STATUS\_SUCCESS  
The offload target successfully queried the state objects.

<a href="" id="ndis-status-failure"></a>NDIS\_STATUS\_FAILURE  
The query operation did not succeed because the hardware state is corrupt. The host stack will terminate the offload of the state objects that could not be queried.

If the hardware state is corrupt, the offload target must do the following:

1.  Call the [**NdisMQueryOffloadStateComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563634) function with a status value of NDIS\_STATUS\_FAILURE.

2.  Call the [**NdisTcpOffloadEventHandler**](https://msdn.microsoft.com/library/windows/hardware/ff564595) function with the *EventType* parameter set to **TcpIndicateRetrieve** and the *EventSpecificInformation* parameter set to **HardwareFailure**.

3.  Call the [**NdisTcpOffloadEventHandler**](https://msdn.microsoft.com/library/windows/hardware/ff564595) function with the *EventType* parameter set to **TcpIndicateAbort**.

4.  When the host stack calls the [**MiniportTerminateOffload**](https://msdn.microsoft.com/library/windows/hardware/ff559468) function, complete any outstanding calls to the [*MiniportTcpOffloadSend*](https://msdn.microsoft.com/library/windows/hardware/ff559464) and [*MiniportTcpOffloadReceive*](https://msdn.microsoft.com/library/windows/hardware/ff559460) functions with a status value of NDIS\_STATUS\_REQUEST\_ABORTED in each NET\_BUFFER\_LIST structure.

5.  Call the [**NdisMTerminateOffloadComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563685) function.

 

 





