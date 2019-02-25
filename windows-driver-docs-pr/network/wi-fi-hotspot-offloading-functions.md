---
title: Wi-Fi Hotspot Offloading Functions
description: Wi-Fi Hotspot Offloading Functions
ms.assetid: 114e1604-0d9a-418c-aee1-a9b615d13d21
ms.date: 07/31/2017
ms.localizationpriority: medium
---

# Wi-Fi Hotspot Offloading Functions

[!include[Wi-Fi Hotspot Offloading deprecation](wi-fi-hotspot-offloading-deprecation.md)]


This section describes the Wi-Fi Hotspot Offloading framework functions. These functions facilitate the interaction between the hotspot plug-in and hotspot plug-in host.

The following functions are exported by the plug-in DLL.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="hsplugingetversion.md" data-raw-source="[HSPluginGetVersion](hsplugingetversion.md)">HSPluginGetVersion</a></p></td>
<td><p>This function verifies that the plug-in and the host versions match.</p></td>
</tr>
<tr class="even">
<td><p><a href="hsplugininitplugin.md" data-raw-source="[HSPluginInitPlugin](hsplugininitplugin.md)">HSPluginInitPlugin</a></p></td>
<td><p>This function is called by the host to initialize the plug-in.</p></td>
</tr>
</tbody>
</table>

 

The hotspot plug-in exposes the following functions through the [HOTSPOT\_PLUGIN\_APIS](hotspot-plugin-apis.md) structure. This structure is passed to the hotspot plug-in host during initialization.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><a href="hs-plugin-check-for-updates.md" data-raw-source="[HS_PLUGIN_CHECK_FOR_UPDATES](hs-plugin-check-for-updates.md)">HS_PLUGIN_CHECK_FOR_UPDATES</a></p></td>
<td><p>This function checks for configuration updates.</p></td>
</tr>
<tr class="even">
<td><p><a href="hs-plugin-deinit.md" data-raw-source="[HS_PLUGIN_DEINIT](hs-plugin-deinit.md)">HS_PLUGIN_DEINIT</a></p></td>
<td><p>This function is called to notify the plug-in that it will be unloaded.</p></td>
</tr>
<tr class="odd">
<td><p><a href="hs-plugin-disconnect-from-network.md" data-raw-source="[HS_PLUGIN_DISCONNECT_FROM_NETWORK](hs-plugin-disconnect-from-network.md)">HS_PLUGIN_DISCONNECT_FROM_NETWORK</a></p></td>
<td><p>This function is called to notify the plug-in when a device will be disconnected from the network.</p></td>
</tr>
<tr class="even">
<td><p><a href="hs-plugin-is-hotspot-network.md" data-raw-source="[HS_PLUGIN_IS_HOTSPOT_NETWORK](hs-plugin-is-hotspot-network.md)">HS_PLUGIN_IS_HOTSPOT_NETWORK</a></p></td>
<td><p>This function is called by the host to determine if a specified network is a hotspot network.</p></td>
</tr>
<tr class="odd">
<td><p><a href="hs-plugin-pre-connect-init.md" data-raw-source="[HS_PLUGIN_PRE_CONNECT_INIT](hs-plugin-pre-connect-init.md)">HS_PLUGIN_PRE_CONNECT_INIT</a></p></td>
<td><p>This function is called to notify the plug-in to initialize its state when a connection to a hotspot network is in progress.</p></td>
</tr>
<tr class="even">
<td><p><a href="hs-plugin-query-cellular-exception-hosts.md" data-raw-source="[HS_PLUGIN_QUERY_CELLULAR_EXCEPTION_HOSTS](hs-plugin-query-cellular-exception-hosts.md)">HS_PLUGIN_QUERY_CELLULAR_EXCEPTION_HOSTS</a></p></td>
<td><p>This function is called to retrieve the list of hosts that the plug-in will be required to connect to over cellular as part of its authentication process.</p></td>
</tr>
<tr class="odd">
<td><p><a href="hs-plugin-query-hidden-network.md" data-raw-source="[HS_PLUGIN_QUERY_HIDDEN_NETWORK](hs-plugin-query-hidden-network.md)">HS_PLUGIN_QUERY_HIDDEN_NETWORK</a></p></td>
<td><p>This function returns the network identity and network profile for a hidden network</p></td>
</tr>
<tr class="even">
<td><p><a href="hs-plugin-reset.md" data-raw-source="[HS_PLUGIN_RESET](hs-plugin-reset.md)">HS_PLUGIN_RESET</a></p></td>
<td><p>This function is called to reset the plug-in.</p></td>
</tr>
<tr class="odd">
<td><p><a href="hs-plugin-send-keep-alive.md" data-raw-source="[HS_PLUGIN_SEND_KEEP_ALIVE](hs-plugin-send-keep-alive.md)">HS_PLUGIN_SEND_KEEP_ALIVE</a></p></td>
<td><p>This function sends a network connection keep-alive message.</p></td>
</tr>
<tr class="even">
<td><p><a href="hs-plugin-start-post-connect-auth.md" data-raw-source="[HS_PLUGIN_START_POST_CONNECT_AUTH](hs-plugin-start-post-connect-auth.md)">HS_PLUGIN_START_POST_CONNECT_AUTH</a></p></td>
<td><p>This function is called to perform any post-connect authentication required to authenticate the device over the network.</p></td>
</tr>
<tr class="odd">
<td><p><a href="hs-plugin-stop-post-connect-auth.md" data-raw-source="[HS_PLUGIN_STOP_POST_CONNECT_AUTH](hs-plugin-stop-post-connect-auth.md)">HS_PLUGIN_STOP_POST_CONNECT_AUTH</a></p></td>
<td><p>This function is called to stop the authentication process.</p></td>
</tr>
</tbody>
</table>

 

