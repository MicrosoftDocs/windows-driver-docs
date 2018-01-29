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
ms.author: windowsdriverdev
ms.date: 01/05/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20CPixel::ComputeMipVolumeSize%20method%20%20RELEASE:%20%281/4/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




