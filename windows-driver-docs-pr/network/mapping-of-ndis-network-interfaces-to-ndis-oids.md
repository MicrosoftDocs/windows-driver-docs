---
title: Mapping of NDIS Network Interfaces to NDIS OIDs
description: Mapping of NDIS Network Interfaces to NDIS OIDs
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

As a proxy interface provider, NDIS typically caches information that it receives about miniport adapters and filter modules. The NDIS proxy interface provider uses the cached information, if appropriate, to respond to interface requests. In some cases, the NDIS proxy interface provider issues OIDs to obtain information for interfaces. For example, the primary source of interface information for NDIS 5.*x* and earlier drivers is through OID requests. In NDIS 6.0 drivers, there are additional sources of interface information, such as the [**NDIS\_RESTART\_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_restart_attributes) and [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_general_attributes) structures. For more information about alternate sources of information in the OIDs, see the reference page for each OID.

The NDIS proxy interface provider also generates some interface information on behalf of miniport adapters and filter modules. For example, NDIS generates an interface alias (*ifAlias* in RFC 2863) in response to the *ifAlias* request. NDIS defines additional OIDs to obtain such information from NDIS interface providers. For example, [OID\_GEN\_ALIAS](./oid-gen-alias.md) allows an interface provider to specify an *ifAlias* object. Such OIDs are specific to interface providers and are never used to obtain information from other NDIS drivers.

In addition to the OIDs that are specific to interface providers, interface providers must support the other NDIS OIDs that NDIS can use to obtain interface information. NDIS can issue these OIDs to the provider and the provider can issue these OIDs, if necessary, to collect information from underlying interfaces.

**Note**  NDIS defines additional statistics that are not included in RFC 2863. For a list that maps all of the NDIS-supported interface statistics to OIDs, see the members of the [**NDIS\_INTERFACE\_INFORMATION**](/windows/win32/api/ifdef/ns-ifdef-ndis_interface_information) structure. The table in this topic defines the mapping for statistics that are defined in the RFC 2863 specification for readers that are trying to relate the specification to the NDIS implementation.

 

