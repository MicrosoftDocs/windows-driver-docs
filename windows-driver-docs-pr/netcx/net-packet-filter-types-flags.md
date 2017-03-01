---
title: NET_PACKET_FILTER_TYPES_FLAGS enumeration
topic_type:
- apiref
api_name:
- NET_PACKET_FILTER_TYPES_FLAGS
api_location:
- netadapter.h
api_type:
- HeaderDef
---

# NET_PACKET_FILTER_TYPES_FLAGS enumeration

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Specifies the packet filters that the adapter supports.

Syntax
------

```cpp
typedef enum _NET_PACKET_FILTER_TYPES_FLAGS { 
  NET_PACKET_FILTER_TYPE_DIRECTED        = NDIS_PACKET_TYPE_DIRECTED,
  NET_PACKET_FILTER_TYPE_MULTICAST       = NDIS_PACKET_TYPE_MULTICAST,
  NET_PACKET_FILTER_TYPE_ALL_MULTICAST   = NDIS_PACKET_TYPE_ALL_MULTICAST,
  NET_PACKET_FILTER_TYPE_BROADCAST       = NDIS_PACKET_TYPE_BROADCAST,
  NET_PACKET_FILTER_TYPE_SOURCE_ROUTING  = NDIS_PACKET_TYPE_SOURCE_ROUTING,
  NET_PACKET_FILTER_TYPE_PROMISCUOUS     = NDIS_PACKET_TYPE_PROMISCUOUS,
  NET_PACKET_FILTER_TYPE_ALL_LOCAL       = NDIS_PACKET_TYPE_ALL_LOCAL,
  NET_PACKET_FILTER_TYPE_MAC_FRAME       = NDIS_PACKET_TYPE_MAC_FRAME,
  NET_PACKET_FILTER_TYPE_NO_LOCAL        = NDIS_PACKET_TYPE_NO_LOCAL
} NET_PACKET_FILTER_TYPES_FLAGS;
```

Constants
---------

**NET_PACKET_FILTER_TYPE_DIRECTED**  
Directed packets. Directed packets contain a destination address equal to the station address of the NIC.

**NET_PACKET_FILTER_TYPE_MULTICAST**  
Multicast address packets sent to addresses in the multicast address list. 

A protocol driver can receive Ethernet (802.3) multicast packets by specifying the multicast or functional address packet type. Setting the multicast address list or functional address determines which multicast address groups the NIC driver enables.

**NET_PACKET_FILTER_TYPE_ALL_MULTICAST**  
All multicast address packets, not just the ones enumerated in the multicast address list.

**NET_PACKET_FILTER_TYPE_BROADCAST**  
Broadcast packets.

**NET_PACKET_FILTER_TYPE_SOURCE_ROUTING**  
All source routing packets. If the protocol driver sets this bit, the NDIS library attempts to act as a source routing bridge.

**NET_PACKET_FILTER_TYPE_PROMISCUOUS**  
Specifies all packets regardless of whether VLAN filtering is enabled or not and whether the VLAN identifier matches or not.

**NET_PACKET_FILTER_TYPE_ALL_LOCAL**  
All packets sent by installed protocols and all packets indicated by the NIC that is identified by a given *NdisBindingHandle*.

**NET_PACKET_FILTER_TYPE_MAC_FRAME**  
NIC driver frames that a Token Ring NIC receives.

**NET_PACKET_FILTER_TYPE_NO_LOCAL**  
No packets sent by installed protocols and no packets indicated by the NIC that is identified by a given *NdisBindingHandle*.

Remarks
-------
The **NET_PACKET_FILTER_TYPES_FLAGS** enumeration is used to specify supported packet filters in the [**NET_ADAPTER_LINK_LAYER_CAPABILITIES**](net-adapter-link-layer-capabilities.md) structure.

The client driver passes an initialized [**NET_ADAPTER_LINK_LAYER_CAPABILITIES**](net-adapter-link-layer-capabilities.md) structure as an input parameter value to [**NetAdapterSetLinkLayerCapabilities**](netadaptersetlinklayercapabilities.md).

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Minimum KMDF version</p></td>
<td align="left"><p>1.21</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum NetAdapterCx version</p></td>
<td align="left"><p>1.0</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Netadapter.h</td>
</tr>
</tbody>
</table>

See Also
-----
[**NET_ADAPTER_LINK_LAYER_CAPABILITIES**](net-adapter-link-layer-capabilities.md)
[**OID_GEN_CURRENT_PACKET_FILTER**](https://msdn.microsoft.com/library/windows/hardware/ff569575)
