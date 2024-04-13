---
title: Rectangle Area Fill Commands
description: Rectangle Area Fill Commands
keywords:
- rectangular area fill commands WDK Unidrv
- filling rectangular areas WDK Unidrv
ms.date: 01/29/2024
---

# Rectangle area fill commands

[!include[Print Support Apps](../includes/print-support-apps.md)]

The following table lists the rectangle area fill commands. All commands are specified using [command entry format](command-entry-format.md).

| Command | Description | Comments |
|--|--|--|
| CmdRectBlackFill | Command to black fill a rectangle. | Optional. If not specified, Unidrv attempts black fill by specifying the CmdRectGrayFill command with a gray percentage of **MaxGrayFill**. |
| CmdRectGrayFill | Command to gray fill a rectangle (does not erase the background). | Optional. If not specified, Unidrv assumes no gray fill capability. Command string typically includes the GrayPercentage variable. |
| CmdRectWhiteFill | Command to white fill a rectangle (erases the background). | Optional. If not specified, Unidrv assumes no erasing white fill. In that case, Unidrv returns failure if an application requests white fill, because gray fill cannot erase the background. |
| CmdSetRectHeight | Command to set the rectangle height. | Optional. Must be specified if CmdSetRectWidth is specified. |
| CmdSetRectWidth | Command to set the rectangle width. | Optional. Must be specified if CmdSetRectHeight is specified. |

For GPD examples, see [Sample GPD files](sample-gpd-files.md).
