---
title: NET_ADAPTER_WAKE_PATTERN_FLAGS enumeration
description: .
ms.assetid: 211fde06-ee4d-412a-84ac-8979f6de2d25
keywords: ["NET_ADAPTER_WAKE_PATTERN_FLAGS enumeration Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NET_ADAPTER_WAKE_PATTERN_FLAGS
api_location:
- netadapter.h
api_type:
- HeaderDef
---

# NET\_ADAPTER\_WAKE\_PATTERN\_FLAGS enumeration


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Syntax
------

```ManagedCPlusPlus
typedef enum _NET_ADAPTER_WAKE_PATTERN_FLAGS { 
  NET_ADAPTER_WAKE_BITMAP_PATTERN            = = NDIS_PM_WOL_BITMAP_PATTERN_ENABLED,
  NET_ADAPTER_WAKE_MAGIC_PACKET              = = NDIS_PM_WOL_MAGIC_PACKET_ENABLED,
  NET_ADAPTER_WAKE_IPV4_TCP_SYN              = = NDIS_PM_WOL_IPV4_TCP_SYN_ENABLED,
  NET_ADAPTER_WAKE_IPV6_TCP_SYN              = = NDIS_PM_WOL_IPV6_TCP_SYN_ENABLED,
  NET_ADAPTER_WAKE_IPV4_DEST_ADDR_WILDCARD   = = NDIS_PM_WOL_IPV4_DEST_ADDR_WILDCARD_ENABLED,
  NET_ADAPTER_WAKE_IPV6_DEST_ADDR_WILDCARD   = = NDIS_PM_WOL_IPV6_DEST_ADDR_WILDCARD_ENABLED,
  NET_ADAPTER_WAKE_EAPOL_REQUEST_ID_MESSAGE  = = NDIS_PM_WOL_EAPOL_REQUEST_ID_MESSAGE_ENABLED
} NET_ADAPTER_WAKE_PATTERN_FLAGS;
```

Constants
---------

<a href="" id="net-adapter-wake-bitmap-pattern"></a>**NET\_ADAPTER\_WAKE\_BITMAP\_PATTERN**  

<a href="" id="net-adapter-wake-magic-packet"></a>**NET\_ADAPTER\_WAKE\_MAGIC\_PACKET**  

<a href="" id="net-adapter-wake-ipv4-tcp-syn"></a>**NET\_ADAPTER\_WAKE\_IPV4\_TCP\_SYN**  

<a href="" id="net-adapter-wake-ipv6-tcp-syn"></a>**NET\_ADAPTER\_WAKE\_IPV6\_TCP\_SYN**  

<a href="" id="net-adapter-wake-ipv4-dest-addr-wildcard"></a>**NET\_ADAPTER\_WAKE\_IPV4\_DEST\_ADDR\_WILDCARD**  

<a href="" id="net-adapter-wake-ipv6-dest-addr-wildcard"></a>**NET\_ADAPTER\_WAKE\_IPV6\_DEST\_ADDR\_WILDCARD**  

<a href="" id="net-adapter-wake-eapol-request-id-message"></a>**NET\_ADAPTER\_WAKE\_EAPOL\_REQUEST\_ID\_MESSAGE**  

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

 

 





