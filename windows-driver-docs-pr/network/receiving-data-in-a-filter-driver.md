---
title: Receiving Data in a Filter Driver
description: Receiving Data in a Filter Driver
keywords:
- receiving data WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Receiving Data in a Filter Driver





Filter drivers can initiate receive indications or filter receive indications from underlying drivers. When a miniport driver calls the [**NdisMIndicateReceiveNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismindicatereceivenetbufferlists) function, NDIS submits the specified [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structure to the lowest overlying filter module in the driver stack.

### Receive Indications Initiated by a Filter Driver

The following figure illustrates a receive indication that is initiated by a filter driver.

![diagram illustrating a receive indication initiated by a filter driver.](images/filterreceive.png)

Filter drivers call the [**NdisFIndicateReceiveNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfindicatereceivenetbufferlists) function to indicate received data. The **NdisFIndicateReceiveNetBufferLists** function passes the indicated list of [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structures up the stack to overlying drivers. The filter driver allocates the structures from pools that it created during initialization.

If a filter driver sets the **NDIS\_RECEIVE\_FLAGS\_RESOURCES** flag in the *ReceiveFlags* parameter of [**NdisFIndicateReceiveNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfindicatereceivenetbufferlists), this indicates that the filter driver must regain ownership of the [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structures immediately. In this case, NDIS does not call the filter driver's [*FilterReturnNetBufferLists*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_return_net_buffer_lists) function to return the **NET\_BUFFER\_LIST** structures. The filter driver regains ownership immediately after **NdisFIndicateReceiveNetBufferLists** returns.

If a filter driver does not set the **NDIS\_RECEIVE\_FLAGS\_RESOURCES** flag in the *ReceiveFlags* parameter of [**NdisFIndicateReceiveNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfindicatereceivenetbufferlists), NDIS returns the indicated [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structures to the filter driver's [*FilterReturnNetBufferLists*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_return_net_buffer_lists) function. In this case, the filter driver relinquishes ownership of the indicated structures until NDIS returns them to *FilterReturnNetBufferLists*.

**Note**  A filter driver should keep track of receive indications that it initiates and make sure that it does not call the [**NdisFReturnNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfreturnnetbufferlists) function when the receive operation is complete.

 

### Filtering Receive Indications

The following figure illustrates a filtered receive indication that is initiated by an underlying driver.

![diagram illustrating a filtered receive indication initiated by an underlying driver.](images/receivefilter.png)

NDIS calls a filter driver's [*FilterReceiveNetBufferLists*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_receive_net_buffer_lists) function to process receive indications that come from underlying drivers. NDIS calls *FilterReceiveNetBufferLists* after an underlying driver calls a receive indication function (for example, [**NdisMIndicateReceiveNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismindicatereceivenetbufferlists)) to indicate received network data or loopback data.

If the **NDIS\_RECEIVE\_FLAGS\_RESOURCES** flag in the *ReceiveFlags* parameter of [*FilterReceiveNetBufferLists*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_receive_net_buffer_lists) is not set, the filter driver keeps ownership of the [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structures until it calls the [**NdisFReturnNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfreturnnetbufferlists) function.

If the **NDIS\_RECEIVE\_FLAGS\_RESOURCES** flag in the *ReceiveFlags* parameter is set, the filter driver cannot keep the [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structure and the associated underlying driver-allocated resources. This flag can indicate that the underlying driver is running low on receive resources. The [*FilterReceiveNetBufferLists*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_receive_net_buffer_lists) function should return as quickly as possible.

**Note**  If the **NDIS\_RECEIVE\_FLAGS\_RESOURCES** flag is set, the filter driver must retain the original set of [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structures in the linked list. For example, when this flag is set, the driver might process the structures and indicate them up the stack one at a time but before the function returns, it must restore the original linked list.

 

Filter drivers can perform filter operations on received data before indicating the data to overlying drivers. For each buffer submitted to its [*FilterReceiveNetBufferLists*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_receive_net_buffer_lists) function a filter driver can do the following:

-   Pass it on to the next overlying driver by calling [**NdisFIndicateReceiveNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfindicatereceivenetbufferlists). The driver can modify the contents of the buffer. NDIS guarantees the availability of context space (see [NET\_BUFFER\_LIST\_CONTEXT structure](net-buffer-list-context-structure.md)).

    A filter driver can change the status that NDIS passed to [*FilterReceiveNetBufferLists*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_receive_net_buffer_lists) or simply pass it on to [**NdisFIndicateReceiveNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfindicatereceivenetbufferlists).

    **Note**  A filter driver can pass on a buffer with [**NdisFIndicateReceiveNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfindicatereceivenetbufferlists) even if NDIS sets the **NDIS\_RECEIVE\_FLAGS\_RESOURCES** flag in the *ReceiveFlags* parameter of [*FilterReceiveNetBufferLists*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_receive_net_buffer_lists). In this case, the filter driver must not return from *FilterReceiveNetBufferLists* until it regains ownership of the buffer.

     

-   Discard the buffer. If NDIS cleared the **NDIS\_RECEIVE\_FLAGS\_RESOURCES** flag in the *ReceiveFlags* parameter of [*FilterReceiveNetBufferLists*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_receive_net_buffer_lists), call the [**NdisFReturnNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfreturnnetbufferlists) function to discard the buffer. If NDIS set the **NDIS\_RECEIVE\_FLAGS\_RESOURCES** flag in the *ReceiveFlags* parameter of *FilterReceiveNetBufferLists*, take no action and return from *FilterReceiveNetBufferLists* to discard the buffer.

-   Queue the buffer in a local data structure for later processing. If NDIS set the **NDIS\_RECEIVE\_FLAGS\_RESOURCES** flag in the *ReceiveFlags* parameter of [*FilterReceiveNetBufferLists*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_receive_net_buffer_lists), the filter driver must create a copy before returning from *FilterReceiveNetBufferLists*.

-   Copy the buffer and originate a receive indication with the copy. The receive indication is similar to a filter-driver-initiated receive indication. In this case, the driver must return the original buffer to the underlying driver.

The [**NdisFIndicateReceiveNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfindicatereceivenetbufferlists) function passes the indicated list of [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structures up the driver stack to overlying drivers. The receive operation proceeds similarly to a filter-driver-initiated receive operation.

If an overlying driver retained ownership of the buffer, NDIS calls the [*FilterReturnNetBufferLists*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_return_net_buffer_lists) function for the filter module. In its *FilterReturnNetBufferLists* function, the filter driver will undo the operations that it performed on the buffer on the receive indication path.

When the lowest layer filter module indicates that it is done with a buffer, NDIS returns the buffer to the miniport driver. If NDIS cleared the **NDIS\_RECEIVE\_FLAGS\_RESOURCES** flag in the *ReceiveFlags* parameter of [*FilterReceiveNetBufferLists*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_receive_net_buffer_lists), the filter driver calls [**NdisFReturnNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfreturnnetbufferlists) to return the buffer. If NDIS set the **NDIS\_RECEIVE\_FLAGS\_RESOURCES** flag in the *ReceiveFlags* parameter of *FilterReceiveNetBufferLists*, returning from *FilterReceiveNetBufferLists* returns the buffer.

 

