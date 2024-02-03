---
title: Standard Variables
description: Standard Variables
keywords:
- GPD file entries WDK Unidrv , standard variables
- variables WDK GPD files
- standard variables WDK GPD files
ms.date: 01/31/2024
---

# Standard variables

[!include[Print Support Apps](../includes/print-support-apps.md)]

The GPD language defines a set of standard variables that can be referenced within command strings, using the [command string format](command-string-format.md). The Unidrv driver assigns values to these variables. From the point of view of a GPD file, the variables are read-only.

All standard variables are stored as DWORD integers.

The following [printer command](printer-commands.md) entry specifies the command string that is sent to an HP LaserJet 4P when a block of raster data is ready:

```cpp
*Command: CmdSendBlockData: "<1B>*b" %d{NumOfDataBytes} "W"
```

The following table contains all of the standard variables, in alphabetic order.

| Standard Variable Name | Value | Comments |
|--|--|--|
| **BlueValue** | Blue component of the current color. | Valid for use in CmdDefinePaletteEntry command strings (see **GreenValue**, **RedValue**). |
| **CurrentFontID** | Identification number of the current downloaded soft font. | Valid if current print job includes downloaded soft fonts. |
| **CurrentPaletteIndex** | Current index into the color palette. | Valid for use in CmdSelectPaletteEntry command strings (see **GreenValue**, **RedValue**). |
| **CursorOriginX** | X coordinate of cursor origin, in master units. | Valid whenever a print job is in progress. |
| **CursorOriginY** | Y coordinate of cursor origin, in master units. | Valid whenever a print job is in progress. |
| **DestX** | X coordinate of cursor destination, in master units, relative to the cursor origin. | Valid for use in CmdXMoveAbsolute command strings. |
| **DestXRel** | X coordinate of cursor destination, in master units, relative to the current cursor position. | Valid for use in CmdXMoveRelLeft and CmdXMoveRelRight command strings. |
| **DestY** | Y coordinate of cursor destination, in master units, relative to the cursor origin. | Valid for use in CmdYMoveAbsolute command strings. |
| **DestYRel** | Y coordinate of cursor destination, in master units, relative to the current cursor position. | Valid for use in CmdYMoveRelUp and CmdYMoveRelDown command strings. |
| **FontBold** | Set to one if current font is bold, or zero otherwise. | Valid when a font has been specified. |
| **FontHeight** | Height, in master units, of the current font. | Valid when a font has been specified. |
| **FontItalic** | Set to one if current font is italic, or zero otherwise. | Valid when a font has been specified. |
| **FontMaxWidth** | Set to the maximum character increment of all glyphs in the font. | Valid when a font has been specified. |
| **FontStrikeThru** | Set to one if strike-through is enabled for the current font, or zero otherwise. | Valid when a font has been specified. |
| **FontUnderLine** | Set to one if current font is underlined, or zero otherwise. | Valid when a font has been specified. |
| **FontWidth** | Width, in master units, of the current font. | Valid when a font has been specified. |
| **GraphicsXRes** | Current horizontal resolution for graphics, in DPI. | Valid whenever a print job is in progress. |
| **GraphicsYRes** | Current vertical resolution for graphics, in DPI. | Valid whenever a print job is in progress. |
| **GrayPercentage** | Gray level (percentage) to use for gray fill. | Valid for use in CmdRectGrayFill command strings. |
| **GreenValue** | Green component of the current color. | Valid for use in CmdDefinePaletteEntry command strings (see **BlueValue**, **RedValue**). |
| **LinefeedSpacing** | Amount of vertical space, in master units, representing a linefeed. | Valid for use in CmdSetLineSpacing command strings. |
| **NextFontID** | Identification number of the next soft font to be downloaded. | Valid for use in CmdSetFontID command strings. |
| **NextGlyph** | The two-byte code of the next glyph to download. | Valid for use in CmdSetCharCode command strings. |
| **NumOfCopies** | Number of copies requested by the user. | Valid whenever a print job is in progress. |
| **NumOfDataBytes** | Number of bytes of raster data ready for transfer. | Valid for use in any CmdSendXXXData command string. If data is compressed, the value is the number of bytes after compression. |
| **PageNumber** | The number of the page currently being printed. Note that this does not necessarily correspond to the application's page number, but rather the number of times [*DrvSendPage*](/windows/win32/api/winddi/nf-winddi-drvsendpage) has been called. This value is initialized by [**DrvStartDoc**](/windows/win32/api/winddi/nf-winddi-drvstartdoc) and is incremented by **DrvSendPage**. For example, if N-up = 4 is selected, **PageNumber** is incremented to 2 only when the fifth page of the document is being printed. As another example, if a document is printed in reverse order (back to front) the **PageNumber** standard variable still reports the first page to be printed as page 1, even though this is the last page of the document. This behavior is needed to properly support the auto-duplexing feature. The OEM should use **PageNumber** only to determine whether the current page is the front or back side. | Valid whenever a print job is in progress. |
| **PaletteIndexToProgram** | Index into the color palette for the next entry to program. | Valid for use in CmdDefinePaletteEntry command strings. (Also see **RedValue**, **GreenValue**, **BlueValue**, **CurrentPaletteIndex**). |
| **PatternBrushID** | Identification number of a downloaded pattern brush. | Valid for use with CmdDownloadPattern and CmdSelectPattern command strings. |
| **PatternBrushSize** | Size, in bytes, of the current pattern brush. | Valid for use with CmdDownloadPattern command string. |
| **PatternBrushType** | Type of the current pattern brush. Value can be: 2: Shading pattern 3: Cross-hatch pattern 4: User-defined pattern. | Valid for use with CmdDownloadPattern and CmdSelectPattern command strings. |
| **PhysPaperLength** | Portrait-mode length, in y-master units, of the paper currently in use. | Valid whenever a print job is in progress. |
| **PhysPaperWidth** | Portrait-mode width, in master units, of the paper currently in use. | Valid whenever a print job is in progress. |
| **PrintDirInCCDegrees** | Amount of rotation, measured counterclockwise, in degrees. | Valid when the driver sends either the CmdSetSimpleRotation or CmdSetAnyRotation command string. |
| **RasterDataHeightInPixels** | Height, in pixels, of the image represented by current data. | Valid for use in any CmdSendXXXData command string, and in CmdSetSrcBmpHeight command strings. Compression does not modify this value. |
| **RasterDataWidthInBytes** | Number of bytes contained in a scan line. | Valid for use in any CmdSendXXXData command string, and in CmdSetSrcBmpWidth command strings. Compression does not modify this value. |
| **RectXSize** | Rectangle width, in x-master units. | Valid for use in CmdSetRectWidth command strings. |
| **RectYSize** | Rectangle length, in y-master units. | Valid for use in CmdSetRectHeight command strings. |
| **RedValue** | Red component of the current color. | Valid for use in CmdDefinePaletteEntry command strings (see **GreenValue**, **BlueValue**). |
| **TextXRes** | Current horizontal resolution for text, in DPI. | Valid whenever a print job is in progress. |
| **TextYRes** | Current vertical resolution for text, in DPI. | Valid whenever a print job is in progress. |
