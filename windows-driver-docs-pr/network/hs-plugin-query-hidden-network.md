---
title: HS_PLUGIN_QUERY_HIDDEN_NETWORK function
author: windows-driver-content
description: The HS\_PLUGIN\_QUERY\_HIDDEN\_NETWORK function returns the network identity and network profile for a hidden network.
ms.assetid: edf5ddb0-22f6-4c24-a118-3915a1f2b0af
keywords: 
- typedef DWORD (WINAPI HS_PLUGIN_QUERY_HIDDEN_NETWORK) function Network Drivers Starting with Windows Vista
ms.author: windowsdriverdev
ms.date: 07/31/2017 
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# HS\_PLUGIN\_QUERY\_HIDDEN\_NETWORK function


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20HS_PLUGIN_QUERY_HIDDEN_NETWORK%20function%20%20RELEASE:%20%287/31/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


