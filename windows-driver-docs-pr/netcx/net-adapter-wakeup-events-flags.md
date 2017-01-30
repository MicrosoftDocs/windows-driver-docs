---
title: NET_ADAPTER_WAKEUP_EVENTS_FLAGS enumeration
description: .
ms.assetid: 073582db-98b7-4128-979c-ade261ce192c
keywords: ["NET_ADAPTER_WAKEUP_EVENTS_FLAGS enumeration Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NET_ADAPTER_WAKEUP_EVENTS_FLAGS
api_location:
- netadapter.h
api_type:
- HeaderDef
---

# NET\_ADAPTER\_WAKEUP\_EVENTS\_FLAGS enumeration


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Syntax
------

```ManagedCPlusPlus
typedef enum _NET_ADAPTER_WAKEUP_EVENTS_FLAGS { 
  NET_ADAPTER_WAKE_ON_MEDIA_CONNECT     = = NDIS_PM_WAKE_ON_MEDIA_CONNECT_SUPPORTED,
  NET_ADAPTER_WAKE_ON_MEDIA_DISCONNECT  = = NDIS_PM_WAKE_ON_MEDIA_DISCONNECT_SUPPORTED
} NET_ADAPTER_WAKEUP_EVENTS_FLAGS;
```

Constants
---------

<a href="" id="net-adapter-wake-on-media-connect"></a>**NET\_ADAPTER\_WAKE\_ON\_MEDIA\_CONNECT**  

<a href="" id="net-adapter-wake-on-media-disconnect"></a>**NET\_ADAPTER\_WAKE\_ON\_MEDIA\_DISCONNECT**  

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

## See also


[**NDIS\_PM\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566748)

 

 






