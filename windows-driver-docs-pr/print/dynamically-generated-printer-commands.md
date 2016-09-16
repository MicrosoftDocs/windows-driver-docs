---
title: Dynamically Generated Printer Commands
author: windows-driver-content
description: Dynamically Generated Printer Commands
MS-HAID:
- 'custdrvr\_b41e36c2-b02c-47cc-ab13-b341d1e9362b.xml'
- 'print.dynamically\_generated\_printer\_commands'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: ba395716-6906-4f23-a050-79d808ccd44b
keywords: ["Unidrv, dynamically generated commands", "dynamically generated print commands WDK Unidrv", "GPD files WDK Unidrv", "Unidrv WDK print"]
---

# Dynamically Generated Printer Commands


## <a href="" id="ddk-dynamically-generated-printer-commands-gg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Dynamically%20Generated%20Printer%20Commands%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


