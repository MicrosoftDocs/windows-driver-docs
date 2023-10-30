---
title: Commands for Downloaded Fonts
description: Commands for Downloaded Fonts
keywords:
- downloaded font commands WDK Unidrv
- font commands WDK Unidrv
ms.date: 01/26/2023
---

# Commands for Downloaded Fonts

[!include[Print Support Apps](../includes/print-support-apps.md)]

The following table lists the commands for controlling downloaded fonts. All commands are specified using the [command entry format](command-entry-format.md).

| Command | Description | Comments |
|---|---|---|
| **CmdDeleteFont** | Command to delete a soft font by specifying its identifier. | Optional. Specify this command only if a deleted font's allocated memory can be immediately reclaimed. |
| **CmdDeselectFontID** | Command to deselect the current font ID in order to make the font inactive. | Optional. If not present, the current font does not need to be deselected when a new font is selected. |
| **CmdSelectFontHeight** | Command to select the height of a downloaded font. | Optional. If not present, the printer does not support scalable, downloadable True Type outline fonts. This command is needed for HPPCL_OUTLINE format. |
| **CmdSelectFontID** | Command to select the current font ID in order to make the font active. | Required if the printer supports downloaded fonts. |
| **CmdSelectFontWidth** | Command to select the width of a downloaded font. | Optional. If not present, the width of the downloaded font is scaled proportionally its height. |
| **CmdSetCharCode** | Command to specify the character code of the next character to be downloaded or deleted. | Required if the printer supports downloaded fonts. |
| **CmdSetFontID** | Command to set the current font ID. | Required if the printer supports downloaded fonts. |

For examples, see the [sample GPD files](sample-gpd-files.md).
