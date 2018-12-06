---
title: Determining Task Offload Capabilities
description: Determining Task Offload Capabilities
ms.assetid: 9348a595-7bc0-467e-aeaf-e23100c99524
keywords:
- task offload WDK TCP/IP transport , capabilities
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Determining Task Offload Capabilities





NDIS supports task offload services that are enhanced forms of the NDIS 5.1 and earlier task offload services. For more information about how to determine connection offload capabilities, see [Determining Connection Offload Capabilities](determining-connection-offload-capabilities.md).

NDIS provides the offload hardware capabilities and the current configuration of the underlying miniport adapter to protocol drivers in the [**NDIS\_BIND\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff564832) structure. NDIS provides the task offload hardware capabilities and current configuration of the underlying miniport adapter to filter drivers in the [**NDIS\_FILTER\_ATTACH\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff565481) structure.

Administrative applications use object identifier (OID) queries to obtain task offload capabilities of a miniport adapter. However, overlying drivers should avoid using OID queries. Protocol drivers must handle changes in the task offload capabilities that underlying drivers report. Miniport drivers can report changes in task offload capabilities in status indications. For a list of status indications, see [NDIS 6.0 TCP/IP Offload Status Indications](https://msdn.microsoft.com/library/windows/hardware/ff567880).

Administrative applications (or overlying drivers) can determine the current task offload configuration of a network interface card (NIC) by querying the [OID\_TCP\_OFFLOAD\_CURRENT\_CONFIG](https://msdn.microsoft.com/library/windows/hardware/ff569805) OID.

The [**NDIS\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff566599) structure that is associated with [OID\_TCP\_OFFLOAD\_CURRENT\_CONFIG](https://msdn.microsoft.com/library/windows/hardware/ff569805) specifies the following:

-   The header information, which includes the task offload version that the TCP/IP transport supports.

-   The checksum offload information, in an [**NDIS\_TCP\_IP\_CHECKSUM\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff567878) structure.

-   The large send offload version 1 (LSOV1) information, in an [**NDIS\_TCP\_LARGE\_SEND\_OFFLOAD\_V1**](https://msdn.microsoft.com/library/windows/hardware/ff567883) structure.

-   The Internet protocol security (IPsec) information, in an [**NDIS\_IPSEC\_OFFLOAD\_V1**](https://msdn.microsoft.com/library/windows/hardware/ff565796) structure.

-   The large send offload version 2 (LSOV2) information, in an [**NDIS\_TCP\_LARGE\_SEND\_OFFLOAD\_V2**](https://msdn.microsoft.com/library/windows/hardware/ff567884) structure.

-   The Internet protocol security (IPsecvOV) information in an [**NDIS\_IPSEC\_OFFLOAD\_V2**](https://msdn.microsoft.com/library/windows/hardware/ff565808) structure.

The following topics contain specific information for each type of offload service:

-   [Reporting a NIC's Checksum Capabilities](reporting-a-nic-s-checksum-capabilities.md)
-   [Reporting a NIC's LSOV1 TCP-Packet-Segmentation Capabilities](reporting-a-nic-s-lsov1-tcp-packet-segmentation-capabilities.md)
-   [Reporting a NIC's LSOV2 TCP-Packet-Segmentation Capabilities](reporting-a-nic-s-lsov2-tcp-packet-segmentation-capabilities.md)
-   [Reporting a NIC's IPsec Capabilities](reporting-a-nic-s-ipsec-capabilities.md)
    - \[The IPsec Task Offload feature is deprecated and should not be used.\]

 

 





