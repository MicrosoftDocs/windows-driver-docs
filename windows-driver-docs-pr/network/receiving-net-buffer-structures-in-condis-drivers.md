---
title: Receiving NET_BUFFER Structures in CoNDIS Drivers
description: Receiving NET_BUFFER Structures in CoNDIS Drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Receiving NET\_BUFFER Structures in CoNDIS Drivers





The following figure illustrates a basic CoNDIS receive operation, which involves a protocol driver, NDIS, and a miniport driver.

![diagram illustrating a basic condis receive operation, which involves a protocol driver, ndis, and a miniport driver.](images/netbuffercoreceive.png)

As the preceding figure shows, miniport drivers call the [**NdisMCoIndicateReceiveNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcoindicatereceivenetbufferlists) function to indicate [**NET\_BUFFER**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer) structures to overlying drivers. In most miniport drivers, each NET\_BUFFER structure is attached to a separate [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structure, so protocol drivers can create a subset of the original list of NET\_BUFFER\_LIST structures and forward them to different clients. However, the number of NET\_BUFFER structures that are attached to a NET\_BUFFER\_LIST depends on the driver.

After the miniport driver links all the NET\_BUFFER\_LIST structures, the miniport driver passes a pointer to the first NET\_BUFFER\_LIST structure in the list to the **NdisMCoIndicateReceiveNetBufferLists** function. NDIS examines the NET\_BUFFER\_LIST structures and calls the [**ProtocolCoReceiveNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_co_receive_net_buffer_lists) function of the protocol driver that is associated with the specified virtual connection (VC). NDIS passes a subset of the list that includes only the NET\_BUFFER\_LIST structures that are associated with the correct binding to each protocol driver.

If the NDIS\_RECEIVE\_FLAGS\_STATUS\_RESOURCES flag is set in the *CoReceiveFlags* parameter for a protocol driver's *ProtocolCoReceiveNetBufferLists* function, NDIS regains ownership of the [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structures immediately after *ProtocolCoReceiveNetBufferLists* returns.

If the NDIS\_RECEIVE\_FLAGS\_STATUS\_RESOURCES flag is not set in the *CoReceiveFlags* parameter for a protocol driver's [**ProtocolCoReceiveNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_co_receive_net_buffer_lists) function, the protocol driver can retain ownership of the NET\_BUFFER\_LIST structures. In this case, the protocol driver must return the NET\_BUFFER\_LIST structures by calling the [**NdisReturnNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisreturnnetbufferlists) function.

If a miniport driver runs low on receive resources, it can set the NDIS\_RECEIVE\_FLAGS\_STATUS\_RESOURCES flag in the *CoReceiveFlags* parameter for the [**NdisMCoIndicateReceiveNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcoindicatereceivenetbufferlists) function. In that case, the driver can reclaim ownership of all of the indicated [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structures and embedded [**NET\_BUFFER**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer) structures as soon as **NdisMCoIndicateReceiveNetBufferLists** returns. If a miniport driver indicates NET\_BUFFER structures with the NDIS\_RECEIVE\_FLAGS\_RESOURCES flag set, the protocol drivers must copy the data, so you should avoid using NDIS\_RECEIVE\_FLAGS\_RESOURCES in this way. A miniport driver should detect when it has low receive resources and should complete any steps that are necessary to avoid this situation.

NDIS calls a miniport driver's [*MiniportReturnNetBufferLists*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_return_net_buffer_lists) function after the protocol driver calls **NdisReturnNetBufferLists**.

**Note**  If a miniport driver indicates a [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structure with a given status, NDIS is not required to indicate the NET\_BUFFER\_LIST structure to the overlying drivers with the same status. For example, NDIS could copy a NET\_BUFFER\_LIST structure with the NDIS\_RECEIVE\_FLAGS\_RESOURCES flag set and indicate the copy to the overlying drivers with this flag cleared.

 

NDIS can return NET\_BUFFER\_LIST structures to the miniport driver in any arbitrary order and in any combination. That is, the linked list of NET\_BUFFER\_LIST structures that NDIS returns to a miniport driver by calling [*MiniportReturnNetBufferLists*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_return_net_buffer_lists) can have NET\_BUFFER\_LIST structures from different previous calls to [**NdisMCoIndicateReceiveNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcoindicatereceivenetbufferlists).

Miniport drivers must set the **SourceHandle** member in the [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structures to the same value as the *NdisVcHandle* parameter of **NdisMCoIndicateReceiveNetBufferLists**. so that NDIS can return the NET\_BUFFER\_LIST structures to the correct miniport driver.

Intermediate drivers also set the **SourceHandle** member in the NET\_BUFFER\_LIST structure to the *NdisVcHandle* value. If an intermediate driver forwards a receive indication, the driver must save the **SourceHandle** value that the underlying driver provided before it writes to the **SourceHandle** member. When NDIS returns a forwarded NET\_BUFFER\_LIST structure to the intermediate driver, the intermediate driver must restore the **SourceHandle** that it saved.

 

