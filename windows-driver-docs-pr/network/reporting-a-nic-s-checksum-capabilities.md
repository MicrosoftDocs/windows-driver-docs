---
title: Reporting a NIC's Checksum Capabilities
description: Reporting a NIC's Checksum Capabilities
ms.assetid: a90f8d01-8318-44de-acf0-7903ef7e85e0
keywords:
- task offload WDK TCP/IP transport , checksum tasks
- checksum tasks WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reporting a NIC's Checksum Capabilities





An NDIS miniport driver reports whether a NIC is currently configured to calculate and validate IP, TCP, and UDP checksums in an [**NDIS\_TCP\_IP\_CHECKSUM\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff567878) structure. Miniport drivers must include the current checksum offload configuration in the [**NDIS\_MINIPORT\_ADAPTER\_OFFLOAD\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565930) structure. Miniport drivers call the [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) function from the [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function and pass in the information in NDIS\_MINIPORT\_ADAPTER\_OFFLOAD\_ATTRIBUTES.

Miniport drivers must report changes in the current checksum offload configuration, if any, in the [**NDIS\_STATUS\_TASK\_OFFLOAD\_CURRENT\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff567424) status indication.

In response to a query of [OID\_TCP\_OFFLOAD\_CURRENT\_CONFIG](https://msdn.microsoft.com/library/windows/hardware/ff569805), NDIS includes the NDIS\_TCP\_IP\_CHECKSUM\_OFFLOAD structure in the [**NDIS\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff566599) structure that NDIS returns in the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure. NDIS uses the information that the miniport driver provided.

A miniport driver indicates the following checksum information for IPv4 and IPv6 send and receive packets:

-   The types of checksums (IP, TCP, or UDP) that a NIC can calculate for send packets and can validate for receive packets.

-   Encapsulation settings, in the **Encapsulation** member. For more information about this member, see the Remarks section in [**NDIS\_TCP\_IP\_CHECKSUM\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff567878).

-   Whether the NIC can calculate or validate (or calculate and validate) checksums for a packet whose IP headers contain IPv4 options.

-   Whether the NIC can calculate or validate (or calculate and validate) checksums for an IPv6 packet whose IP headers contain IPv6 extension headers.

-   Whether the NIC can calculate or validate (or calculate and validate) checksums for a packet whose TCP header contain TCP options.

## Related topics


[Determining Task Offload Capabilities](determining-task-offload-capabilities.md)

 

 






