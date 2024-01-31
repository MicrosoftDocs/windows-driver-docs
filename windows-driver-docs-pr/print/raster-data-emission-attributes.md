---
title: Raster Data Emission Attributes
description: Raster Data Emission Attributes
keywords:
- data emission raster printing attributes WDK Unidrv
- emission raster printing attributes WDK Unidrv
ms.date: 01/29/2024
---

# Raster data emission attributes

[!include[Print Support Apps](../includes/print-support-apps.md)]

The following table lists attributes describing the printer's support for raster data emission.

| Attribute name | Attribute parameter | Comments |
|--|--|--|
| **CursorXAfterSendBlockData** | Constant value indicating the cursor's x-position after a block of raster data has been sent. Can be one of: AT_GRXDATA_END AT_GRXDATA_ORIGIN AT_CURSOR_X_ORIGIN meaning the pixel at the start of the graphics block, the pixel after the last one in the block, or the cursor origin. | Optional. If not specified, the default value is AT_GRXDATA_END. |
| **CursorYAfterSendBlockData** | Constant value indicating the cursor's y-position after a block of raster data has been sent. Can be one of: NO_MOVE AUTO_INCREMENT | Optional. If not specified, the default value is NO_MOVE, meaning the cursor's y-position is unchanged. |
| **MaxMultipleRowBytes** | Numeric value indicating the maximum-size raster block to use when downloading raster data on devices that set SendMultipleRows? to **TRUE** | The default value is 32 KB. The largest allowed value is 256 KB. |
| **MirrorRasterByte?** | **TRUE** or **FALSE**, indicating whether Unidrv should mirror (reverse) each byte of image data. | Optional. If not specified, the default value is **FALSE**. |
| **MirrorRasterPage?** | **TRUE** or **FALSE**, indicating whether output is to be mirrored. When **TRUE**, this attribute causes everything on the page to be printed as raster, and then mirrored in the opposite direction from banding. This means that portrait pages are mirrored left to right, landscape pages are mirrored top to bottom. This attribute is most useful for printing on transparencies or back-print film. | Optional. The default value is **FALSE**. This attribute is a relocatable global attribute. It may appear as a root-level attribute (see [Root-level-only attributes](root-level-only-attributes.md)) when there are no configuration dependencies, or it may appear with Option or Case constructs on a per-media type basis. |
| **MoveToX0BeforeSetColor?** | **TRUE** or **FALSE**, indicating whether the cursor's x-coordinate must be set to zero before an explicit color selection command can be sent. | Optional. If not specified, the default value is **FALSE**. Can be **TRUE** only if **UseExpColorSelectCmd?** is also **TRUE**. |
| **OptimizeLeftBound?** | **TRUE** or **FALSE**, indicating whether Unidrv should remove blanks at the left bound of each band. | Optional. If not specified, the default value is **FALSE**. |
| **OutputDataFormat** | H_BYTE or V_BYTE, indicating whether the bits in a data byte are mapped to horizontal pixels or vertical pixels. | Optional. If not specified, the default value is H_BYTE. |
| **PreAnalysisOptions** | Numeric value, one of 0, 1, 2, 4, or 8. For information about the meaning of each attribute parameter, see [Preanalysis infrastructure](preanalysis-infrastructure.md). | Optional. If not specified, the default value is 1. |
| **RasterSendAllData?** | **TRUE** or **FALSE**, indicating whether Unidrv should send all raster data, including blank scan lines and blanks within scan lines. | Optional. If not specified, the default value is **FALSE**. |
| **SendMultipleRows?** | **TRUE** or **FALSE**, indicating whether the command specified by CmdSendBlockData can send multiple blocks at one time. |  |
| **StripBlanks** | LIST indicating which blanks in a raster data block should be stripped. Can be one or more of: LEADING ENCLOSED TRAILING | Optional. If not specified, Unidrv does not strip any blanks. Also see **MinStripBlankPixels** in [Option attributes for the resolution feature](option-attributes-for-the-resolution-feature.md). |
| **UseExpColorSelectCmd?** | **TRUE** or **FALSE**, indicating whether the printer requires explicit color selection commands, separate from color raster data. | Optional. If not specified, the default value is **FALSE**. Dot-matrix printers require a value of **TRUE**. |

For information about commands associated with raster data emission, see [Raster data emission commands](raster-data-emission-commands.md).

For GPD examples, see [Sample GPD files](sample-gpd-files.md).
