---
title: HS_PLUGIN_START_POST_CONNECT_AUTH function
description: The HS_PLUGIN_START_POST_CONNECT_AUTH function is called to perform any post-connect authentication required to authenticate the device over the network.
ms.assetid: f52236fc-2afd-46e2-ae88-7c4fa10f8d59
keywords: 
- typedef DWORD (WINAPI HS_PLUGIN_START_POST_CONNECT_AUTH) function Network Drivers Starting with Windows Vista
ms.date: 07/31/2017
ms.localizationpriority: medium
---

# HS\_PLUGIN\_START\_POST\_CONNECT\_AUTH function

[!include[Wi-Fi Hotspot Offloading deprecation](wi-fi-hotspot-offloading-deprecation.md)]


The **HS\_PLUGIN\_START\_POST\_CONNECT\_AUTH** function is called to perform any post-connect authentication required to authenticate the device over the network.

Syntax
------

```ManagedCPlusPlus
 typedef DWORD (WINAPI *HS_PLUGIN_START_POST_CONNECT_AUTH)(
  _In_ DWORD                 dwConnectionId,
  _In_ HS_CONNECTION_CONTEXT *pConnectContext,
  _In_ HS_SIM_DATA           *pSIMData,
  _In_ HS_NETWORK_IDENTITY   *pNetworkIdentity,
  _In_ HS_NETWORK_PROFILE    *pNetworkProfile
);
```

Parameters
----------

*dwConnectionId* \[in\]  
Unique identifier for the network connection.

*\*pConnectContext* \[in\]  
Pointer to a [**HS\_CONNECTION\_CONTEXT**](hs-connection-context.md) structure that contains the information required by the plugin for post-connect authentication.

*\*pSIMData* \[in\]  
Pointer to a [**HS\_SIM\_DATA**](hs-sim-data.md) structure that contains information from the SIM required by the plugin for post-connect authentication.

*\*pNetworkIdentity* \[in\]  
Pointer to the [**HS\_NETWORK\_IDENTITY**](hs-network-identity.md) structure for the network.

*\*pNetworkProfile* \[in\]  
Pointer to the [**HS\_NETWORK\_PROFILE**](hs-network-profile.md) structure that contains the network profile.

Return value
------------

This function is called by the host to communicate with the plugin and does not return a value.

Remarks
-------

After calling this function, the plugin must call the [**HS\_HOST\_POST\_CONNECT\_AUTH\_COMPLETION**](hs-host-post-connect-auth-completion.md) handler to inform the host of the status of the request.

If the network uses EAP-SIM/AKA authentication, the plugin is not expected to perform any activity in this state. However, if the network requires HTTP-based authentication, the plugin must perform the appropriate authentication.

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


[**HS\_CONNECTION\_CONTEXT**](hs-connection-context.md)

[**HS\_SIM\_DATA**](hs-sim-data.md)

[**HS\_NETWORK\_IDENTITY**](hs-network-identity.md)

[**HS\_NETWORK\_PROFILE**](hs-network-profile.md)

 

 




