---
title: CPixel ComputeMipVolumeOffset method
description: The CPixel ComputeMipVolumeOffset method determines the subvolume offset of a mipmap volume texture.
ms.assetid: 4fb2f49a-2c1a-4b07-bbd3-76c4e345b243
keywords: ["ComputeMipVolumeOffset method Display Devices", "ComputeMipVolumeOffset method Display Devices , CPixel interface", "CPixel interface Display Devices , ComputeMipVolumeOffset method"]
topic_type:
- apiref
api_name:
- CPixel.ComputeMipVolumeOffset
api_location:
- pixel.hpp
api_type:
- COM
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# CPixel::ComputeMipVolumeOffset method


The **CPixel::ComputeMipVolumeOffset** method determines the subvolume offset of a mipmap volume texture.

Syntax
------

```ManagedCPlusPlus
static void  ComputeMipVolumeOffset(
   const D3DVOLUME_DESC *pDescTopLevel,
         UINT           iLevel,
         BYTE           *pBits,
   const D3DBOX         *pBox,
   const D3DLOCKED_BOX  *pLockedBoxData
);
```

Parameters
----------

*pDescTopLevel*
Pointer to a D3DVOLUME\_DESC structure that describes the top level of the mipmap texture volume.

*iLevel*
Specifies the level of the mipmap volume where the offset is determined.

*pBits*
Pointer to the beginning of the top level of the mipmap volume texture or **NULL** if the caller only requires the offset.

*pBox*
Pointer to a D3DBOX structure that describes the subvolume or **NULL** if the caller only requires the beginning of the sublevel.

*pLockedBoxData*
Pointer to a D3DLOCKED\_BOX structure that receives the pointer or offset to the locked volume region.

Return value
------------

None

Remarks
-------

Given the surface description, the level of the mipmap volume, a pointer to the top level, and the subvolume, **CPixel::ComputeMipVolumeOffset** returns a pointer or offset to the locked box region in the **pBits** member of the D3DLOCKED\_BOX structure at **pLockedBoxData**.

For more information about D3DLOCKED\_BOX, D3DVOLUME\_DESC, and D3DBOX, see the Microsoft DirectX SDK documentation.

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

 

 





