---
title: HS_PLUGIN_STOP_POST_CONNECT_AUTH function
description: The HS_PLUGIN_STOP_POST_CONNECT_AUTH function is called to notify the plugin to stop the authentication process.
ms.assetid: 2e4e01b1-e41a-41db-a3ca-6cc6b53b3a8b
keywords: 
- typedef DWORD (WINAPI HS_PLUGIN_STOP_POST_CONNECT_AUTH) function Network Drivers Starting with Windows Vista
ms.date: 07/31/2017
ms.localizationpriority: medium
---

# HS\_PLUGIN\_STOP\_POST\_CONNECT\_AUTH function

[!include[Wi-Fi Hotspot Offloading deprecation](wi-fi-hotspot-offloading-deprecation.md)]


The **HS\_PLUGIN\_STOP\_POST\_CONNECT\_AUTH** function is called to notify the plugin to stop the authentication process.

Syntax
------

```ManagedCPlusPlus
 typedef DWORD (WINAPI *HS_PLUGIN_STOP_POST_CONNECT_AUTH)(
  _In_ HS_NETWORK_IDENTITY *pNetworkIdentity
);
```

Parameters
----------

*\*pNetworkIdentity* \[in\]  
The [**HS\_NETWORK\_IDENTITY**](hs-network-identity.md) structure that uniquely identifies the network.

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


[**HS\_NETWORK\_IDENTITY**](hs-network-identity.md)

 

 




