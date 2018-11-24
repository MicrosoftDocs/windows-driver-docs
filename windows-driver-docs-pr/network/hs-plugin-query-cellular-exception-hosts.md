---
title: HS_PLUGIN_QUERY_CELLULAR_EXCEPTION_HOSTS function
description: The HS_PLUGIN_QUERY_CELLULAR_EXCEPTION_HOSTS function queries the list of hosts that the plugin will need to connect to over cellular as part of its authentication process.
ms.assetid: 7f38f146-a637-4ec3-8610-ea4934c4a57a
keywords: 
- typedef DWORD (WINAPI HS_PLUGIN_QUERY_CELLULAR_EXCEPTION_HOSTS) function Network Drivers Starting with Windows Vista
ms.date: 07/31/2017
ms.localizationpriority: medium
---

# HS\_PLUGIN\_QUERY\_CELLULAR\_EXCEPTION\_HOSTS function

[!include[Wi-Fi Hotspot Offloading deprecation](wi-fi-hotspot-offloading-deprecation.md)]


The **HS\_PLUGIN\_QUERY\_CELLULAR\_EXCEPTION\_HOSTS** function queries the list of hosts that the plugin will need to connect to over cellular as part of its authentication process.

Syntax
------

```ManagedCPlusPlus
 typedef DWORD (WINAPI *HS_PLUGIN_QUERY_CELLULAR_EXCEPTION_HOSTS)(
  _Inout_ HS_PLUGIN_CELLULAR_EXCEPTION_HOSTS *pExceptionsList
);
```

Parameters
----------

*\*pExceptionsList* \[in, out\]  
The [**HS\_PLUGIN\_CELLULAR\_EXCEPTION\_HOSTS**](hs-plugin-cellular-exception-hosts.md) structure that contains the list of cellular host names.

Return value
------------

This function is called by the host to communicate with the plugin and does not return a value.

Remarks
-------

This function is called only if the plugin sets the **dwNumCellularExceptions** field of its [**HS\_PLUGIN\_PROFILE**](hs-plugin-profile.md) to a value greater than zero.

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


[**HS\_PLUGIN\_CELLULAR\_EXCEPTION\_HOSTS**](hs-plugin-cellular-exception-hosts.md)

[**HS\_PLUGIN\_PROFILE**](hs-plugin-profile.md)

 

 




