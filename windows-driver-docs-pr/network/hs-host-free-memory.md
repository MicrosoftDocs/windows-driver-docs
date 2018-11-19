---
title: HS_HOST_FREE_MEMORY function
description: The HS_HOST_FREE_MEMORY function frees any memory that was allocated earlier by a call to HS_HOST_ALLOCATE_MEMORY.
ms.assetid: 2090ecf8-e1d5-4410-acbf-1b97f418e185
keywords: 
- typedef VOID (WINAPI HS_HOST_FREE_MEMORY) function Network Drivers Starting with Windows Vista
ms.date: 07/31/2017
ms.localizationpriority: medium
---

# HS\_HOST\_FREE\_MEMORY function

[!include[Wi-Fi Hotspot Offloading deprecation](wi-fi-hotspot-offloading-deprecation.md)]


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

 

 




