---
title: NET_ADAPTER_PROTOCOL_OFFLOADS_FLAGS enumeration
description: .
ms.assetid: 51d3d4fd-d43b-4f0b-8434-4dbe70e73b4f
keywords: ["NET_ADAPTER_PROTOCOL_OFFLOADS_FLAGS enumeration Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NET_ADAPTER_PROTOCOL_OFFLOADS_FLAGS
api_location:
- netadapter.h
api_type:
- HeaderDef
---

# NET\_ADAPTER\_PROTOCOL\_OFFLOADS\_FLAGS enumeration


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Syntax
------

```ManagedCPlusPlus
typedef enum _NET_ADAPTER_PROTOCOL_OFFLOADS_FLAGS { 
  NET_ADAPTER_PROTOCOL_OFFLOAD_ARP              = = NDIS_PM_PROTOCOL_OFFLOAD_ARP_ENABLED,
  NET_ADAPTER_PROTOCOL_OFFLOAD_NS               = = NDIS_PM_PROTOCOL_OFFLOAD_NS_ENABLED,
  NET_ADAPTER_PROTOCOL_OFFLOAD_80211_RSN_REKEY  = = NDIS_PM_PROTOCOL_OFFLOAD_80211_RSN_REKEY_ENABLED
} NET_ADAPTER_PROTOCOL_OFFLOADS_FLAGS;
```

Constants
---------

<a href="" id="net-adapter-protocol-offload-arp"></a>**NET\_ADAPTER\_PROTOCOL\_OFFLOAD\_ARP**  

<a href="" id="net-adapter-protocol-offload-ns"></a>**NET\_ADAPTER\_PROTOCOL\_OFFLOAD\_NS**  

<a href="" id="net-adapter-protocol-offload-80211-rsn-rekey"></a>**NET\_ADAPTER\_PROTOCOL\_OFFLOAD\_80211\_RSN\_REKEY**  

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

 

 





