---
title: Returning the Completion Status of a Terminate Offload Operation
description: Returning the Completion Status of a Terminate Offload Operation
ms.assetid: 2c900a72-47ec-4e26-aeb3-2a67511690c0
keywords:
- terminating offload state WDK TCP chimney offload , completion status
- completion status of termination WDK TCP chimney offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Returning the Completion Status of a Terminate Offload Operation


\[The TCP chimney offload feature is deprecated and should not be used.\]




Before calling the [**NdisMTerminateOffloadComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563685) function, the offload target must write either of the following NDIS\_STATUS values to the **Status** member of each NDIS\_MINIPORT\_OFFLOAD\_BLOCK\_LIST structure in the state tree:

<a href="" id="ndis-status-success"></a>NDIS\_STATUS\_SUCCESS  
The offload target successfully terminated the offload of the state object that is referenced by the NDIS\_MINIPORT\_OFFLOAD\_BLOCK\_LIST structure. If this structure is followed by a delegated state structure (*XXX*\_OFFLOAD\_STATE\_DELEGATED), the offload target successfully wrote the delegated variable values for that state object to the delegated state structure.

<a href="" id="ndis-status-failure"></a>NDIS\_STATUS\_FAILURE  
The terminate operation did not succeed. Such a failure is caused by a catastrophic failure that resulted in the loss of the state object that was to be terminated.

If corrupted hardware state prevents the offload target from completing the terminate offload operation, the offload target must do the following:

1.  Call **NdisMTerminateOffloadComplete** with a status value of NDIS\_STATUS\_FAILURE.

2.  Call the [**NdisTcpOffloadEventHandler**](https://msdn.microsoft.com/library/windows/hardware/ff564595) function with the *EventType* parameter set to **TcpIndicateRetrieve** and the *EventSpecificInformation* parameter set to **HardwareFailure**.

3.  Call the **NdisTcpOffloadEventHandler** function with the EventType parameter set to TcpIndicateAbort.

4.  When the host stack calls the [**MiniportTerminateOffload**](https://msdn.microsoft.com/library/windows/hardware/ff559468) function, complete any outstanding calls to the [*MiniportTcpOffloadSend*](https://msdn.microsoft.com/library/windows/hardware/ff559464) and [*MiniportTcpOffloadReceive*](https://msdn.microsoft.com/library/windows/hardware/ff559460) functions with a status value of NDIS\_STATUS\_REQUEST\_ABORTED in each NET\_BUFFER\_LIST structure.

5.  Call the [**NdisMTerminateOffloadComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563685) function.

 

 





