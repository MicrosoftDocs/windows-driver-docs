---
title: HS_PLUGIN_SEND_KEEP_ALIVE function
description: The HS_PLUGIN_SEND_KEEP_ALIVE function is called by the host to send a network connection keep-alive message. It will be called at the frequency specified in the dwKeepAliveTimeMins member of the plugin's HS_PLUGIN_PROFILE structure.
ms.assetid: 1db91146-03bb-4513-9c1b-f0dbd5c941f5
keywords: 
- typedef DWORD (WINAPI HS_PLUGIN_SEND_KEEP_ALIVE) function Network Drivers Starting with Windows Vista
ms.date: 07/31/2017
ms.localizationpriority: medium
---

# HS\_PLUGIN\_SEND\_KEEP\_ALIVE function

[!include[Wi-Fi Hotspot Offloading deprecation](wi-fi-hotspot-offloading-deprecation.md)]


The **HS\_PLUGIN\_SEND\_KEEP\_ALIVE** function is called by the host to send a network connection keep-alive message. It will be called at the frequency specified in the **dwKeepAliveTimeMins** member of the plugin's [**HS\_PLUGIN\_PROFILE**](hs-plugin-profile.md) structure.

Syntax
------

```ManagedCPlusPlus
 typedef DWORD (WINAPI *HS_PLUGIN_SEND_KEEP_ALIVE)(
    
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

 

 




