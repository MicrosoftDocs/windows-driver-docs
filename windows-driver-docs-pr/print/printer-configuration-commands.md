---
title: Printer configuration commands
description: Printer configuration commands
keywords:
- printer commands WDK Unidrv , configuration
- configuration commands WDK Unidrv
ms.date: 07/19/2023
---

# Printer configuration commands

[!include[Print Support Apps](../includes/print-support-apps.md)]

The following table lists the printer configuration commands. All commands are specified using the [command entry format](command-entry-format.md).

| Command | Description | Comments |
|--|--|--|
| CmdStartJob | Command to initialize a print job. | Optional. [Command execution order](command-execution-order.md)> must be specified. |
| CmdStartDoc | Command to initialize a document. | Optional. [Command execution order](command-execution-order.md) must be specified. |
| CmdStartPage | Command to initialize a page and set the cursor position to (0,0) in cursor coordinates. | Optional. [Command execution order](command-execution-order.md) must be specified. |
| CmdEndPage | Command to finish printing a page. | Optional. [Command execution order](command-execution-order.md) must be specified. |
| CmdEndDoc | Command to finish printing a document. | Optional. [Command execution order](command-execution-order.md) must be specified. |
| CmdEndJob | Command to complete a print job. | Optional. [Command execution order](command-execution-order.md) must be specified. |
| CmdCopies | Command to specify the number of copies to print. | Optional. [Command execution order](command-execution-order.md) must be specified. |
| CmdSleepTimeOut | Command to specify the number of minutes for the printer to wait before entering power-save mode. | Optional. [Command execution order](command-execution-order.md) must be specified. |

For examples, see the [sample GPD files](sample-gpd-files.md).
