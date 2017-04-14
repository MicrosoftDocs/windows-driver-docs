---
title: Option Attributes for the PaperSize Feature
author: windows-driver-content
description: Option Attributes for the PaperSize Feature
ms.assetid: cfd82bc5-b89b-41c2-b542-28cb5905e37a
keywords: ["PaperSize Feature"]
---

# Option Attributes for the PaperSize Feature


## <a href="" id="ddk-option-attributes-for-the-papersize-feature-gg"></a>


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
<td><p>*<strong>BottomMargin</strong></p></td>
<td><p>Numeric value representing the minimum allowable bottom margin, in x master units, for user-specified paper sizes associated with the CUSTOMSIZE option. Value is relative to the bottom of the physical page.</p></td>
<td><p>Optional. If not specified, the default value is 0. Used only with the CUSTOMSIZE option. Portrait orientation is assumed. See [Specifying Paper Sizes](specifying-paper-sizes.md).</p></td>
</tr>
<tr class="even">
<td><p>*<strong>CenterPrintable?</strong></p></td>
<td><p><strong>TRUE</strong> or <strong>FALSE</strong>, indicating whether the value specified by *<strong>MaxPrintableWidth</strong> is centered.</p></td>
<td><p>Optional. If not specified, the printable area is to the right of the margin specified by *<strong>MinLeftMargin</strong>. Used only with the CUSTOMSIZE option. See [Specifying Paper Sizes](specifying-paper-sizes.md).</p></td>
</tr>
<tr class="odd">
<td><p>*<strong>CursorOrigin</strong></p></td>
<td><p>PAIR of numeric values representing the cursor origin position, in master units, where PAIR (0, 0) is the upper left corner. Alternatively for CUSTOMSIZE, specify these values using *<strong>CustCursorOriginX</strong> and *<strong>CustCursorOriginY</strong>.</p></td>
<td><p>Optional. If not specified, the default value is PAIR (0, 0). Unidrv assumes the cursor origin, relative to the printer, is constant with different paper sizes.</p></td>
</tr>
<tr class="even">
<td><p>*<strong>CustCursorOriginX</strong></p></td>
<td><p>CUSTOMSIZE parameter expression, used to create a value for the x index of *<strong>CursorOrigin</strong>.</p></td>
<td><p>Optional. Use only with the CUSTOMSIZE option. See [Specifying Paper Sizes](specifying-paper-sizes.md).</p></td>
</tr>
<tr class="odd">
<td><p>*<strong>CustCursorOriginY</strong></p></td>
<td><p>CUSTOMSIZE parameter expression, used to create a value for the y index of *<strong>CursorOrigin</strong>.</p></td>
<td><p>Optional. Use only with the CUSTOMSIZE option. See [Specifying Paper Sizes](specifying-paper-sizes.md).</p></td>
</tr>
<tr class="even">
<td><p>*<strong>CustPrintableOriginX</strong></p></td>
<td><p>CUSTOMSIZE parameter expression, used to create a value for the x index of *<strong>PrintableOrigin</strong>.</p></td>
<td><p>Optional. Use only with the CUSTOMSIZE option. See [Specifying Paper Sizes](specifying-paper-sizes.md).</p></td>
</tr>
<tr class="odd">
<td><p>*<strong>CustPrintableOriginY</strong></p></td>
<td><p>CUSTOMSIZE parameter expression, used to create a value for the y index of *<strong>PrintableOrigin</strong>.</p></td>
<td><p>Optional. Use only with the CUSTOMSIZE option. See [Specifying Paper Sizes](specifying-paper-sizes.md).</p></td>
</tr>
<tr class="even">
<td><p>*<strong>CustPrintableSizeX</strong></p></td>
<td><p>CUSTOMSIZE parameter expressions, used to create a value for the x value of *<strong>PrintableArea</strong>.</p></td>
<td><p>Optional. Use only with the CUSTOMSIZE option. See [Specifying Paper Sizes](specifying-paper-sizes.md).</p></td>
</tr>
<tr class="odd">
<td><p>*<strong>CustPrintableSizeY</strong></p></td>
<td><p>CUSTOMSIZE parameter expression, used to create a value for the y value of *<strong>PrintableArea</strong>.</p></td>
<td><p>Optional. Use only with the CUSTOMSIZE option. See [Specifying Paper Sizes](specifying-paper-sizes.md).</p></td>
</tr>
<tr class="even">
<td><p>*<strong>MaxSize</strong></p></td>
<td><p>PAIR of numeric values representing maximum allowable page length (x) and height (y) values, in master units, for user-specified paper sizes associated with the CUSTOMSIZE option.</p></td>
<td><p>Required for the CUSTOMSIZE option. Portrait orientation is assumed. See [Specifying Paper Sizes](specifying-paper-sizes.md).</p></td>
</tr>
<tr class="odd">
<td><p>*<strong>MaxPrintableWidth</strong></p></td>
<td><p>Numeric value representing the maximum printable width, in x master units, for user-specified paper sizes associated with the CUSTOMSIZE option.</p></td>
<td><p>Required for the CUSTOMSIZE option. Portrait orientation is assumed. See [Specifying Paper Sizes](specifying-paper-sizes.md).</p></td>
</tr>
<tr class="even">
<td><p>*<strong>MinLeftMargin</strong></p></td>
<td><p>Numeric value representing the minimum allowable left margin, in x master units, for user-specified paper sizes associated with the CUSTOMSIZE option. Value is relative to the left edge of the physical page</p></td>
<td><p>Optional. If not specified, the default value is 0. Used only with the CUSTOMSIZE option. Portrait orientation is assumed. See [Specifying Paper Sizes](specifying-paper-sizes.md).</p></td>
</tr>
<tr class="odd">
<td><p>*<strong>MinSize</strong></p></td>
<td><p>PAIR of numeric values representing minimum allowable page length (x) and height (y) values, in master units, for user-specified paper sizes associated with the CUSTOMSIZE option.</p></td>
<td><p>Required for the CUSTOMSIZE option. Portrait orientation is assumed. See [Specifying Paper Sizes](specifying-paper-sizes.md).</p></td>
</tr>
<tr class="even">
<td><p>*<strong>PageDimensions</strong></p></td>
<td><p>PAIR of numeric values representing the page length (x) and height (y) values, in master units, for any customized options for the PaperSize feature.</p></td>
<td><p>Used only for vendor-defined paper sizes. See [Specifying Paper Sizes](specifying-paper-sizes.md).</p></td>
</tr>
<tr class="odd">
<td><p>*<strong>PageProtectMem</strong></p></td>
<td><p>Numeric value representing the amount of printer memory, in kilobytes, required to protect a page.</p></td>
<td><p>Required if the PageProtect feature is specified. See [Specifying Paper Sizes](specifying-paper-sizes.md).</p></td>
</tr>
<tr class="even">
<td><p>*<strong>PrintableArea</strong></p></td>
<td><p>PAIR of numeric values representing the x- and y-plane lengths, in master units, of the printable page area.</p></td>
<td><p>Required for all PaperSize options except CUSTOMSIZE. See [Specifying Paper Sizes](specifying-paper-sizes.md).</p></td>
</tr>
<tr class="odd">
<td><p>*<strong>PrintableOrigin</strong></p></td>
<td><p>PAIR of numeric values representing the origin of the printable area, in master units, relative to the upper left-hand corner of the paper.</p></td>
<td><p>Required for all PaperSize options except CUSTOMSIZE. For CUSTOMSIZE, you can specify these values using *<strong>CustPrintableOriginX</strong> and *<strong>CustPrintableOriginY</strong>.</p></td>
</tr>
<tr class="even">
<td><p>*<strong>RotateSize?</strong></p></td>
<td><p><strong>TRUE</strong> or <strong>FALSE</strong>, indicating whether Unidrv should rotate the page dimensions because the paper (typically envelopes) is fed in sideways.</p></td>
<td><p>Optional. If not specified, the default value is <strong>FALSE</strong>. Can be used with any standard option for the PaperSize feature, except CUSTOMSIZE.</p></td>
</tr>
<tr class="odd">
<td><p>*<strong>TopMargin</strong></p></td>
<td><p>Numeric value representing the minimum allowable top margin, in y master units, for user-specified paper sizes associated with the CUSTOMSIZE option. Value is relative to the top of the physical page.</p></td>
<td><p>Optional. If not specified, the default value is 0. Used only with the CUSTOMSIZE option. Portrait orientation is assumed. See [Specifying Paper Sizes](specifying-paper-sizes.md).</p></td>
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

```
*CustCursorOriginX: %d{((PhysPaperWidth-14040)/2)+300}
*CustCursorOriginY: %d{180}
*CustPrintableOriginX: %d{300}
*CustPrintableOriginY: %d{300}
*CustPrintableSizeX: %d{PhysPaperWidth-600}
*CustPrintableSizeY: %d{PhysPaperLength-600}
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Option%20Attributes%20for%20the%20PaperSize%20Feature%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


