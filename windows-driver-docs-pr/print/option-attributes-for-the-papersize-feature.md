---
title: Option Attributes for the PaperSize Feature
description: Option Attributes for the PaperSize Feature
ms.assetid: cfd82bc5-b89b-41c2-b542-28cb5905e37a
keywords:
- PaperSize Feature
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Option Attributes for the PaperSize Feature





The following table lists the attributes associated with the PaperSize feature. For more information about the PaperSize feature, see [Standard Features](standard-features.md).

**Note**   All paper size specifications for the following attributes must be expressed relative to PORTRAIT orientation, even if the attributes are being used to describe a different orientation, such as LANDSCAPE.

 

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
<td><p><em><strong>BottomMargin</strong></p></td>
<td><p>Numeric value representing the minimum allowable bottom margin, in x master units, for user-specified paper sizes associated with the CUSTOMSIZE option. Value is relative to the bottom of the physical page.</p></td>
<td><p>Optional. If not specified, the default value is 0. Used only with the CUSTOMSIZE option. Portrait orientation is assumed. See <a href="specifying-paper-sizes.md" data-raw-source="[Specifying Paper Sizes](specifying-paper-sizes.md)">Specifying Paper Sizes</a>.</p></td>
</tr>
<tr class="even">
<td><p></em><strong>CenterPrintable?</strong></p></td>
<td><p><strong>TRUE</strong> or <strong>FALSE</strong>, indicating whether the value specified by <em><strong>MaxPrintableWidth</strong> is centered.</p></td>
<td><p>Optional. If not specified, the printable area is to the right of the margin specified by <em><strong>MinLeftMargin</strong>. Used only with the CUSTOMSIZE option. See <a href="specifying-paper-sizes.md" data-raw-source="[Specifying Paper Sizes](specifying-paper-sizes.md)">Specifying Paper Sizes</a>.</p></td>
</tr>
<tr class="odd">
<td><p></em><strong>CursorOrigin</strong></p></td>
<td><p>PAIR of numeric values representing the cursor origin position, in master units, where PAIR (0, 0) is the upper left corner. Alternatively for CUSTOMSIZE, specify these values using <em><strong>CustCursorOriginX</strong> and *<strong>CustCursorOriginY</strong>.</p></td>
<td><p>Optional. If not specified, the default value is PAIR (0, 0). Unidrv assumes the cursor origin, relative to the printer, is constant with different paper sizes.</p></td>
</tr>
<tr class="even">
<td><p></em><strong>CustCursorOriginX</strong></p></td>
<td><p>CUSTOMSIZE parameter expression, used to create a value for the x index of <em><strong>CursorOrigin</strong>.</p></td>
<td><p>Optional. Use only with the CUSTOMSIZE option. See <a href="specifying-paper-sizes.md" data-raw-source="[Specifying Paper Sizes](specifying-paper-sizes.md)">Specifying Paper Sizes</a>.</p></td>
</tr>
<tr class="odd">
<td><p></em><strong>CustCursorOriginY</strong></p></td>
<td><p>CUSTOMSIZE parameter expression, used to create a value for the y index of <em><strong>CursorOrigin</strong>.</p></td>
<td><p>Optional. Use only with the CUSTOMSIZE option. See <a href="specifying-paper-sizes.md" data-raw-source="[Specifying Paper Sizes](specifying-paper-sizes.md)">Specifying Paper Sizes</a>.</p></td>
</tr>
<tr class="even">
<td><p></em><strong>CustPrintableOriginX</strong></p></td>
<td><p>CUSTOMSIZE parameter expression, used to create a value for the x index of <em><strong>PrintableOrigin</strong>.</p></td>
<td><p>Optional. Use only with the CUSTOMSIZE option. See <a href="specifying-paper-sizes.md" data-raw-source="[Specifying Paper Sizes](specifying-paper-sizes.md)">Specifying Paper Sizes</a>.</p></td>
</tr>
<tr class="odd">
<td><p></em><strong>CustPrintableOriginY</strong></p></td>
<td><p>CUSTOMSIZE parameter expression, used to create a value for the y index of <em><strong>PrintableOrigin</strong>.</p></td>
<td><p>Optional. Use only with the CUSTOMSIZE option. See <a href="specifying-paper-sizes.md" data-raw-source="[Specifying Paper Sizes](specifying-paper-sizes.md)">Specifying Paper Sizes</a>.</p></td>
</tr>
<tr class="even">
<td><p></em><strong>CustPrintableSizeX</strong></p></td>
<td><p>CUSTOMSIZE parameter expressions, used to create a value for the x value of <em><strong>PrintableArea</strong>.</p></td>
<td><p>Optional. Use only with the CUSTOMSIZE option. See <a href="specifying-paper-sizes.md" data-raw-source="[Specifying Paper Sizes](specifying-paper-sizes.md)">Specifying Paper Sizes</a>.</p></td>
</tr>
<tr class="odd">
<td><p></em><strong>CustPrintableSizeY</strong></p></td>
<td><p>CUSTOMSIZE parameter expression, used to create a value for the y value of <em><strong>PrintableArea</strong>.</p></td>
<td><p>Optional. Use only with the CUSTOMSIZE option. See <a href="specifying-paper-sizes.md" data-raw-source="[Specifying Paper Sizes](specifying-paper-sizes.md)">Specifying Paper Sizes</a>.</p></td>
</tr>
<tr class="even">
<td><p></em><strong>MaxSize</strong></p></td>
<td><p>PAIR of numeric values representing maximum allowable page length (x) and height (y) values, in master units, for user-specified paper sizes associated with the CUSTOMSIZE option.</p></td>
<td><p>Required for the CUSTOMSIZE option. Portrait orientation is assumed. See <a href="specifying-paper-sizes.md" data-raw-source="[Specifying Paper Sizes](specifying-paper-sizes.md)">Specifying Paper Sizes</a>.</p></td>
</tr>
<tr class="odd">
<td><p><em><strong>MaxPrintableWidth</strong></p></td>
<td><p>Numeric value representing the maximum printable width, in x master units, for user-specified paper sizes associated with the CUSTOMSIZE option.</p></td>
<td><p>Required for the CUSTOMSIZE option. Portrait orientation is assumed. See <a href="specifying-paper-sizes.md" data-raw-source="[Specifying Paper Sizes](specifying-paper-sizes.md)">Specifying Paper Sizes</a>.</p></td>
</tr>
<tr class="even">
<td><p></em><strong>MinLeftMargin</strong></p></td>
<td><p>Numeric value representing the minimum allowable left margin, in x master units, for user-specified paper sizes associated with the CUSTOMSIZE option. Value is relative to the left edge of the physical page</p></td>
<td><p>Optional. If not specified, the default value is 0. Used only with the CUSTOMSIZE option. Portrait orientation is assumed. See <a href="specifying-paper-sizes.md" data-raw-source="[Specifying Paper Sizes](specifying-paper-sizes.md)">Specifying Paper Sizes</a>.</p></td>
</tr>
<tr class="odd">
<td><p><em><strong>MinSize</strong></p></td>
<td><p>PAIR of numeric values representing minimum allowable page length (x) and height (y) values, in master units, for user-specified paper sizes associated with the CUSTOMSIZE option.</p></td>
<td><p>Required for the CUSTOMSIZE option. Portrait orientation is assumed. See <a href="specifying-paper-sizes.md" data-raw-source="[Specifying Paper Sizes](specifying-paper-sizes.md)">Specifying Paper Sizes</a>.</p></td>
</tr>
<tr class="even">
<td><p></em><strong>PageDimensions</strong></p></td>
<td><p>PAIR of numeric values representing the page length (x) and height (y) values, in master units, for any customized options for the PaperSize feature.</p></td>
<td><p>Used only for vendor-defined paper sizes. See <a href="specifying-paper-sizes.md" data-raw-source="[Specifying Paper Sizes](specifying-paper-sizes.md)">Specifying Paper Sizes</a>.</p></td>
</tr>
<tr class="odd">
<td><p><em><strong>PageProtectMem</strong></p></td>
<td><p>Numeric value representing the amount of printer memory, in kilobytes, required to protect a page.</p></td>
<td><p>Required if the PageProtect feature is specified. See <a href="specifying-paper-sizes.md" data-raw-source="[Specifying Paper Sizes](specifying-paper-sizes.md)">Specifying Paper Sizes</a>.</p></td>
</tr>
<tr class="even">
<td><p></em><strong>PrintableArea</strong></p></td>
<td><p>PAIR of numeric values representing the x- and y-plane lengths, in master units, of the printable page area.</p></td>
<td><p>Required for all PaperSize options except CUSTOMSIZE. See <a href="specifying-paper-sizes.md" data-raw-source="[Specifying Paper Sizes](specifying-paper-sizes.md)">Specifying Paper Sizes</a>.</p></td>
</tr>
<tr class="odd">
<td><p><em><strong>PrintableOrigin</strong></p></td>
<td><p>PAIR of numeric values representing the origin of the printable area, in master units, relative to the upper left-hand corner of the paper.</p></td>
<td><p>Required for all PaperSize options except CUSTOMSIZE. For CUSTOMSIZE, you can specify these values using *<strong>CustPrintableOriginX</strong> and *<strong>CustPrintableOriginY</strong>.</p></td>
</tr>
<tr class="even">
<td><p></em><strong>RotateSize?</strong></p></td>
<td><p><strong>TRUE</strong> or <strong>FALSE</strong>, indicating whether Unidrv should rotate the page dimensions because the paper (typically envelopes) is fed in sideways.</p></td>
<td><p>Optional. If not specified, the default value is <strong>FALSE</strong>. Can be used with any standard option for the PaperSize feature, except CUSTOMSIZE.</p></td>
</tr>
<tr class="odd">
<td><p></em><strong>TopMargin</strong></p></td>
<td><p>Numeric value representing the minimum allowable top margin, in y master units, for user-specified paper sizes associated with the CUSTOMSIZE option. Value is relative to the top of the physical page.</p></td>
<td><p>Optional. If not specified, the default value is 0. Used only with the CUSTOMSIZE option. Portrait orientation is assumed. See <a href="specifying-paper-sizes.md" data-raw-source="[Specifying Paper Sizes](specifying-paper-sizes.md)">Specifying Paper Sizes</a>.</p></td>
</tr>
</tbody>
</table>

 

For examples, see the [sample GPD files](sample-gpd-files.md).

### <a href="" id="ddk-customsize-parameter-expressions-gg"></a>CUSTOMSIZE Parameter Expressions

CUSTOMIZE parameter expressions are a restricted form of the [command string format](command-string-format.md). Text strings are not allowed.

Within the expression's **ArgumentType** segment, the following restrictions apply:

-   The only **ArgumentType** value allowed is %d.

-   Bracketed value ranges are not allowed.

Within the expression's **StandardVariableExpression** segment, the following restrictions apply:

-   Only the PhysPaperWidth and PhysPaperLength standard variables can be used.

-   The **Max\_Repeat** operator is not allowed.

Following are example expressions:

```cpp
*CustCursorOriginX: %d{((PhysPaperWidth-14040)/2)+300}
*CustCursorOriginY: %d{180}
*CustPrintableOriginX: %d{300}
*CustPrintableOriginY: %d{300}
*CustPrintableSizeX: %d{PhysPaperWidth-600}
*CustPrintableSizeY: %d{PhysPaperLength-600}
```

 

 




