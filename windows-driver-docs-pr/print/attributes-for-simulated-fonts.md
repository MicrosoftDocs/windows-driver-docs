---
title: Attributes for simulated fonts
description: Provides information about attributes for simulated fonts.
keywords:
- simulated font attributes WDK Unidrv
- font attributes WDK Unidrv
ms.date: 01/26/2023
---

# Attributes for simulated fonts

[!include[Print Support Apps](../includes/print-support-apps.md)]

The following table lists attributes describing the printer's support for simulated fonts.

| Attribute name | Attribute parameter | Comments |
|--|--|--|
| **\*DiffFontsPerByteMode?** | **TRUE** or **FALSE**. For printers supporting both single-byte and double-byte modes, this indicates whether the printer maintains separate fonts and font characteristics for each mode. | Optional. If not specified, the default value is **FALSE**. |

For examples, see the [sample GPD files](sample-gpd-files.md).
