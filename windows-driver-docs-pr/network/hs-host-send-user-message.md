---
title: HS_HOST_SEND_USER_MESSAGE function
description: The HS_HOST_SEND_USER_MESSAGE function is called to communicate with the user. The message content is contained in custom UI display strings that are passed to the hotspot offload service.
ms.assetid: c4ab1fda-18eb-44e4-aa64-f7b37b4147a3
keywords: 
- typedef DWORD (WINAPI HS_HOST_SEND_USER_MESSAGE) function Network Drivers Starting with Windows Vista
ms.date: 07/31/2017
ms.localizationpriority: medium
---

# HS\_HOST\_SEND\_USER\_MESSAGE function

[!include[Wi-Fi Hotspot Offloading deprecation](wi-fi-hotspot-offloading-deprecation.md)]


The **HS\_HOST\_SEND\_USER\_MESSAGE** function is called to communicate with the user. The message content is contained in custom UI display strings that are passed to the hotspot offload service.

Syntax
------

```ManagedCPlusPlus
 typedef DWORD (WINAPI *HS_HOST_SEND_USER_MESSAGE)(
  _In_ HANDLE hPluginContext,
  _In_ DWORD  dwConnectionId,
  _In_ DWORD  dwStringID
);
```

Parameters
----------

*hPluginContext* \[in\]  
Context handle for the plugin making the call to this function.

*dwConnectionId* \[in\]  
Unique identifier for the network connection.

*dwStringID* \[in\]  
The string ID, used as an index into the string table where the message is stored.

Return value
------------

This function is called by the plugin to communicate with the host and does not return a value.

Remarks
-------

The hotspot plugin stores the messages in a string table. The plugin must pass the string IDs to the hotspot offload service to enable it to load the appropriate strings.

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

 

 




