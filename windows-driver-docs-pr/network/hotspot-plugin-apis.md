---
title: HOTSPOT_PLUGIN_APIS structure
description: The HOTSPOT_PLUGIN_APIS structure contains the Hotspot plugin APIs function table.
ms.assetid: eee56f84-2c7f-4218-b7ec-b4fc0181d767
keywords: 
- HOTSPOT_PLUGIN_APIS structure Network Drivers Starting with Windows Vista
- PHOTSPOT_PLUGIN_APIS structure pointer Network Drivers Starting with Windows Vista
ms.date: 07/31/2017
ms.localizationpriority: medium
---

# HOTSPOT\_PLUGIN\_APIS structure

[!include[Wi-Fi Hotspot Offloading deprecation](wi-fi-hotspot-offloading-deprecation.md)]


The **HOTSPOT\_PLUGIN\_APIS** structure contains the Hotspot plugin APIs function table. This function table is returned by the plugin when [**HSPluginInitPlugin**](hsplugininitplugin.md) is called to initialize the plugin. The table contains functions that are called by the hotspot host to communicate with the plugin.

Syntax
------

```ManagedCPlusPlus
typedef struct _HOTSPOT_PLUGIN_APIS {
  HS_PLUGIN_QUERY_SUPPORTED_SIMS     HSPluginQuerySupportedSIMs;
  HS_PLUGIN_QUERY_HIDDEN_NETWORK     HSPluginQueryCellularExceptionHosts;
  HS_PLUGIN_IS_HOTSPOT_NETWORK       HSPluginIsHotspotNetwork;
  HS_PLUGIN_PRE_CONNECT_INIT         HSPluginPreConnectInit;
  HS_PLUGIN_START_POST_CONNECT_AUTH  HSPluginStartPostConnectAuth;
  HS_PLUGIN_STOP_POST_CONNECT_AUTH   HSPluginStopPostConnectAuth;
  HS_PLUGIN_DISCONNECT_FROM_NETWORK  HSPluginDisconnectFromNetwork;
  HS_PLUGIN_RESET                    HSPluginReset;
  HS_PLUGIN_SEND_KEEP_ALIVE          HSPluginSendKeepAlive;
  HS_PLUGIN_CHECK_FOR_UPDATES        HSPluginCheckForUpdates;
  HS_PLUGIN_DEINIT                   HSPluginDeinit;
} HOTSPOT_PLUGIN_APIS, *PHOTSPOT_PLUGIN_APIS;
```

Members
-------

**HSPluginQuerySupportedSIMs**  
API called during plugin initialization.

Called by the hotspot host to retrieve the list of SIMs that the plugin supports. It can be called to retrieve the complete list of supported SIMs, or just the SIMs for a specific network. For more information, see [**HS\_PLUGIN\_QUERY\_SUPPORTED\_SIMS**](hs-plugin-query-supported-sims.md).

**HSPluginQueryCellularExceptionHosts**  
API called during plugin initialization.

Called by the hotspot host if the plugin has specified the **HS\_FLAG\_CAPABILITY\_NETWORK\_TYPE\_HIDDEN** capability by way of the [**HS\_PLUGIN\_PROFILE**](hs-plugin-profile.md) structure. For more information, see [**HS\_PLUGIN\_QUERY\_HIDDEN\_NETWORK**](hs-plugin-query-hidden-network.md).

**HSPluginIsHotspotNetwork**  
API called while processing scan results.

Called by the hotspot host to request the plugin to identify if the network passed in the *pHiddenNetworkIdentity* parameter is a hotspot network. For more information, see [**HS\_PLUGIN\_IS\_HOTSPOT\_NETWORK**](hs-plugin-is-hotspot-network.md).

**HSPluginPreConnectInit**  
Connection-process API.

Called by the hotspot host to notify the plugin to initialize its state when a connection is in progress. For more information, see [**HS\_PLUGIN\_PRE\_CONNECT\_INIT**](hs-plugin-pre-connect-init.md).

**HSPluginStartPostConnectAuth**  
Connection-process API.

Called by the hotspot host to request the plugin to perform any post-connect authentication required to authenticate the device over the network. For more information, see [**HS\_PLUGIN\_START\_POST\_CONNECT\_AUTH**](hs-plugin-start-post-connect-auth.md).

**HSPluginStopPostConnectAuth**  
Connection-process API.

Called by the hotspot host to notify the plugin to stop the authentication process. For more information, see [**HS\_PLUGIN\_STOP\_POST\_CONNECT\_AUTH**](hs-plugin-stop-post-connect-auth.md).

**HSPluginDisconnectFromNetwork**  
Connection-process API.

Called by the hotspot host to notify the plugin of disconnection from network. For more information, see [**HS\_PLUGIN\_DISCONNECT\_FROM\_NETWORK**](hs-plugin-disconnect-from-network.md).

**HSPluginReset**  
API to reset the plugin. If the plugin does not release any pending calls before returning from this call, the plugin will be unloaded.

Called by the hotspot host to reset the plugin. For more information, see [**HS\_PLUGIN\_RESET**](hs-plugin-reset.md).

**HSPluginSendKeepAlive**  
API for plugin to do periodic updates.

Called by the hotspot host to send a keep-alive message to the plugin. For more information, see [**HS\_PLUGIN\_SEND\_KEEP\_ALIVE**](hs-plugin-send-keep-alive.md).

**HSPluginCheckForUpdates**  
API for plugin to do periodic updates.

Called by the hotspot host to check for updates. For more information, see [**HS\_PLUGIN\_CHECK\_FOR\_UPDATES**](hs-plugin-check-for-updates.md).

**HSPluginDeinit**  
API called to de-initialize and clean up the plugin before unloading.

Called by the hotspot host to notify the plugin that it is about to be unloaded. For more information, see [**HS\_PLUGIN\_DEINIT**](hs-plugin-deinit.md).

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

[**HS\_PLUGIN\_QUERY\_SUPPORTED\_SIMS**](hs-plugin-query-supported-sims.md)

[**HS\_PLUGIN\_PROFILE**](hs-plugin-profile.md)

[**HS\_PLUGIN\_QUERY\_HIDDEN\_NETWORK**](hs-plugin-query-hidden-network.md)

[**HS\_PLUGIN\_IS\_HOTSPOT\_NETWORK**](hs-plugin-is-hotspot-network.md)

[**HS\_PLUGIN\_PRE\_CONNECT\_INIT**](hs-plugin-pre-connect-init.md)

[**HS\_PLUGIN\_START\_POST\_CONNECT\_AUTH**](hs-plugin-start-post-connect-auth.md)

[**HS\_PLUGIN\_STOP\_POST\_CONNECT\_AUTH**](hs-plugin-stop-post-connect-auth.md)

[**HS\_PLUGIN\_DISCONNECT\_FROM\_NETWORK**](hs-plugin-disconnect-from-network.md)

[**HS\_PLUGIN\_RESET**](hs-plugin-reset.md)

[**HS\_PLUGIN\_SEND\_KEEP\_ALIVE**](hs-plugin-send-keep-alive.md)

[**HS\_PLUGIN\_CHECK\_FOR\_UPDATES**](hs-plugin-check-for-updates.md)

[**HS\_PLUGIN\_DEINIT**](hs-plugin-deinit.md)

 

 




