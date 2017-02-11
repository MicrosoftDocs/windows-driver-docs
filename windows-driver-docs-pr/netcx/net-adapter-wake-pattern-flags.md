---
title: NET_ADAPTER_WAKE_PATTERN_FLAGS enumeration
topic_type:
- apiref
api_name:
- NET_ADAPTER_WAKE_PATTERN_FLAGS
api_location:
- netadapter.h
api_type:
- HeaderDef
---

# NET_ADAPTER_WAKE_PATTERN_FLAGS enumeration


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Syntax
------

```ManagedCPlusPlus
typedef enum _NET_ADAPTER_WAKE_PATTERN_FLAGS { 
  NET_ADAPTER_WAKE_BITMAP_PATTERN            = NDIS_PM_WOL_BITMAP_PATTERN_ENABLED,
  NET_ADAPTER_WAKE_MAGIC_PACKET              = NDIS_PM_WOL_MAGIC_PACKET_ENABLED,
  NET_ADAPTER_WAKE_IPV4_TCP_SYN              = NDIS_PM_WOL_IPV4_TCP_SYN_ENABLED,
  NET_ADAPTER_WAKE_IPV6_TCP_SYN              = NDIS_PM_WOL_IPV6_TCP_SYN_ENABLED,
  NET_ADAPTER_WAKE_IPV4_DEST_ADDR_WILDCARD   = NDIS_PM_WOL_IPV4_DEST_ADDR_WILDCARD_ENABLED,
  NET_ADAPTER_WAKE_IPV6_DEST_ADDR_WILDCARD   = NDIS_PM_WOL_IPV6_DEST_ADDR_WILDCARD_ENABLED,
  NET_ADAPTER_WAKE_EAPOL_REQUEST_ID_MESSAGE  = NDIS_PM_WOL_EAPOL_REQUEST_ID_MESSAGE_ENABLED
} NET_ADAPTER_WAKE_PATTERN_FLAGS;
```

Constants
---------

**NET_ADAPTER_WAKE_BITMAP_PATTERN**  

**NET_ADAPTER_WAKE_MAGIC_PACKET**  

**NET_ADAPTER_WAKE_IPV4_TCP_SYN**  

**NET_ADAPTER_WAKE_IPV6_TCP_SYN**  

**NET_ADAPTER_WAKE_IPV4_DEST_ADDR_WILDCARD**  

**NET_ADAPTER_WAKE_IPV6_DEST_ADDR_WILDCARD**  

**NET_ADAPTER_WAKE_EAPOL_REQUEST_ID_MESSAGE**  

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

 

 





