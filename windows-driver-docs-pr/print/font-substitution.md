---
title: Font Substitution
author: windows-driver-content
description: Font Substitution
ms.assetid: a67f42cd-1c10-46b7-8d24-0cb26339bc92
keywords:
- printer font descriptions WDK Unidrv , substitutions
- substitution font table WDK Unidrv
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Font Substitution


## <a href="" id="ddk-font-substitution-gg"></a>


For printers that provide hardware-resident or cartridge fonts, a font substitution table can be specified. By providing a font substitution table, you specify hardware-resident or cartridge fonts that can be substituted for TrueType fonts that must be downloaded. When Unidrv receives text in such a TrueType font, it first checks to see if the font substitution table contains a hardware-resident substitution for the font. If Unidrv finds a substituted resident font, and if the font metrics (such as character set, weight, italic, orientation, and so on) are compatible, the resident font is used.

You can create a default font substitution table by using a series of \*TTFS entries. The format of each entry is:

<table>
<colgroup>
<col width="100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p></p>
*TTFS: <em>FontName</em>
{
*TTFontName: &quot;<em>TTFontNameString</em>&quot;
*DevFontName: &quot;<em>DeviceFontNameString</em>&quot;
<strong>}</strong></td>
</tr>
</tbody>
</table>

 

where *FontName* is a symbol specifying the entry name, *TTFontNameString* is a text string identifying the TrueType font to be replaced, and *DeviceFontNameString* is a text string identifying the hardware-resident or cartridge font to be used. Following is an example table:

```
*TTFS: Arial
{
    *TTFontName: "Arial"
    *DevFontName "Arial"
}
*TTFS: TNR
{
    *TTFontName: "Times New Roman"
    *DevFontName: "Times New Roman"
}
*TTFS: CurrierNew 
{
    *TTFontName:  "Courier New"
    *DevFontName: "Courier New"
}
```

If there are duplicate \*TTFS entries with the same *FontName* value, the last entry read by the parser supersedes the previous one.

The substitution table you specify is a default table, because Unidrv allows users to modify the substitutions.

All \*TTFS entries must be located at the GPD file's root level (that is, not within braces).

To control whether or not font substitution is enabled by default, use the \*TTFSEnabled? entry. This entry's format is:

<table>
<colgroup>
<col width="100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>*TTFSEnabled?: <em>BooleanValue</em></p></td>
</tr>
</tbody>
</table>

 

where *BooleanValue* is **TRUE** or **FALSE**. If *BooleanValue* is **TRUE**, Unidrv enables font substitution. If *BooleanValue* is **FALSE**, or if you do not include a \*TTFSEnabled? entry in the GPD file, Unidrv disables font substitution until it is enabled by a user.

The \*TTFSEnable? entry is relocatable, but \*TTFS entries are not. (For information about relocatable entries, see What to Place Inside \*Switch, \*Case, and \*Default Statements).

### Default TrueType Font Substitutions

A default table of TrueType font substitutions is provided in the file named ttfsub.gpd. To use it, add the following entry at the GPD file's root level (that is, not within braces):

```
*Include: "ttfsub.gpd"
```

Additionally, this file must be installed. For more information, see [Printer INF File Install Sections](printer-inf-file-install-sections.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Font%20Substitution%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


