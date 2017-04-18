---
title: GDI Support for Palettes
description: GDI Support for Palettes
ms.assetid: 8c6ebf1e-6c83-45d9-bf83-f0684d28fc32
keywords: ["DrvEnablePDEV", "GDI WDK Windows 2000 display , colors", "graphics drivers WDK Windows 2000 display , colors", "color management WDK GDI", "palettes WDK Windows 2000 display", "drawing WDK GDI , colors", "DrvSetPalette", "color index WDK GDI"]
---

# GDI Support for Palettes


## <span id="ddk_gdi_support_for_palettes_gg"></span><span id="DDK_GDI_SUPPORT_FOR_PALETTES_GG"></span>


GDI can do most of the work with regard to palette management. When GDI calls the [**DrvEnablePDEV**](https://msdn.microsoft.com/library/windows/hardware/ff556211) function, the driver returns its default palette to GDI as part of the [**DEVINFO**](https://msdn.microsoft.com/library/windows/hardware/ff552835) structure. The driver must create this palette using the [**EngCreatePalette**](https://msdn.microsoft.com/library/windows/hardware/ff564212) function.

A palette effectively maps 32-bit *color indexes* into 24-bit RGB color values, which is the way GDI uses palettes. A driver specifies its palette so GDI can determine how different color indexes are to appear on the device.

The driver need not deal with most palette operations and calculations as long as it uses the [**XLATEOBJ**](https://msdn.microsoft.com/library/windows/hardware/ff570634) provided by GDI.

If the device supports a modifiable palette, it should implement the function [**DrvSetPalette**](https://msdn.microsoft.com/library/windows/hardware/ff556282). GDI calls *DrvSetPalette* when an application changes the palette for a device and passes the resulting new palette to the driver. The driver should set its internal hardware palette to match the new palette as closely as possible.

A palette can be defined for GDI in either of the two different formats listed in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Palette Format</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Indexed</p></td>
<td align="left"><p>A color index is an index into an array of RGB values. The array can be small, containing, for example, 16 color indexes, or large, containing, for example, 4096 color indexes or more.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Bit Fields</p></td>
<td align="left"><p>Bit fields in the color index specify colors in terms of the amounts of R, G, and B in each color. For example, 5 bits could be used for each, providing a value between 0 and 31 for each color. The 5-bit value would be scaled up to cover a range of 0 to 255 for each component when converting to RGB. (The usual RGB representation itself is defined by bitfields.)</p></td>
</tr>
</tbody>
</table>

 

GDI typically uses the palette mapping in reverse. That is, an application specifies an RGB color for drawing and GDI must locate the color index that causes the device to display that color. As indicated in the next table, GDI provides two primary palette service functions for creating and deleting the palette, as well as some service functions related to the [**PALOBJ**](https://msdn.microsoft.com/library/windows/hardware/ff568844) and the [**XLATEOBJ**](https://msdn.microsoft.com/library/windows/hardware/ff570634) used to translate color indexes between two palettes.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Function</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>EngCreatePalette</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564212)</p></td>
<td align="left"><p>Creates a palette. The driver associates the palette with a device by returning a handle to the palette in the [<strong>DEVINFO</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552835) structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngDeletePalette</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564808)</p></td>
<td align="left"><p>Deletes the given palette.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngDitherColor</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564842)</p></td>
<td align="left"><p>Returns a standard 8x8 dither that approximates the specified RGB color.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngQueryPalette</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564993)</p></td>
<td align="left"><p>Queries a palette for its attributes.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>PALOBJ_cGetColors</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568845)</p></td>
<td align="left"><p>Allows a driver to download RGB colors from an indexed palette. Called by the display driver in the [<strong>DrvSetPalette</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556282) function.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>XLATEOBJ_cGetPalette</strong>](https://msdn.microsoft.com/library/windows/hardware/ff570637)</p></td>
<td align="left"><p>Retrieves the 24-bit RGB colors or the bitfield format for the colors in an indexed source palette. The driver can use this function to obtain information from the palette to perform color blending.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>XLATEOBJ_hGetColorTransform</strong>](https://msdn.microsoft.com/library/windows/hardware/ff570639)</p></td>
<td align="left"><p>Returns the color transform for the specified translation object.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>XLATEOBJ_iXlate</strong>](https://msdn.microsoft.com/library/windows/hardware/ff570642)</p></td>
<td align="left"><p>Translates a single source color index to a destination color index.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>XLATEOBJ_piVector</strong>](https://msdn.microsoft.com/library/windows/hardware/ff570644)</p></td>
<td align="left"><p>Retrieves a translation vector from an indexed source palette. The driver can use this vector to perform its own translation of the source indexes to destination indexes.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20GDI%20Support%20for%20Palettes%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




