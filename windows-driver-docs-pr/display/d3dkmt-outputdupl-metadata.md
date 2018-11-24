---
title: D3DKMT\_OUTPUTDUPL\_METADATA structure
description: Reserved for system use. Do not use in your driver.
ms.assetid: abf4f00a-05bb-48f6-989e-f1b453fb0708
keywords: ["D3DKMT_OUTPUTDUPL_METADATA structure Display Devices"]
topic_type:
- apiref
api_name:
- D3DKMT_OUTPUTDUPL_METADATA
api_location:
- D3dkmthk.h
api_type:
- HeaderDef
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# D3DKMT\_OUTPUTDUPL\_METADATA structure


Reserved for system use. Do not use in your driver.

Syntax
------

```ManagedCPlusPlus
typedef struct _D3DKMT_OUTPUTDUPL_METADATA {
  D3DKMT_HANDLE                  hAdapter;
  D3DDDI_VIDEO_PRESENT_SOURCE_ID VidPnSourceId;
  D3DKMT_OUTPUTDUPL_METADATATYPE Type;
  UINT                           BufferSizeSupplied;
  PVOID                          pBuffer;
  UINT                           BufferSizeRequired;
} D3DKMT_OUTPUTDUPL_METADATA;
```

Members
-------

**hAdapter**

**VidPnSourceId**

**Type**

**BufferSizeSupplied**

**pBuffer**

**BufferSizeRequired**

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

 

 





