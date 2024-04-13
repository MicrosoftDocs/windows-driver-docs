---
title: Pausing a Binding
description: Pausing a Binding
keywords:
- protocol drivers WDK networking , binding pause
- NDIS protocol drivers WDK , binding pause
- binding pause WDK networking
- binding states WDK networking
- pausing binding for protocol driver
ms.date: 04/20/2017
---

# Pausing a Binding





After NDIS sends a protocol driver a network Plug and Play (PnP) pause event notification for a binding, the binding enters the Pausing state.

To notify the protocol driver of the PnP pause event, NDIS calls the [*ProtocolNetPnPEvent*](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_net_pnp_event) function with the **NetEvent** member of the [**NET\_PNP\_EVENT\_NOTIFICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_net_pnp_event_notification) structure is set to **NetEventPause**. The **Buffer** member contains an [**NDIS\_PROTOCOL\_PAUSE\_PARAMETERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_protocol_pause_parameters) structure.

For a binding in the Pausing state, the protocol driver:

-   Should not initiate any new send requests.

-   Must wait for outstanding send requests to complete. The pause operation is not complete until NDIS calls the [**ProtocolSendNetBufferListsComplete**](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_send_net_buffer_lists_complete) function for all of the driver's outstanding send requests.

-   Should handle receive indications as usual. The underlying miniport driver waits for outstanding receive data to return before completing a pause operation. This ensures that there are no ongoing receive operations in the driver stack after the miniport driver is paused.

-   Should return new receive indications to NDIS immediately. If necessary, the driver can copy such receive indications before it returns them.

For more information about protocol driver send and receive operations, see [Protocol Driver Send and Receive Operations](protocol-driver-send-and-receive-operations.md).

A binding enters the Paused state after the protocol driver is done returning outstanding receive indications for the binding and NDIS has completed all of the outstanding send requests for the binding.

For a binding in the Paused state, the protocol driver:

-   Must not make any send requests.

-   Should return receive indications immediately. If necessary, the driver can copy such receive indications before it returns them.

 

