---
title: HSPluginGetVersion function
description: The HSPluginGetVersion function is exported by the plugin DLL and is called to verify that the plugin version matches the host version.
ms.assetid: dfdd534c-43c0-4d96-b85b-de9c2830322d
keywords: 
- HSPluginGetVersion function Network Drivers Starting with Windows Vista
ms.date: 07/31/2017
ms.localizationpriority: medium
---

# HSPluginGetVersion function

[!include[Wi-Fi Hotspot Offloading deprecation](wi-fi-hotspot-offloading-deprecation.md)]


The **HSPluginGetVersion** function is exported by the plugin DLL and is called to verify that the plugin version matches the host version.

Syntax
------

```ManagedCPlusPlus
DWORD HSPluginGetVersion(
  _Out_ HS_PLUGIN_VERSION *pHotspotPluginVersion
);
```

Parameters
----------

*\*pHotspotPluginVersion* \[out\]  
A pointer to the [**HS\_PLUGIN\_VERSION**](hs-plugin-version.md) structure that contains version information for the plugin.

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


[**HS\_PLUGIN\_VERSION**](hs-plugin-version.md)

 

 




