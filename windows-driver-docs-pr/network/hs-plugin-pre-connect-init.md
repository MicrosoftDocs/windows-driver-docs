---
title: HS_PLUGIN_PRE_CONNECT_INIT function
description: The HS_PLUGIN_PRE_CONNECT_INIT function is called to notify the plugin to initialize its state when a connection to a hotspot network is in progress.
ms.assetid: 799242a0-144f-4d3f-b48c-9e96a851d8c4
keywords: 
- typedef DWORD (WINAPI HS_PLUGIN_PRE_CONNECT_INIT) function Network Drivers Starting with Windows Vista
ms.date: 07/31/2017
ms.localizationpriority: medium
---

# HS\_PLUGIN\_PRE\_CONNECT\_INIT function

[!include[Wi-Fi Hotspot Offloading deprecation](wi-fi-hotspot-offloading-deprecation.md)]


The **HS\_PLUGIN\_PRE\_CONNECT\_INIT** function is called to notify the plugin to initialize its state when a connection to a hotspot network is in progress.

Syntax
------

```ManagedCPlusPlus
 typedef DWORD (WINAPI *HS_PLUGIN_PRE_CONNECT_INIT)(
  _In_ HS_NETWORK_IDENTITY *pNetworkIdentity
);
```

Parameters
----------

*\*pNetworkIdentity* \[in\]  
Pointer to the [**HS\_NETWORK\_IDENTITY**](hs-network-identity.md) structure for the target network.

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

 

 




