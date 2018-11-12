---
title: Introduction to IPsec Offload Version 2
description: Introduction to IPsec Offload Version 2
ms.assetid: d8fd0bf8-f7b6-44ad-a3dc-f10bb20ce651
keywords:
- IPsecOV2 WDK TCP/IP transport , about IPsecOV2
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Introduction to IPsec Offload Version 2

\[The IPsec Task Offload feature is deprecated and should not be used.\]




IPsec offload version 2 (IPsecOV2) extends services that are provided in IPsec offload version 1 (IPsecOV1). For more information about IPsecOV1 offload and IPsec, see [IPsec Offload Version 1](ipsec-offload-version-1.md).

An NDIS 6.1 and later miniport driver reports the IPsecOV2 offload capabilities of a miniport adapter to NDIS. To report IPsec capabilities:

-   During initialization, a miniport driver reports the task offload default configuration and the hardware capabilities of a miniport adapter in the [**NDIS\_MINIPORT\_ADAPTER\_OFFLOAD\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565930) structure.

-   If the configured capabilities change, the miniport driver reports the current configuration with the [**NDIS\_STATUS\_TASK\_OFFLOAD\_CURRENT\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff567424) status indication. The configuration can change if the [OID\_TCP\_OFFLOAD\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff569807) OID sets the current task offload configuration of a miniport adapter. Also, if the hardware configuration under a [MUX intermediate driver](ndis-mux-intermediate-drivers.md) changes, the MUX intermediate driver must report the hardware configuration changes with the [**NDIS\_STATUS\_TASK\_OFFLOAD\_HARDWARE\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff567425) status indication.

NDIS reports the default configuration of the offload capabilities of a miniport adapter to overlying protocol drivers in the [**NDIS\_BIND\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff564832) structure. Overlying protocol drivers can choose IPsecOV2 task offload services from the services that are supported in the current configuration. The [**NDIS\_STATUS\_TASK\_OFFLOAD\_CURRENT\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff567424) status indication ensures that all of the overlying protocol drivers are updated with the new capabilities information.

When reporting hardware capabilities during initialization, the miniport driver must read the standardized keywords from the registry. For more information about IPsecOV2 offload capabilities, see [Reporting a NIC's IPsec Offload Version 2 Capabilities](reporting-a-nic-s-ipsec-offload-version-2-capabilities.md).

**Note**  NDIS provides a direct OID request interface for NDIS 6.1 and later drivers. The [direct OID request path](https://msdn.microsoft.com/library/windows/hardware/ff564736) supports OID requests that are queried or set frequently.

 

IPsecOV2 provides the [OID\_TCP\_TASK\_IPSEC\_OFFLOAD\_V2\_ADD\_SA](https://msdn.microsoft.com/library/windows/hardware/ff569812), [OID\_TCP\_TASK\_IPSEC\_OFFLOAD\_V2\_UPDATE\_SA](https://msdn.microsoft.com/library/windows/hardware/ff569814), and [OID\_TCP\_TASK\_IPSEC\_OFFLOAD\_V2\_DELETE\_SA](https://msdn.microsoft.com/library/windows/hardware/ff569813) direct OID requests to enable protocol drivers to add, update, and delete security associations (SAs). For more information about SAs, see [Managing Security Associations in IPsec Offload Version 2](managing-security-associations-in-ipsec-offload-version-2.md).

A NIC can perform IPsec offload tasks on the send and receive paths. NDIS drivers use the [**NDIS\_IPSEC\_OFFLOAD\_V2\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff565818), [**NDIS\_IPSEC\_OFFLOAD\_V2\_HEADER\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff565812), and [**NDIS\_IPSEC\_OFFLOAD\_V2\_TUNNEL\_NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff565843) structures to access the IPsec out-of-band (OOB) information.

On the send path, the overlying drivers set the handle to the outbound SA and IPsec header information in OOB information in the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure to specify that the NIC should perform IPsecOV2 offload tasks.

On the receive path, after the SA is offloaded, the NIC must perform the IPsec processing on all the received packets that match the capabilities that the miniport driver reported to NDIS. The miniport driver sets the appropriate flags in OOB information in the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure to specify specific offload tasks that the NIC performed and the result of those operations.

For more information about send and receive processing in IPsecOV2, see [Sending Network Data with IPsec Offload Version 2](sending-network-data-with-ipsec-offload-version-2.md) and [Receiving Network Data with IPsec Offload Version 2](receiving-network-data-with-ipsec-offload-version-2.md).

 

 





