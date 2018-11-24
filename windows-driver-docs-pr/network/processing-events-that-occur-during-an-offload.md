---
title: Processing Events That Occur During an Offload
description: Processing Events That Occur During an Offload
ms.assetid: 475fa20c-a9c6-4725-b9b4-c5862483cceb
keywords:
- state offloading process WDK TCP chimney offload , events
- offloading state process WDK TCP chimney offload , events
- events WDK TCP chimney offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Processing Events That Occur During an Offload


\[The TCP chimney offload feature is deprecated and should not be used.\]




An offload target must be able to process the following events while an offload operation is in progress (that is, before the offload target's call to [**NdisMInitiateOffloadComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563604) has returned):

-   Initiating another offload operation

The host stack will not attempt to offload a state object if an offload of that state object is already in progress. However, while an offload operation is in progress, NDIS can call an offload target's [*MiniportInitiateOffload*](https://msdn.microsoft.com/library/windows/hardware/ff559393) function one or more times to initiate one or more additional offload operations of other state objects.

-   Receiving and indicating receive segments

An offload target can start processing receive segments on TCP connections as soon as the necessary state objects for those connections have been offloaded. An offload target must indicate receive segments on offloaded TCP connections only after the operation that offloaded those connections completes (that is, after [**NdisMInitiateOffloadComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563604) has returned). An offload target always indicates such receive segments by calling the [**NdisTcpOffloadReceiveHandler**](https://msdn.microsoft.com/library/windows/hardware/ff564606) function.

Note also that the offload target will not receive the following before an offload operation completes:

-   A send request (a call to the [*MiniportTcpOffloadSend*](https://msdn.microsoft.com/library/windows/hardware/ff559464) function) on a TCP connection that is being offloaded

-   Posted receive buffers (a call to the [*MiniportTcpOffloadReceive*](https://msdn.microsoft.com/library/windows/hardware/ff559460) function) on a TCP connection that is being offloaded

-   An update request (a call to the [**MiniportUpdateOffload**](https://msdn.microsoft.com/library/windows/hardware/ff560463) function) on a state object that is being offloaded

-   A query request (a call to the [**MiniportQueryOffload**](https://msdn.microsoft.com/library/windows/hardware/ff559423) function) on a state object that is being offloaded

-   An invalidate request (a call to the [**MiniportInvalidateOffload**](https://msdn.microsoft.com/library/windows/hardware/ff559406) function) on a state object that is being offloaded

-   A terminate request (a call to the [**MiniportTerminateOffload**](https://msdn.microsoft.com/library/windows/hardware/ff559468) function) on a state object that is being offloaded

-   A forward data request (a call to the [*MiniportTcpOffloadForward*](https://msdn.microsoft.com/library/windows/hardware/ff559458) function) on a TCP connection that is being offloaded

We recommend that an offload target not call the following indication functions while an offload is in progress:

-   [**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600)

-   [**NdisMOffloadEventIndicate**](https://msdn.microsoft.com/library/windows/hardware/ff563619)

-   [**NdisTcpOffloadEventHandler**](https://msdn.microsoft.com/library/windows/hardware/ff564595)

-   [**NdisTcpOffloadReceiveHandler**](https://msdn.microsoft.com/library/windows/hardware/ff564606)

 

 





