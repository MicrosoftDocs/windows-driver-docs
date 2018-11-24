---
title: HS_PLUGIN_QUERY_SUPPORTED_SIMS function
description: The HS_PLUGIN_QUERY_SUPPORTED_SIMS function returns the list of SIMs that the plugin supports.
ms.assetid: e1b41bb1-7f82-4298-b070-20cb557fa0fc
keywords: 
- typedef DWORD (WINAPI HS_PLUGIN_QUERY_SUPPORTED_SIMS) function Network Drivers Starting with Windows Vista
ms.date: 07/31/2017
ms.localizationpriority: medium
---

# HS\_PLUGIN\_QUERY\_SUPPORTED\_SIMS function

[!include[Wi-Fi Hotspot Offloading deprecation](wi-fi-hotspot-offloading-deprecation.md)]


The **HS\_PLUGIN\_QUERY\_SUPPORTED\_SIMS** function returns the list of SIMs that the plugin supports.

Syntax
------

```ManagedCPlusPlus
 typedef DWORD (WINAPI *HS_PLUGIN_QUERY_SUPPORTED_SIMS)(
  _In_opt_ HS_NETWORK_IDENTITY      *pNetworkIdentity,
  _Inout_  HS_PLUGIN_SUPPORTED_SIMS *pSupportedSIMs
);
```

Parameters
----------

*\*pNetworkIdentity* \[in, optional\]  
The [**HS\_NETWORK\_IDENTITY**](hs-network-identity.md) structure that uniquely identifies the network.

*\*pSupportedSIMs* \[in, out\]  
Pointer to an array of one or more [**HS\_PLUGIN\_SUPPORTED\_SIMS**](hs-plugin-supported-sims.md) structures that contains the list of supported SIMs.

Return value
------------

This function is called by the host to communicate with the plugin and does not return a value.

Remarks
-------

If the *pNetworkIdentity* parameter exists then only those SIM identities required for connecting to the specified network must be provided, otherwise the entire list of SIMs for connecting to all networks must be provided.

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

[**HS\_PLUGIN\_SUPPORTED\_SIMS**](hs-plugin-supported-sims.md)

 

 




