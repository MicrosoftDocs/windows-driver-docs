---
title: HS_PLUGIN_PROFILE structure
description: The HS_PLUGIN_PROFILE structure provides information about the plugin. The members of this structure are set by the plugin during execution of the HSPluginInitPlugin function that is called by the host.
ms.assetid: 0c4f7088-737e-479a-b46e-a55e96719775
keywords: 
- HS_PLUGIN_PROFILE structure Network Drivers Starting with Windows Vista
- PHS_PLUGIN_PROFILE structure pointer Network Drivers Starting with Windows Vista
ms.date: 07/31/2017
ms.localizationpriority: medium
---

# HS\_PLUGIN\_PROFILE structure

[!include[Wi-Fi Hotspot Offloading deprecation](wi-fi-hotspot-offloading-deprecation.md)]


The **HS\_PLUGIN\_PROFILE** structure provides information about the plugin. The members of this structure are set by the plugin during execution of the [**HSPluginInitPlugin**](hsplugininitplugin.md) function that is called by the host.

Syntax
------

```ManagedCPlusPlus
typedef struct _HS_PLUGIN_PROFILE {
  DWORD dwPluginCapabilities;
  DWORD dwNumNetworksSupported;
  DWORD dwProviderNameStringID;
  DWORD dwGenericNetworkNameStringID;
  DWORD dwAdvancedPageStringID;
  DWORD dwProfileUpdateTimeDays;
  WCHAR szRealm[HS_CONST_MAX_REALM_LENGTH+1];
  DWORD dwSupportedSIMCount;
} HS_PLUGIN_PROFILE, *PHS_PLUGIN_PROFILE;
```

Members
-------

**dwPluginCapabilities**  
Required.

A subset of the possible **HS\_FLAG\_CAPABILITY\_NETWORK\_\\*** values. For more information about hotspot host capabilities, see [**Wi-Fi Hotspot Offloading Constants**](wi-fi-hotspot-offloading-constants.md).

**dwNumNetworksSupported**  
Required.

Total number of networks supported by this plugin.

**dwProviderNameStringID**  
Required.

The network provider name which is displayed to the user. Maximum string size = MAX\_PROVIDER\_NAME\_LENGTH.

**dwGenericNetworkNameStringID**  
Optional.

Network name. Maximum string size = MAX\_NETWORK\_DISPLAY\_NAME\_LENGTH.

**dwAdvancedPageStringID**  
Optional.

Maximum string size = HS\_CONST\_MAX\_ADVANCED\_PAGE\_STRING\_LENGTH.

**dwProfileUpdateTimeDays**  
Optional.

Must be greater than or equal to HS\_CONST\_MIN\_PROFILE\_UPDATE\_TIME\_IN\_DAYS.

**szRealm**  
Required if HS\_FLAG\_CAPABILITIES\_NETWORK\_CUSTOM\_REALM is set.

Network-specific realm value.

**dwSupportedSIMCount**  
The size of the list pointed to by **pSupported SIMs**.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Hotspotoffloadplugin.h (include Hotspotoffloadplugin.h)</td>
</tr>
</tbody>
</table>

## See also


[**HSPluginInitPlugin**](hsplugininitplugin.md)

[**Wi-Fi Hotspot Offloading Constants**](wi-fi-hotspot-offloading-constants.md)

 

 




