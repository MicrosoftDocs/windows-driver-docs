---
title: Pausing an Adapter
description: Pausing an Adapter
ms.assetid: e24a9886-a1d7-4ca5-bed8-85db4a49ed9c
keywords:
- miniport adapters WDK networking , pausing
- adapters WDK networking , pausing
- Pausing state WDK networking
- Paused state WDK networking
- MiniportPause
- pausing miniport adapters
- stopping miniport adapters
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Pausing an Adapter





NDIS calls a miniport driver's [*MiniportPause*](https://msdn.microsoft.com/library/windows/hardware/ff559418) function to initiate a pause operation. The adapter remains in the Pausing state until the pause operation is complete.

In the Pausing state, the miniport driver must complete outstanding receive operations. The driver must also complete any outstanding send operations and it should reject any new send requests.

To complete receive operations, the driver waits for all calls to the [**NdisMIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff563598) function to return and NDIS must return all outstanding [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures to the miniport driver's [*MiniportReturnNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff559437) function.

To complete outstanding send operations, the miniport driver should call the [**NdisMSendNetBufferListsComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563668) function for all of the outstanding NET\_BUFFER\_LIST structures. The driver should reject any new send requests made to its [*MiniportSendNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff559440) function immediately.

After a miniport driver completes all outstanding send and receive operations, the driver must complete the pause request either synchronously or asynchronously. If the pause operation is completed asynchronously, the driver calls [**NdisMPauseComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563628) to complete the pause request. After completing the pause request, the miniport driver is in the Paused state.

NDIS does not initiate other Plug and Play operations, such as halt, initialize, power change, or restart operations, while the miniport driver is in the Pausing state. NDIS can initiate these Plug and Play operations after a miniport driver is in the Paused state.

 

 





