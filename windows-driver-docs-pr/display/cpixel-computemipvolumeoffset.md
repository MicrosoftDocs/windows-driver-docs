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
ms.author: windowsdriverdev
ms.date: 01/05/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20CPixel::ComputeMipVolumeOffset%20method%20%20RELEASE:%20%281/4/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