The hotspot plug-in host exposes the following functions through the [HOTSPOT\_HOST\_HANDLERS](hotspot-host-handlers.md) structure. This structure is passed to the hotspot plug-in during initialization.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="hs-host-allocate-memory.md" data-raw-source="[HS_HOST_ALLOCATE_MEMORY](hs-host-allocate-memory.md)">HS_HOST_ALLOCATE_MEMORY</a></p></td>
<td><p>This function returns an amount of memory specified by the caller.</p></td>
</tr>
<tr class="even">
<td><p><a href="hs-host-free-memory.md" data-raw-source="[HS_HOST_FREE_MEMORY](hs-host-free-memory.md)">HS_HOST_FREE_MEMORY</a></p></td>
<td><p>This function frees any memory that was allocated by the caller.</p></td>
</tr>
<tr class="odd">
<td><p><a href="hs-host-post-connect-auth-completion.md" data-raw-source="[HS_HOST_POST_CONNECT_AUTH_COMPLETION](hs-host-post-connect-auth-completion.md)">HS_HOST_POST_CONNECT_AUTH_COMPLETION</a></p></td>
<td><p>This function indicates the success or failure of an authentication attempt.</p></td>
</tr>
<tr class="even">
<td><p><a href="hs-host-send-keep-alive-completion.md" data-raw-source="[HS_HOST_SEND_KEEP_ALIVE_COMPLETION](hs-host-send-keep-alive-completion.md)">HS_HOST_SEND_KEEP_ALIVE_COMPLETION</a></p></td>
<td><p>This function indicates the success or failure of a &quot;Send keep-alive&quot; request.</p></td>
</tr>
<tr class="odd">
<td><p><a href="hs-host-update-configuration-completion.md" data-raw-source="[HS_HOST_UPDATE_CONFIGURATION_COMPLETION](hs-host-update-configuration-completion.md)">HS_HOST_UPDATE_CONFIGURATION_COMPLETION</a></p></td>
<td><p>This function indicates the success or failure of a &quot;Check for updates&quot; request.</p></td>
</tr>
</tbody>
</table>

 

## Related topics
[Wi-Fi Hotspot Offloading Reference](wi-fi-hotspot-offloading-reference.md)  



