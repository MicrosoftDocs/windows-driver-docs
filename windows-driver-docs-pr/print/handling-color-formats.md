---
title: Handling Color Formats
description: Handling Color Formats
ms.assetid: 4d0faba6-1994-474f-a5d3-e25cd2800cf7
keywords:
- Unidrv, color formats
- color formats WDK Unidrv
- ColorMode Feature
- printer color formats WDK Unidrv
- color management WDK print , formats
- Unidrv WDK print
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling Color Formats





Each color format that a printer supports is specified as an option to the ColorMode feature. By using [option attributes for the ColorMode feature](option-attributes-for-the-colormode-feature.md), you can describe each color format that your printer accepts. The following table illustrates the color data formats that Unidrv can handle.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Number of Color Planes</th>
<th>Number of Bits per Pixel</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>in Device (<em>DevNumOfPlanes)</td>
<td>in Device (</em>DevBPP)</td>
</tr>
<tr class="even">
<td><p>1</p></td>
<td><p>1 (Black and white)</p></td>
</tr>
<tr class="odd">
<td><p>1</p></td>
<td><p>8</p></td>
</tr>
<tr class="even">
<td><p>1</p></td>
<td><p>24</p></td>
</tr>
<tr class="odd">
<td><p>3</p></td>
<td><p>1 (CMY and RGB)</p></td>
</tr>
<tr class="even">
<td><p>4</p></td>
<td><p>1 (<a href="https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-cmyk" data-raw-source="[&lt;em&gt;CMYK&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-cmyk)"><em>CMYK</em></a>)</p></td>
</tr>
</tbody>
</table>

 

For these formats, Unidrv can convert [*device-independent bitmap (DIB)*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-independent-bitmap--dib-) data into the proper format and send it to the printer. (Halftoning operations that can be performed on this data are described in [Halftoning with Unidrv](halftoning-with-unidrv.md).)

If your printer supports color formats that are not listed in the preceding table, you must do the following:

-   Set the \*DevNumOfPlanes and \*DevBPP attributes to zero. Doing this prevents Unidrv from sending DIB data to the printer.

-   Provide a [rendering plug-in](rendering-plug-ins.md) that implements the [**IPrintOemUni::ImageProcessing**](https://msdn.microsoft.com/library/windows/hardware/ff554261) method.

The [**IPrintOemUni::ImageProcessing**](https://msdn.microsoft.com/library/windows/hardware/ff554261) method must perform the following operations:

-   Convert DIB data into the printer's color format.

-   Perform halftoning operations on the data.

-   Send the data to the print spooler.

For more information about providing an [**IPrintOemUni::ImageProcessing**](https://msdn.microsoft.com/library/windows/hardware/ff554261) function, see [Customized Color Formats](customized-color-formats.md).

### Rendering High Quality Images

For each color format, you specify both the bits per pixel that the printer hardware accepts and the bits per pixel you want Unidrv to use when creating DIBs. These values are specified with the \*DevBPP and \*DrvBPP attributes, respectively. Sometimes, it is desirable for images to be rendered as bitmaps having a higher number of bits per pixel than the printer can handle (in order, for example, to attempt reproducing high-quality photographs). Therefore, it is allowable to specify a \***DrvBPP** value that is larger than the result of multiplying the \***DevBPP** value by the \*DevNumOfPlanes value.

For example, suppose you want to define a ColorMode option that causes images to be rendered as 24 bits/pixel bitmaps, but then you want the bitmap to be sent to the printer as [*CMYK*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-cmyk) data. You might define this mode as follows:

```cpp
*Feature: ColorMode
{
    *Option: 24toCMYK
    {
        *Name: "Photographic Quality"
        *DrvBPP: 24
        *DevNumOfPlanes: 4
        *DevBPP: 1
        *ColorPlaneOrder: LIST(CYAN, MAGENTA, YELLOW, BLACK)
        *IPCallbackID: 1
    }
 other options
}
```

In this example, the \***DevBPP** and \***DevNumOfPlanes** attributes represent the four-plane, one-bit-per-plane CMYK format that Unidrv can render and then send to the printer. However, in this case, halftoning operations must be performed on the rendered image before it is printed. [Minidriver-supplied halftoning](minidriver-supplied-halftoning.md) must be used.

 

 




