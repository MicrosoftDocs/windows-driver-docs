---
title: Obtaining and Updating Power Management Parameters
description: Obtaining and Updating Power Management Parameters
ms.assetid: 46c4d2ab-e6d9-4d23-bf40-0037b80b01af
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Obtaining and Updating Power Management Parameters





Protocol drivers can use the [OID\_PM\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff569768) OID to query the hardware capabilities of a network adapter that is currently enabled. After a successful return from the query, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to an [**NDIS\_PM\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff566759) structure.

Protocol drivers can also use OID\_PM\_PARAMETERS as a set request to enable or disable the current hardware capabilities of a network adapter. The protocol driver provides a pointer to an NDIS\_PM\_PARAMETERS structure in the **InformationBuffer** member of the NDIS\_OID\_REQUEST structure.

**Note**  Protocol drives cannot disable capabilities that were enabled by other protocol drivers. If none of the protocol drivers enable a capability, that capability is unused.

 

**Note**  NDIS enables magic packet and low power on disconnect capabilities based on the user settings, and these capabilities cannot be disabled by protocol drivers.

 

NDIS\_PM\_PARAMETERS includes the following information:

<a href="" id="enabledwolpacketpatterns"></a>**EnabledWoLPacketPatterns**  
Contains flags that correspond to capabilities that the miniport driver reported in the **SupportedWoLPacketPatterns** member of the [**NDIS\_PM\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566748) structure. For example, the network adapter is enabled to generate a wake-up event when it receives a bitmap, a WOL magic packet, or an EAP over LAN (EAPOL) request identifier message. For a complete list of the patterns that are possible in the current operating system, see the [**NDIS\_PM\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff566759) reference page.

<a href="" id="enabledprotocoloffloads"></a>**EnabledProtocolOffloads**  
Contains flags that correspond to capabilities that the miniport driver reported in the **SupportedProtocolOffloads** member of the [**NDIS\_PM\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566748) structure. NDIS uses these flags to enable or disable the low power protocol offload capabilities on a network adapter. For example, the network adapter offload for IPv4 ARP, IPv6 Neighbor Solicitation (NS), or IEEE 802.11 robust secure network (RSN) 4-way and 2-way handshake is enabled. For a complete list of the protocol offloads that are supported in the current operating system, see the [**NDIS\_PM\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff566759) reference page.

<a href="" id="wakeupflags"></a>**WakeUpFlags**  
Contains flags that NDIS uses to enable or disable wake-up capabilities on a network adapter.

For NDIS 6.20, the NDIS\_PM\_WAKE\_ON\_LINK\_CHANGE\_ENABLED flag enables the capability to wake on a link change (media connect). For more information about this flag, see [Low Power on Media Disconnect](low-power-on-media-disconnect.md).

Starting with NDIS 6.30, the NDIS\_PM\_SELECTIVE\_SUSPEND\_ENABLED flag enables the support for NDIS selective suspend on underlying USB network adapters. For more information, see [NDIS Selective Suspend](ndis-selective-suspend.md).

When a driver sets the [OID\_PM\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff569768) OID, NDIS completes the request without forwarding it to the miniport driver. NDIS stores the requested settings and combines them with the settings from other such requests.

Before NDIS transitions the network adapter to the low power state, NDIS sends a set request to the miniport driver that contains the combined settings from all of the requests that NDIS stored. For more information about setting a low power state, see [Low Power for Wake on LAN](low-power-for-wake-on-lan.md).

The capabilities that are currently enabled can be a subset of the capabilities that the hardware supports. For more information about the capabilities that the hardware supports, see [Reporting Power Management Capabilities](reporting-power-management-capabilities.md).

 

 





