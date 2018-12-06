---
title: CPixel ComputeSurfaceOffset method
description: The CPixel ComputeSurfaceOffset method determines the subrectangular offset of a surface.
ms.assetid: 3589ea80-94f8-418b-895d-c52310536e45
keywords: ["ComputeSurfaceOffset method Display Devices", "ComputeSurfaceOffset method Display Devices , CPixel interface", "CPixel interface Display Devices , ComputeSurfaceOffset method"]
topic_type:
- apiref
api_name:
- CPixel.ComputeSurfaceOffset
api_location:
- pixel.hpp
api_type:
- COM
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# CPixel::ComputeSurfaceOffset method


The **CPixel::ComputeSurfaceOffset** method determines the subrectangular offset of a surface.

Syntax
------

```ManagedCPlusPlus
static void ComputeSurfaceOffset(
   const D3DSURFACE_DESC *pDescTopLevel,
         BYTE            *pBits,
   const RECT            *pRect,
         D3DLOCKED_RECT  *pLockedRectData
);
```

Parameters
----------

*pDescTopLevel*
Pointer to a D3DSURFACE\_DESC structure that describes the surface.

*pBits*
Pointer to the beginning of the surface or **NULL** if the caller only requires the offset.

*pRect*
Pointer to a RECT structure that describes the subrectangular region or **NULL** if the caller only requires the beginning of the surface.

*pLockedRectData*
Pointer to a D3DLOCKED\_RECT structure that receives the pointer or offset to the locked rectangular region.

Return value
------------

None

Remarks
-------

Given the surface description, a pointer to the beginning of the surface, and the subrectangle, **CPixel::ComputeSurfaceOffset** returns a pointer or offset to the locked rectangular region in the **pBits** member of the D3DLOCKED\_RECT structure at **pLockedRectData**.

For more information about D3DLOCKED\_RECT, D3DSURFACE\_DESC, and RECT, see the Microsoft DirectX SDK documentation.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Target platform</p></td>
<td align="left">Desktop</td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Pixel.hpp (include Pixel.hpp)</td>
</tr>
</tbody>
</table>

 

 





