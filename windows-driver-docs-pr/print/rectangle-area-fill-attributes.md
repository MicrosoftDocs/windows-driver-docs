---
title: Rectangle Area Fill Attributes
description: Rectangle Area Fill Attributes
keywords:
- rectangular area fill attributes WDK Unidrv
- filling rectangular areas WDK Unidrv
ms.date: 01/29/2024
---

# Rectangle area fill attributes

[!include[Print Support Apps](../includes/print-support-apps.md)]

The following table lists attributes describing the printer's support for filling rectangle areas.

| Attribute name | Attribute parameter | Comments |
|--|--|--|
| CursorXAfterRectFill | AT_RECT_X_ORIGIN or AT_RECT_X_END, indicating where the cursor's x-coordinate is after the printer fills a rectangle area. | Optional. If not specified, the default value is AT_RECT_X_ORIGIN. |
| CursorYAfterRectFill | AT_RECT_Y_ORIGIN or AT_RECT_Y_END, indicating where the cursor's y-coordinate is after the printer fills a rectangle area. | Optional. If not specified, the default value is AT_RECT_Y_ORIGIN. |
| MaxGrayFill | Numeric value representing the maximum gray fill percentage allowed as an argument to the CmdRectGrayFill command. | Optional. If not specified, the default value is 100 (percent). |
| MinGrayFill | Numeric value representing the minimum gray fill percentage allowed as an argument to the CmdRectGrayFill command. | Optional. If not specified, the default value is 1 (percent). |

For information about commands associated with a printer's rectangle area fill capabilities, see [Rectangle area fill commands](rectangle-area-fill-commands.md).

For GPD examples, see [Sample GPD files](sample-gpd-files.md).
