---
title: NET_DRIVER_GLOBALS structure
description: Call NET\_DRIVER\_GLOBALS\_INIT to initialize this structure.
ms.assetid: 1d6c5f47-52ba-475d-b3c4-e86cf12562b4
keywords: ["NET_DRIVER_GLOBALS structure Network Drivers Starting with Windows Vista", "PNET_DRIVER_GLOBALS structure pointer Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NET_DRIVER_GLOBALS
api_location:
- netadaptercxtypes.h
api_type:
- HeaderDef
---

# NET\_DRIVER\_GLOBALS structure


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Call NET\_DRIVER\_GLOBALS\_INIT to initialize this structure.

Syntax
------

```ManagedCPlusPlus
typedef struct _NET_DRIVER_GLOBALS {
  ULONG Unused;
} NET_DRIVER_GLOBALS, *PNET_DRIVER_GLOBALS;
```

Members
-------

**Unused**  

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
<td align="left">Netadaptercxtypes.h</td>
</tr>
</tbody>
</table>

 

 





