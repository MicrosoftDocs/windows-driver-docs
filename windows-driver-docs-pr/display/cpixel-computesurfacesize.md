---
title: CPixel::ComputeSurfaceSize Method
description: The CPixel::ComputeSurfaceSize method determines the amount of memory required to allocate a surface.
keywords: ["ComputeSurfaceSize method Display Devices", "ComputeSurfaceSize method Display Devices , CPixel interface", "CPixel interface Display Devices , ComputeSurfaceSize method"]
topic_type:
- apiref
ms.topic: reference
api_name:
- CPixel.ComputeSurfaceSize
api_location:
- pixel.hpp
api_type:
- COM
ms.date: 01/05/2018
---

# CPixel::ComputeSurfaceSize method


The **CPixel::ComputeSurfaceSize** method determines the amount of memory required to allocate a surface.

## Syntax

```ManagedCPlusPlus
static UINT ComputeSurfaceSize(
   UINT      cpWidth,
   UINT      cpHeight,
   D3DFORMAT Format
);
```

## Parameters

*cpWidth*
Specifies the width in pixels of the surface.

*cpHeight*
Specifies the height in pixels of the surface.

*Format*
Uses a value from the D3DFORMAT enumeration to specify the surface format.

## Return value

Returns the size, in bytes, of the surface.

## Remarks

For more information about D3DFORMAT, see the Microsoft DirectX SDK documentation.

## Requirements

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

 

 





