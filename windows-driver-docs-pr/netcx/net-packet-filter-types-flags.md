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

Syntax
------

```ManagedCPlusPlus
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

**NET_PACKET_FILTER_TYPE_MULTICAST**  

**NET_PACKET_FILTER_TYPE_ALL_MULTICAST**  

**NET_PACKET_FILTER_TYPE_BROADCAST**  

**NET_PACKET_FILTER_TYPE_SOURCE_ROUTING**  

**NET_PACKET_FILTER_TYPE_PROMISCUOUS**  

**NET_PACKET_FILTER_TYPE_ALL_LOCAL**  

**NET_PACKET_FILTER_TYPE_MAC_FRAME**  

**NET_PACKET_FILTER_TYPE_NO_LOCAL**  

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

 

 





