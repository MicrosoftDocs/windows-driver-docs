---
title: NET\_PACKET\_FILTER\_TYPES\_FLAGS enumeration
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NET_PACKET_FILTER_TYPES_FLAGS%20enumeration%20%20RELEASE:%20%281/19/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




