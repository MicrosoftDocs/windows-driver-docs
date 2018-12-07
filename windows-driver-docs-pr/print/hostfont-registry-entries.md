---
title: Hostfont Registry Entries
description: Hostfont Registry Entries
ms.assetid: f7ce2591-197a-4094-8b21-5e0cc48506ea
keywords:
- PostScript Printer Driver WDK print , HostFontXxx registry entries
- Pscript WDK print , HostFontXxx registry entries
- HostFontXxx registry entries WDK Pscript
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Hostfont Registry Entries





An OEM plug-in can notify the Pscript5 driver that the %hostfont%-ready PostScript interpreter has a set of fonts and CIDFonts that are available to use and are identical to those that the Pscript5 driver might download in the course of a print job. Notification of which fonts are to be handled this way is done by placing keys in the registry. The Pscript5 driver checks the registry for new information when its [**DrvEnablePDEV**](https://msdn.microsoft.com/library/windows/hardware/ff556211) function is called. The plug-in can then ensure that the data is current before the PDEV is enabled.

The following table lists the %hostfont% registry entry names, their types, and their values. The OEM plug-in should call SetPrinterData (described in the Microsoft Windows SDK documentation) to set these entry names. The HostFont*Xxx* entry names are mutually exclusive. That is, only one of the following entry names can exist in the registry at any given time.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Entry Name</th>
<th>Type and Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>HostFontExceptCIDFonts</p></td>
<td><p>REG_BINARY</p>
<p>Can contain multiple, NULL-terminated ASCII strings containing the PostScript CIDFont names. The final string is terminated by an extra null character.</p></td>
<td><p>Similar to HostFontExceptFonts except that it applies to CIDFonts.</p></td>
</tr>
<tr class="even">
<td><p>HostFontExceptFonts</p></td>
<td><p>REG_BINARY</p>
<p>Can contain multiple, NULL-terminated ASCII strings containing the PostScript font names. The final string is terminated by an extra null character.</p></td>
<td><p>Fonts that the Pscript5 driver does not &quot;see&quot; as available and identical to those fonts in the %hostfont%-ready PostScript interpreter. The Pscript5 driver downloads only these fonts.</p></td>
</tr>
<tr class="odd">
<td><p>HostFontHasMostFonts</p></td>
<td><p>REG_DWORD</p>
<p>Can be any value.</p></td>
<td><p>Treat all fonts as %hostfont%-able. If this entry name appears with any value, the Pscript5 driver does not download any fonts.</p></td>
</tr>
<tr class="even">
<td><p>HostFontIncludesCIDFonts</p></td>
<td><p>REG_BINARY</p>
<p>Can contain multiple, NULL-terminated ASCII strings containing the PostScript CIDFont names. The final string is terminated by an extra null character.</p></td>
<td><p>Similar to HostFontIncludesFonts except that it applies to CIDFonts.</p></td>
</tr>
<tr class="odd">
<td><p>HostFontIncludesFonts</p></td>
<td><p>REG_BINARY</p>
<p>Can contain multiple, NULL-terminated ASCII strings containing the PostScript font names. The final string is terminated by an extra null character.</p></td>
<td><p>Fonts that the Pscript5 driver &quot;sees&quot; as the only ones that are available and identical in the %hostfont%-ready PostScript interpreter. The Pscript5 driver does not download these fonts.</p></td>
</tr>
</tbody>
</table>

 

### Additional Notes on Hostfont Registry Entry Names

HostFontExceptFonts is REG\_BINARY data consisting of a sequence of NULL-terminated single-byte strings containing the PostScript findfont names of TTF-based, OTF-based, or PFB-based encoding-and-glyph-name-based fonts. The names are listed in no particular order; the last name is terminated by two NULLs, and there are no bytes after the NULLs. This entry name is checked only when HostFontHasMostFonts is not found.

The existence of the HostFontHasMostFonts key with any value assigned to it means that the driver should assume that all TTF-based, OTF-based, and PFB-based host fonts are available in their "native" format, that is, as a PostScript font or a CIDFont format as appropriate, on the target interpreter.

HostFontIncludesFonts is similar to HostFontExceptFonts except that it explicitly lists PostScript font names that are available on the target interpreter.

 

 




