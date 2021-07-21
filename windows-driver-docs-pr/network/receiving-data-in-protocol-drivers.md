---
title: Receiving Data in Protocol Drivers
description: Receiving Data in Protocol Drivers
keywords:
- receiving data WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Receiving Data in Protocol Drivers





The following figure illustrates a basic receive operation, which involves a protocol driver, NDIS, and underlying drivers in a driver stack.

![diagram illustrating a basic receive operation, which involves a protocol driver, ndis, and underlying drivers in a driver stack.](images/protocolreceive.png)

NDIS calls a protocol driver's [*ProtocolReceiveNetBufferLists*](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_receive_net_buffer_lists) function to process receive indications that come from underlying drivers. NDIS calls *ProtocolReceiveNetBufferLists* after an underlying driver calls a receive indication function (for example, [**NdisMIndicateReceiveNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismindicatereceivenetbufferlists)) to indicate received network data or loop-back data.

If the **NDIS\_RECEIVE\_FLAGS\_RESOURCES** flag in the *ReceiveFlags* parameter of [*ProtocolReceiveNetBufferLists*](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_receive_net_buffer_lists) is not set, the protocol driver retains ownership of the [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structures until it calls the [**NdisReturnNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisreturnnetbufferlists) function. If NDIS sets the **NDIS\_RECEIVE\_FLAGS\_RESOURCES** flag, the protocol driver cannot retain the **NET\_BUFFER\_LIST** structure and the associated resources. The set **NDIS\_RECEIVE\_FLAGS\_RESOURCES** flag indicates that an underlying driver is running low on receive resources. In this case, the *ProtocolReceiveNetBufferLists* function should copy the received data into protocol-allocated storage and return as quickly as possible.

**Note**  NDIS can change the flags that an underlying driver indicates. For example, if a miniport driver sets the **NDIS\_RECEIVE\_FLAGS\_RESOURCES** flag in the *ReceiveFlags* parameter of the [**NdisMIndicateReceiveNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismindicatereceivenetbufferlists) function, NDIS can copy the indicated data and pass the copy to [*ProtocolReceiveNetBufferLists*](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_receive_net_buffer_lists) with the **NDIS\_RECEIVE\_FLAGS\_RESOURCES** flag cleared.

 

**Note**  If the **NDIS\_RECEIVE\_FLAGS\_RESOURCES** flag is set, the protocol driver must retain the original set of [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structures in the linked list. For example, when this flag is set the driver might process the structures and indicate them up the stack one at a time but before the function returns it must restore the original linked list.

 

Protocol drivers call the [**NdisReturnNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisreturnnetbufferlists) function to release ownership of a list of [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structures, along with the associated [**NET\_BUFFER**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer) structures, and network data.

 

