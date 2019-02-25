---
title: CPixel ComputeMipVolumeSize method
description: The CPixel ComputeMipVolumeSize method determines the amount of memory required to allocate a mipmap texture volume.
ms.assetid: f759421a-a41e-4705-8a18-124f7efb059b
keywords: ["ComputeMipVolumeSize method Display Devices", "ComputeMipVolumeSize method Display Devices , CPixel interface", "CPixel interface Display Devices , ComputeMipVolumeSize method"]
topic_type:
- apiref
api_name:
- CPixel.ComputeMipVolumeSize
api_location:
- pixel.hpp
api_type:
- COM
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# CPixel::ComputeMipVolumeSize method


The **CPixel::ComputeMipVolumeSize** method determines the amount of memory required to allocate a mipmap texture volume.

Syntax
------

```ManagedCPlusPlus
static UINT ComputeMipVolumeSize(
   UINT      cpWidth,
   UINT      cpHeight,
   UINT      cpDepth,
   UINT      cLevels,
   D3DFORMAT Format
);
```

Parameters
----------

*cpWidth*
Specifies the width in pixels of the mipmap volume.

*cpHeight*
Specifies the height in pixels of the mipmap volume.

*cpDepth*
Specifies the depth in pixels of the mipmap volume.

*cLevels*
Specifies the number of levels of the mipmap volume texture.

*Format*
Uses a value from the D3DFORMAT enumeration to specify the surface format.

Return value
------------

Returns the size, in bytes, of the mipmap volume.

Remarks
-------

For more information about D3DFORMAT, see the Microsoft DirectX SDK documentation.

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

 

 





