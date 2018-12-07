---
title: OID_GEN_CURRENT_PACKET_FILTER
description: As a query, the OID_GEN_CURRENT_PACKET_FILTER OID reports the types of net packets that are in receive indications from a miniport driver.
ms.assetid: d5a32626-caff-4708-a134-d80a845dee91
ms.date: 08/08/2017
keywords: 
 -OID_GEN_CURRENT_PACKET_FILTER Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_CURRENT\_PACKET\_FILTER


As a query, the OID\_GEN\_CURRENT\_PACKET\_FILTER OID reports the types of net packets that are in receive indications from a miniport driver.

As a set, the OID\_GEN\_CURRENT\_PACKET\_FILTER OID specifies the types of net packets for which a protocol receives indications from a miniport driver.

**Version Information**

<a href="" id="windows-vista-and-later-versions-of-windows"></a>Windows Vista and later versions of Windows  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Mandatory. (see Remarks section)

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Mandatory.

<a href="" id="windows-xp"></a>Windows XP  
Supported.

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Mandatory.

Remarks
-------

For NDIS 6.0 and later miniport drivers, the query is not requested and the set is mandatory. NDIS handles the query for miniport drivers. The miniport driver reports the packet filter information during initialization.

The miniport driver reports its medium type as one for which the system provides a filter library. The packet filter uses the OR operation to inclusively combine the following types:

<a href="" id="ndis-packet-type-directed"></a>NDIS\_PACKET\_TYPE\_DIRECTED  
Directed packets. Directed packets contain a destination address equal to the station address of the NIC.

<a href="" id="ndis-packet-type-multicast"></a>NDIS\_PACKET\_TYPE\_MULTICAST  
Multicast address packets sent to addresses in the multicast address list.

A protocol driver can receive Ethernet (802.3) multicast packets by specifying the multicast or functional address packet type. Setting the multicast address list or functional address determines which multicast address groups the NIC driver enables.

<a href="" id="ndis-packet-type-all-multicast"></a>NDIS\_PACKET\_TYPE\_ALL\_MULTICAST  
All multicast address packets, not just the ones enumerated in the multicast address list.

<a href="" id="ndis-packet-type-broadcast"></a>NDIS\_PACKET\_TYPE\_BROADCAST  
Broadcast packets.

<a href="" id="ndis-packet-type-promiscuous"></a>NDIS\_PACKET\_TYPE\_PROMISCUOUS  
Specifies all packets regardless of whether VLAN filtering is enabled or not and whether the VLAN identifier matches or not.

<a href="" id="ndis-packet-type-all-functional"></a>NDIS\_PACKET\_TYPE\_ALL\_FUNCTIONAL  
All functional address packets, not just the ones in the current functional address.

<a href="" id="ndis-packet-type-all-local"></a>NDIS\_PACKET\_TYPE\_ALL\_LOCAL  
All packets sent by installed protocols and all packets indicated by the NIC that is identified by a given *NdisBindingHandle* .

<a href="" id="ndis-packet-type-functional"></a>NDIS\_PACKET\_TYPE\_FUNCTIONAL  
Functional address packets sent to addresses included in the current functional address.

<a href="" id="ndis-packet-type-group"></a>NDIS\_PACKET\_TYPE\_GROUP  
Packets sent to the current group address.

<a href="" id="ndis-packet-type-mac-frame"></a>NDIS\_PACKET\_TYPE\_MAC\_FRAME  
NIC driver frames that a Token Ring NIC receives.

<a href="" id="ndis-packet-type-smt"></a>NDIS\_PACKET\_TYPE\_SMT  
SMT packets that an FDDI NIC receives.

<a href="" id="ndis-packet-type-source-routing"></a>NDIS\_PACKET\_TYPE\_SOURCE\_ROUTING  
All source routing packets. If the protocol driver sets this bit, the NDIS library attempts to act as a source routing bridge.

