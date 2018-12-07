---
title: HS_PLUGIN_DISCONNECT_FROM_NETWORK function
description: The HS_PLUGIN_DISCONNECT_FROM_NETWORK function notifies the plugin that the device will be disconnected from the network.
ms.assetid: 8a53c824-18f7-4000-b264-fe852595a9e3
keywords: 
- typedef DWORD (WINAPI HS_PLUGIN_DISCONNECT_FROM_NETWORK) function Network Drivers Starting with Windows Vista
ms.date: 07/31/2017
ms.localizationpriority: medium
---

# HS\_PLUGIN\_DISCONNECT\_FROM\_NETWORK function

[!include[Wi-Fi Hotspot Offloading deprecation](wi-fi-hotspot-offloading-deprecation.md)]


The **HS\_PLUGIN\_DISCONNECT\_FROM\_NETWORK** function notifies the plugin that the device will be disconnected from the network.

Syntax
------

```ManagedCPlusPlus
 typedef DWORD (WINAPI *HS_PLUGIN_DISCONNECT_FROM_NETWORK)(
  _In_ HS_NETWORK_IDENTITY *pNetworkIdentity
);
```

Parameters
----------

*\*pNetworkIdentity* \[in\]  
Pointer to the [**HS\_NETWORK\_IDENTITY**](hs-network-identity.md) structure for the network from which the device is to be disconnected.

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

 

 




