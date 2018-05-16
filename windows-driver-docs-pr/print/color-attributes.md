---
title: Color Attributes
author: windows-driver-content
description: Color Attributes
ms.assetid: c8de0186-9cf5-43e5-81e7-33351a34c13c
keywords:
- color attributes WDK Unidrv
- general printer attributes WDK Unidrv , color
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 




