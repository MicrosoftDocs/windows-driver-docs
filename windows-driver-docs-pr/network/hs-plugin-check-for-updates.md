---
title: HS_PLUGIN_CHECK_FOR_UPDATES function
description: The HS_PLUGIN_CHECK_FOR_UPDATES function checks for configuration updates at the frequency specified in the dwProfileUpdateTimeDays member of the plugin’s HS_PLUGIN_PROFILE structure.
ms.assetid: 8db3c237-d61b-4dca-b3a5-2fdaeb683b15
keywords: 
- typedef DWORD (WINAPI HS_PLUGIN_CHECK_FOR_UPDATES) function Network Drivers Starting with Windows Vista
ms.date: 07/31/2017
ms.localizationpriority: medium
---

# HS\_PLUGIN\_CHECK\_FOR\_UPDATES function

[!include[Wi-Fi Hotspot Offloading deprecation](wi-fi-hotspot-offloading-deprecation.md)]


The **HS\_PLUGIN\_CHECK\_FOR\_UPDATES** function checks for configuration updates at the frequency specified in the **dwProfileUpdateTimeDays** member of the plugin’s [**HS\_PLUGIN\_PROFILE**](hs-plugin-profile.md) structure.

Syntax
------

```ManagedCPlusPlus
 typedef DWORD (WINAPI *HS_PLUGIN_CHECK_FOR_UPDATES)(
    
);
```

Parameters
----------

This function has no parameters.

**   

Return value
------------

This function is called by the host to communicate with the plugin and does not return a value.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Windows 10 Mobile</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Hotspotoffloadplugin.h (include Hotspotoffloadplugin.h)</td>
</tr>
</tbody>
</table>

## See also


[**HS\_PLUGIN\_PROFILE**](hs-plugin-profile.md)

 

 




