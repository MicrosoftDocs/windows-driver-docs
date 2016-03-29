---
title: Font Cartridge Attributes
description: Font Cartridge Attributes
ms.assetid: d1f99322-9c77-428a-beb5-6d0ff166c3e5
keywords: ["printer font descriptions WDK Unidrv , cartridges", "font cartridges WDK Unidrv", "cartridge fonts WDK Unidrv"]
---

# Font Cartridge Attributes


## <a href="" id="ddk-font-cartridge-attributes-gg"></a>


The following table contains attributes that can be included in a \*FontCartridge GPD entry.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Attribute Name</th>
<th align="left">Attribute Parameter</th>
<th align="left">Comments</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>*CartridgeName</strong></p></td>
<td align="left"><p>Text string representing the cartridge name.</p></td>
<td align="left"><p>Required, unless *<strong>rcCartridgeNameID</strong> is specified.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>*Fonts</strong></p></td>
<td align="left"><p>LIST of RC_UFM or RC_FONT resource identifiers representing fonts contained in the cartridge that are available for both portrait and landscape orientations.</p></td>
<td align="left"><p>At least one of *<strong>Fonts</strong>, *<strong>PortraitFonts</strong> or *<strong>LandscapeFonts</strong> must be specified. Font resource identifiers should be numbered contiguously from 1.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>*LandscapeFonts</strong></p></td>
<td align="left"><p>LIST of RC_UFM or RC_FONT resource identifiers representing fonts contained in the cartridge that are available only for landscape orientation.</p></td>
<td align="left"><p>At least one of *<strong>Fonts</strong>, *<strong>PortraitFonts</strong> or *<strong>LandscapeFonts</strong> must be specified. Font resource identifiers should be numbered contiguously from 1.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>*PortraitFonts</strong></p></td>
<td align="left"><p>LIST of RC_UFM or RC_FONT resource identifiers representing fonts contained in the cartridge that are available only for portrait orientation.</p></td>
<td align="left"><p>At least one of *<strong>Fonts</strong>, *<strong>PortraitFonts</strong> or *<strong>LandscapeFonts</strong> must be specified. Font resource identifiers should be numbered contiguously from 1.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>*rcCartridgeNameID</strong></p></td>
<td align="left"><p>Resource identifier of a String resource representing the cartridge name.</p></td>
<td align="left"><p>Required, unless *<strong>CartridgeName</strong> is specified.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Font%20Cartridge%20Attributes%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




