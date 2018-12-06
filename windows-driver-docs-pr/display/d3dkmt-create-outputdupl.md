---
title: D3DKMT\_CREATE\_OUTPUTDUPL structure
description: Reserved for system use. Do not use in your driver.
ms.assetid: 3fdbf129-331d-4dd5-a417-79c88b7e7947
keywords: ["D3DKMT_CREATE_OUTPUTDUPL structure Display Devices"]
topic_type:
- apiref
api_name:
- D3DKMT_CREATE_OUTPUTDUPL
api_location:
- D3dkmthk.h
api_type:
- HeaderDef
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# D3DKMT\_CREATE\_OUTPUTDUPL structure


Reserved for system use. Do not use in your driver.

Syntax
------

```ManagedCPlusPlus
typedef struct _D3DKMT_CREATE_OUTPUTDUPL {
  D3DKMT_HANDLE                  hAdapter;
  D3DDDI_VIDEO_PRESENT_SOURCE_ID VidPnSourceId;
  D3DKMT_HANDLE                  hSharedSurfaceGlobal;
  D3DKMT_HANDLE                  hGPUFencefaceGlobal;
  D3DKMT_HANDLE                  hKeyedMutexGlobal;
} D3DKMT_CREATE_OUTPUTDUPL;
```

Members
-------

**hAdapter**

**VidPnSourceId**

**hSharedSurfaceGlobal**

**hGPUFencefaceGlobal**

**hKeyedMutexGlobal**

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Minimum supported client</p></td>
<td align="left"><p>Windows 8</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum supported server</p></td>
<td align="left"><p>Windows Server 2012</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">D3dkmthk.h (include D3dkmthk.h)</td>
</tr>
</tbody>
</table>

 

 





