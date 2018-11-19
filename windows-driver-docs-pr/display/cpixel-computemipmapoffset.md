---
title: CPixel ComputeMipMapOffset method
description: The CPixel ComputeMipMapOffset method determines the sublevel offset of a mipmap texture.
ms.assetid: f7181577-c94f-436c-8b3e-2befe89185d3
keywords: ["ComputeMipMapOffset method Display Devices", "ComputeMipMapOffset method Display Devices , CPixel interface", "CPixel interface Display Devices , ComputeMipMapOffset method"]
topic_type:
- apiref
api_name:
- CPixel.ComputeMipMapOffset
api_location:
- pixel.hpp
api_type:
- COM
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# CPixel::ComputeMipMapOffset method


The **CPixel::ComputeMipMapOffset** method determines the sublevel offset of a mipmap texture.

Syntax
------

```cpp
static void  ComputeMipMapOffset(
   const D3DSURFACE_DESC *pDescTopLevel,
         UINT            iLevel,
         BYTE            *pBits,
   const RECT            *pRect,
         D3DLOCKED_RECT  *pLockedRectData
);
```

Parameters
----------

*pDescTopLevel*
Pointer to a D3DSURFACE\_DESC structure that describes the top level of the mipmap texture.

*iLevel*
Specifies the level of the mipmap texture where the offset is determined.

*pBits*
Pointer to the beginning of the top level of the mipmap texture or **NULL** if the caller only requires the offset.

*pRect*
Pointer to a RECT structure that describes the subrectangular region or **NULL** if the caller only requires the beginning of the sublevel.

*pLockedRectData*
Pointer to a D3DLOCKED\_RECT structure that receives the pointer or offset to the locked rectangular region.

Return value
------------

None

Remarks
-------

Given the surface description, the level of the mipmap texture, a pointer to the top level, and the subrectangle, **CPixel::ComputeMipMapOffset** returns a pointer or offset to the locked rectangular region in the **pBits** member of the D3DLOCKED\_RECT structure at **pLockedRectData**.

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

 

 





