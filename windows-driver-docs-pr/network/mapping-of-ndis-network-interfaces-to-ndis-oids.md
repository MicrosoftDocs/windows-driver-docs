---
title: Mapping of NDIS Network Interfaces to NDIS OIDs
description: Mapping of NDIS Network Interfaces to NDIS OIDs
ms.assetid: 117f94fd-829d-4ad8-be25-a6a90a8d4c50
keywords:
- NDIS network interfaces WDK , mapping
- network interfaces WDK , mapping
- OIDs WDK networking , network interfaces
- OID requests WDK networking
- proxy interface providers WDK networking
- NDIS proxy interface providers WDK
- NDIS network interfaces
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Mapping of NDIS Network Interfaces to NDIS OIDs





To respond to NDIS interface object requests, NDIS interface providers can cache information that they obtain from underlying drivers and can also issue OID requests to obtain information about underlying interfaces.

As a proxy interface provider, NDIS typically caches information that it receives about miniport adapters and filter modules. The NDIS proxy interface provider uses the cached information, if appropriate, to respond to interface requests. In some cases, the NDIS proxy interface provider issues OIDs to obtain information for interfaces. For example, the primary source of interface information for NDIS 5.*x* and earlier drivers is through OID requests. In NDIS 6.0 drivers, there are additional sources of interface information, such as the [**NDIS\_RESTART\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff567255) and [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923) structures. For more information about alternate sources of information in the OIDs, see the reference page for each OID.

