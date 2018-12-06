---
title: D3DKMT\_OUTPUTDUPL\_FRAMEINFO structure
description: Reserved for system use. Do not use in your driver.
ms.assetid: e35389b2-52aa-4481-a5d7-6c45c795885f
keywords: ["D3DKMT_OUTPUTDUPL_FRAMEINFO structure Display Devices"]
topic_type:
- apiref
api_name:
- D3DKMT_OUTPUTDUPL_FRAMEINFO
api_location:
- D3dkmthk.h
api_type:
- HeaderDef
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# D3DKMT\_OUTPUTDUPL\_FRAMEINFO structure


Reserved for system use. Do not use in your driver.

Syntax
------

```ManagedCPlusPlus
typedef struct _D3DKMT_OUTPUTDUPL_FRAMEINFO {
  LARGE_INTEGER                      LastPresentTime;
  LARGE_INTEGER                      LastMouseUpdateTime;
  UINT                               AccumulatedFrames;
  BOOL                               RectsCoalesced;
  BOOL                               ProtectedContentMaskedOut;
  D3DKMT_OUTPUTDUPL_POINTER_POSITION PointerPosition;
  UINT                               TotalMetadataBufferSize;
  UINT                               PointerShapeBufferSize;
} D3DKMT_OUTPUTDUPL_FRAMEINFO;
```

Members
-------

**LastPresentTime**

**LastMouseUpdateTime**

**AccumulatedFrames**

**RectsCoalesced**

**ProtectedContentMaskedOut**

**PointerPosition**

**TotalMetadataBufferSize**

**PointerShapeBufferSize**

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

 

 





