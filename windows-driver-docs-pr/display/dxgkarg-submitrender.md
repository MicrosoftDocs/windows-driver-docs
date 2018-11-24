---
title: \_DXGKARG\_SUBMITRENDER structure
description: The DXGKARG\_SUBMITRENDER structure is reserved for system use. Do not use it in your driver.
ms.assetid: eecc3c47-1387-4fca-9113-12dfedc58e80
keywords: ["_DXGKARG_SUBMITRENDER structure Display Devices", "DXGKARG_SUBMITRENDER structure Display Devices"]
topic_type:
- apiref
api_name:
- DXGKARG_SUBMITRENDER
api_location:
- d3dkmddi.h
api_type:
- HeaderDef
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# \_DXGKARG\_SUBMITRENDER structure


The DXGKARG\_SUBMITRENDER structure is reserved for system use. Do not use it in your driver.

Syntax
------

```ManagedCPlusPlus
typedef struct _DXGKARG_SUBMITRENDER {
  VOID                   *pContextSaveArea;
  D3DGPU_VIRTUAL_ADDRESS DmaBuffer;
  UINT                   DmaSize;
  VOID                   *pPrivateDriverData;
  UINT                   PrivateDriverDataSize;
  VOID                   *pDmaBufferPrivateData;
  UINT                   DmaBufferPrivateDataSize;
  VOID                   *pDmaBuffer;
} DXGKARG_SUBMITRENDER;
```

Members
-------

**pContextSaveArea**
Reserved for system use.

**DmaBuffer**
Reserved for system use.

**DmaSize**
Reserved for system use.

**pPrivateDriverData**
Reserved for system use.

**PrivateDriverDataSize**
Reserved for system use.

**pDmaBufferPrivateData**
Reserved for system use.

**DmaBufferPrivateDataSize**
Reserved for system use.

**pDmaBuffer**
Reserved for system use.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Available in Windows 7 and later versions of the Windows operating systems.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">D3dkmddi.h (include D3dkmddi.h)</td>
</tr>
</tbody>
</table>

 

 





