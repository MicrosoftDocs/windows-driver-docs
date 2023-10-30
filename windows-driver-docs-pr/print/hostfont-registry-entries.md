---
title: Hostfont registry entries
description: Provides information about hostfont registry entries.
keywords:
- PostScript Printer Driver WDK print , HostFontXxx registry entries
- Pscript WDK print , HostFontXxx registry entries
- HostFontXxx registry entries WDK Pscript
ms.date: 01/27/2023
---

# Hostfont registry entries

[!include[Print Support Apps](../includes/print-support-apps.md)]

An OEM plug-in can notify the Pscript5 driver that the %hostfont%-ready PostScript interpreter has a set of fonts and CIDFonts that are available to use and are identical to those that the Pscript5 driver might download in the course of a print job. Notification of which fonts are to be handled this way is done by placing keys in the registry. The Pscript5 driver checks the registry for new information when its [**DrvEnablePDEV**](/windows/win32/api/winddi/nf-winddi-drvenablepdev) function is called. The plug-in can then ensure that the data is current before the PDEV is enabled.

The following table lists the %hostfont% registry entry names, their types, and their values. The OEM plug-in should call SetPrinterData (described in the Microsoft Windows SDK documentation) to set these entry names. The HostFont*Xxx* entry names are mutually exclusive. That is, only one of the following entry names can exist in the registry at any given time.

| Entry Name | Type and value | Description |
|--|--|--|
| HostFontExceptCIDFonts | REG_BINARY | Can contain multiple, NULL-terminated ASCII strings containing the PostScript CIDFont names. The final string is terminated by an extra null character.<br><br>Similar to HostFontExceptFonts except that it applies to CIDFonts. |
| HostFontExceptFonts | REG_BINARY | Can contain multiple, NULL-terminated ASCII strings containing the PostScript font names. The final string is terminated by an extra null character.<br><br>Fonts that the Pscript5 driver does not "see" as available and identical to those fonts in the %hostfont%-ready PostScript interpreter. The Pscript5 driver downloads only these fonts.<br><br>Treat all fonts as %hostfont%-able. If this entry name appears with any value, the Pscript5 driver does not download any fonts. |
| Row3 | REG_DWORD | Can be any value. |
| Row4 | REG_BINARY | Can contain multiple, NULL-terminated ASCII strings containing the PostScript CIDFont names. The final string is terminated by an extra null character.<br><br>Similar to HostFontIncludesFonts except that it applies to CIDFonts. |
| Row5 | REG_BINARY | Can contain multiple, NULL-terminated ASCII strings containing the PostScript font names. The final string is terminated by an extra null character.<br><br>Fonts that the Pscript5 driver "sees" as the only ones that are available and identical in the %hostfont%-ready PostScript interpreter. The Pscript5 driver does not download these fonts. |

## Additional notes on hostfont registry entry names

HostFontExceptFonts is REG_BINARY data consisting of a sequence of NULL-terminated single-byte strings containing the PostScript findfont names of TTF-based, OTF-based, or PFB-based encoding-and-glyph-name-based fonts. The names are listed in no particular order; the last name is terminated by two NULLs, and there are no bytes after the NULLs. This entry name is checked only when HostFontHasMostFonts is not found.

The existence of the HostFontHasMostFonts key with any value assigned to it means that the driver should assume that all TTF-based, OTF-based, and PFB-based host fonts are available in their "native" format, that is, as a PostScript font or a CIDFont format as appropriate, on the target interpreter.

HostFontIncludesFonts is similar to HostFontExceptFonts except that it explicitly lists PostScript font names that are available on the target interpreter.
