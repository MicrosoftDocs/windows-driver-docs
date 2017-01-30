---
title: NET_PACKET_FILTER_TYPES_FLAGS enumeration
description: .
ms.assetid: 0895f608-619e-4b16-b0e9-5e31b382e346
keywords: ["NET_PACKET_FILTER_TYPES_FLAGS enumeration Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NET_PACKET_FILTER_TYPES_FLAGS
api_location:
- netadapter.h
api_type:
- HeaderDef
---

# NET\_PACKET\_FILTER\_TYPES\_FLAGS enumeration


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Syntax
------

```ManagedCPlusPlus
typedef enum _NET_PACKET_FILTER_TYPES_FLAGS { 
  NET_PACKET_FILTER_TYPE_DIRECTED        = = NDIS_PACKET_TYPE_DIRECTED,
  NET_PACKET_FILTER_TYPE_MULTICAST       = = NDIS_PACKET_TYPE_MULTICAST,
  NET_PACKET_FILTER_TYPE_ALL_MULTICAST   = = NDIS_PACKET_TYPE_ALL_MULTICAST,
  NET_PACKET_FILTER_TYPE_BROADCAST       = = NDIS_PACKET_TYPE_BROADCAST,
  NET_PACKET_FILTER_TYPE_SOURCE_ROUTING  = = NDIS_PACKET_TYPE_SOURCE_ROUTING,
  NET_PACKET_FILTER_TYPE_PROMISCUOUS     = = NDIS_PACKET_TYPE_PROMISCUOUS,
  NET_PACKET_FILTER_TYPE_ALL_LOCAL       = = NDIS_PACKET_TYPE_ALL_LOCAL,
  NET_PACKET_FILTER_TYPE_MAC_FRAME       = = NDIS_PACKET_TYPE_MAC_FRAME,
  NET_PACKET_FILTER_TYPE_NO_LOCAL        = = NDIS_PACKET_TYPE_NO_LOCAL
} NET_PACKET_FILTER_TYPES_FLAGS;
```

Constants
---------

<a href="" id="net-packet-filter-type-directed"></a>**NET\_PACKET\_FILTER\_TYPE\_DIRECTED**  

<a href="" id="net-packet-filter-type-multicast"></a>**NET\_PACKET\_FILTER\_TYPE\_MULTICAST**  

<a href="" id="net-packet-filter-type-all-multicast"></a>**NET\_PACKET\_FILTER\_TYPE\_ALL\_MULTICAST**  

<a href="" id="net-packet-filter-type-broadcast"></a>**NET\_PACKET\_FILTER\_TYPE\_BROADCAST**  

<a href="" id="net-packet-filter-type-source-routing"></a>**NET\_PACKET\_FILTER\_TYPE\_SOURCE\_ROUTING**  

<a href="" id="net-packet-filter-type-promiscuous"></a>**NET\_PACKET\_FILTER\_TYPE\_PROMISCUOUS**  

<a href="" id="net-packet-filter-type-all-local"></a>**NET\_PACKET\_FILTER\_TYPE\_ALL\_LOCAL**  

<a href="" id="net-packet-filter-type-mac-frame"></a>**NET\_PACKET\_FILTER\_TYPE\_MAC\_FRAME**  

<a href="" id="net-packet-filter-type-no-local"></a>**NET\_PACKET\_FILTER\_TYPE\_NO\_LOCAL**  

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

 

 





