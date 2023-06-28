---
title: Cursor commands
description: Cursor commands
keywords:
- printer commands WDK Unidrv , cursors
- cursor commands WDK Unidrv
ms.date: 06/16/2023
---

# Cursor commands

[!include[Print Support Apps](../includes/print-support-apps.md)]

The [printer commands](printer-commands.md) in the following table control cursor movement. All commands are specified using the [command entry format](command-entry-format.md).

| Command | Description | Comments |
|--|--|--|
| **CmdBackSpace** | Command to move the cursor back over the last printed character. | Optional. Used only for overstriking. |
| **CmdCR** | Command to move the cursor to its left-most x-position. | Required. |
| **CmdFF** | Command to eject a page. | Required. |
| **CmdLF** | Command to move the cursor to the next line. | Required. Amount of movement is specified by **CmdSetLineSpacing**. |
| **CmdPopCursor** | Command to pop the last saved cursor position from the stack. | Required if **CmdPushCursor** is specified. |
| **CmdPushCursor** | Command to push the current cursor position onto the stack. | Optional. |
| **CmdSetAnyRotation** | Command to set the rotation to an arbitrary angle (measured in degrees in the counterclockwise direction). | Optional. If not present, the printer does not support rotation through arbitrary angles. |
| **CmdSetLineSpacing** | Command to set the distance the cursor moves when a **CmdLF** command is issued. | Optional. |
| **CmdSetSimpleRotation** | Command to set the rotation angle in multiples of 90 degrees in the counterclockwise direction. | Optional. If the printer supports rotations through angles of arbitrary sizes, the **CmdSetAnyRotation** command can replace this command. |
| **CmdUniDirectionOff** | Command to disable unidirectional printing, thereby enabling bidirectional printing. | Optional. |
| **CmdUniDirectionOn** | Command to enable unidirectional printing. | Optional. If not present, print in bidirectional mode. |
| **CmdXMoveAbsolute** | Command to move the cursor to an absolute x-position. | Optional. The command string can include only one standard variable, which is used to specify the distance. |
| **CmdXMoveRelLeft** | Command to move the cursor to the left from the current x-position, by the specified amount. | Optional. The command string can include only one standard variable, which is used to specify the distance. |
| **CmdXMoveRelRight** | Command to move the cursor to the right from the current x-position, by the specified amount. | Optional. The command string can include only one standard variable, which is used to specify the distance. |
| **CmdYMoveAbsolute** | Command to move the cursor to an absolute y-position. | Optional. The command string can include only one standard variable, which is used to specify the distance. |
| **CmdYMoveRelDown** | Command to move the cursor down from the current y-position, by the specified amount. | Optional. The command string can include only one standard variable, which is used to specify the distance. |
| **CmdYMoveRelUp** | Command to move the cursor up from the current y-position, by the specified amount. | Optional. The command string can include only one standard variable, which is used to specify the distance. |

For examples, see the [sample GPD files](sample-gpd-files.md).
