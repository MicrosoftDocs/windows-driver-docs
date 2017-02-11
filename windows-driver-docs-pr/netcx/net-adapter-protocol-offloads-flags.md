---
title: NET_ADAPTER_PROTOCOL_OFFLOADS_FLAGS enumeration
topic_type:
- apiref
api_name:
- NET_ADAPTER_PROTOCOL_OFFLOADS_FLAGS
api_location:
- netadapter.h
api_type:
- HeaderDef
---

# NET_ADAPTER_PROTOCOL_OFFLOADS_FLAGS enumeration


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Syntax
------

```ManagedCPlusPlus
typedef enum _NET_ADAPTER_PROTOCOL_OFFLOADS_FLAGS { 
  NET_ADAPTER_PROTOCOL_OFFLOAD_ARP              = NDIS_PM_PROTOCOL_OFFLOAD_ARP_ENABLED,
  NET_ADAPTER_PROTOCOL_OFFLOAD_NS               = NDIS_PM_PROTOCOL_OFFLOAD_NS_ENABLED,
  NET_ADAPTER_PROTOCOL_OFFLOAD_80211_RSN_REKEY  = NDIS_PM_PROTOCOL_OFFLOAD_80211_RSN_REKEY_ENABLED
} NET_ADAPTER_PROTOCOL_OFFLOADS_FLAGS;
```

Constants
---------

**NET_ADAPTER_PROTOCOL_OFFLOAD_ARP**  

**NET_ADAPTER_PROTOCOL_OFFLOAD_NS**  

**NET_ADAPTER_PROTOCOL_OFFLOAD_80211_RSN_REKEY**  

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

 

 





