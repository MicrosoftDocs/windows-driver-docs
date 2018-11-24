---
title: HS_PLUGIN_IS_HOTSPOT_NETWORK function
description: The HS_PLUGIN_IS_HOTSPOT_NETWORK function is called by the host to determine if a specified network is a hotspot network.
ms.assetid: 24a26ee0-9eb1-49fa-95da-40315a4aab3a
keywords: 
- typedef DWORD (WINAPI HS_PLUGIN_IS_HOTSPOT_NETWORK) function Network Drivers Starting with Windows Vista
ms.date: 07/31/2017
ms.localizationpriority: medium
---

# HS\_PLUGIN\_IS\_HOTSPOT\_NETWORK function

[!include[Wi-Fi Hotspot Offloading deprecation](wi-fi-hotspot-offloading-deprecation.md)]


The **HS\_PLUGIN\_IS\_HOTSPOT\_NETWORK** function is called by the host to determine if a specified network is a hotspot network.

Syntax
------

```ManagedCPlusPlus
 typedef DWORD (WINAPI *HS_PLUGIN_IS_HOTSPOT_NETWORK)(
  _In_      HS_NETWORK_IDENTITY *pNetworkIdentity,
  _Out_     eHS_NETWORK_STATE   *pNetworkState,
  _Out_opt_ HS_NETWORK_PROFILE  *pNetworkProfile
);
```

Parameters
----------

*\*pNetworkIdentity* \[in\]  
Pointer to the [**HS\_NETWORK\_IDENTITY**](hs-network-identity.md) structure for the network from which the device is to be disconnected.

*\*pNetworkState* \[out\]  
An [**eHS\_NETWORK\_STATE**](ehs-network-state.md) enumeration value that indicates the type of network.

*\*pNetworkProfile* \[out, optional\]  
Pointer to the [**HS\_NETWORK\_PROFILE**](hs-network-profile.md) structure for the network.

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

[**eHS\_NETWORK\_STATE**](ehs-network-state.md)

[**HS\_NETWORK\_PROFILE**](hs-network-profile.md)

 

 




