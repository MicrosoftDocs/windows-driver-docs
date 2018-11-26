---
title: Dynamically Generated Printer Commands
description: Dynamically Generated Printer Commands
ms.assetid: ba395716-6906-4f23-a050-79d808ccd44b
keywords:
- Unidrv, dynamically generated commands
- dynamically generated print commands WDK Unidrv
- GPD files WDK Unidrv
- Unidrv WDK print
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Dynamically Generated Printer Commands





Each time you specify a [printer command](printer-commands.md) in a [*GPD*](https://msdn.microsoft.com/library/windows/hardware/ff556283#wdkgloss-generic-printer-description--gpd-) file for a Unidrv minidriver, you can use one of the following two methods:

-   Place the command string in the GPD file.

    When you place the command string in a GPD file, Unidrv sends the command to the print spooler at the appropriate time. These command strings can include standard variables, which Unidrv evaluates before sending the command.

-   Provide a callback function.

    If you provide a callback function, Unidrv calls the function when it is time to send the command, and the function is responsible to send the command to the print spooler. This enables you to include the code that dynamically generates a command string and then sends it to the printer.

To place a command string in a GPD file, you need to include a \*Cmd attribute within the command's \*Command entry.

To provide code that dynamically generates a command string, you must do the following:

-   Provide a rendering plug-in that implements the [**IPrintOemUni::CommandCallback**](https://msdn.microsoft.com/library/windows/hardware/ff554216) method.

-   Include a \*CallbackID command attribute and, optionally, a \*Params attribute, within the command's \*Command entry in the GPD file.

When Unidrv is ready to issue a printer command, it checks the minidriver database to determine if the command has been specified with a \*Cmd attribute or with a \*CallbackID attribute. In the former case, Unidrv sends the command string to the print spooler. In the latter case, Unidrv calls the **IPrintOemUni::CommandCallback** method, passing the \*CallbackID and \*Params values as input arguments.

 

 




