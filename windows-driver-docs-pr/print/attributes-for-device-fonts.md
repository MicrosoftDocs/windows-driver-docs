---
title: Attributes for device fonts
description: Provides information about attributes for device fonts.
keywords:
- device fonts WDK Unidrv
- font attributes WDK Unidrv
ms.date: 09/06/2022
---

# Attributes for device fonts

The following table lists attributes describing the printer's support for device fonts.

| Attribute name | Attribute parameter | Comments |
|--|--|--|
| ***CharPosition*** | UPPERLEFT or BASELINE. Indicates the area of the character bounding box to which the print head should be positioned before printing a character. | Optional. If not specified, the default value is UPPERLEFT. |
| **DefaultCTT** | Numeric value representing the RC_CTT resource identifier of the default character translation table. | Optional. Applies only to TTY printers. If not specified, there is no translation table. (This attribute is provided only for backward compatibility with GPC files.) |
| ***DefaultFont*** | Numeric value representing the RC_FONT or RC_UFM resource identifier of the default font. | Required if the printer supports device fonts. |
| **LookAheadRegion** | Numeric (integer) value representing how far ahead the driver must "look" to determine whether it should emit text. This value is in *y* master units, but must be convertible to an integral number of pixels. For more information, see the comment that follows this table. | Optional. If not specified, the default value is zero. Used only with serial printers, (for example, HP DeskJet), for ordering text and bitmap data. |
| ***MaxFontUsePerPage*** | Numeric value representing the maximum number of fonts the printer can use per page. | Optional. If not specified, there is no limit. |
| **TextYOffset** | Numeric value representing the vertical distance, in *y* master units, by which resident fonts must be repositioned to align with bitmap font baselines. | Optional. If not specified, the default value is 0. (Used with some dot-matrix printers.) |

For examples, see the [sample GPD files](sample-gpd-files.md).

To determine the size of the lookahead region, the printer driver must perform an addition based on the current scan line and the value of the **\*LookAheadRegion** attribute. Because the scan line is in units of pixels while **\*LookAheadRegion** is in vertical master units, the driver must convert the attribute value into pixels.
>
For example, if the value of the **\*LookAheadRegion** attribute is 600, and there are 1200 vertical master units per inch, then the size of the lookahead region one-half inch. If the current resolution is 300 dpi, one-half inch corresponds to 150 pixels (vertical), or 150 scan lines. If the printer is currently on scan line 100, the driver must look for text baselines between scan lines 100 and 250.

The driver repeats this process for each scan line, although it emits the text it finds only once.