The NDIS proxy interface provider also generates some interface information on behalf of miniport adapters and filter modules. For example, NDIS generates an interface alias (*ifAlias* in RFC 2863) in response to the *ifAlias* request. NDIS defines additional OIDs to obtain such information from NDIS interface providers. For example, [OID\_GEN\_ALIAS](https://msdn.microsoft.com/library/windows/hardware/ff569438) allows an interface provider to specify an *ifAlias* object. Such OIDs are specific to interface providers and are never used to obtain information from other NDIS drivers.

In addition to the OIDs that are specific to interface providers, interface providers must support the other NDIS OIDs that NDIS can use to obtain interface information. NDIS can issue these OIDs to the provider and the provider can issue these OIDs, if necessary, to collect information from underlying interfaces.

**Note**  NDIS defines additional statistics that are not included in RFC 2863. For a list that maps all of the NDIS-supported interface statistics to OIDs, see the members of the [**NDIS\_INTERFACE\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff565736) structure. The table in this topic defines the mapping for statistics that are defined in the RFC 2863 specification for readers that are trying to relate the specification to the NDIS implementation.

 

The following table shows the mapping from the objects that are defined in the management information base (MIB) to NDIS 6.0 OIDs and to OIDs that NDIS might use to obtain information from NDIS 5.*x* and earlier drivers. The table also includes some additional interface objects that are not defined as MIB objects. The interface objects also correspond to members in the [**NDIS\_INTERFACE\_INFORMATION**](ndis-interface-information.md) structure that is associated with the [OID\_GEN\_INTERFACE\_INFO](https://msdn.microsoft.com/library/windows/hardware/ff569589) OID.

**Note**  The NDIS 6.0 OIDs in the table that are marked with a asterisk (\*) prefix are specific to interface providers. The other NDIS 6.0 OIDs can be issued to interface providers and other NDIS drivers.

 

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Interfaces MIB value</th>
<th align="left">NDIS 6.0 OIDs</th>
<th align="left">NDIS 5.x and earlier OIDs</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><em>ifAdminStatus</em></p></td>
<td align="left"><p>* <a href="https://msdn.microsoft.com/library/windows/hardware/ff569437" data-raw-source="[OID_GEN_ADMIN_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff569437)">OID_GEN_ADMIN_STATUS</a></p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p><em>ifAlias</em></p></td>
<td align="left"><p>* <a href="https://msdn.microsoft.com/library/windows/hardware/ff569438" data-raw-source="[OID_GEN_ALIAS](https://msdn.microsoft.com/library/windows/hardware/ff569438)">OID_GEN_ALIAS</a></p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p><em>ifCounterDiscontinuityTime</em></p></td>
<td align="left"><p>* <a href="https://msdn.microsoft.com/library/windows/hardware/ff569581" data-raw-source="[OID_GEN_DISCONTINUITY_TIME](https://msdn.microsoft.com/library/windows/hardware/ff569581)">OID_GEN_DISCONTINUITY_TIME</a></p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p><em>ifHCInBroadcastPkts</em></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569441" data-raw-source="[OID_GEN_BROADCAST_FRAMES_RCV](https://msdn.microsoft.com/library/windows/hardware/ff569441)">OID_GEN_BROADCAST_FRAMES_RCV</a></p></td>
<td align="left"><p>OID_GEN_BROADCAST_FRAMES_RCV</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>ifHCInMulticastPkts</em></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569613" data-raw-source="[OID_GEN_MULTICAST_FRAMES_RCV](https://msdn.microsoft.com/library/windows/hardware/ff569613)">OID_GEN_MULTICAST_FRAMES_RCV</a></p></td>
<td align="left"><p>OID_GEN_MULTICAST_FRAMES_RCV</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>ifHCInOctets</em></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569443" data-raw-source="[OID_GEN_BYTES_RCV](https://msdn.microsoft.com/library/windows/hardware/ff569443)">OID_GEN_BYTES_RCV</a></p></td>
<td align="left"><p>NDIS adds the results from these OIDs to collect the <em>ifHCInOctets</em> value from NDIS 5.<em>x</em> drivers:</p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569577" data-raw-source="[OID_GEN_DIRECTED_BYTES_RCV](https://msdn.microsoft.com/library/windows/hardware/ff569577)">OID_GEN_DIRECTED_BYTES_RCV</a>+</p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569611" data-raw-source="[OID_GEN_MULTICAST_BYTES_RCV](https://msdn.microsoft.com/library/windows/hardware/ff569611)">OID_GEN_MULTICAST_BYTES_RCV</a>+</p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569439" data-raw-source="[OID_GEN_BROADCAST_BYTES_RCV](https://msdn.microsoft.com/library/windows/hardware/ff569439)">OID_GEN_BROADCAST_BYTES_RCV</a></p>
<p>NDIS 6.0 interface providers should also support these OIDs.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>ifHCInUcastPkts</em></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569579" data-raw-source="[OID_GEN_DIRECTED_FRAMES_RCV](https://msdn.microsoft.com/library/windows/hardware/ff569579)">OID_GEN_DIRECTED_FRAMES_RCV</a></p></td>
<td align="left"><p>OID_GEN_DIRECTED_FRAMES_RCV</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>ifHCOutBroadcastPkts</em></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569442" data-raw-source="[OID_GEN_BROADCAST_FRAMES_XMIT](https://msdn.microsoft.com/library/windows/hardware/ff569442)">OID_GEN_BROADCAST_FRAMES_XMIT</a></p></td>
<td align="left"><p>OID_GEN_BROADCAST_FRAMES_XMIT</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>ifHCOutMulticastPkts</em></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569614" data-raw-source="[OID_GEN_MULTICAST_FRAMES_XMIT](https://msdn.microsoft.com/library/windows/hardware/ff569614)">OID_GEN_MULTICAST_FRAMES_XMIT</a></p></td>
<td align="left"><p>OID_GEN_MULTICAST_FRAMES_XMIT</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>ifHCOutOctets</em></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569445" data-raw-source="[OID_GEN_BYTES_XMIT](https://msdn.microsoft.com/library/windows/hardware/ff569445)">OID_GEN_BYTES_XMIT</a></p></td>
<td align="left"><p>NDIS adds the results from these OIDs to collect the <em>ifHCInOctets</em> value from NDIS 5.<em>x</em> drivers:</p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569578" data-raw-source="[OID_GEN_DIRECTED_BYTES_XMIT](https://msdn.microsoft.com/library/windows/hardware/ff569578)">OID_GEN_DIRECTED_BYTES_XMIT</a>+</p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569612" data-raw-source="[OID_GEN_MULTICAST_BYTES_XMIT](https://msdn.microsoft.com/library/windows/hardware/ff569612)">OID_GEN_MULTICAST_BYTES_XMIT</a>+</p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569440" data-raw-source="[OID_GEN_BROADCAST_BYTES_XMIT](https://msdn.microsoft.com/library/windows/hardware/ff569440)">OID_GEN_BROADCAST_BYTES_XMIT</a></p>
<p>NDIS 6.0 interface providers should also support these OIDs.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>ifHCOutUCastPkts</em></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569580" data-raw-source="[OID_GEN_DIRECTED_FRAMES_XMIT](https://msdn.microsoft.com/library/windows/hardware/ff569580)">OID_GEN_DIRECTED_FRAMES_XMIT</a></p></td>
<td align="left"><p>OID_GEN_DIRECTED_FRAMES_XMIT</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>ifHighSpeed</em></p></td>
<td align="left"><p>* <a href="https://msdn.microsoft.com/library/windows/hardware/ff569594" data-raw-source="[OID_GEN_LINK_SPEED_EX](https://msdn.microsoft.com/library/windows/hardware/ff569594)">OID_GEN_LINK_SPEED_EX</a>, * <a href="https://msdn.microsoft.com/library/windows/hardware/ff569655" data-raw-source="[OID_GEN_XMIT_LINK_SPEED](https://msdn.microsoft.com/library/windows/hardware/ff569655)">OID_GEN_XMIT_LINK_SPEED</a>, * <a href="https://msdn.microsoft.com/library/windows/hardware/ff569630" data-raw-source="[OID_GEN_RCV_LINK_SPEED](https://msdn.microsoft.com/library/windows/hardware/ff569630)">OID_GEN_RCV_LINK_SPEED</a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569593" data-raw-source="[OID_GEN_LINK_SPEED](https://msdn.microsoft.com/library/windows/hardware/ff569593)">OID_GEN_LINK_SPEED</a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>ifInDiscards</em></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569628" data-raw-source="[OID_GEN_RCV_DISCARDS](https://msdn.microsoft.com/library/windows/hardware/ff569628)">OID_GEN_RCV_DISCARDS</a></p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p><em>ifInErrors</em></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569629" data-raw-source="[OID_GEN_RCV_ERROR](https://msdn.microsoft.com/library/windows/hardware/ff569629)">OID_GEN_RCV_ERROR</a></p></td>
<td align="left"><p>OID_GEN_RCV_ERROR</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>ifLastChange</em></p></td>
<td align="left"><p>* <a href="https://msdn.microsoft.com/library/windows/hardware/ff569591" data-raw-source="[OID_GEN_LAST_CHANGE](https://msdn.microsoft.com/library/windows/hardware/ff569591)">OID_GEN_LAST_CHANGE</a></p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p><em>ifMtu</em></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569598" data-raw-source="[OID_GEN_MAXIMUM_FRAME_SIZE](https://msdn.microsoft.com/library/windows/hardware/ff569598)">OID_GEN_MAXIMUM_FRAME_SIZE</a></p></td>
<td align="left"><p>OID_GEN_MAXIMUM_FRAME_SIZE</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>ifOperStatus</em></p></td>
<td align="left"><p>* <a href="https://msdn.microsoft.com/library/windows/hardware/ff569619" data-raw-source="[OID_GEN_OPERATIONAL_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff569619)">OID_GEN_OPERATIONAL_STATUS</a></p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p><em>ifOutDiscards</em></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569653" data-raw-source="[OID_GEN_XMIT_DISCARDS](https://msdn.microsoft.com/library/windows/hardware/ff569653)">OID_GEN_XMIT_DISCARDS</a></p></td>
<td align="left"><p>OID_GEN_XMIT_DISCARDS</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>ifOutErrors</em></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569654" data-raw-source="[OID_GEN_XMIT_ERROR](https://msdn.microsoft.com/library/windows/hardware/ff569654)">OID_GEN_XMIT_ERROR</a></p></td>
<td align="left"><p>OID_GEN_XMIT_ERROR</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>ifPhysAddress</em></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569069" data-raw-source="[OID_802_3_CURRENT_ADDRESS](https://msdn.microsoft.com/library/windows/hardware/ff569069)">OID_802_3_CURRENT_ADDRESS</a></p></td>
<td align="left"><p>OID_802_3_CURRENT_ADDRESS</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>ifPromiscuousMode</em></p></td>
<td align="left"><p>* <a href="https://msdn.microsoft.com/library/windows/hardware/ff569625" data-raw-source="[OID_GEN_PROMISCUOUS_MODE](https://msdn.microsoft.com/library/windows/hardware/ff569625)">OID_GEN_PROMISCUOUS_MODE</a></p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>Not applicable</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569074" data-raw-source="[OID_802_3_PERMANENT_ADDRESS](https://msdn.microsoft.com/library/windows/hardware/ff569074)">OID_802_3_PERMANENT_ADDRESS</a></p></td>
<td align="left"><p>OID_802_3_PERMANENT_ADDRESS</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Not applicable</p></td>
<td align="left"><p>* <a href="https://msdn.microsoft.com/library/windows/hardware/ff569589" data-raw-source="[OID_GEN_INTERFACE_INFO](https://msdn.microsoft.com/library/windows/hardware/ff569589)">OID_GEN_INTERFACE_INFO</a></p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>Not applicable</p></td>
<td align="left"><p>* <a href="https://msdn.microsoft.com/library/windows/hardware/ff569605" data-raw-source="[OID_GEN_MEDIA_CONNECT_STATUS_EX](https://msdn.microsoft.com/library/windows/hardware/ff569605)">OID_GEN_MEDIA_CONNECT_STATUS_EX</a></p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>Not applicable</p></td>
<td align="left"><p>* <a href="https://msdn.microsoft.com/library/windows/hardware/ff569606" data-raw-source="[OID_GEN_MEDIA_DUPLEX_STATE](https://msdn.microsoft.com/library/windows/hardware/ff569606)">OID_GEN_MEDIA_DUPLEX_STATE</a></p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>Not applicable</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569640" data-raw-source="[OID_GEN_STATISTICS](https://msdn.microsoft.com/library/windows/hardware/ff569640)">OID_GEN_STATISTICS</a></p></td>
<td align="left"></td>
</tr>
</tbody>
</table>

 

 

 





