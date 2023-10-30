---
title: Option attributes for the Halftone feature
description: Option attributes for the Halftone feature
keywords:
- Halftone Feature
ms.date: 07/19/2023
---

# Option attributes for the Halftone feature

[!include[Print Support Apps](../includes/print-support-apps.md)]

The following table lists the attributes associated with the Halftone feature. For more information about the Halftone feature, see [Standard Features](standard-features.md).

| Attribute name | Attribute parameter | Comments |
|--|--|--|
| \***HTCallbackID** | Positive numeric value passed to the rendering plug-in's [**IPrintOemUni::HalftonePattern**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-halftonepattern) method as its *dwCallbackID* parameter. | Required if an **IPrintOemUni::HalftonePattern** method is provided. For more information, see [Halftoning with Unidrv](halftoning-with-unidrv.md). |
| \***HTNumPatterns** | Numeric value representing the number of halftone patterns provided. For more information, see [Halftoning with Unidrv](halftoning-with-unidrv.md). | Optional. Can be 1 or 3, where 3 implies separate patterns for red, green, and blue, in that order. If not specified, the default value is 1. Can be used with either \***rcHTPatternID** or \***HTCallbackID**. |
| \***HTPatternSize** | [Pair](pairs.md) of numeric values representing the width and height, in pixels, of the pattern specified by \***rcHTPatternID**. | Required if \***rcHTPatternID** is specified. The maximum pattern size is PAIR (256, 256). Width and height, multiplied together, must be divisible by 4 for storage as DWORDs |
| \***rcHTPatternID** | Resource identifier for an RC_HTPATTERN resource representing halftone pattern data. | Required if a halftone pattern is provided in a resource DLL. For more information, see [Halftoning with Unidrv](halftoning-with-unidrv.md). |

For examples, see the [sample GPD files](sample-gpd-files.md).

For more information about using these attributes, see [Halftoning with Unidrv](halftoning-with-unidrv.md). These attributes are not used with [minidriver-supplied halftoning](minidriver-supplied-halftoning.md).
