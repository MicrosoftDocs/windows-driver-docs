---
title: Font Substitution
description: Font Substitution
ms.assetid: a67f42cd-1c10-46b7-8d24-0cb26339bc92
keywords:
- printer font descriptions WDK Unidrv , substitutions
- substitution font table WDK Unidrv
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Font Substitution





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

```cpp
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

```cpp
*Include: "ttfsub.gpd"
```

Additionally, this file must be installed. For more information, see [Printer INF File Install Sections](printer-inf-file-install-sections.md).

 

 




