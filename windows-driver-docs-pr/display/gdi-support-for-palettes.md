---
title: GDI Support for Palettes
description: GDI Support for Palettes
ms.assetid: 8c6ebf1e-6c83-45d9-bf83-f0684d28fc32
keywords:
- DrvEnablePDEV
- GDI WDK Windows 2000 display , colors
- graphics drivers WDK Windows 2000 display , colors
- color management WDK GDI
- palettes WDK Windows 2000 display
- drawing WDK GDI , colors
- DrvSetPalette
- color index WDK GDI
ms.date: 04/20/2017
ms.localizationpriority: medium
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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564212" data-raw-source="[&lt;strong&gt;EngCreatePalette&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564212)"><strong>EngCreatePalette</strong></a></p></td>
<td align="left"><p>Creates a palette. The driver associates the palette with a device by returning a handle to the palette in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552835" data-raw-source="[&lt;strong&gt;DEVINFO&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552835)"><strong>DEVINFO</strong></a> structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564808" data-raw-source="[&lt;strong&gt;EngDeletePalette&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564808)"><strong>EngDeletePalette</strong></a></p></td>
<td align="left"><p>Deletes the given palette.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564842" data-raw-source="[&lt;strong&gt;EngDitherColor&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564842)"><strong>EngDitherColor</strong></a></p></td>
<td align="left"><p>Returns a standard 8x8 dither that approximates the specified RGB color.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564993" data-raw-source="[&lt;strong&gt;EngQueryPalette&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564993)"><strong>EngQueryPalette</strong></a></p></td>
<td align="left"><p>Queries a palette for its attributes.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff568845" data-raw-source="[&lt;strong&gt;PALOBJ_cGetColors&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff568845)"><strong>PALOBJ_cGetColors</strong></a></p></td>
<td align="left"><p>Allows a driver to download RGB colors from an indexed palette. Called by the display driver in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556282" data-raw-source="[&lt;strong&gt;DrvSetPalette&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556282)"><strong>DrvSetPalette</strong></a> function.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff570637" data-raw-source="[&lt;strong&gt;XLATEOBJ_cGetPalette&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff570637)"><strong>XLATEOBJ_cGetPalette</strong></a></p></td>
<td align="left"><p>Retrieves the 24-bit RGB colors or the bitfield format for the colors in an indexed source palette. The driver can use this function to obtain information from the palette to perform color blending.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff570639" data-raw-source="[&lt;strong&gt;XLATEOBJ_hGetColorTransform&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff570639)"><strong>XLATEOBJ_hGetColorTransform</strong></a></p></td>
<td align="left"><p>Returns the color transform for the specified translation object.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff570642" data-raw-source="[&lt;strong&gt;XLATEOBJ_iXlate&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff570642)"><strong>XLATEOBJ_iXlate</strong></a></p></td>
<td align="left"><p>Translates a single source color index to a destination color index.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff570644" data-raw-source="[&lt;strong&gt;XLATEOBJ_piVector&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff570644)"><strong>XLATEOBJ_piVector</strong></a></p></td>
<td align="left"><p>Retrieves a translation vector from an indexed source palette. The driver can use this vector to perform its own translation of the source indexes to destination indexes.</p></td>
</tr>
</tbody>
</table>

 

 

 