For miniport adapters whose media type is **NdisMedium802\_3** or **NdisMedium802\_5**, NDIS disables packet reception, along with multicast and functional addresses during a call to the [**NdisOpenAdapterEx**](https://msdn.microsoft.com/library/windows/hardware/ff563715) function.

For miniport adapters with all other media types, the protocol driver can begin receiving packets at any time during the [**NdisOpenAdapterEx**](https://msdn.microsoft.com/library/windows/hardware/ff563715) call. Note that the protocol can even receive packets before **NdisOpenAdapterEx** returns. In general, packet filtering is best effort, and protocol drivers must be prepared to handle receive indications even when the packet filter is zero.

For a query, NDIS returns the binding filters that are combined using the OR operator.

For a set, the specified packet filter replaces the previous packet filter for the binding. If the miniport driver previously enabled a packet type but the protocol driver does not specify that type in a new filter, the protocol driver will not receive packets of this type.

For miniport adapters whose media type is **NdisMedium802\_3** or **NdisMedium802\_5**, if the miniport driver does not set a bit for a particular packet type in response to this query, the protocol driver will not receive packets of that type. Consequently, a protocol driver can disable packet reception by calling the [**NdisOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff563710) or [**NdisCoOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561711) function using a filter of zero.

For miniport adapters with all other media types, NDIS does not check the packet type. For these media types, a protocol driver cannot disable packet reception by specifying a filter of zero.

When a miniport driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function is called, the miniport driver's packet filter should be set to zero. When the packet filter is zero, receive indications are disabled. After a miniport driver's *MiniportInitializeEx* function has returned, a protocol driver can set OID\_GEN\_CURRENT\_PACKET\_FILTER to a nonzero value, thereby enabling the miniport driver to indicate received packets to that protocol.

If promiscuous mode is enabled with the NDIS\_PACKET\_TYPE\_PROMISCUOUS bit, the protocol driver continues to receive packets even if the sending network node does not direct them to it. NDIS then sends the protocol driver all packets the NIC receives.

Setting a specific packet filter does not alter the packet filter for other protocol drivers that are bound to (or above) the same NIC. For example, if one bound protocol enables promiscuous mode, other bound protocol drivers do not receive packets that they have not specifically requested with their own packet filters.

**Native 802.11 Packet Filters**

The Native 802.11 miniport driver must only support the following standard packet filter types:

-   NDIS\_PACKET\_TYPE\_DIRECTED

-   NDIS\_PACKET\_TYPE\_MULTICAST

-   NDIS\_PACKET\_TYPE\_BROADCAST

-   NDIS\_PACKET\_TYPE\_PROMISCUOUS

When enabled, these standard packet filters are only applicable to 802.11 data packets.

In addition, the Native 802.11 miniport driver must support the following packet filter types, which are specific to the Native 802.11 media:

<a href="" id="ndis-packet-type-802-11-raw-data"></a>NDIS\_PACKET\_TYPE\_802\_11\_RAW\_DATA  
An 802.11 media access control (MAC) protocol data unit (MPDU) frame, which contains all of the data in the format received by the 802.11 station. When this filter is set, the driver must indicate every unmodified MPDU fragment before it indicates the MAC service data unit (MSDU) packet reassembled from the MPDU fragments.

If an MPDU fragment is encrypted, it must not decrypt the fragment before it is indicated. However, the miniport driver must decrypt each MPDU fragment before reassembling and indicating the MSDU packet.

If enabled, this filter type only affects other standard packet filters, such as NDIS\_PACKET\_TYPE\_DIRECTED or NDIS\_PACKET\_TYPE\_BROADCAST.

For more information about the method for indicating raw 802.11 data packets, see [Indicating Raw 802.11 Packets](https://msdn.microsoft.com/library/windows/hardware/ff554833).

<a href="" id="ndis-packet-type-802-11-directed-mgmt"></a>NDIS\_PACKET\_TYPE\_802\_11\_DIRECTED\_MGMT  
Directed 802.11 management packets. Directed packets contain a destination address equal to the station address of the NIC.

<a href="" id="ndis-packet-type-802-11-multicast-mgmt"></a>NDIS\_PACKET\_TYPE\_802\_11\_MULTICAST\_MGMT  
Multicast 802.11 management packets sent to addresses in the multicast address list.

<a href="" id="ndis-packet-type-802-11-all-multicast-mgmt"></a>NDIS\_PACKET\_TYPE\_802\_11\_ALL\_MULTICAST\_MGMT  
All multicast 802.11 management packets received by the 802.11 station, regardless of whether the destination address in the 802.11 MAC header is in the multicast address list.

<a href="" id="ndis-packet-type-802-11-broadcast-mgmt"></a>NDIS\_PACKET\_TYPE\_802\_11\_BROADCAST\_MGMT  
Broadcast 802.11 management packets received by the 802.11 station.

<a href="" id="ndis-packet-type-802-11-promiscuous-mgmt"></a>NDIS\_PACKET\_TYPE\_802\_11\_PROMISCUOUS\_MGMT  
All 802.11 management packets received by the 802.11 station.

<a href="" id="ndis-packet-type-802-11-raw-mgmt"></a>NDIS\_PACKET\_TYPE\_802\_11\_RAW\_MGMT  
An 802.11 MPDU management frame, which contains all of the data in the format received by the 802.11 station. When this filter is set, the driver must indicate every unmodified MPDU fragment before it indicates the MAC management protocol data unit (MMPDU) packet reassembled from the MPDU fragments.

If enabled, this filter type only affects other 802.11 management packet filters, such as NDIS\_PACKET\_TYPE\_802\_11\_DIRECTED\_MGMT or NDIS\_PACKET\_TYPE\_802\_11\_MULTICAST\_MGMT.

For more information about the method for indicating raw 802.11 management packets, see [Indicating Raw 802.11 Packets](https://msdn.microsoft.com/library/windows/hardware/ff554833).

<a href="" id="ndis-packet-type-802-11-directed-ctrl"></a>NDIS\_PACKET\_TYPE\_802\_11\_DIRECTED\_CTRL  
Directed 802.11 control packets. Directed packets contain a destination address equal to the station address of the NIC.

<a href="" id="ndis-packet-type-802-11-broadcast-ctrl"></a>NDIS\_PACKET\_TYPE\_802\_11\_BROADCAST\_CTRL  
Broadcast 802.11 control packets received by the 802.11 station.

<a href="" id="ndis-packet-type-802-11-promiscuous-ctrl"></a>NDIS\_PACKET\_TYPE\_802\_11\_PROMISCUOUS\_CTRL  
All 802.11 control packets received by the 802.11 station.

If a miniport driver is operating in Native 802.11 Network Monitor (NetMon) or Extensible Access Point (AP) modes, the driver must enable the following packet filters through a set request of OID\_GEN\_CURRENT\_PACKET\_FILTER.

-   NDIS\_PACKET\_TYPE\_PROMISCUOUS

-   NDIS\_PACKET\_TYPE\_802\_11\_RAW\_DATA

-   NDIS\_PACKET\_TYPE\_802\_11\_PROMISCUOUS\_MGMT

-   NDIS\_PACKET\_TYPE\_802\_11\_RAW\_MGMT

-   NDIS\_PACKET\_TYPE\_802\_11\_PROMISCUOUS\_CTRL

A miniport driver operating in other Native 802.11 modes besides NetMon must not enable these packet filter settings, with the exception of NDIS\_PACKET\_TYPE\_802\_11\_PROMISCUOUS\_CTRL. A miniport driver that is not operating in NetMon mode can optionally enable NDIS\_PACKET\_TYPE\_802\_11\_PROMISCUOUS\_CTRL through a set request of OID\_GEN\_CURRENT\_PACKET\_FILTER.

**Note**  When the miniport driver is in Native 802.11 modes other than NetMon, and OID\_GEN\_CURRENT\_PACKET\_FILTER is set, the driver must not fail the set request if any promiscuous or raw filter settings are enabled in the OID data.

 

For more information about the NetMon and ExtAP operating modes, see the following topics:

[Network Monitor Operation Mode](https://msdn.microsoft.com/library/windows/hardware/ff568369)

[Extensible Access Point Operation Mode](https://msdn.microsoft.com/library/windows/hardware/ff549858)

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389)

[**NdisCoOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561711)

[**NdisOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff563710)

[**NdisOpenAdapterEx**](https://msdn.microsoft.com/library/windows/hardware/ff563715)

 

 




