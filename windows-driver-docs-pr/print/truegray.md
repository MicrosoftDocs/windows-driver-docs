---
title: TrueGray Feature
description: The TrueGray feature checks RGB colors in text and vector graphics, but not in bitmaps.
keywords:
- minidrivers WDK Pscript , TrueGray feature
- TrueGray feature
- RGB colors WDK printer
- gray color space WDK Pscript
- ADTrueGray
- color checking WDK Pscript
- checking RGB colors
ms.date: 01/30/2023
---

# TrueGray feature

[!include[Print Support Apps](../includes/print-support-apps.md)]

The TrueGray feature checks RGB colors in text and vector graphics, but not in bitmaps. For colors that are gray (that is, colors whose red, green, and blue values are equal), the TrueGray feature translates the colors from the RGB color space to the color printer's gray color space before printing them. This feature is not available for monochrome printers.

The TrueGray feature uses a private *PPD* keyword, \***ADTrueGray**, to allow PScript minidriver writers to enable or disable this feature.

| Keyword and Value | Meaning |
|--|--|
| **ADTrueGray**: True | The TrueGray feature is enabled by default for this printer. |
| **ADTrueGray**: False | The TrueGray feature is disabled by default for this printer. |

When the user interface indicates that the TrueGray feature is enabled, the driver detects RGB colors for which R = G = B, and one of the following conditions is true:

- When ICM processing is off

- When ICM processing is carried out on the host and the destination color profile is RGB data and the converted color is R' = G' = B' (that is, different from the original color)

- When ICM processing would normally be done using CIE-based color spaces and the original color is R = G = B

No attempt is made to detect gray in CMYK colors. This is the color space normally used when ICM color processing is carried out on the host.
