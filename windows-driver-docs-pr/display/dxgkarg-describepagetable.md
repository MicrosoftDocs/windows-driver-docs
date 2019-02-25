---
title: \_DXGKARG\_DESCRIBEPAGETABLE structure
description: The DXGKARG\_DESCRIBEPAGETABLE structure is reserved for system use. Do not use it in your driver.
ms.assetid: f439ba7c-216e-4286-9a63-d8f596996ac2
keywords: ["_DXGKARG_DESCRIBEPAGETABLE structure Display Devices", "DXGKARG_DESCRIBEPAGETABLE structure Display Devices"]
topic_type:
- apiref
api_name:
- DXGKARG_DESCRIBEPAGETABLE
api_location:
- d3dkmddi.h
api_type:
- HeaderDef
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# \_DXGKARG\_DESCRIBEPAGETABLE structure


The DXGKARG\_DESCRIBEPAGETABLE structure is reserved for system use. Do not use it in your driver.

Syntax
------

```ManagedCPlusPlus
typedef struct _DXGKARG_DESCRIBEPAGETABLE {
  D3DGPU_VIRTUAL_ADDRESS CoverageStart;
  UINT                   CoverageSizeInBytes;
  UINT                   SizeInBytes;
  UINT                   SubtableOffset1;
  UINT                   SubtableOffset2;
} DXGKARG_DESCRIBEPAGETABLE;
```

Members
-------

**CoverageStart**
Reserved for system use.

**CoverageSizeInBytes**
Reserved for system use.

**SizeInBytes**
Reserved for system use.

**SubtableOffset1**
Reserved for system use.

**SubtableOffset2**
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

 

 





