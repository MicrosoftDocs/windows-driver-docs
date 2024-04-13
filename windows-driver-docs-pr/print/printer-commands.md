---
title: Printer Commands
description: Printer Commands
keywords:
- Unidrv, commands
- GPD files WDK Unidrv , printer commands
- commands WDK Unidrv
- printer commands WDK Unidrv
- printer commands WDK Unidrv , about printer commands
- Unidrv WDK print
ms.date: 01/30/2023
---

# Printer Commands

[!include[Print Support Apps](../includes/print-support-apps.md)]

The GPD language provides a predefined command name for each commonly used printer operation. Additionally, customized commands can be defined for device-specific [printer options](printer-options.md).

Each printer command can be implemented in either of two ways:

- You can place a device-specific command string in a GPD file. Unidrv sends the command string to the print spooler at the appropriate time.

- You can implement the [**IPrintOemUni::CommandCallback**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-commandcallback) COM method, which dynamically generates a command string. Unidrv calls the method whenever it has to send the command to the spooler. For more information see [Dynamically Generated Printer Commands](dynamically-generated-printer-commands.md) in [Customizing Microsoft's Printer Drivers](customizing-microsoft-s-printer-drivers.md).

The following topics describe how to specify printer commands in GPD files:

[Command Entry Format](command-entry-format.md)

[Command Names](command-names.md)

[Command Attributes](command-attributes.md)

[Command String Format](command-string-format.md)

[Command Execution Order](command-execution-order.md)
