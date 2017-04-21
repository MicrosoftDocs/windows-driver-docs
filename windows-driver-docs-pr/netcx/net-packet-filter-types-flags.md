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

Specifies the packet filters that select which types of packets the NIC indicates on its receive path.

Syntax
------

```cpp
typedef enum _NET_PACKET_FILTER_TYPES_FLAGS { 
  NET_PACKET_FILTER_TYPE_DIRECTED        = 0x00000001,
  NET_PACKET_FILTER_TYPE_MULTICAST       = 0x00000002,
  NET_PACKET_FILTER_TYPE_ALL_MULTICAST   = 0x00000004,
  NET_PACKET_FILTER_TYPE_BROADCAST       = 0x00000008,
  NET_PACKET_FILTER_TYPE_PROMISCUOUS     = 0x00000020,
} NET_PACKET_FILTER_TYPES_FLAGS;
```

Constants
---------

**NET_PACKET_FILTER_TYPE_DIRECTED**  
The NIC should receive directed packets that contain a destination address equal to the station address of the NIC.

**NET_PACKET_FILTER_TYPE_MULTICAST**  
Multicast address packets contain a destination address equal to one of the addresses in the multicast address list.

**NET_PACKET_FILTER_TYPE_ALL_MULTICAST**  
All multicast address packets, not just the ones enumerated in the multicast address list.

**NET_PACKET_FILTER_TYPE_BROADCAST**  
Broadcast packets.

**NET_PACKET_FILTER_TYPE_PROMISCUOUS**  
Specifies all packets regardless of whether VLAN filtering is enabled or not and whether the VLAN identifier matches or not.

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
