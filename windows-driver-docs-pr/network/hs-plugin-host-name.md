---
title: HS_PLUGIN_HOST_NAME structure
description: The HS_PLUGIN_HOST_NAME structure contains the host name.
ms.assetid: 3995fff6-6992-4dd6-a94c-a27b2ee44436
keywords: 
- HS_PLUGIN_HOST_NAME structure Network Drivers Starting with Windows Vista
- PHS_PLUGIN_HOST_NAME structure pointer Network Drivers Starting with Windows Vista
ms.date: 07/31/2017
ms.localizationpriority: medium
---

# HS\_PLUGIN\_HOST\_NAME structure

[!include[Wi-Fi Hotspot Offloading deprecation](wi-fi-hotspot-offloading-deprecation.md)]


The **HS\_PLUGIN\_HOST\_NAME** structure contains the host name.

Syntax
------

```ManagedCPlusPlus
typedef struct _HS_PLUGIN_HOST_NAME {
  WHCAR pszHostName[HS_CONST_MAX_HOST_NAME_LENGTH+1];
} HS_PLUGIN_HOST_NAME, *PHS_PLUGIN_HOST_NAME;
```

Members
-------

**pszHostName**  
Pointer to the host name.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Hotspotoffloadplugin.h (include Hotspotoffloadplugin.h)</td>
</tr>
</tbody>
</table>

 

 




