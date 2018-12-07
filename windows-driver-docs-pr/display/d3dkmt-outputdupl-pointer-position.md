---
title: D3DKMT\_OUTPUTDUPL\_POINTER\_POSITION structure
description: Reserved for system use. Do not use in your driver.
ms.assetid: c05205bf-3f7c-487d-8cce-d708d50eb4d9
keywords: ["D3DKMT_OUTPUTDUPL_POINTER_POSITION structure Display Devices"]
topic_type:
- apiref
api_name:
- D3DKMT_OUTPUTDUPL_POINTER_POSITION
api_location:
- D3dkmthk.h
api_type:
- HeaderDef
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# D3DKMT\_OUTPUTDUPL\_POINTER\_POSITION structure


Reserved for system use. Do not use in your driver.

Syntax
------

```ManagedCPlusPlus
typedef struct _D3DKMT_OUTPUTDUPL_POINTER_POSITION {
  POINT Position;
  BOOL  Visible;
} D3DKMT_OUTPUTDUPL_POINTER_POSITION;
```

Members
-------

**Position**

**Visible**

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

 

 





