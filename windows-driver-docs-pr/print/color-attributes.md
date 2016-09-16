---
title: Color Attributes
author: windows-driver-content
description: Color Attributes
MS-HAID:
- 'nt5gpd\_082abbe3-496e-4d9e-bbf4-0f637c4a61a4.xml'
- 'print.color\_attributes'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: c8de0186-9cf5-43e5-81e7-33351a34c13c
keywords: ["color attributes WDK Unidrv", "general printer attributes WDK Unidrv , color"]
---

# Color Attributes


## <a href="" id="ddk-color-attributes-gg"></a>


Color attributes are [general printing attributes](general-printing-attributes.md) that specify characteristics for controlling color printing.

The following table lists the color attributes.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute Name</th>
<th>Attribute Parameter</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>*ChangeColorModeOnDoc?</strong></p></td>
<td><p><strong>TRUE</strong> or <strong>FALSE</strong>. Indicates whether a printer's color mode can be changed between pages of a document without side effects.</p></td>
<td><p>Optional. If not specified, the default value is <strong>TRUE</strong>. Unidrv uses this value to optimize printing speed. For additional information, see Note following this table.</p></td>
</tr>
<tr class="even">
<td><p><strong>*CyanInMagentaDye</strong></p></td>
<td><p>Numeric value, from 0 to 1000, indicating the percentage of cyan contamination in magenta dye. The value is the contamination percentage times 100. For example, 8.4% contamination is specified as 840 and 10% is 1000.</p></td>
<td><p>Optional. If not specified, a Unidrv-supplied default value is used.</p></td>
</tr>
<tr class="odd">
<td><p><strong>*CyanInYellowDye</strong></p></td>
<td><p>Numeric value, from 0 to 1000, indicating the percentage of cyan contamination in yellow dye. The value is the contamination percentage times 100. For example, 8.4% contamination is specified as 840 and 10% is 1000.</p></td>
<td><p>Optional. If not specified, a Unidrv-supplied default value is used.</p></td>
</tr>
<tr class="even">
<td><p><strong>*EnableGDIColorMapping</strong></p></td>
<td><p><strong>TRUE</strong> or <strong>FALSE</strong>. Indicates whether GDI should perform gamut mapping from display to printer color space.</p></td>
<td><p>Optional. If not specified, the default value is <strong>FALSE</strong>. If <strong>TRUE</strong>, Unidrv sets the HT_FLAG_DO_DEVCLR_XFORM flag in the [<strong>GDIINFO</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566484) structure.</p></td>
</tr>
<tr class="odd">
<td><p><strong>*MagentaInCyanDye</strong></p></td>
<td><p>Numeric value, from 0 to 1000, indicating the percentage of magenta contamination in cyan dye. The value is the contamination percentage times 100. For example, 8.4% contamination is specified as 840 and 10% is 1000.</p></td>
<td><p>Optional. If not specified, a Unidrv-supplied default value is used.</p></td>
</tr>
<tr class="even">
<td><p><strong>*MagentaInYellowDye</strong></p></td>
<td><p>Numeric value, from 0 to 1000, indicating the percentage of magenta contamination in yellow dye. The value is the contamination percentage times 100. For example, 8.4% contamination is specified as 840 and 10% is 1000.</p></td>
<td><p>Optional. If not specified, a Unidrv-supplied default value is used.</p></td>
</tr>
<tr class="odd">
<td><p><strong>*YellowInCyanDye</strong></p></td>
<td><p>Numeric value, from 0 to 1000, indicating the percentage of yellow contamination in cyan dye. The value is the contamination percentage times 100. For example, 8.4% contamination is specified as 840 and 10% is 1000.</p></td>
<td><p>Optional. If not specified, a Unidrv-supplied default value is used.</p></td>
</tr>
<tr class="even">
<td><p><strong>*YellowInMagentaDye</strong></p></td>
<td><p>Numeric value, from 0 to 1000, indicating the percentage of yellow contamination in magenta dye. The value is the contamination percentage times 100. For example, 8.4% contamination is specified as 840 and 10% is 1000.</p></td>
<td><p>Optional. If not specified, a Unidrv-supplied default value is used.</p></td>
</tr>
</tbody>
</table>

 

**Note**   When the **\*ChangeColorModeOnDoc?** color attribute is set to **TRUE**, color optimization is enabled. When this attribute is set to **FALSE**, no optimization is performed. When color optimization is enabled, the presence of color in the spool file causes the spool file to be played in color; the lack of color in the spool file causes the spool file to be played in monochrome.
If you are creating a Unidrv rendering plug-in to generate color watermarks, be advised that color optimization causes color watermarks to be printed in black and white when they are printed on black-and-white documents. To ensure that color watermarks print correctly with color and black-and-white documents, disable color optimization.

The color optimization controlled by the **\*ChangeColorModeOnDoc?** color attribute can also be controlled by setting the **dwColorOptimization** member of the [**ATTRIBUTE\_INFO\_2**](https://msdn.microsoft.com/library/windows/hardware/ff545091) or [**ATTRIBUTE\_INFO\_3**](https://msdn.microsoft.com/library/windows/hardware/ff545093) structures. Color optimization also can be controlled by using the [**GdiEndPageEMF**](https://msdn.microsoft.com/library/windows/hardware/ff549468) function.

 

For examples of the color attributes listed on this page, see the [sample GPD files](sample-gpd-files.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Color%20Attributes%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