The following table shows the mapping from the objects that are defined in the management information base (MIB) to NDIS 6.0 OIDs and to OIDs that NDIS might use to obtain information from NDIS 5.*x* and earlier drivers. The table also includes some additional interface objects that are not defined as MIB objects. The interface objects also correspond to members in the [**NDIS\_INTERFACE\_INFORMATION**](ndis-interface-information.md) structure that is associated with the [OID\_GEN\_INTERFACE\_INFO](./oid-gen-interface-info.md) OID.

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
<td align="left"><p>* <a href="/windows-hardware/drivers/network/oid-gen-admin-status" data-raw-source="[OID_GEN_ADMIN_STATUS](./oid-gen-admin-status.md)">OID_GEN_ADMIN_STATUS</a></p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p><em>ifAlias</em></p></td>
<td align="left"><p>* <a href="/windows-hardware/drivers/network/oid-gen-alias" data-raw-source="[OID_GEN_ALIAS](./oid-gen-alias.md)">OID_GEN_ALIAS</a></p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p><em>ifCounterDiscontinuityTime</em></p></td>
<td align="left"><p>* <a href="/windows-hardware/drivers/network/oid-gen-discontinuity-time" data-raw-source="[OID_GEN_DISCONTINUITY_TIME](./oid-gen-discontinuity-time.md)">OID_GEN_DISCONTINUITY_TIME</a></p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p><em>ifHCInBroadcastPkts</em></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-broadcast-frames-rcv" data-raw-source="[OID_GEN_BROADCAST_FRAMES_RCV](./oid-gen-broadcast-frames-rcv.md)">OID_GEN_BROADCAST_FRAMES_RCV</a></p></td>
<td align="left"><p>OID_GEN_BROADCAST_FRAMES_RCV</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>ifHCInMulticastPkts</em></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-multicast-frames-rcv" data-raw-source="[OID_GEN_MULTICAST_FRAMES_RCV](./oid-gen-multicast-frames-rcv.md)">OID_GEN_MULTICAST_FRAMES_RCV</a></p></td>
<td align="left"><p>OID_GEN_MULTICAST_FRAMES_RCV</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>ifHCInOctets</em></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-bytes-rcv" data-raw-source="[OID_GEN_BYTES_RCV](./oid-gen-bytes-rcv.md)">OID_GEN_BYTES_RCV</a></p></td>
<td align="left"><p>NDIS adds the results from these OIDs to collect the <em>ifHCInOctets</em> value from NDIS 5.<em>x</em> drivers:</p>
<p><a href="/windows-hardware/drivers/network/oid-gen-directed-bytes-rcv" data-raw-source="[OID_GEN_DIRECTED_BYTES_RCV](./oid-gen-directed-bytes-rcv.md)">OID_GEN_DIRECTED_BYTES_RCV</a>+</p>
<p><a href="/windows-hardware/drivers/network/oid-gen-multicast-bytes-rcv" data-raw-source="[OID_GEN_MULTICAST_BYTES_RCV](./oid-gen-multicast-bytes-rcv.md)">OID_GEN_MULTICAST_BYTES_RCV</a>+</p>
<p><a href="/windows-hardware/drivers/network/oid-gen-broadcast-bytes-rcv" data-raw-source="[OID_GEN_BROADCAST_BYTES_RCV](./oid-gen-broadcast-bytes-rcv.md)">OID_GEN_BROADCAST_BYTES_RCV</a></p>
<p>NDIS 6.0 interface providers should also support these OIDs.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>ifHCInUcastPkts</em></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-directed-frames-rcv" data-raw-source="[OID_GEN_DIRECTED_FRAMES_RCV](./oid-gen-directed-frames-rcv.md)">OID_GEN_DIRECTED_FRAMES_RCV</a></p></td>
<td align="left"><p>OID_GEN_DIRECTED_FRAMES_RCV</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>ifHCOutBroadcastPkts</em></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-broadcast-frames-xmit" data-raw-source="[OID_GEN_BROADCAST_FRAMES_XMIT](./oid-gen-broadcast-frames-xmit.md)">OID_GEN_BROADCAST_FRAMES_XMIT</a></p></td>
<td align="left"><p>OID_GEN_BROADCAST_FRAMES_XMIT</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>ifHCOutMulticastPkts</em></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-multicast-frames-xmit" data-raw-source="[OID_GEN_MULTICAST_FRAMES_XMIT](./oid-gen-multicast-frames-xmit.md)">OID_GEN_MULTICAST_FRAMES_XMIT</a></p></td>
<td align="left"><p>OID_GEN_MULTICAST_FRAMES_XMIT</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>ifHCOutOctets</em></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-bytes-xmit" data-raw-source="[OID_GEN_BYTES_XMIT](./oid-gen-bytes-xmit.md)">OID_GEN_BYTES_XMIT</a></p></td>
<td align="left"><p>NDIS adds the results from these OIDs to collect the <em>ifHCInOctets</em> value from NDIS 5.<em>x</em> drivers:</p>
<p><a href="/windows-hardware/drivers/network/oid-gen-directed-bytes-xmit" data-raw-source="[OID_GEN_DIRECTED_BYTES_XMIT](./oid-gen-directed-bytes-xmit.md)">OID_GEN_DIRECTED_BYTES_XMIT</a>+</p>
<p><a href="/windows-hardware/drivers/network/oid-gen-multicast-bytes-xmit" data-raw-source="[OID_GEN_MULTICAST_BYTES_XMIT](./oid-gen-multicast-bytes-xmit.md)">OID_GEN_MULTICAST_BYTES_XMIT</a>+</p>
<p><a href="/windows-hardware/drivers/network/oid-gen-broadcast-bytes-xmit" data-raw-source="[OID_GEN_BROADCAST_BYTES_XMIT](./oid-gen-broadcast-bytes-xmit.md)">OID_GEN_BROADCAST_BYTES_XMIT</a></p>
<p>NDIS 6.0 interface providers should also support these OIDs.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>ifHCOutUCastPkts</em></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-directed-frames-xmit" data-raw-source="[OID_GEN_DIRECTED_FRAMES_XMIT](./oid-gen-directed-frames-xmit.md)">OID_GEN_DIRECTED_FRAMES_XMIT</a></p></td>
<td align="left"><p>OID_GEN_DIRECTED_FRAMES_XMIT</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>ifHighSpeed</em></p></td>
<td align="left"><p>* <a href="/windows-hardware/drivers/network/oid-gen-link-speed-ex" data-raw-source="[OID_GEN_LINK_SPEED_EX](./oid-gen-link-speed-ex.md)">OID_GEN_LINK_SPEED_EX</a>, * <a href="/windows-hardware/drivers/network/oid-gen-xmit-link-speed" data-raw-source="[OID_GEN_XMIT_LINK_SPEED](./oid-gen-xmit-link-speed.md)">OID_GEN_XMIT_LINK_SPEED</a>, * <a href="/windows-hardware/drivers/network/oid-gen-rcv-link-speed" data-raw-source="[OID_GEN_RCV_LINK_SPEED](./oid-gen-rcv-link-speed.md)">OID_GEN_RCV_LINK_SPEED</a></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-link-speed" data-raw-source="[OID_GEN_LINK_SPEED](./oid-gen-link-speed.md)">OID_GEN_LINK_SPEED</a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>ifInDiscards</em></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-rcv-discards" data-raw-source="[OID_GEN_RCV_DISCARDS](./oid-gen-rcv-discards.md)">OID_GEN_RCV_DISCARDS</a></p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p><em>ifInErrors</em></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-rcv-error" data-raw-source="[OID_GEN_RCV_ERROR](./oid-gen-rcv-error.md)">OID_GEN_RCV_ERROR</a></p></td>
<td align="left"><p>OID_GEN_RCV_ERROR</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>ifLastChange</em></p></td>
<td align="left"><p>* <a href="/windows-hardware/drivers/network/oid-gen-last-change" data-raw-source="[OID_GEN_LAST_CHANGE](./oid-gen-last-change.md)">OID_GEN_LAST_CHANGE</a></p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p><em>ifMtu</em></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-maximum-frame-size" data-raw-source="[OID_GEN_MAXIMUM_FRAME_SIZE](./oid-gen-maximum-frame-size.md)">OID_GEN_MAXIMUM_FRAME_SIZE</a></p></td>
<td align="left"><p>OID_GEN_MAXIMUM_FRAME_SIZE</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>ifOperStatus</em></p></td>
<td align="left"><p>* <a href="/windows-hardware/drivers/network/oid-gen-operational-status" data-raw-source="[OID_GEN_OPERATIONAL_STATUS](./oid-gen-operational-status.md)">OID_GEN_OPERATIONAL_STATUS</a></p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p><em>ifOutDiscards</em></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-xmit-discards" data-raw-source="[OID_GEN_XMIT_DISCARDS](./oid-gen-xmit-discards.md)">OID_GEN_XMIT_DISCARDS</a></p></td>
<td align="left"><p>OID_GEN_XMIT_DISCARDS</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>ifOutErrors</em></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-xmit-error" data-raw-source="[OID_GEN_XMIT_ERROR](./oid-gen-xmit-error.md)">OID_GEN_XMIT_ERROR</a></p></td>
<td align="left"><p>OID_GEN_XMIT_ERROR</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>ifPhysAddress</em></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-802-3-current-address" data-raw-source="[OID_802_3_CURRENT_ADDRESS](./oid-802-3-current-address.md)">OID_802_3_CURRENT_ADDRESS</a></p></td>
<td align="left"><p>OID_802_3_CURRENT_ADDRESS</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>ifPromiscuousMode</em></p></td>
<td align="left"><p>* <a href="/windows-hardware/drivers/network/oid-gen-promiscuous-mode" data-raw-source="[OID_GEN_PROMISCUOUS_MODE](./oid-gen-promiscuous-mode.md)">OID_GEN_PROMISCUOUS_MODE</a></p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>Not applicable</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-802-3-permanent-address" data-raw-source="[OID_802_3_PERMANENT_ADDRESS](./oid-802-3-permanent-address.md)">OID_802_3_PERMANENT_ADDRESS</a></p></td>
<td align="left"><p>OID_802_3_PERMANENT_ADDRESS</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Not applicable</p></td>
<td align="left"><p>* <a href="/windows-hardware/drivers/network/oid-gen-interface-info" data-raw-source="[OID_GEN_INTERFACE_INFO](./oid-gen-interface-info.md)">OID_GEN_INTERFACE_INFO</a></p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>Not applicable</p></td>
<td align="left"><p>* <a href="/windows-hardware/drivers/network/oid-gen-media-connect-status-ex" data-raw-source="[OID_GEN_MEDIA_CONNECT_STATUS_EX](./oid-gen-media-connect-status-ex.md)">OID_GEN_MEDIA_CONNECT_STATUS_EX</a></p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>Not applicable</p></td>
<td align="left"><p>* <a href="/windows-hardware/drivers/network/oid-gen-media-duplex-state" data-raw-source="[OID_GEN_MEDIA_DUPLEX_STATE](./oid-gen-media-duplex-state.md)">OID_GEN_MEDIA_DUPLEX_STATE</a></p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>Not applicable</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-gen-statistics" data-raw-source="[OID_GEN_STATISTICS](./oid-gen-statistics.md)">OID_GEN_STATISTICS</a></p></td>
<td align="left"></td>
</tr>
</tbody>
</table>

 

