---
title: HS_HOST_UPDATE_CONFIGURATION_COMPLETION function
description: The HS_HOST_UPDATE_CONFIGURATION_COMPLETION function indicates the success or failure of a request to check for updates.
ms.assetid: 7e9eda04-db8e-4181-90e3-8716a99429a8
keywords: 
- typedef DWORD (WINAPI HS_HOST_UPDATE_CONFIGURATION_COMPLETION) function Network Drivers Starting with Windows Vista
ms.date: 07/31/2017
ms.localizationpriority: medium
---

# HS\_HOST\_UPDATE\_CONFIGURATION\_COMPLETION function

[!include[Wi-Fi Hotspot Offloading deprecation](wi-fi-hotspot-offloading-deprecation.md)]


The **HS\_HOST\_UPDATE\_CONFIGURATION\_COMPLETION** function indicates the success or failure of a request to check for updates.

Syntax
------

```ManagedCPlusPlus
 typedef DWORD (WINAPI *HS_HOST_UPDATE_CONFIGURATION_COMPLETION)(
  _In_ HANDLE            hPluginContext,
  _In_ eHS_UPDATE_RESULT UpdateResult
);
```

Parameters
----------

*hPluginContext* \[in\]  
Context handle for the plugin making the call to this function.

*UpdateResult* \[in\]  
The [**eHS\_UPDATE\_RESULT**](ehs-update-result.md) enumeration value that indicates the result of the request to check for updates.

Return value
------------

This function is called by the plugin to communicate with the host and does not return a value.

Remarks
-------

The plugin must call this function to inform the host of the result of a previous call to [**HS\_PLUGIN\_CHECK\_FOR\_UPDATES**](hs-plugin-check-for-updates.md).

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


[**eHS\_UPDATE\_RESULT**](ehs-update-result.md)

[**HS\_PLUGIN\_CHECK\_FOR\_UPDATES**](hs-plugin-check-for-updates.md)

 

 




