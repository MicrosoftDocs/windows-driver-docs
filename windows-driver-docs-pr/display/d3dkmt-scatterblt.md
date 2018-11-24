---
title: D3DKMT\_SCATTERBLT structure
description: Reserved for system use. Do not use in your driver.
ms.assetid: 94463e11-8a18-4d23-b7b6-d2486dc7dc9d
keywords: ["D3DKMT_SCATTERBLT structure Display Devices"]
topic_type:
- apiref
api_name:
- D3DKMT_SCATTERBLT
api_location:
- D3dkmthk.h
api_type:
- HeaderDef
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# D3DKMT\_SCATTERBLT structure


Reserved for system use. Do not use in your driver.

Syntax
------

```ManagedCPlusPlus
typedef struct _D3DKMT_SCATTERBLT {
  ULONG64 hLogicalSurfaceDestination;
  LONG64  hDestinationCompSurfDWM;
  UINT64  DestinationCompositionBindingId;
  RECT    SourceRect;
  POINT   DestinationOffset;
} D3DKMT_SCATTERBLT;
```

Members
-------

**hLogicalSurfaceDestination**

**hDestinationCompSurfDWM**

**DestinationCompositionBindingId**

**SourceRect**

**DestinationOffset**

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

 

 





