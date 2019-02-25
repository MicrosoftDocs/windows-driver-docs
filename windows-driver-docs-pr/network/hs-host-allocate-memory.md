---
title: HS_HOST_ALLOCATE_MEMORY function
description: The HS_HOST_ALLOCATE_MEMORY function returns an amount of memory specified by the caller.
ms.assetid: afa59680-d85b-4be5-8642-152ff653a0b0
keywords: 
- (WINAPI HS_HOST_ALLOCATE_MEMORY) function Network Drivers Starting with Windows Vista
ms.date: 07/31/2017
ms.localizationpriority: medium
---

# HS\_HOST\_ALLOCATE\_MEMORY function

[!include[Wi-Fi Hotspot Offloading deprecation](wi-fi-hotspot-offloading-deprecation.md)]


The **HS\_HOST\_ALLOCATE\_MEMORY** function returns an amount of memory specified by the caller.

Syntax
------

```ManagedCPlusPlus
 (WINAPI *HS_HOST_ALLOCATE_MEMORY)(
  _In_  HANDLE                        hPluginContext,
  _In_  DWORD                         dwByteCount,
  _Out_ _bcount (dwByteCount) LPVOID* ppvBuffer
);
```

Parameters
----------

*hPluginContext* \[in\]  
Context handle for the plugin making the call to this function.

*dwByteCount* \[in\]  
The amount of memory to allocate.

*ppvBuffer* \[out\]  
Pointer to the buffer that contains the allocated memory.

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

 

 




