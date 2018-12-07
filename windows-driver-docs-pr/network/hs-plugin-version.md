---
title: HS_PLUGIN_VERSION structure
description: The HS_PLUGIN_VERSION structure contains the minimum and maximum hotspot host versions supported by the plugin.
ms.assetid: ced24606-0379-4b13-831c-11de3ed6cd2b
keywords: 
- HS_PLUGIN_VERSION structure Network Drivers Starting with Windows Vista
- PHS_PLUGIN_VERSION structure pointer Network Drivers Starting with Windows Vista
ms.date: 07/31/2017
ms.localizationpriority: medium
---

# HS\_PLUGIN\_VERSION structure

[!include[Wi-Fi Hotspot Offloading deprecation](wi-fi-hotspot-offloading-deprecation.md)]


The **HS\_PLUGIN\_VERSION** structure contains the minimum and maximum hotspot host versions supported by the plugin.

Syntax
------

```ManagedCPlusPlus
typedef struct _HS_PLUGIN_VERSION {
  DWORD dwVerMin;
  DWORD dwVerMax;
} HS_PLUGIN_VERSION, *PHS_PLUGIN_VERSION;
```

Members
-------

**dwVerMin**  
The minimum hotspot host version supported by the plugin.

**dwVerMax**  
The maximum hotspot host version supported by the plugin.

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

 

 




