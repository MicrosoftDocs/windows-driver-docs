---
title: NET_ADAPTER_POWER_FLAGS enumeration
description: Defines flags that are used in a client driver's NET\_ADAPTER\_POWER\_CAPABILITIES structure.
ms.assetid: bbfa310a-2de6-4d98-9f6b-e7b8ac1e3439
keywords: ["NET_ADAPTER_POWER_FLAGS enumeration Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NET_ADAPTER_POWER_FLAGS
api_location:
- netadapter.h
api_type:
- HeaderDef
---

# NET\_ADAPTER\_POWER\_FLAGS enumeration


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Defines flags that are used in a client driver's [**NET\_ADAPTER\_POWER\_CAPABILITIES**](net-adapter-power-capabilities.md) structure.

Syntax
------

```ManagedCPlusPlus
typedef enum _NET_ADAPTER_POWER_FLAGS { 
  NET_ADAPTER_POWER_WAKE_PACKET_INDICATION  = = NDIS_PM_WAKE_PACKET_INDICATION_SUPPORTED,
  NET_ADAPTER_POWER_SELECTIVE_SUSPEND       = = NDIS_PM_SELECTIVE_SUSPEND_SUPPORTED
} NET_ADAPTER_POWER_FLAGS;
```

Constants
---------

**NET_ADAPTER_POWER_WAKE_PACKET_INDICATION**  

**NET_ADAPTER_POWER_SELECTIVE_SUSPEND**  
Specifies that NetAdapterCx should suspend an idle network adapter by transitioning the adapter to a low-power state.

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


[**NET\_ADAPTER\_POWER\_CAPABILITIES**](net-adapter-power-capabilities.md)

 

 






