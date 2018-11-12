---
title: CPixel ComputeMipMapSize method
description: The CPixel ComputeMipMapSize method determines the amount of memory required to allocate a mipmap texture.
ms.assetid: f60883df-9200-4ae7-b130-21a6892e14be
keywords: ["ComputeMipMapSize method Display Devices", "ComputeMipMapSize method Display Devices , CPixel interface", "CPixel interface Display Devices , ComputeMipMapSize method"]
topic_type:
- apiref
api_name:
- CPixel.ComputeMipMapSize
api_location:
- pixel.hpp
api_type:
- COM
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# CPixel::ComputeMipMapSize method


The **CPixel::ComputeMipMapSize** method determines the amount of memory required to allocate a mipmap texture.

Syntax
------

```ManagedCPlusPlus
static UINT  ComputeMipMapSize(
   UINT      cpWidth,
   UINT      cpHeight,
   UINT      cLevels,
   D3DFORMAT Format
);
```

Parameters
----------

*cpWidth*
Specifies the width in pixels of the mipmap texture.

*cpHeight*
Specifies the height in pixels of the mipmap texture.

*cLevels*
Specifies the number of levels of the mipmap texture.

*Format*
Uses a value from the D3DFORMAT enumeration to specify the surface format.

Return value
------------

Returns the size, in bytes, of the mipmap texture.

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

 

 





