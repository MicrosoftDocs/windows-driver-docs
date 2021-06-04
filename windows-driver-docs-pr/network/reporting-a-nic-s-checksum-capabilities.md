---
title: Reporting a NIC's Checksum Capabilities
description: Reporting a NIC's Checksum Capabilities
keywords:
- task offload WDK TCP/IP transport , checksum tasks
- checksum tasks WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reporting a NIC's Checksum Capabilities





An NDIS miniport driver reports whether a NIC is currently configured to calculate and validate IP, TCP, and UDP checksums in an [**NDIS\_TCP\_IP\_CHECKSUM\_OFFLOAD**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_tcp_ip_checksum_offload) structure. Miniport drivers must include the current checksum offload configuration in the [**NDIS\_MINIPORT\_ADAPTER\_OFFLOAD\_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_offload_attributes) structure. Miniport drivers call the [**NdisMSetMiniportAttributes**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsetminiportattributes) function from the [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function and pass in the information in NDIS\_MINIPORT\_ADAPTER\_OFFLOAD\_ATTRIBUTES.

Miniport drivers must report changes in the current checksum offload configuration, if any, in the [**NDIS\_STATUS\_TASK\_OFFLOAD\_CURRENT\_CONFIG**](./ndis-status-task-offload-current-config.md) status indication.

In response to a query of [OID\_TCP\_OFFLOAD\_CURRENT\_CONFIG](./oid-tcp-offload-current-config.md), NDIS includes the NDIS\_TCP\_IP\_CHECKSUM\_OFFLOAD structure in the [**NDIS\_OFFLOAD**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_offload) structure that NDIS returns in the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure. NDIS uses the information that the miniport driver provided.

A miniport driver indicates the following checksum information for IPv4 and IPv6 send and receive packets:

-   The types of checksums (IP, TCP, or UDP) that a NIC can calculate for send packets and can validate for receive packets.

-   Encapsulation settings, in the **Encapsulation** member. For more information about this member, see the Remarks section in [**NDIS\_TCP\_IP\_CHECKSUM\_OFFLOAD**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_tcp_ip_checksum_offload).

-   Whether the NIC can calculate or validate (or calculate and validate) checksums for a packet whose IP headers contain IPv4 options.

-   Whether the NIC can calculate or validate (or calculate and validate) checksums for an IPv6 packet whose IP headers contain IPv6 extension headers.

-   Whether the NIC can calculate or validate (or calculate and validate) checksums for a packet whose TCP header contain TCP options.

## Related topics


[Determining Task Offload Capabilities](determining-task-offload-capabilities.md)

 

