---
title: Adding and Deleting Wake on LAN Patterns
description: Adding and Deleting Wake on LAN Patterns
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Adding and Deleting Wake on LAN Patterns





To add a wake-on-LAN (WOL) pattern, NDIS protocol drivers issue an OID set request of [OID\_PM\_ADD\_WOL\_PATTERN](./oid-pm-add-wol-pattern.md). The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure contains a pointer to an [**NDIS\_PM\_WOL\_PATTERN**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_pm_wol_pattern) structure. Protocol drivers should specify a WOL packet if that WOL packet is supported by a network adapter. When the network adapter does not support the WOL packet, the protocol driver should use the WOL bitmap wake method.

NDIS\_PM\_WOL\_PATTERN includes the following information:

<a href="" id="priority"></a>**Priority**  
Contains the priority of the WOL pattern. If an overlying driver adds a higher priority WOL pattern when there are no resources available for more WOL patterns, NDIS might remove a lower priority WOL pattern to free resources. Miniport drivers should ignore this member. A protocol driver can specify any priority that is within the pre-defined range from NDIS\_PM\_WOL\_PRIORITY\_LOWEST to NDIS\_PM\_WOL\_PRIORITY\_HIGHEST.

<a href="" id="wolpackettype"></a>**WoLPacketType**  
Contains an [**NDIS\_PM\_WOL\_PACKET**](/windows-hardware/drivers/ddi/ntddndis/ne-ntddndis-_ndis_pm_wol_packet) enumeration value that specifies the type of the WOL packet.

<a href="" id="friendlyname"></a>**FriendlyName**  
Contains an [**NDIS\_PM\_COUNTED\_STRING**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_pm_counted_string) structure that contains the user-readable description of the WOL packet.

<a href="" id="patternid"></a>**PatternId**  
Contains an NDIS-provided value that identifies the WOL pattern. Before NDIS sends the [OID\_PM\_ADD\_WOL\_PATTERN](./oid-pm-add-wol-pattern.md) OID request down to the underlying NDIS drivers or completes the request to the overlying driver, NDIS sets **PatternId** to a value that is unique among the WOL patterns on a network adapter.

<a href="" id="nextwolpatternoffset"></a>**NextWoLPatternOffset**  
Contains the offset (from the beginning of the OID request **InformationBuffer**) of one [**NDIS\_PM\_WOL\_PATTERN**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_pm_wol_pattern) structure to the next NDIS\_PM\_WOL\_PATTERN structure in a list for the [OID\_PM\_WOL\_PATTERN\_LIST](./oid-pm-wol-pattern-list.md) OID. For more information about OID\_PM\_WOL\_PATTERN\_LIST, see [Obtaining the Current Settings of WOL Patterns](obtaining-the-current-settings-of-wol-patterns.md).

<a href="" id="wolpattern"></a>**WoLPattern**  
Contains one of the **IPv4TcpSynParameters**, **IPv6TcpSynParameters**, **EapolRequestIdMessageParameters**, or **WoLBitMapPattern** structures in a union.

<a href="" id="ipv4tcpsynparameters"></a>**IPv4TcpSynParameters**  
Contains IPv4 TCP synchronize (SYN) information.

<a href="" id="ipv6tcpsynparameters"></a>**IPv6TcpSynParameters**  
Contains IPv6 TCP SYN information.

<a href="" id="eapolrequestidmessageparameters"></a>**EapolRequestIdMessageParameters**  
Contains 802.1X EAP over LAN (EAPOL) request identity message parameters.

<a href="" id="wolbitmappattern"></a>**WoLBitMapPattern**  
Contains a WOL bitmap pattern specification.

NDIS assigns an identifier that is unique for network adapter to every WOL pattern. The pattern identifier is a unique value for each of the patterns that are set on a network adapter. However, the pattern identifier is not globally unique across all network adapters. NDIS passes the identifier to the underlying network adapter when NDIS sends the [OID\_PM\_ADD\_WOL\_PATTERN](./oid-pm-add-wol-pattern.md) OID request to the miniport driver. If adding the WOL pattern is successful, NDIS returns the identifier to the overlying driver that added the WOL pattern. The overlying driver uses the identifier to remove a previously added WOL pattern. The pattern identifier is also used in status indications to the overlying drivers when a WOL pattern is removed from a network adapter.

Protocol drivers must issue the OID set request of [OID\_PM\_REMOVE\_WOL\_PATTERN](./oid-pm-remove-wol-pattern.md) to remove all of the patterns that they added to a network adapter before they close a binding to that network adapter. The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure contains a pointer to a pattern identifier.

User-mode applications use the GUID\_PM\_REMOVE\_WOL\_PATTERN WMI GUID to remove a previously added WOL pattern from a network adapter. NDIS translates this WMI request to the OID set request of [OID\_PM\_REMOVE\_WOL\_PATTERN](./oid-pm-remove-wol-pattern.md) for the network adapter. NDIS deletes all of the WOL patterns that an application added from the network adapter before it halts the network adapter.

NDIS allows multiple NDIS protocol drivers to add WOL patterns to the same network adapter. To ensure that the right set of WOL patterns have been set when the number of requested WOL patterns is higher than what a network adapter can support, protocol drivers assign a priority to each requested WOL pattern in the **Priority** member of the NDIS\_PM\_WOL\_PATTERN structure. When NDIS cannot add a new high priority WOL pattern because the network adapter is out of resources, NDIS deletes one of the lower priority patterns (if any) and attempts to add the high priority pattern again.

**Note**  A miniport driver should fail a pattern add request and return the STATUS\_NDIS\_PM\_WOL\_PATTERN\_LIST\_FULL status code to allow NDIS to re-prioritize the patterns.

 

If NDIS deletes one of the lower priority patterns, it notifies the overlying driver that set the deleted pattern with an [**NDIS\_STATUS\_PM\_WOL\_PATTERN\_REJECTED**](./ndis-status-pm-wol-pattern-rejected.md) status indication. The **StatusBuffer** member of the [**NDIS\_STATUS\_INDICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_status_indication) structure contains a ULONG for the WOL pattern identifier of the rejected WOL pattern. NDIS provided the WOL pattern identifier in the **PatternId** member of the [**NDIS\_PM\_WOL\_PATTERN**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_pm_wol_pattern) structure.

For wireless network adapter's that might use an infrastructure element to offload the patterns as it roams across the infrastructure, a new infrastructure element might not support the same capabilities and the miniport driver can send an [**NDIS\_STATUS\_PM\_WOL\_PATTERN\_REJECTED**](./ndis-status-pm-wol-pattern-rejected.md) status indication with an appropriate status code.

 

