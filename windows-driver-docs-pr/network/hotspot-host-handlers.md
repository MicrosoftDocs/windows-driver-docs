---
title: HOTSPOT_HOST_HANDLERS structure
author: windows-driver-content
description: The HOTSPOT_HOST_HANDLERS structure contains the hotspot host handlers function table.
ms.assetid: b381e471-7713-401a-b3fa-eae1801b0e81
keywords: 
- HOTSPOT_HOST_HANDLERS structure Network Drivers Starting with Windows Vista
- PHOTSPOT_HOST_HANDLERS structure pointer Network Drivers Starting with Windows Vista
ms.author: windowsdriverdev
ms.date: 07/31/2017 
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# HOTSPOT\_HOST\_HANDLERS structure

[!include[Wi-Fi Hotspot Offloading deprecation](wi-fi-hotspot-offloading-deprecation.md)]


The **HOTSPOT\_HOST\_HANDLERS** structure contains the hotspot host handlers function table. This function table is passed to the plugin when [**HSPluginInitPlugin**](hsplugininitplugin.md) is called to initialize it. The table contains functions that are called by the plugin to communicate with the hotspot host.

Syntax
------

```ManagedCPlusPlus
typedef struct _HOTSPOT_HOST_HANDLERS {
  HS_HOST_ALLOCATE_MEMORY                          HSHostAllocateMemory;
  HS_HOST_FREE_MEMORY                              HSHostFreeMemory;
  HS_HOST_POST_CONNECT_AUTH_COMPLETION             HSHostPostConnectAuthCompletion;
  HS_HOST_SEND_KEEP_ALIVE_COMPLETION               HSHostSendKeepAliveCompletion;
  HS_HOST_UPDATE_CONFIGURATION_COMPLETION          HSHostUpdateConfigurationCompletion;
  HS_HOST_SEND_USER_MESSAGE                        HSHostSendUserMessage;
} HOTSPOT_HOST_HANDLERS, *PHOTSPOT_HOST_HANDLERS;
```

Members
-------

**HSHostAllocateMemory**  
Optional memory management handler.

Handle to the function that is called by the plugin to allocate any memory needed by the plugin. For more information, see [**HS\_HOST\_ALLOCATE\_MEMORY**](hs-host-allocate-memory.md).

**HSHostFreeMemory**  
Optional memory management handler.

Handle to the function that is called by the plugin to free any memory that had been allocated earlier by the call to [**HS\_HOST\_ALLOCATE\_MEMORY**](hs-host-allocate-memory.md). For more information, see [**HS\_HOST\_FREE\_MEMORY**](hs-host-free-memory.md).

**HSHostPostConnectAuthCompletion**  
Required connection-process handler.

Handle to the function that is called by the plugin to indicate the success or failure status resulting from the authentication attempt following a Wi-Fi connection setup at layer 2. For more information, see [**HS\_PLUGIN\_START\_POST\_CONNECT\_AUTH**](hs-plugin-start-post-connect-auth.md).

**HSHostSendKeepAliveCompletion**  
Optional periodic request.

Handle to the function that is called by the plugin to indicate the success or failure status resulting from the Send Keep Alive request. For more information, see [**HS\_PLUGIN\_SEND\_KEEP\_ALIVE**](hs-plugin-send-keep-alive.md).

**HSHostUpdateConfigurationCompletion**  
Optional periodic request.

Handle to the function that is called by the plugin to indicate the success or failure of a call to check for updates. For more information, see [**HS\_PLUGIN\_CHECK\_FOR\_UPDATES**](hs-plugin-check-for-updates.md).

**HSHostSendUserMessage**  
Optional periodic request.

Handle to the function that is called to communicate with the user. For more information see [**HS\_HOST\_SEND\_USER\_MESSAGE**](hs-host-send-user-message.md).

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

[**HS\_HOST\_ALLOCATE\_MEMORY**](hs-host-allocate-memory.md)

[**HS\_HOST\_FREE\_MEMORY**](hs-host-free-memory.md)

[**HS\_PLUGIN\_START\_POST\_CONNECT\_AUTH**](hs-plugin-start-post-connect-auth.md)

[**HS\_PLUGIN\_SEND\_KEEP\_ALIVE**](hs-plugin-send-keep-alive.md)

[**HS\_PLUGIN\_CHECK\_FOR\_UPDATES**](hs-plugin-check-for-updates.md)

[**HS\_HOST\_SEND\_USER\_MESSAGE**](hs-host-send-user-message.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20HOTSPOT_HOST_HANDLERS%20structure%20%20RELEASE:%20%287/31/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


