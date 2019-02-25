---
title: HS_HOST_SEND_KEEP_ALIVE_COMPLETION function
description: The HS_HOST_SEND_KEEP_ALIVE_COMPLETION function indicates the success or failure of a request for a network send keep-alive message.
ms.assetid: 19fc1210-2c3a-46ca-96fb-dccafa9e9eef
keywords: 
- typedef DWORD (WINAPI HS_HOST_SEND_KEEP_ALIVE_COMPLETION) function Network Drivers Starting with Windows Vista
ms.date: 07/31/2017
ms.localizationpriority: medium
---

# HS\_HOST\_SEND\_KEEP\_ALIVE\_COMPLETION function

[!include[Wi-Fi Hotspot Offloading deprecation](wi-fi-hotspot-offloading-deprecation.md)]


The **HS\_HOST\_SEND\_KEEP\_ALIVE\_COMPLETION** function indicates the success or failure of a request for a network send keep-alive message.

Syntax
------

```ManagedCPlusPlus
 typedef DWORD (WINAPI *HS_HOST_SEND_KEEP_ALIVE_COMPLETION)(
  _In_ HANDLE hPluginContext,
  _In_ DWORD  dwResult
);
```

Parameters
----------

*hPluginContext* \[in\]  
Context handle for the plugin making the call to this function.

*dwResult* \[in\]  
The result code.

Return value
------------

This function is called by the plugin to communicate with the host and does not return a value.

Remarks
-------

The plugin must call this function to inform the host of the result of a previous call to [**HS\_PLUGIN\_SEND\_KEEP\_ALIVE**](hs-plugin-send-keep-alive.md).

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


[**HS\_PLUGIN\_SEND\_KEEP\_ALIVE**](hs-plugin-send-keep-alive.md)

 

 




