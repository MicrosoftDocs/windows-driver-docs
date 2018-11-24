---
title: HS_PLUGIN_RESET function
description: The HS_PLUGIN_RESET function is called by the host to notify the plugin that it must reset its state.
ms.assetid: 9f5683c9-b426-4802-85bd-c1ce770b9e46
keywords: 
- typedef DWORD (WINAPI HS_PLUGIN_RESET) function Network Drivers Starting with Windows Vista
ms.date: 07/31/2017
ms.localizationpriority: medium
---

# HS\_PLUGIN\_RESET function

[!include[Wi-Fi Hotspot Offloading deprecation](wi-fi-hotspot-offloading-deprecation.md)]


The **HS\_PLUGIN\_RESET** function is called by the host to notify the plugin that it must reset its state.

Syntax
------

```ManagedCPlusPlus
 typedef DWORD (WINAPI *HS_PLUGIN_RESET)(
    
);
```

Parameters
----------

This function has no parameters.

**   

Return value
------------

This function is called by the host to communicate with the plugin and does not return a value.

Remarks
-------

The plugin should terminate all threads and stop any activities in progress.

The plugin is unloaded if it fails to reset.

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

 

 




