---
title: Handling color formats
description: Handling color formats
keywords:
- Unidrv, color formats
- color formats WDK Unidrv
- ColorMode Feature
- printer color formats WDK Unidrv
- color management WDK print , formats
- Unidrv WDK print
ms.date: 06/22/2023
---

# Handling color formats

[!include[Print Support Apps](../includes/print-support-apps.md)]

Each color format that a printer supports is specified as an option to the ColorMode feature. By using [option attributes for the ColorMode feature](option-attributes-for-the-colormode-feature.md), you can describe each color format that your printer accepts. The following table illustrates the color data formats that Unidrv can handle.

| Number of color planes | Number of bits per pixel |
|--|--|
| in Device (\*DevNumOfPlanes) | in Device (\*DevBPP) |
| 1 | 1 (Black and white) |
| 1 | 8 |
| 1 | 24 |
| 3 | 1 (CMY and RGB) |
| 4 | 1 (CMYK) |

For these formats, Unidrv can convert *device-independent bitmap (DIB)* data into the proper format and send it to the printer. (Halftoning operations that can be performed on this data are described in [Halftoning with Unidrv](halftoning-with-unidrv.md).)

If your printer supports color formats that are not listed in the preceding table, you must do the following:

- Set the \*DevNumOfPlanes and \*DevBPP attributes to zero. Doing this prevents Unidrv from sending DIB data to the printer.

- Provide a [rendering plug-in](rendering-plug-ins.md) that implements the [**IPrintOemUni ImageProcessing**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-imageprocessing) method.

The [**IPrintOemUni ImageProcessing**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-imageprocessing) method must perform the following operations:

- Convert DIB data into the printer's color format.

- Perform halftoning operations on the data.

- Send the data to the print spooler.

For more information about providing an [**IPrintOemUni ImageProcessing**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-imageprocessing) function, see [Customized Color Formats](customized-color-formats.md).

## Rendering High Quality Images

For each color format, you specify both the bits per pixel that the printer hardware accepts and the bits per pixel you want Unidrv to use when creating DIBs. These values are specified with the \*DevBPP and \*DrvBPP attributes, respectively. Sometimes, it is desirable for images to be rendered as bitmaps having a higher number of bits per pixel than the printer can handle (in order, for example, to attempt reproducing high-quality photographs). Therefore, it is allowable to specify a \***DrvBPP** value that is larger than the result of multiplying the \***DevBPP** value by the \*DevNumOfPlanes value.

For example, suppose you want to define a ColorMode option that causes images to be rendered as 24 bits/pixel bitmaps, but then you want the bitmap to be sent to the printer as *CMYK* data. You might define this mode as follows:

```GPD
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
