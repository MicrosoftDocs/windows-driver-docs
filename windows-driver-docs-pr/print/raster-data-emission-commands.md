---
title: Raster Data Emission Commands
description: Raster Data Emission Commands
keywords:
- data emission raster printing commands WDK Unidrv
- emission raster printing commands WDK Unidrv
ms.date: 01/29/2024
---

# Raster data emission commands

[!include[Print Support Apps](../includes/print-support-apps.md)]

The following table lists the raster data emission commands. All commands are specified using the [command entry format](command-entry-format.md).

| Command | Description | Comments |
|--|--|--|
| CmdBeginRaster | Command to initialize a raster data transfer. | Optional. If not specified, Unidrv assumes no initialization is needed. |
| CmdEndRaster | Command to complete a raster data transfer. | Optional. If not specified, Unidrv assumes no transfer-completion operations are needed. |
| CmdSetDestBmpHeight | Command to set the height of a destination bitmap. | Optional. Applicable only if the printer supports scalable bitmaps. |
| CmdSetDestBmpWidth | Command to set the width of a destination bitmap. |Optional. Applicable only if the printer supports scalable bitmaps. |
| CmdSetSrcBmpHeight | Command to set the height of a source bitmap. | Optional. Applicable only if the printer supports scalable bitmaps. |
| CmdSetSrcBmpWidth | Command to set the width of a source bitmap. | Optional. Applicable only if the printer supports scalable bitmaps. |
| CmdSendBlockData | Command to deliver a block of data to the printer. | Required. If **OutputDataFormat** is V_BYTE, a block contains the data for one physical pass of the print head (see [PinsPerPhysPass](/windows-hardware/drivers/print/option-attributes-for-the-resolution-feature)). If *OutputDataFormat is H_BYTE, a block contains the data for one logical pass of the print head (see [PinsPerLogPass](/windows-hardware/drivers/print/option-attributes-for-the-resolution-feature)). |
| CmdEndBlockData | Command to indicate the end of a block of data that was sent using the CmdSendBlockData command. | Optional. If not specified, Unidrv assumes no command is needed to indicate the end of a block (used by some dot-matrix printers) |
| CmdSendBlackData | Command to deliver black plane data to the printer. | Required if **UseExpColorSelectCmd?** attribute is **FALSE**. |
| CmdSendBlueData | Command to deliver blue plane data to the printer. | Required if **UseExpColorSelectCmd?** attribute is **FALSE**. |
| CmdSendCyanData | Command to deliver cyan plane data to the printer. | Required if **UseExpColorSelectCmd?** attribute is **FALSE**. |
| CmdSendGreenData | Command to deliver green plane data to the printer. | Required if **UseExpColorSelectCmd?** attribute is **FALSE**. |
| CmdSendMagentaData | Command to deliver magenta plane data to the printer. | Required if **UseExpColorSelectCmd?** attribute is **FALSE**. |
| CmdSendRedData | Command to deliver red plane data to the printer. | Required if **UseExpColorSelectCmd?** attribute is **FALSE**. |
| CmdSendYellowData | Command to deliver yellow plane data to the printer. | Required if **UseExpColorSelectCmd?** attribute is **FALSE**. |

For GPD examples, see [Sample GPD files](sample-gpd-files.md).
