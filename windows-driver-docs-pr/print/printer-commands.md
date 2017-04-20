---
title: Printer Commands
author: windows-driver-content
description: Printer Commands
ms.assetid: 4f47ae57-cfca-4670-823e-526e2f40de82
keywords:
- Unidrv, commands
- GPD files WDK Unidrv , printer commands
- commands WDK Unidrv
- printer commands WDK Unidrv
- printer commands WDK Unidrv , about printer commands
- Unidrv WDK print
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Printer Commands


## <a href="" id="ddk-printer-commands-gg"></a>


The GPD language provides a predefined command name for each commonly used printer operation. Additionally, customized commands can be defined for device-specific [printer options](printer-options.md).

Each printer command can be implemented in either of two ways:

-   You can place a device-specific command string in a GPD file. Unidrv sends the command string to the print spooler at the appropriate time.

-   You can implement the [**IPrintOemUni::CommandCallback**](https://msdn.microsoft.com/library/windows/hardware/ff554216) COM method, which dynamically generates a command string. Unidrv calls the method whenever it has to send the command to the spooler. For more information see [Dynamically Generated Printer Commands](dynamically-generated-printer-commands.md) in [Customizing Microsoft's Printer Drivers](customizing-microsoft-s-printer-drivers.md).

The following topics describe how to specify printer commands in GPD files:

[Command Entry Format](command-entry-format.md)

[Command Names](command-names.md)

[Command Attributes](command-attributes.md)

[Command String Format](command-string-format.md)

[Command Execution Order](command-execution-order.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Printer%20Commands%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


