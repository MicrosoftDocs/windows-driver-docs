---
title: HS_HOST_FREE_MEMORY function
author: windows-driver-content
description: The HS\_HOST\_FREE\_MEMORY function frees any memory that was allocated earlier by a call to HS\_HOST\_ALLOCATE\_MEMORY.
ms.assetid: 2090ecf8-e1d5-4410-acbf-1b97f418e185
keywords: 
- typedef VOID (WINAPI HS_HOST_FREE_MEMORY) function Network Drivers Starting with Windows Vista
ms.author: windowsdriverdev
ms.date: 07/31/2017 
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# HS\_HOST\_FREE\_MEMORY function


The **HS\_HOST\_FREE\_MEMORY** function frees any memory that was allocated earlier by a call to [**HS\_HOST\_ALLOCATE\_MEMORY**](hs-host-allocate-memory.md).

Syntax
------

```ManagedCPlusPlus
 typedef VOID (WINAPI *HS_HOST_FREE_MEMORY)(
  _In_     HANDLE hPluginContext,
  _In_opt_ LPVOID pvBuffer
);
```

Parameters
----------

*hPluginContext* \[in\]  
Context handle for the plugin making the call to this function.

*pvBuffer* \[in, optional\]  
Pointer to the memory buffer.

Return value
------------

This function is called by the plugin to communicate with the host and does not return a value.

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


[**HS\_HOST\_ALLOCATE\_MEMORY**](hs-host-allocate-memory.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20HS_HOST_FREE_MEMORY%20function%20%20RELEASE:%20%287/31/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


