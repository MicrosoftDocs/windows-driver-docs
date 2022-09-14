---
title: Attributes for downloaded fonts
description: Provides information about attributes for downloaded fonts.
keywords:
- downloaded font attributes WDK Unidrv
- font attributes WDK Unidrv
ms.date: 09/06/2022
---

# Attributes for downloaded fonts

The following table lists attributes describing the printer's support for downloaded fonts.

| Attribute name | Attribute parameter | Comments |
|--|--|--|
| ***DLSymbolSet*** | Constant that represents the symbol set to be used when downloading TrueType fonts. Can be either PC-8 or ROMAN-8. | Optional. If not specified, the glyph range is assumed to be contiguous within limits specified by **\*MinGlyphID** and **\*MaxGlyphID**. |
| **FontFormat** | Constant value indicating the type of downloading supported. Must be one of the following:<br<br>HPPCL<br>HPPCL_RES<br>HPPCL_OUTLINE<br >OEM_CALLBACK | Required if the printer can download fonts. If OEM_CALLBACK is specified, font callback functions must be provided. For more information about these callbacks, see [Customizing Microsoft's Printer Drivers](customizing-microsoft-s-printer-drivers.md). |
| ***MaxFontID*** | Numeric value representing the maximum identifier for soft fonts. | Optional. If not specified, the default value is 65535. |
| **MaxGlyphID** | Numeric value representing the maximum identifier for downloaded font glyphs. | Optional. If not specified and **\*DLSymbolSet** is not specified, the default value is 255. Ignored if **\*DLSymbolSet** is specified. |
| **MaxNumDownFonts** | Numeric value representing the maximum number of soft fonts that can be stored in printer memory at one time. | Optional. If not specified, Unidrv assumes an unlimited number of soft fonts can be stored. |
| ***MinFontID*** | Numeric value representing the minimum identifier for soft fonts. | Optional. If not specified, the default value is one. |
| **MinGlyphID** | Numeric value representing the minimum identifier for downloaded font glyphs. | Optional. If not specified and **\*DLSymbolSet** is not specified, the default value is 32. Ignored if **\*DLSymbolSet** is specified. |
| **TextHalftoneThreshold** | Numeric value that determines whether Unidrv performs text halftoning for TrueType fonts. If the driver's resolution is greater than or equal to the value specified in this attribute, Unidrv halftones text. | Optional. The default value is 600. |

For examples, see the [sample GPD files](sample-gpd-files.md).
