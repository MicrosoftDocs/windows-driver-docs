---
title: Reporting a NIC's IPsec Capabilities
description: Reporting a NIC's IPsec Capabilities
ms.assetid: 6ed02d4a-9b5e-4245-a3f9-f0b5fc8366a7
keywords:
- task offload WDK TCP/IP transport , IPsec tasks
- IPsec offload WDK TCP/IP transport , capabilities
- IPsec offload WDK TCP/IP transport
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reporting a NIC's IPsec Capabilities

\[The IPsec Task Offload feature is deprecated and should not be used.\]




An NDIS miniport driver specifies the current Internet protocol security (IPsec) offload configuration of a NIC in an [**NDIS\_IPSEC\_OFFLOAD\_V1**](https://msdn.microsoft.com/library/windows/hardware/ff565796) structure.Miniport drivers must include the current IPsec offload configuration in the [**NDIS\_MINIPORT\_ADAPTER\_OFFLOAD\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565930) structure. Miniport drivers call the [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) function from the [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function and pass in the information in NDIS\_MINIPORT\_ADAPTER\_OFFLOAD\_ATTRIBUTES.

Miniport drivers must report changes in the IPsec offload capabilities, if any, in the [**NDIS\_STATUS\_TASK\_OFFLOAD\_CURRENT\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff567424) status indication.

In response to a query of [OID\_TCP\_OFFLOAD\_CURRENT\_CONFIG](https://msdn.microsoft.com/library/windows/hardware/ff569805), NDIS includes the NDIS\_IPSEC\_OFFLOAD\_V1 structure in the [**NDIS\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff566599) structure that NDIS returns in the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure. NDIS uses the information that the miniport driver provided.

A miniport driver indicates the following information in the NDIS\_IPSEC\_OFFLOAD\_V1 structure:

-   Encapsulation settings, in the **Encapsulation** member. For more information about this member, see the Remarks section in [**NDIS\_IPSEC\_OFFLOAD\_V1**](https://msdn.microsoft.com/library/windows/hardware/ff565796).

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

 

 






