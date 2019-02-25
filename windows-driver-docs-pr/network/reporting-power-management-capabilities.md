---
title: Reporting Power Management Capabilities
description: Reporting Power Management Capabilities
ms.assetid: cfacd885-e18a-44a5-939d-88e62b573ace
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reporting Power Management Capabilities





Miniport drivers that support NDIS 6.20 and later versions of NDIS report their hardware power management capabilities during initialization. NDIS reports the current capabilities to overlying NDIS protocol drivers during the bind operation. However, NDIS can hide some capabilities from the protocol driver. For example, NDIS might report different capabilities when a user disables some or all of the power management capabilities.

Note that the current power management capabilities that NDIS reports to a protocol driver are not necessarily the same as the hardware capabilities that the miniport driver reported to NDIS.

If an NDIS 6.1 or earlier miniport driver is bound to an NDIS 6.20 protocol driver, NDIS translates the power management capabilities to a format that is supported by the NDIS 6.20 protocol driver. NDIS also translates power management capabilities that an NDIS 6.20 miniport driver reports into a format that is supported by the NDIS 6.1 and earlier overlying drivers.

The hardware capabilities that a miniport driver reports can be enabled or disabled in INF file settings. For more information about power management INF file settings, see [Standardized INF Keywords for Power Management](standardized-inf-keywords-for-power-management.md).

During miniport initialization, a miniport driver initializes an [**NDIS\_PM\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566748) structure with the power management capabilities of the underlying hardware. The miniport driver sets the **PowerManagementCapabilitiesEx** member of the [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923) structure to point to the **NDIS\_PM\_CAPABILITIES** structure.

The [**NDIS\_PM\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566748) structure includes the following information:

**Flags**  
For NDIS 6.20, this member is reserved for NDIS.

Starting with NDIS 6.30, the following flags are defined:

<a href="" id="ndis-pm-wake-packet-indication-supported"></a>NDIS\_PM\_WAKE\_PACKET\_INDICATION\_SUPPORTED  
If this flag is set, the network adapter can save the received packet that caused the adapter to generate a wake-up event.

For more information about this power management capability, see [NDIS Wake Reason Status Indications](ndis-wake-reason-status-indications.md).

<a href="" id="ndis-pm-selective-suspend-supported"></a>NDIS\_PM\_SELECTIVE\_SUSPEND\_SUPPORTED  
If this flag is set, the miniport driver supports NDIS selective suspend for network adapters.

For more information about this power management capability, see [NDIS Selective Suspend](ndis-selective-suspend.md).

<a href="" id="supportedwolpacketpatterns"></a>**SupportedWoLPacketPatterns**  
Contains flags that specify the wake-on-LAN (WOL) packet patterns that a network adapter supports. For example, the network adapter can generate a wake-up event when it receives a bitmap, a WOL magic packet, or an EAP over LAN (EAPOL) request identifier message. For a complete list of the patterns that are supported in the current operating system, see the [**NDIS\_PM\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566748) reference page.

<a href="" id="numtotalwolpatterns"></a>**NumTotalWoLPatterns**  
A **ULONG** value that contains the total number of WOL patterns that a network adapter supports. This is the sum of "number of supported WOL protocol patterns" and "number of supported WOL bitmap patterns."

For example, if your driver supports 8 flexible bitmap patterns, IPv4 TCP SYN (via preset filter), and magic packet, then you would report 9 in NumTotalWoLPatterns. (8 bitmaps + 1 IPv4 TCP SYN = 9)

**Note**  The total number of WOL patterns does not include the magic packet wake-up pattern.

 

For more information about WOL protocol patterns, see [**NDIS\_PM\_WOL\_PATTERN**](https://msdn.microsoft.com/library/windows/hardware/ff566768).

<a href="" id="maxwolpatternsize"></a>**MaxWoLPatternSize**  
Contains the maximum number of bytes that can be compared with a pattern.

<a href="" id="maxwolpatternoffset"></a>**MaxWoLPatternOffset**  
Contains the number of bytes in a packet that can be examined, which starts from the beginning of the MAC header.

<a href="" id="maxwolpacketsavebuffer"></a>**MaxWoLPacketSaveBuffer**  
Contains the number of bytes of a WOL protocol pattern that a miniport driver can save to a buffer and indicate up the driver stack.

<a href="" id="supportedprotocoloffloads"></a>**SupportedProtocolOffloads**  
Contains flags that specify the power management protocol offload features that a network adapter supports. Miniport drivers use these flags to report the low power protocol offload capabilities of a network adapter. For example, the network adapter can support IPv4 ARP offload, IPv6 Neighbor Solicitation (NS), or IEEE 802.11 robust secure network (RSN) 4-way and 2-way handshake. For a complete list of the protocol offloads that are supported in the current operating system, see the [**NDIS\_PM\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566748) reference page.

<a href="" id="numarpoffloadipv4addresses"></a>**NumArpOffloadIPv4Addresses**  
Contains the number of ARP offload IPv4 addresses.

<a href="" id="numnsoffloadipv6addresses"></a>**NumNSOffloadIPv6Addresses**  
Contains the number of network solicitation (NS) offload IPv6 requests that the network adapter supports.

<a href="" id="minmagicpacketwakeup"></a>**MinMagicPacketWakeUp**  
Specifies the lowest device power state from which a network adapter can signal a wake-up event on receipt of a *magic packet*. (A *magic packet* is a packet that contains 16 contiguous copies of the receiving network adapter's Ethernet address.)

<a href="" id="minpatternwakeup"></a>**MinPatternWakeUp**  
Specifies the lowest device power state from which a network adapter can signal a wake-up event on receipt of a network frame that contains a pattern that is specified by the protocol driver.

<a href="" id="minlinkchangewakeup"></a>**MinLinkChangeWakeUp**  
Specifies the lowest device power state from which a network adapter can signal a wake-up event when there is a link change (media connect or disconnect).

<a href="" id="supportedwakeupevents"></a>**SupportedWakeUpEvents**  
Specifies the media-independent wake-up events that a network adapter supports. These events are not specific to media type. For example, these wake-up events include link change events.

<a href="" id="mediaspecificwakeupevents"></a>**MediaSpecificWakeUpEvents**  
Specifies the media-specific wake-up events that a network adapter supports. For example, these events include following:

-   The 802.11 network adapter disassociates with the access point (AP).

-   The mobile broadband (MB) network adapter detects a change in its registration state to the MB Service.

If a miniport driver supports offloading protocols to a network adapter in a low power state, it must support the same low power state for the protocol offload that it supports for a pattern match WOL event; that is, the value that is specified in the **MinPatternWakeUp** or **MinMagicPacketWakeUp** member.

NDIS initializes an [**NDIS\_PM\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566748) structure with the currently available power management capabilities of the underlying network adapter and passes it the protocol overlying protocol drivers during the bind operation. NDIS sets the **PowerManagementCapabilitiesEx** member of the [**NDIS\_BIND\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff564832) structure to point to the NDIS\_PM\_CAPABILITIES structure.

Overlying drivers can use the [OID\_PM\_HARDWARE\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff569767) OID query to obtain the hardware power management capabilities of the network adapter. NDIS handles this OID request on behalf of the miniport driver. NDIS miniport drivers are not required to support the OID\_PM\_HARDWARE\_CAPABILITIES OID request.

Overlying drivers can use the [OID\_PM\_CURRENT\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff569765) OID to query the currently available power management capabilities of a network adapter. NDIS handles this OID request on behalf of the miniport driver. NDIS miniport drivers are not required to support the OID\_PM\_CURRENT\_CAPABILITIES OID request.

 

 





