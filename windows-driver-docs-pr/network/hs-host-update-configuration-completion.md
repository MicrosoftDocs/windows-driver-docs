---
title: HS_HOST_UPDATE_CONFIGURATION_COMPLETION function
author: windows-driver-content
description: The HS\_HOST\_UPDATE\_CONFIGURATION\_COMPLETION function indicates the success or failure of a request to check for updates.
ms.assetid: 7e9eda04-db8e-4181-90e3-8716a99429a8
keywords: 
- typedef DWORD (WINAPI HS_HOST_UPDATE_CONFIGURATION_COMPLETION) function Network Drivers Starting with Windows Vista
ms.author: windowsdriverdev
ms.date: 07/31/2017 
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# HS\_HOST\_UPDATE\_CONFIGURATION\_COMPLETION function


The **HS\_HOST\_UPDATE\_CONFIGURATION\_COMPLETION** function indicates the success or failure of a request to check for updates.

Syntax
------

```ManagedCPlusPlus
 typedef DWORD (WINAPI *HS_HOST_UPDATE_CONFIGURATION_COMPLETION)(
  _In_ HANDLE            hPluginContext,
  _In_ eHS_UPDATE_RESULT UpdateResult
);
```

Parameters
----------

*hPluginContext* \[in\]  
Context handle for the plugin making the call to this function.

*UpdateResult* \[in\]  
The [**eHS\_UPDATE\_RESULT**](ehs-update-result.md) enumeration value that indicates the result of the request to check for updates.

Return value
------------

This function is called by the plugin to communicate with the host and does not return a value.

Remarks
-------

The plugin must call this function to inform the host of the result of a previous call to [**HS\_PLUGIN\_CHECK\_FOR\_UPDATES**](hs-plugin-check-for-updates.md).

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


[**eHS\_UPDATE\_RESULT**](ehs-update-result.md)

[**HS\_PLUGIN\_CHECK\_FOR\_UPDATES**](hs-plugin-check-for-updates.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20HS_HOST_UPDATE_CONFIGURATION_COMPLETION%20function%20%20RELEASE:%20%287/31/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


