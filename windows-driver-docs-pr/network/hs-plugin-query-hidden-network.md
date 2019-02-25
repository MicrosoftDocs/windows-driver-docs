---
title: HS_PLUGIN_QUERY_HIDDEN_NETWORK function
description: The HS_PLUGIN_QUERY_HIDDEN_NETWORK function returns the network identity and network profile for a hidden network.
ms.assetid: edf5ddb0-22f6-4c24-a118-3915a1f2b0af
keywords: 
- typedef DWORD (WINAPI HS_PLUGIN_QUERY_HIDDEN_NETWORK) function Network Drivers Starting with Windows Vista
ms.date: 07/31/2017
ms.localizationpriority: medium
---

# HS\_PLUGIN\_QUERY\_HIDDEN\_NETWORK function

[!include[Wi-Fi Hotspot Offloading deprecation](wi-fi-hotspot-offloading-deprecation.md)]


The **HS\_PLUGIN\_QUERY\_HIDDEN\_NETWORK** function returns the network identity and network profile for a hidden network.

Syntax
------

```ManagedCPlusPlus
 typedef DWORD (WINAPI *HS_PLUGIN_QUERY_HIDDEN_NETWORK)(
  _Out_ HS_NETWORK_IDENTITY *pHiddenNetworkIdentity,
  _Out_ HS_NETWORK_PROFILE  *pHiddenNetworkProfile
);
```

Parameters
----------

*\*pHiddenNetworkIdentity* \[out\]  
The [**HS\_NETWORK\_IDENTITY**](hs-network-identity.md) structure that uniquely identifies the network.

*\*pHiddenNetworkProfile* \[out\]  
The [**HS\_NETWORK\_PROFILE**](hs-network-profile.md) structure that contains the network profile.

Return value
------------

This function is called by the host to communicate with the plugin and does not return a value.

Remarks
-------

The host calls this function only if the **dwPluginCapabilities** field of the associated plugin's [**HS\_PLUGIN\_PROFILE**](hs-plugin-profile.md) structure includes the **HS\_FLAG\_CAPABILITY\_NETWORK\_TYPE\_HIDDEN** capability.

The plugin must provide both the network identity and the network profile for the hidden Wi-Fi network.

This network must have the highest priority (1) among all the hotspot networks.

The hotspot offload service imposes a limitation of one hidden network for the life of the service. Therefore, in the case where there are multiple plugins installed, only the first plugin's request to specify a hidden network will be accepted.

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

[**HS\_NETWORK\_PROFILE**](hs-network-profile.md)

[**HS\_PLUGIN\_PROFILE**](hs-plugin-profile.md)

 

 




