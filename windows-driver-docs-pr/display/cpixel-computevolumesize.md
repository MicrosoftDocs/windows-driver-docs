---
title: CPixel ComputeVolumeSize method
description: The CPixel ComputeVolumeSize method determines the amount of memory required to allocate a volume.
ms.assetid: 85e00793-8c30-41a4-91b0-9f0503a6ce09
keywords: ["ComputeVolumeSize method Display Devices", "ComputeVolumeSize method Display Devices , CPixel interface", "CPixel interface Display Devices , ComputeVolumeSize method"]
topic_type:
- apiref
api_name:
- CPixel.ComputeVolumeSize
api_location:
- pixel.hpp
api_type:
- COM
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# CPixel::ComputeVolumeSize method


The **CPixel::ComputeVolumeSize** method determines the amount of memory required to allocate a volume.

Syntax
------

```ManagedCPlusPlus
static UINT ComputeVolumeSize(
   UINT      cpWidth,
   UINT      cpHeight,
   UINT      cpDepth,
   D3DFORMAT Format
);
```

Parameters
----------

*cpWidth*
Specifies the width in pixels of the volume.

*cpHeight*
Specifies the height in pixels of the volume.

*cpDepth*
Specifies the depth in pixels of the volume.

*Format*
Uses a value from the D3DFORMAT enumeration to specify the surface format.

Return value
------------

Returns the size, in bytes, of the volume.

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

 

 





