---
title: Reporting a NIC's IPsec Capabilities
description: Reporting a NIC's IPsec Capabilities
keywords:
- task offload WDK TCP/IP transport , IPsec tasks
- IPsec offload WDK TCP/IP transport , capabilities
- IPsec offload WDK TCP/IP transport
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reporting a NIC's IPsec Capabilities

\[The IPsec Task Offload feature is deprecated and should not be used.\]




An NDIS miniport driver specifies the current Internet protocol security (IPsec) offload configuration of a NIC in an [**NDIS\_IPSEC\_OFFLOAD\_V1**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_ipsec_offload_v1) structure.Miniport drivers must include the current IPsec offload configuration in the [**NDIS\_MINIPORT\_ADAPTER\_OFFLOAD\_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_offload_attributes) structure. Miniport drivers call the [**NdisMSetMiniportAttributes**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsetminiportattributes) function from the [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function and pass in the information in NDIS\_MINIPORT\_ADAPTER\_OFFLOAD\_ATTRIBUTES.

Miniport drivers must report changes in the IPsec offload capabilities, if any, in the [**NDIS\_STATUS\_TASK\_OFFLOAD\_CURRENT\_CONFIG**](./ndis-status-task-offload-current-config.md) status indication.

In response to a query of [OID\_TCP\_OFFLOAD\_CURRENT\_CONFIG](./oid-tcp-offload-current-config.md), NDIS includes the NDIS\_IPSEC\_OFFLOAD\_V1 structure in the [**NDIS\_OFFLOAD**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_offload) structure that NDIS returns in the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure. NDIS uses the information that the miniport driver provided.

A miniport driver indicates the following information in the NDIS\_IPSEC\_OFFLOAD\_V1 structure:

-   Encapsulation settings, in the **Encapsulation** member. For more information about this member, see the Remarks section in [**NDIS\_IPSEC\_OFFLOAD\_V1**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_ipsec_offload_v1).

-   Whether a NIC can perform combined IPsec operations on a packet--that is, whether the NIC can process a packet that contains both an authentication header (AH) and an encapsulating security payload (ESP) in a packet with the following format:

    \[IP\]\[AH\]\[ESP\]\[rest of packet\]

-   Whether a NIC can perform IP security processing on both the transport-mode portion and the tunnel-mode portion of send and receive packets. The transport-mode portion of a packet pertains to an end-to-end security association, and the tunnel-mode portion of a packet pertains to a tunnel security association.

-   Whether a NIC can perform IP security operations on packets if the packet's IP headers contain IP options.

A miniport driver specifies the following capabilities of a NIC to calculate or validate (or calculate and validate) encrypted checksums for AH payloads and authentication information:

-   The integrity algorithms (MD5 or SHA 1) that the NIC can use

-   Whether the NIC can process AH security payloads for:
    -   The transport-mode portion of a packet
    -   The tunnel-mode portion of a packet
    -   Send packets
    -   Receive packets

A miniport driver specifies the following capabilities of a NIC to process ESP payloads:

-   The confidentiality algorithms (DES, triple DES, or both) that the NIC can use

-   Whether the NIC supports null encryption (that is, the ESP payload without encryption but with authentication hashes)

-   Whether the NIC can do ESP processing for:
    -   The transport-mode portion of a packet
    -   The tunnel-mode portion of a packet
    -   Send packets
    -   Receive packets

## Related topics


[Determining Task Offload Capabilities](determining-task-offload-capabilities.md)

 

