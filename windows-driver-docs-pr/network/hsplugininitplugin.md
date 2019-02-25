---
title: HSPluginInitPlugin function
description: The HSPluginInitPlugin function is exported by the plugin DLL and is called to initialize the plugin.
ms.assetid: db51267c-4f38-47bd-bde2-7b27a93dd2a7
keywords: 
- HSPluginInitPlugin function Network Drivers Starting with Windows Vista
ms.date: 07/31/2017
ms.localizationpriority: medium
---

# HSPluginInitPlugin function

[!include[Wi-Fi Hotspot Offloading deprecation](wi-fi-hotspot-offloading-deprecation.md)]


The **HSPluginInitPlugin** function is exported by the plugin DLL and is called to initialize the plugin.

Syntax
------

```ManagedCPlusPlus
DWORD HSPluginInitPlugin(
  _In_  HANDLE                hPluginContext,
  _In_  DWORD                 dwVerNumUsed,
  _In_  DWORD                 dwHostCapabilities,
  _In_  HS_DEVICE_IDENTITY    *pDeviceIdentity,
  _In_  HOTSPOT_HOST_HANDLERS *pHotspotHostHandlers,
  _Out_ HOTSPOT_PLUGIN_APIS   *pHotspotPluginAPIs,
  _Out_ HS_PLUGIN_PROFILE     *pPluginProfile
);
```

Parameters
----------

*hPluginContext* \[in\]  
A handle, provided by the host, that the plugin is required to save and then use when it needs to make a request to the host by way of the host handler functions.

*dwVerNumUsed* \[in\]  
The host's current version number.

*dwHostCapabilities* \[in\]  
Value that specifies the list of capabilities that the host can provide to the plugin. This value is the bitwise OR combination of the applicable capability flags. For more information about capability flags, see the **HS\_FLAG\_CAPABILITY\_\\*** constants in [**Wi-Fi Hotspot Offloading Constants**](wi-fi-hotspot-offloading-constants.md).

**Note**  If the host does not supply all the capabilities required by the plugin, the plugin will not be initialized.

 

*\*pDeviceIdentity* \[in\]  
Pointer to a [**HS\_DEVICE\_IDENTITY**](hs-device-identity.md) structure that contains information about the device manufacturer and model.

*\*pHotspotHostHandlers* \[in\]  
Pointer to a [**HOTSPOT\_HOST\_HANDLERS**](hotspot-host-handlers.md) structure that contains the hotspot host handlers function table. This table contains pointers to functions that are called by the plugin to communicate with the hotspot host.

*\*pHotspotPluginAPIs* \[out\]  
Pointer to the [**HOTSPOT\_PLUGIN\_APIS**](hotspot-plugin-apis.md) structure that contains the hotspot plugin APIs function table. This table is returned by the plugin and contains pointers to functions that are called by the host to communicate with the plugin.

*\*pPluginProfile* \[out\]  
Pointer to a [**HS\_PLUGIN\_PROFILE**](hs-plugin-profile.md) structure, returned by the plugin, that provides information about the plugin.

Remarks
-------

During initialization, the host provides the following:

-   The plugin context handle
-   The current version number
-   A list of capabilities that the host can provide to the plugin
-   A pointer to the host handler function table through which the plugin can communicate with the host

The plugin returns a pointer to its own function table and a pointer to its [**HS\_PLUGIN\_PROFILE**](hs-plugin-profile.md) structure.

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


[**Wi-Fi Hotspot Offloading Constants**](wi-fi-hotspot-offloading-constants.md)

[**HS\_DEVICE\_IDENTITY**](hs-device-identity.md)

[**HOTSPOT\_HOST\_HANDLERS**](hotspot-host-handlers.md)

[**HOTSPOT\_PLUGIN\_APIS**](hotspot-plugin-apis.md)

[**HS\_PLUGIN\_PROFILE**](hs-plugin-profile.md)

 

 




