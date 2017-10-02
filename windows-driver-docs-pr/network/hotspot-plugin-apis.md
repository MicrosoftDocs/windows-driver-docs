---
title: HOTSPOT_PLUGIN_APIS structure
author: windows-driver-content
description: The HOTSPOT\_PLUGIN\_APIS structure contains the Hotspot plugin APIs function table.
ms.assetid: eee56f84-2c7f-4218-b7ec-b4fc0181d767
keywords: 
- HOTSPOT_PLUGIN_APIS structure Network Drivers Starting with Windows Vista
- PHOTSPOT_PLUGIN_APIS structure pointer Network Drivers Starting with Windows Vista
ms.author: windowsdriverdev
ms.date: 07/31/2017 
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20HOTSPOT_PLUGIN_APIS%20structure%20%20RELEASE:%20%287/31/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


