---
title: Reporting a NIC's Connection Offload Capabilities
description: Reporting a NIC's Connection Offload Capabilities
keywords:
- connection offload WDK TCP/IP transport , reporting capabilities
- reporting connection offload capabilities
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reporting a NIC's Connection Offload Capabilities





An NDIS miniport driver specifies the current connection offload configuration of a NIC in an [**NDIS\_TCP\_CONNECTION\_OFFLOAD**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_tcp_connection_offload) structure. Miniport drivers must include the current connection offload configuration in the [**NDIS\_MINIPORT\_ADAPTER\_OFFLOAD\_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_offload_attributes) structure. Miniport drivers call the [**NdisMSetMiniportAttributes**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsetminiportattributes) function from the [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function and pass in the information in NDIS\_MINIPORT\_TCP\_CONNECTION\_OFFLOAD\_ATTRIBUTES.

Miniport drivers must report changes in the connection offload capabilities. The drivers request the stack to pause and upload all of the connections by issuing an status indication. (For information on NDIS\_STATUS\_OFFLOAD\_PAUSE, see [Full TCP Offload](full-tcp-offload.md).) After any configuration changes are complete, the drivers request the stack to restart and re-query the miniport adapter's offload capabilities by issuing an status indication. (For information on NDIS\_STATUS\_OFFLOAD\_RESUME, see Full TCP Offload.)

In response to a query of [OID\_TCP\_CONNECTION\_OFFLOAD\_CURRENT\_CONFIG](./oid-tcp-connection-offload-current-config.md), NDIS returns the [**NDIS\_TCP\_CONNECTION\_OFFLOAD**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_tcp_connection_offload) structure in the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure. NDIS uses the information that the miniport driver provided.

For more information about specifying connection offload capabilities, see Initializing an Offload Target in the [NDIS 6.0 TCP chimney offload documentation](full-tcp-offload.md).

 

