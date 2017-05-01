---
title: Hostfont Registry Entries
author: windows-driver-content
description: Hostfont Registry Entries
ms.assetid: f7ce2591-197a-4094-8b21-5e0cc48506ea
keywords:
- PostScript Printer Driver WDK print , HostFontXxx registry entries
- Pscript WDK print , HostFontXxx registry entries
- HostFontXxx registry entries WDK Pscript
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Hostfont Registry Entries


## <a href="" id="ddk-hostfont-registry-entries-gg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Hostfont%20Registry%20Entries%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


