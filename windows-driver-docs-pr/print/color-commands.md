---
title: Color commands
description: Provides information about color commands for printing.
keywords:
- printer commands WDK Unidrv, colors
- color commands WDK Unidrv
- background color options WDK Unidrv
- palettes WDK Unidrv
- patterns WDK Unidrv
- brushes WDK Unidrv
ms.date: 09/09/2022
---

# Color commands

This topic describes the color commands for printing, and it contains the following sections:

- Commands for selecting primary background colors

- Commands for controlling printer palettes

- Commands for selecting pattern brushes

All commands are specified using the [command entry format](command-entry-format.md).

## Commands for selecting primary background colors

The [printer commands](printer-commands.md) in the following table are used by printers that do not support programmable color palettes, such as planar color printers (for example, dot matrix printers) and some palette printers (for example, early ink jet printers).

| Command | Description | Comments |
|--|--|--|
| **CmdSelectBlackColor** | Command to select black background color. | Optional |
| **CmdSelectBlueColor** | Command to select blue background color. | Optional |
| **CmdSelectCyanColor** | Command to select background cyan color. | Optional |
| **CmdSelectGreenColor** | Command to select green background color. | Optional |
| **CmdSelectMagentaColor** | Command to select magenta background color. | Optional |
| **CmdSelectRedColor** | Command to select red background color. | Optional |
| **CmdSelectYellowColor** | Command to select yellow background color. | Optional |
| **CmdSelectWhiteColor** | Command to select background white color. | Optional |

For examples, see the [sample GPD files](sample-gpd-files.md).

## Commands for controlling printer palettes

The [printer commands](printer-commands.md) in the following table are used by printers that support programmable palettes for both foreground (text and vector) printing and for raster printing.

| Command | Description | Comments |
|--|--|--|
| **CmdBeginPaletteDef** | Command to initialize a color palette definition. | Optional. If not specified, no initialization of palette definitions is needed. |
| **CmdEndPaletteDef** | Command to end a palette definition. | Optional. If not specified, no command is required to end a palette definition.<br><br>The Order attribute can be specified. If it is not, the **Order** attribute associated with the most recently executed [option selection command](option-selection-command.md) for the ColorMode feature is used. |
| **CmdBeginPaletteReDef** | Command to initialize a color palette redefinition. | Optional. If not specified, no initialization of palette redefinitions is needed. |
| **CmdEndPaletteReDef** | Command to end a palette redefinition. | Optional. If not specified, no command is required to end a palette redefinition. |
| **CmdDefinePaletteEntry** | Command to define a palette entry. | Required if the printer supports palettes.<br><br>In 24 BPP mode, Unidrv allows palettes for which **PaletteSize** is 1.<br><br>This allows GPD developers to implement a direct RGB color selection command for their devices. To do so, set **PaletteSize** to 1, and specify the selection color command in the **CmdDefinePaletteEntry** command. The **CmdSelectPaletteEntry** command must also be specified but can be defined as a **NULL** command. |
| **CmdRedefinePaletteEntry** | Command to redefine a palette entry. | Optional. If not specified, **CmdDefinePaletteEntry** is used to redefined palette entries. |
| **CmdSelectPaletteEntry** | Command to select a palette entry as the current color. | Required if the printer supports palettes. |

For examples, see the [sample GPD files](sample-gpd-files.md).

## Commands for selecting pattern brushes

The [printer commands](printer-commands.md) in the following table are used by printers that support downloading and selecting pattern brushes.

| Command | Description | Comments |
|--|--|--|
| **CmdDownloadPattern** | Command to deliver a brush pattern to the printer. | Optional. If specified, **CmdSelectPattern** must also be specified. |
| **CmdSelectBlackBrush** | Command to a solid black brush as the current brush. | Required if the printer supports brushes. |
| **CmdSelectPattern** | Command to select a downloaded brush pattern. | Optional. If specified, **CmdDownloadPattern** must also be specified. |
| **CmdSelectWhiteBrush** | Command to select a solid white brush as the current brush. | Optional |
