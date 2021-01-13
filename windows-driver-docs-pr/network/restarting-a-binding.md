---
title: Restarting a Binding
description: Restarting a Binding
keywords:
- protocol drivers WDK networking , binding restarts
- NDIS protocol drivers WDK , binding restarts
- binding restarts WDK networking
- binding states WDK networking
- restarting binding for protocol driver
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Restarting a Binding





To restart a binding that is paused, NDIS sends the protocol driver a network Plug and Play (PnP) restart event notification. After the protocol driver receives the restart notification, the affected binding enters the Restarting state.

To send a restart notification, NDIS calls a protocol driver's [*ProtocolNetPnPEvent*](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_net_pnp_event) function. The [**NET\_PNP\_EVENT\_NOTIFICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_net_pnp_event_notification) structure that NDIS passes to *ProtocolNetPnPEvent* specifies **NetEventRestart** in the **NetEvent** member and the **Buffer** member contains a pointer to the [**NDIS\_PROTOCOL\_RESTART\_PARAMETERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_protocol_restart_parameters) structure. NDIS provides a pointer to an [**NDIS\_RESTART\_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_restart_attributes) structure in the **RestartAttributes** member of the NDIS\_PROTOCOL\_RESTART\_PARAMETERS structure.

**Note**  While the binding was paused, NDIS could have reconfigured the driver stack. The new stack configuration can support a different set of capabilities for the underlying adapter. These new capabilities can affect how the protocol driver communicates on a binding.

 

The protocol driver should use the information in the [**NDIS\_PROTOCOL\_RESTART\_PARAMETERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_protocol_restart_parameters) structure to avoid unnecessary OID requests.

In the Restarting state, the protocol driver can:

-   Use OID requests to query the driver stack. For example, the driver can find out about support for receive side scaling by using [OID\_GEN\_RECEIVE\_SCALE\_CAPABILITIES](./oid-gen-receive-scale-capabilities.md).

-   Reallocate [**NET\_BUFFER**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer) and [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) pools, if necessary.

-   Enumerate the list of the underlying filter modules.

-   Use OID requests to reveal new adapter capabilities.

After the driver is ready to resume send and receive operations for the binding, the binding enters the Running state.

 

