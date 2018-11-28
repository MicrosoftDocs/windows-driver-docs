---
title: eHS_UPDATE_RESULT enumeration
description: The eHS_UPDATE_RESULT enumeration indicates the result of a “check for updates” request.
ms.assetid: 7b9b8ddc-3101-466a-9640-b936f6d14de4
keywords: 
- eHS_UPDATE_RESULT enumeration Network Drivers Starting with Windows Vista
ms.date: 07/31/2017
ms.localizationpriority: medium
---

# eHS\_UPDATE\_RESULT enumeration

[!include[Wi-Fi Hotspot Offloading deprecation](wi-fi-hotspot-offloading-deprecation.md)]


The **eHS\_UPDATE\_RESULT** enumeration indicates the result of a “check for updates” request.

Syntax
------

```ManagedCPlusPlus
typedef enum _eHS_UPDATE_RESULT { 
  HS_UPDATE_RESULT_SUCCESS,
  HS_UPDATE_RESULT_ACTION_RECONNECT,
  HS_UPDATE_RESULT_ACTION_RELOAD,
  HS_UPDATE_RESULT_MAX
} eHS_UPDATE_RESULT;
```

Constants
---------

<a href="" id="hs-update-result-success"></a>**HS\_UPDATE\_RESULT\_SUCCESS**  
Indicates the update was successful.

<a href="" id="hs-update-result-action-reconnect"></a>**HS\_UPDATE\_RESULT\_ACTION\_RECONNECT**  
The result of the update request requires the service to disconnect and reconnect.

<a href="" id="hs-update-result-action-reload"></a>**HS\_UPDATE\_RESULT\_ACTION\_RELOAD**  
The result of the update request requires the service to unload and reload the plugin.

<a href="" id="hs-update-result-max"></a>**HS\_UPDATE\_RESULT\_MAX**  
Indicates an out-of-range value.

Remarks
-------

The plugin passes this enumeration value to the hotspot plugin host through the [**HS\_HOST\_UPDATE\_CONFIGURATION\_COMPLETION**](hs-host-update-configuration-completion.md) function, which is used to inform the hotspot plugin host of the results of a call to [**HS\_PLUGIN\_CHECK\_FOR\_UPDATES**](hs-plugin-check-for-updates.md).

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
<td><p>Windows 10 Mobile</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Hotspotoffloadplugin.h (include Hotspotoffloadplugin.h)</td>
</tr>
</tbody>
</table>

## See also


[**HS\_HOST\_UPDATE\_CONFIGURATION\_COMPLETION**](hs-host-update-configuration-completion.md)

[**HS\_PLUGIN\_CHECK\_FOR\_UPDATES**](hs-plugin-check-for-updates.md)

 

 




