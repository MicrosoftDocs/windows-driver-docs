---
title: HS\_PLUGIN\_QUERY\_CELLULAR\_EXCEPTION\_HOSTS function
author: windows-driver-content
description: The HS\_PLUGIN\_QUERY\_CELLULAR\_EXCEPTION\_HOSTS function queries the list of hosts that the plugin will need to connect to over cellular as part of its authentication process.
ms.assetid: 7f38f146-a637-4ec3-8610-ea4934c4a57a
keywords: 
- typedef DWORD (WINAPI HS_PLUGIN_QUERY_CELLULAR_EXCEPTION_HOSTS) function Network Drivers Starting with Windows Vista
ms.author: windowsdriverdev
ms.date: 07/31/2017 
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# HS\_PLUGIN\_QUERY\_CELLULAR\_EXCEPTION\_HOSTS function


The **HS\_PLUGIN\_QUERY\_CELLULAR\_EXCEPTION\_HOSTS** function queries the list of hosts that the plugin will need to connect to over cellular as part of its authentication process.

Syntax
------

```ManagedCPlusPlus
 typedef DWORD (WINAPI *HS_PLUGIN_QUERY_CELLULAR_EXCEPTION_HOSTS)(
  _Inout_ HS_PLUGIN_CELLULAR_EXCEPTION_HOSTS *pExceptionsList
);
```

Parameters
----------

*\*pExceptionsList* \[in, out\]  
The [**HS\_PLUGIN\_CELLULAR\_EXCEPTION\_HOSTS**](hs-plugin-cellular-exception-hosts.md) structure that contains the list of cellular host names.

Return value
------------

This function is called by the host to communicate with the plugin and does not return a value.

Remarks
-------

This function is called only if the plugin sets the **dwNumCellularExceptions** field of its [**HS\_PLUGIN\_PROFILE**](hs-plugin-profile.md) to a value greater than zero.

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


[**HS\_PLUGIN\_CELLULAR\_EXCEPTION\_HOSTS**](hs-plugin-cellular-exception-hosts.md)

[**HS\_PLUGIN\_PROFILE**](hs-plugin-profile.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20HS_PLUGIN_QUERY_CELLULAR_EXCEPTION_HOSTS%20function%20%20RELEASE:%20%287/31/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


