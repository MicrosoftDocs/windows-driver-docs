---
title: Conditionally Required Display Driver Functions
description: Conditionally Required Display Driver Functions
ms.assetid: c2de7e48-2ce6-466f-947e-bdac1d4fe422
keywords: ["graphics DDI functions WDK Windows 2000 display"]
---

# Conditionally Required Display Driver Functions


## <span id="ddk_conditionally_required_display_driver_functions_gg"></span><span id="DDK_CONDITIONALLY_REQUIRED_DISPLAY_DRIVER_FUNCTIONS_GG"></span>


Depending on how a driver is implemented and on the features of the underlying adapter, other graphics DDI functions may be required. For example, if a driver manages its own surface (using [**EngCreateDeviceSurface**](https://msdn.microsoft.com/library/windows/hardware/ff564206) to get a handle to the surface), that driver must also, at a minimum, support the following [drawing functions](optional-display-driver-functions.md#ddk-drawing-functions-gg):

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
<td align="left"><p>[<strong>DrvCopyBits</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556182)</p></td>
<td align="left"><p>Translates between device-managed raster surfaces and GDI standard-format bitmaps.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DrvStrokePath</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556316)</p></td>
<td align="left"><p>Draws a path (curve or line) when called by GDI.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DrvTextOut</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557277)</p></td>
<td align="left"><p>Renders a set of glyphs at specified positions.</p></td>
</tr>
</tbody>
</table>

 

**Note**   Driver calls are serialized for any given surface.

 

Drivers that write to standard-format [*DIBs*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-independent-bitmap--dib-) usually allow GDI to manage most or all of these operations. Displays that support *settable palettes* must support the [**DrvSetPalette**](https://msdn.microsoft.com/library/windows/hardware/ff556282) function.

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
<td align="left"><p>[<strong>DrvSetPalette</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556282)</p></td>
<td align="left"><p>Requests that the driver realize the palette for a specified device. The driver sets the hardware palette to match the entries in the given palette as closely as possible.</p></td>
</tr>
</tbody>
</table>

 

A list of conditionally required functions for all graphics drivers appears in [Conditionally Required Graphics Driver Functions](conditionally-required-graphics-driver-functions.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Conditionally%20Required%20Display%20Driver%20Functions%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




