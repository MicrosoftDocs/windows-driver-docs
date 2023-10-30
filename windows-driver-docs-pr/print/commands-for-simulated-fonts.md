---
title: Commands for Simulated Fonts
description: Commands for Simulated Fonts
keywords:
- simulated font commands WDK Unidrv
- font commands WDK Unidrv
ms.date: 01/26/2023
---

# Commands for Simulated Fonts

[!include[Print Support Apps](../includes/print-support-apps.md)]

The following table lists the commands for controlling simulated fonts. All commands are specified using the [command entry format](command-entry-format.md).

| Command | Description | Comments |
|---|---|---|
| **CmdBoldOff** | Command to disable bolding. | Optional. Must be specified if **CmdBoldOn** is specified. |
| **CmdBoldOn** | Command to enable bolding. | Optional. If specified, Unidrv sends this command to enable bolding and sends **CmdBoldOff** to disable bolding. |
| **CmdClearAllFontAttribs** | Single command to disable bold, italic, and underline capabilities. | Optional. Can be specified if the printer supports bold, italic, or underlining, but supports only a single command to disable them all. Use instead of **CmdBoldOff**, **CmdItalicOff** and **CmdUnderlineOff**. |
| **CmdItalicOff** | Command to disable italics. | Optional. Must be specified if **CmdItalicOn** is specified. |
| **CmdItalicOn** | Command to enable italics. | Optional. If specified, Unidrv sends this command to enable italics and sends **CmdItalicOff** to disable italics. |
| **CmdSelectDoubleByteMode** | Command to enable double-byte printing. | Optional. Must be specified if **CmdSelectSingleByteMode** is specified. |
| **CmdSelectSingleByteMode** | Command to enable single-byte printing. | Optional. Must be specified if the printer can be switched between single-byte and double-byte modes. |
| **CmdSetFontSim** | Single command to set bold, italic, underline, and strike-through capabilities. | Optional. Must be specified if font characteristics must be set each time the font is used (for printers that do not store font characteristics). |
| **CmdStrikeThruOff** | Command to disable strike-through. | Optional. Must be specified if **CmdStrikeThruOn** is specified. |
| **CmdStrikeThruOn** | Command to enable strike-through. | Optional. If specified, Unidrv sends this command to enable strike-through and sends **CmdStrikeThruOff** to disable strike-through. |
| **CmdUnderlineOff** | Command to disable underlining. | Optional. Must be specified if **CmdUnderlineOn** is specified. |
| **CmdUnderlineOn** | Command to enable underlining. | Optional. If specified, Unidrv sends this command to enable underlining and sends **CmdUnderlineOff** to disable underlining. |
| **CmdVerticalPrintingOff** | Command to disable vertical printing. | Optional. Must be specified if **CmdVerticalPrintingOn** is specified. |
| **CmdVerticalPrintingOn** | Command to enable vertical printing. | Optional. Must be specified if the printer supports vertical printing. |
| **CmdWhiteTextOff** | Command to disable printing white text. | Optional. Must be specified if **CmdWhiteTextOn** is specified. |
| **CmdWhiteTextOn** | Command to enable printing white text. | Optional. If specified, Unidrv sends this command to enable printing white text and sends **CmdWhiteTextOff** to disable printing white text. (This command is provided for backwards compatibility with GPC 3.0.) |

For examples, see the [sample GPD files](sample-gpd-files.md).
