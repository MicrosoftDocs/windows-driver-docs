---
title: Option attributes for the ColorMode feature
description: Option attributes for the ColorMode feature
keywords:
- ColorMode Feature
ms.date: 07/19/2023
---

# Option attributes for the ColorMode feature

[!include[Print Support Apps](../includes/print-support-apps.md)]

The following table lists the attributes associated with the ColorMode feature. For more information about the ColorMode feature, see [Standard Features](standard-features.md).

| Attribute name | Attribute parameter | Comments |
|--|--|--|
| \***Color?** | **TRUE** or **FALSE**, indicating whether the option produces color. | Optional. If not specified, the default value is **TRUE** for \***DrvBPP** > 1. To create gray scaling, set to **FALSE** with \***DrvBPP** > 1. |
| \***ColorPlaneOrder** | LIST indicating the order in which Unidrv should send color plane data.<br><br>Examples:<br><br>LIST (YELLOW, MAGENTA, CYAN, BLACK)<br><br>LIST (RED, GREEN, BLUE)<br><br>Colors can be repeated in the list. | Required if \***DevNumOfPlanes** is greater than 1. The number of colors specified must equal \***DevNumOfPlanes**. |
| \***DevBPP** | Numeric value indicating the number of bits per pixel of color data supported by the printer. | Optional. If not specified, the default value is 1. |
| \***DevNumOfPlanes** | Numeric value indicating the number of color planes supported by the printer. | Optional. If not specified, the default value is 1. (For color printers, a value of 1 is referred to as pixel mode.) |
| \***DrvBPP** | Numeric value indicating the number of bits per pixel that Unidrv should use for its bitmap rendering buffer. The bitmap format is a Windows device-independent bitmap (DIB), and valid values are 1, 4, 8, 16, 24, or 32. | Optional. If not specified, the default value is 1. (For color printers, a value of 1 is referred to as "planar mode".)<br><br><p>Windows DIBs always use one color plane. |
| \***IPCallbackID** | Positive numeric value, passed to the rendering plug-in's [**IPrintOemUni::ImageProcessing**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-imageprocessing) method as its **IPCallbackID** argument. | Required if a [rendering plug-in](rendering-plug-ins.md) is supplied that contains an **IPrintOemUn::ImageProcessing** method. |
| \***PaletteProgrammable** | **TRUE** or **FALSE**, indicating whether the color palette is programmable. | Optional. If not specified, the default value is **FALSE**. |
| \***PaletteSize** | Numeric value representing the number of entries in the color palette used with the specified option. | Optional. If not specified, the default value is 2. |
| \***RasterMode** | DIRECT or INDEXED, indicating whether the raster data is sent directly to the printer or is indexed through a color palette. | Optional. If not specified, the default value is INDEXED. |

For examples, see the [sample GPD files](sample-gpd-files.md).

For information about additional option attributes, see [Option Attributes for All Features](option-attributes-for-all-features.md).

Also see [Controlling Image Quality](controlling-image-quality.md).
