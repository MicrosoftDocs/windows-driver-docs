---
title: Command attributes
description: Command attributes
keywords:
- printer attributes WDK Unidrv , commands
- commands WDK Unidrv
- printer commands WDK Unidrv , attributes
- CallbackID
- Cmd
- NoPageEject
- Order
- Params
ms.date: 06/16/2023
---

# Command attributes

[!include[Print Support Apps](../includes/print-support-apps.md)]

When specifying a printer command, you use attributes to provide Unidrv with the following information:

- The escape sequence that causes the hardware to perform the operation, if the operation is implemented in printer hardware.

- The callback identifier and parameters required by the [**IPrintOemUni::CommandCallback**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-commandcallback) method, if the operation is implemented in a [rendering plug-in](rendering-plug-ins.md).

- The order in which the command should be sent, relative to other commands.

The following table lists the command attributes in alphabetic order and describes their parameters.

| Attribute name | Attribute parameter | Comments |
|--|--|--|
| ***CallbackID*** | Positive numeric value, passed to the rendering plug-in's [**IPrintOemUni::CommandCallback**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-commandcallback) method as its *dCmdCbID* argument. | Required for [dynamically generated printer commands](dynamically-generated-printer-commands.md). Not valid if ***Cmd*** is specified. |
| ***Cmd*** | Text string containing a printer command escape sequence, specified using the [command string format](command-string-format.md). | Required unless ***CallbackID*** is specified. |
| ***NoPageEject?*** | **TRUE** or **FALSE**, indicating whether executing the command causes the printer to eject the current physical page.<br><br>Used only if ***Order*** specifies the DOC_SETUP section and if DUPLEX printing is enabled. To avoid premature page ejection between duplexed document pages, Unidrv only issues commands with this attribute set to **TRUE**, if possible. | Optional. If not specified, the default value is **FALSE**, meaning the command might cause page ejection.<br><br>Must not be **TRUE** if a command causes side effects (that is, if the command modifies printer settings outside of those controlled by commands with ***NoPageEject?*** set to **TRUE**). |
| ***Order*** | Section name and order number, as described in [Command Execution Order](command-execution-order.md). | Valid only with configuration commands and customized option commands, unless stated in the command description. |
| ***Params*** | [List](lists.md) of [standard variables](standard-variables.md), passed to the rendering plug-in's IPrintOemUni::CommandCallback method in the **EXTRAPARAM** structure that is passed as its *pdwParams* argument. | Valid only if ***CallbackID*** is also specified. |

For examples, see the [sample GPD files](sample-gpd-files.md).
