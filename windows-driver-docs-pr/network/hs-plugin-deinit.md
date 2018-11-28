---
title: HS_PLUGIN_DEINIT function
description: The HS_PLUGIN_DEINIT function is called by the host to notify the plugin that it will be unloaded.
ms.assetid: 3bb0ad85-91db-476e-b347-0fa8ed4ae24e
keywords: 
- typedef DWORD (WINAPI HS_PLUGIN_DEINIT) function Network Drivers Starting with Windows Vista
ms.date: 07/31/2017
ms.localizationpriority: medium
---

# HS\_PLUGIN\_DEINIT function

[!include[Wi-Fi Hotspot Offloading deprecation](wi-fi-hotspot-offloading-deprecation.md)]


The **HS\_PLUGIN\_DEINIT** function is called by the host to notify the plugin that it will be unloaded.

Syntax
------

```ManagedCPlusPlus
 typedef DWORD (WINAPI *HS_PLUGIN_DEINIT)(
  _In_ eHS_UNLOAD_REASON UnloadReason
);
```

Parameters
----------

*UnloadReason* \[in\]  
An [**eHS\_UNLOAD\_REASON**](ehs-unload-reason.md) enumeration value that indicates the reason for the unload.

Return value
------------

This function is called by the host to communicate with the plugin and does not return a value.

Remarks
-------

Upon receiving notification that it will be unloaded, the plugin should complete any current activity and save state, if required.

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


[**eHS\_UNLOAD\_REASON**](ehs-unload-reason.md)

 

 




