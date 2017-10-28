---
title: HS_PLUGIN_QUERY_SUPPORTED_SIMS function
author: windows-driver-content
description: The HS_PLUGIN_QUERY_SUPPORTED_SIMS function returns the list of SIMs that the plugin supports.
ms.assetid: e1b41bb1-7f82-4298-b070-20cb557fa0fc
keywords: 
- typedef DWORD (WINAPI HS_PLUGIN_QUERY_SUPPORTED_SIMS) function Network Drivers Starting with Windows Vista
ms.author: windowsdriverdev
ms.date: 07/31/2017 
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20HS_PLUGIN_QUERY_SUPPORTED_SIMS%20function%20%20RELEASE:%20%287/31/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


