---
title: Option attributes for the Resolution feature
description: Option attributes for the Resolution feature
keywords:
- Resolution Feature
ms.date: 07/19/2023
---

# Option attributes for the Resolution feature

[!include[Print Support Apps](../includes/print-support-apps.md)]**

The following table lists the attributes associated with the Resolution feature. For more information about the Resolution feature, see [Standard Features](standard-features.md).

| Attribute name | Attribute parameter | Comments |
|--|--|--|
| \***DPI** | PAIR of numeric values representing the x and y values for the printer's resolution, in dots per inch. | Required. The x and y values must equal \***TextDPI** x and y values, or they must be equal to \***TextDPI** x and y values divided by a power of two. For example, if \***TextDPI** is PAIR(300, 300), then \***DPI** values might be PAIR(300, 300), PAIR(150, 150), or PAIR(75, 75), but not PAIR(100, 100). |
| \***MinStripBlankPixels** | Numeric value representing the minimum number of blank bytes that Unidrv should encounter within a scan line before stripping enclosing blank bytes. | Optional. If not specified, the default value is zero. This attribute is relevant only if a \***StripBlanks** entry specifies ENCLOSED. For more information, see [Raster Data Emission Attributes](raster-data-emission-attributes.md). |
| \***PinsPerLogPass** | Numeric value presenting the number of scan lines printed by one logical pass of the print head. Must be a multiple of \***PinsPerPhysPass**, since each logical pass consists of one or more physical passes. | Optional. If not specified, the default value is 1. Required if a printer performs interlacing, requiring multiple passes of the print head across a set of scan lines, to print all the scan lines. |
| \***PinsPerPhysPass** | Numeric value representing the number of scan lines printed as the print head moves across the page. Must be one, or a multiple of eight. | Optional. If not specified, the default value is 1.<br><br>The horizontal and vertical resolutions should be multiples of \***PinsPerPhysPass**, or the output might be unpredictable. |
| \***RequireUniDir?** | **TRUE** or **FALSE**, indicating whether the specified resolution requires unidirectional printing to be enabled. | Optional. If not specified, the default value is **FALSE**. |
| \***SpotDiameter** | Numeric value representing the spot diameter size, as a percentage of the pixel size, for the resolution specified by \***DPI**. | Required.<br><br>Examples:<br><br>100 means the spot diameter equals the pixel size.<br><br>200 means the spot diameter is twice the pixel size.<br><br>50 means the spot diameter is half the pixel size. |
| \***TextDPI** | PAIR or numeric values representing the x and y values for the printer's text resolution, in dots per inch. | Required. See \***DPI** comments. This resolution is used for drawing fonts and vector graphics. |

For GPD examples, see the [sample GPD files](sample-gpd-files.md).

For information about additional option attributes, see [Option Attributes for All Features](option-attributes-for-all-features.md).

Also, see [Controlling Image Quality](controlling-image-quality.md).
