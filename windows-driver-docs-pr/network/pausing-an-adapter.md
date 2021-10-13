---
title: Pausing an Adapter
description: Pausing an Adapter
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





NDIS calls a miniport driver's [*MiniportPause*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_pause) function to initiate a pause operation. The adapter remains in the Pausing state until the pause operation is complete.

In the Pausing state, the miniport driver must complete outstanding receive operations. The driver must also complete any outstanding send operations and it should reject any new send requests.

To complete receive operations, the driver waits for all calls to the [**NdisMIndicateReceiveNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismindicatereceivenetbufferlists) function to return and NDIS must return all outstanding [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structures to the miniport driver's [*MiniportReturnNetBufferLists*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_return_net_buffer_lists) function.

To complete outstanding send operations, the miniport driver should call the [**NdisMSendNetBufferListsComplete**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsendnetbufferlistscomplete) function for all of the outstanding NET\_BUFFER\_LIST structures. The driver should reject any new send requests made to its [*MiniportSendNetBufferLists*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_send_net_buffer_lists) function immediately.

After a miniport driver completes all outstanding send and receive operations, the driver must complete the pause request either synchronously or asynchronously. If the pause operation is completed asynchronously, the driver calls [**NdisMPauseComplete**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismpausecomplete) to complete the pause request. After completing the pause request, the miniport driver is in the Paused state.

NDIS does not initiate other Plug and Play operations, such as halt, initialize, power change, or restart operations, while the miniport driver is in the Pausing state. NDIS can initiate these Plug and Play operations after a miniport driver is in the Paused state.

 

