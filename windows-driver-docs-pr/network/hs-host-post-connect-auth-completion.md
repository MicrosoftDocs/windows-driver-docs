---
title: HS_HOST_POST_CONNECT_AUTH_COMPLETION function
description: The HS_HOST_POST_CONNECT_AUTH_COMPLETION function indicates the success or failure of an authentication attempt following a Wi-Fi connection setup at layer 2.
ms.assetid: 2c69802b-968b-400c-b02c-c2d39fa51d5a
keywords: 
- typedef DWORD (WINAPI HS_HOST_POST_CONNECT_AUTH_COMPLETION) function Network Drivers Starting with Windows Vista
ms.date: 07/31/2017
ms.localizationpriority: medium
---

# HS\_HOST\_POST\_CONNECT\_AUTH\_COMPLETION function

[!include[Wi-Fi Hotspot Offloading deprecation](wi-fi-hotspot-offloading-deprecation.md)]


The **HS\_HOST\_POST\_CONNECT\_AUTH\_COMPLETION** function indicates the success or failure of an authentication attempt following a Wi-Fi connection setup at layer 2.

Syntax
------

```ManagedCPlusPlus
 typedef DWORD (WINAPI *HS_HOST_POST_CONNECT_AUTH_COMPLETION)(
  _In_     HANDLE                    hPluginContext,
  _In_     DWORD                     dwConnectionId,
  _In_     eHS_AUTHENTICATION_RESULT AuthResult,
  _In_opt_ LPVOID                    pvReserved
);
```

Parameters
----------

*hPluginContext* \[in\]  
Context handle for the plugin making the call to this function.

*dwConnectionId* \[in\]  
Unique identifier for the network connection.

*AuthResult* \[in\]  
The [**eHS\_AUTHENTICATION\_RESULT**](ehs-authentication-result.md) enumeration value that indicates success or failure.

*pvReserved* \[in, optional\]  
Reserved for future use.

Return value
------------

This function is called by the plugin to communicate with the host and does not return a value.

Remarks
-------

The plugin must call this function to inform the host of the result of a previous call to [**HS\_PLUGIN\_START\_POST\_CONNECT\_AUTH**](hs-plugin-start-post-connect-auth.md).

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


[**eHS\_AUTHENTICATION\_RESULT**](ehs-authentication-result.md)

[**HS\_PLUGIN\_START\_POST\_CONNECT\_AUTH**](hs-plugin-start-post-connect-auth.md)

 

 




