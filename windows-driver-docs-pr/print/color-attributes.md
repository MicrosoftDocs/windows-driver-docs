---
title: Color attributes
description: Provides information about color attributes.
keywords:
- color attributes WDK Unidrv
- general printer attributes WDK Unidrv, color
ms.date: 01/26/2023
---

# Color attributes

[!include[Print Support Apps](../includes/print-support-apps.md)]

Color attributes are [general printing attributes](general-printing-attributes.md) that specify characteristics for controlling color printing.

The following table lists the color attributes.

| Attribute name | Attribute parameter | Comments |
|--|--|--|
| **ChangeColorModeOnDoc?** | **TRUE** or **FALSE**. Indicates whether a printer's color mode can be changed between pages of a document without side effects. | Optional. If not specified, the default value is **TRUE**. Unidrv uses this value to optimize printing speed. For more information, see the text following this table. |
| **CyanInMagentaDye** | Numeric value, from 0 to 1000, indicating the percentage of cyan contamination in magenta dye. The value is the contamination percentage times 100. For example, 8.4% contamination is specified as 840 and 10% is 1000. | Optional. If not specified, a Unidrv-supplied default value is used. |
| **CyanInYellowDye** | Numeric value, from 0 to 1000, indicating the percentage of cyan contamination in yellow dye. The value is the contamination percentage times 100. For example, 8.4% contamination is specified as 840 and 10% is 1000. | Optional. If not specified, a Unidrv-supplied default value is used. |
| **EnableGDIColorMapping** | **TRUE** or **FALSE**. Indicates whether GDI should perform gamut mapping from display to printer color space. | Optional. If not specified, the default value is **FALSE**. If **TRUE**, Unidrv sets the HT_FLAG_DO_DEVCLR_XFORM flag in the [**GDIINFO**](/windows/win32/api/winddi/ns-winddi-gdiinfo) structure. |
| **MagentaInCyanDye** | Numeric value, from 0 to 1000, indicating the percentage of magenta contamination in cyan dye. The value is the contamination percentage times 100. For example, 8.4% contamination is specified as 840 and 10% is 1000. | Optional. If not specified, a Unidrv-supplied default value is used. |
| **MagentaInYellowDye** | Numeric value, from 0 to 1000, indicating the percentage of magenta contamination in yellow dye. The value is the contamination percentage times 100. For example, 8.4% contamination is specified as 840 and 10% is 1000. | Optional. If not specified, a Unidrv-supplied default value is used. |
| **YellowInCyanDye** | Numeric value, from 0 to 1000, indicating the percentage of yellow contamination in cyan dye. The value is the contamination percentage times 100. For example, 8.4% contamination is specified as 840 and 10% is 1000. | Optional. If not specified, a Unidrv-supplied default value is used. |
| **YellowInMagentaDye** | Numeric value, from 0 to 1000, indicating the percentage of yellow contamination in magenta dye. The value is the contamination percentage times 100. For example, 8.4% contamination is specified as 840 and 10% is 1000. | Optional. If not specified, a Unidrv-supplied default value is used. |

When the **\*ChangeColorModeOnDoc?** color attribute is set to **TRUE**, color optimization is enabled. When this attribute is set to **FALSE**, no optimization is performed. When color optimization is enabled, color in the spool file causes the spool file to be played in color. The lack of color in the spool file causes the spool file to be played in monochrome.

If you're creating a Unidrv rendering plug-in to generate color watermarks, color optimization causes color watermarks to be printed in black and white when they're printed on black-and-white documents. To ensure that color watermarks print correctly with color and black-and-white documents, disable color optimization.

The color optimization controlled by the **\*ChangeColorModeOnDoc?** color attribute can also be controlled by setting the **dwColorOptimization** member of the [**ATTRIBUTE_INFO_2**](/windows-hardware/drivers/ddi/winddiui/ns-winddiui-_attribute_info_2) or [**ATTRIBUTE_INFO_3**](/windows-hardware/drivers/ddi/winddiui/ns-winddiui-_attribute_info_3) structures. Color optimization also can be controlled by using the [**GdiEndPageEMF**](/windows-hardware/drivers/ddi/winppi/nf-winppi-gdiendpageemf) function.

For examples of the color attributes listed on this page, see the [sample GPD files](sample-gpd-files.md).
