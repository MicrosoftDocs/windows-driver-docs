---
title: Option attributes for the PaperSize feature
description: Option attributes for the PaperSize feature
keywords:
- PaperSize Feature
ms.date: 07/19/2023
---

# Option attributes for the PaperSize feature

[!include[Print Support Apps](../includes/print-support-apps.md)]

The following table lists the attributes associated with the PaperSize feature. For more information about the PaperSize feature, see [Standard Features](standard-features.md).

All paper size specifications for the following attributes must be expressed relative to PORTRAIT orientation, even if the attributes are being used to describe a different orientation, such as LANDSCAPE.

| Attribute name | Attribute parameter | Comments |
|--|--|--|
| \***BottomMargin** | Numeric value representing the minimum allowable bottom margin, in x master units, for user-specified paper sizes associated with the CUSTOMSIZE option. Value is relative to the bottom of the physical page. | Optional. If not specified, the default value is 0. Used only with the CUSTOMSIZE option. Portrait orientation is assumed. For more information, see [Specifying Paper Sizes](specifying-paper-sizes.md). |
| \***CenterPrintable?** | **TRUE** or **FALSE**, indicating whether the value specified by \***MaxPrintableWidth** is centered. | Optional. If not specified, the printable area is to the right of the margin specified by \***MinLeftMargin**. Used only with the CUSTOMSIZE option. For more information, see [Specifying Paper Sizes](specifying-paper-sizes.md). |
| \***CursorOrigin** | PAIR of numeric values representing the cursor origin position, in master units, where PAIR (0, 0) is the upper left corner. Alternatively for CUSTOMSIZE, specify these values using \***CustCursorOriginX** and \***CustCursorOriginY**. | Optional. If not specified, the default value is PAIR (0, 0). Unidrv assumes the cursor origin, relative to the printer, is constant with different paper sizes. |
| \***CustCursorOriginX** | CUSTOMSIZE parameter expression, used to create a value for the x index of \***CursorOrigin**. | Optional. Use only with the CUSTOMSIZE option. For more information, see [Specifying Paper Sizes](specifying-paper-sizes.md). |
| \***CustCursorOriginY** | CUSTOMSIZE parameter expression, used to create a value for the y index of \***CursorOrigin**. | Optional. Use only with the CUSTOMSIZE option. For more information, see [Specifying Paper Sizes](specifying-paper-sizes.md). |
| \***CustPrintableOriginX** | CUSTOMSIZE parameter expression, used to create a value for the x index of \***PrintableOrigin**. | Optional. Use only with the CUSTOMSIZE option. For more information, see [Specifying Paper Sizes](specifying-paper-sizes.md). |
| \***CustPrintableOriginY** | CUSTOMSIZE parameter expression, used to create a value for the y index of \***PrintableOrigin**. | Optional. Use only with the CUSTOMSIZE option. For more information, see [Specifying Paper Sizes](specifying-paper-sizes.md). |
| \***CustPrintableSizeX** | CUSTOMSIZE parameter expressions, used to create a value for the x value of \***PrintableArea**. | Optional. Use only with the CUSTOMSIZE option. For more information, see [Specifying Paper Sizes](specifying-paper-sizes.md). |
| \***CustPrintableSizeY** | CUSTOMSIZE parameter expression, used to create a value for the y value of \***PrintableArea**. | Optional. Use only with the CUSTOMSIZE option. For more information, see [Specifying Paper Sizes](specifying-paper-sizes.md). |
| \***MaxSize** | PAIR of numeric values representing maximum allowable page length (x) and height (y) values, in master units, for user-specified paper sizes associated with the CUSTOMSIZE option. | Required for the CUSTOMSIZE option. Portrait orientation is assumed. For more information, see [Specifying Paper Sizes](specifying-paper-sizes.md). |
| \***MaxPrintableWidth** | Numeric value representing the maximum printable width, in x master units, for user-specified paper sizes associated with the CUSTOMSIZE option. | Required for the CUSTOMSIZE option. Portrait orientation is assumed. For more information, see [Specifying Paper Sizes](specifying-paper-sizes.md). |
| \***MinLeftMargin** | Numeric value representing the minimum allowable left margin, in x master units, for user-specified paper sizes associated with the CUSTOMSIZE option. Value is relative to the left edge of the physical page. | Optional. If not specified, the default value is 0. Used only with the CUSTOMSIZE option. Portrait orientation is assumed. For more information, see [Specifying Paper Sizes](specifying-paper-sizes.md). |
| \***MinSize** | PAIR of numeric values representing minimum allowable page length (x) and height (y) values, in master units, for user-specified paper sizes associated with the CUSTOMSIZE option. | Required for the CUSTOMSIZE option. Portrait orientation is assumed. For more information, see [Specifying Paper Sizes](specifying-paper-sizes.md). |
| \***PageDimensions** | PAIR of numeric values representing the page length (x) and height (y) values, in master units, for any customized options for the PaperSize feature. | Used only for vendor-defined paper sizes. For more information, see [Specifying Paper Sizes](specifying-paper-sizes.md). |
| \***PageProtectMem** | Numeric value representing the amount of printer memory, in kilobytes, required to protect a page. | Required if the PageProtect feature is specified. For more information, see [Specifying Paper Sizes](specifying-paper-sizes.md). |
| \***PrintableArea** | PAIR of numeric values representing the x- and y-plane lengths, in master units, of the printable page area. | Required for all PaperSize options except CUSTOMSIZE. For more information, see [Specifying Paper Sizes](specifying-paper-sizes.md). |
| \***PrintableOrigin** | PAIR of numeric values representing the origin of the printable area, in master units, relative to the upper left-hand corner of the paper. | Required for all PaperSize options except CUSTOMSIZE. For CUSTOMSIZE, you can specify these values using \***CustPrintableOriginX** and \***CustPrintableOriginY**. |
| \***RotateSize?** | **TRUE** or **FALSE**, indicating whether Unidrv should rotate the page dimensions because the paper (typically envelopes) is fed in sideways. | Optional. If not specified, the default value is **FALSE**. Can be used with any standard option for the PaperSize feature, except CUSTOMSIZE. |
| \***TopMargin** | Numeric value representing the minimum allowable top margin, in y master units, for user-specified paper sizes associated with the CUSTOMSIZE option. Value is relative to the top of the physical page. | Optional. If not specified, the default value is 0. Used only with the CUSTOMSIZE option. Portrait orientation is assumed. For more information, see [Specifying Paper Sizes](specifying-paper-sizes.md). |

For examples, see the [sample GPD files](sample-gpd-files.md).

## CUSTOMSIZE Parameter Expressions

CUSTOMIZE parameter expressions are a restricted form of the [command string format](command-string-format.md). Text strings are not allowed.

Within the expression's **ArgumentType** segment, the following restrictions apply:

- The only **ArgumentType** value allowed is %d.

- Bracketed value ranges are not allowed.

Within the expression's **StandardVariableExpression** segment, the following restrictions apply:

- Only the PhysPaperWidth and PhysPaperLength standard variables can be used.

- The **Max_Repeat** operator is not allowed.

Following are example expressions:

```GPD
*CustCursorOriginX: %d{((PhysPaperWidth-14040)/2)+300}
*CustCursorOriginY: %d{180}
*CustPrintableOriginX: %d{300}
*CustPrintableOriginY: %d{300}
*CustPrintableSizeX: %d{PhysPaperWidth-600}
*CustPrintableSizeY: %d{PhysPaperLength-600}
```
