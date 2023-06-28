---
title: Cursor attributes
description: Cursor attributes
keywords:
- cursor attributes WDK Unidrv
- general printer attributes WDK Unidrv , cursor
ms.date: 06/16/2023
---

# Cursor attributes

[!include[Print Support Apps](../includes/print-support-apps.md)]

Cursor attributes are [general printing attributes](general-printing-attributes.md) that specify characteristics of a printer's cursor.

The following table lists the cursor attributes.

| Attribute name | Attribute parameter | Comments |
|--|--|--|
| **AbsXMovesRightOnly?** | **TRUE** or **FALSE**. This parameter is used to specify that a device can accept only absolute move commands that move the current position to the right. If a move to the left of the current position is required, Unidrv first sends a carriage return so that the absolute command that is sent is to the right of the new current position. | Optional. If not specified, the default value is **FALSE**. |
| **BadCursorMoveInGrxMode** | [LIST](lists.md) of values representing illegal cursor movements in raster graphics mode. Can be one or more of:<br><br>X_PORTRAIT<br><br>X_LANDSCAPE<br><br>Y_PORTRAIT<br><br>Y_LANDSCAPE | Optional. If not specified, the default is no restrictions. As an example, LIST(X_PORTRAIT) indicates x-direction movement is not allowed for portrait orientation. |
| **CursorXAfterCR** | One of:<br><br>AT_PRINTABLE_X_ORIGIN<br><br>AT_CURSOR_X_ORIGIN<br><br>Indicates cursor's x-position after a carriage return. | Optional. If not specified, the default value is AT_CURSOR_X_ORIGIN, which is the physical zero position. |
| **EjectPageWithFF?** | **TRUE** or **FALSE**.<br><br>Indicates whether the printer uses form-feed to eject a page. | Optional. If not specified, the default value is **FALSE**. |
| **LineSpacingMoveUnit** | Positive integer value. Specifies the move units for the CmdSetLineSpacing command. Units are expressed in dots per inch. For a printer whose line spacing move unit is 1/60th of an inch, this entry should be 60.<br><br>Note that the line spacing move unit must divide evenly into the master Y unit.<br><br>The *MaxLineSpacing parameter is still in master units independent of whether **\*LineSpacingMoveUnit** is specified. | Optional. The default value is 1 master unit. |
| **MaxLineSpacing** | Numeric value representing the maximum line spacing, in y-master units. | Optional. If not specified, Unidrv assumes there is no maximum value. |
| **UseSpaceForXMove?** | **TRUE** or **FALSE**.<br><br>Indicates whether space characters can be used to perform cursor x-direction movements. | Optional. If not specified, the default value is **TRUE**.<br><br>If **TRUE**, Unidrv uses spaces for coarse moves and NULLs for fine moves. If **FALSE**, Unidrv uses NULLs for all moves. |
| **XMoveThreshold** | Numeric value, in x-master units, representing the movement threshold beyond which **CmdXMoveAbsolute** should be used instead of **CmdXMoveRelLeft** or **CmdXMoveRelRight**. | Optional. If not specified, the default value is zero, meaning **CmdXMoveAbsolute** should always be used. Only applicable if all three x-movement commands are specified. |
| **XMoveUnit** | Numeric value, in dots per inch, representing the smallest horizontal movement the printer is capable of. For example, if the movement unit is 1/600th of an inch, the specified value is 600. | Required if the printer supports horizontal movement [cursor commands](cursor-commands.md). If specified, include this value when calculating [master units](master-units.md). |
| **YMoveAttributes** | LIST of values indicating y-movement attributes. Can be one or more of:<br><br>FAV_LF (favor LF spacing)<br><br>SEND_CR_FIRST | Optional. If not specified, no attributes are assumed. |
| **YMoveThreshold** | Numeric value, in y-master units, representing the movement threshold beyond which **CmdYMoveAbsolute** should be used instead of **CmdYMoveRelLeft** or **CmdYMoveRelRight**. | Optional. If not specified, the default value is zero, meaning **CmdYMoveAbsolute** should always be used. Only applicable if all three y-movement commands are specified. |
| **YMoveUnit** | Numeric value, in dots per inch, representing the smallest vertical movement the printer is capable of. For example, if the movement unit is 1/600th of an inch, the specified value is 600. | Required if the printer supports vertical movement [cursor commands](cursor-commands.md). If specified, include this value when calculating [master units](master-units.md). |

For examples, see the [sample GPD files](sample-gpd-files.md).
