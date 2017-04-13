---
title: Printer Driver Support for Printer Directory Services
author: windows-driver-content
description: Printer Driver Support for Printer Directory Services
ms.assetid: 6b0b3cda-a9e5-458d-b5e2-89667059bde4
keywords: ["Directory Services WDK printer"]
---

# Printer Driver Support for Printer Directory Services


## <a href="" id="ddk-printer-driver-support-for-printer-directory-services-gg"></a>


Printer drivers are not responsible for publishing a print queue to Directory Services. The Microsoft Windows 2000 and later print folder creates a print queue object (by calling the spooler's **SetPrinter** function) during the process of installing the printer. (See [Publishing Print Queues](print-spooler-support-for-printer-directory-services.md#ddk-publishing-print-queues-gg).)

Print queue properties are published so that a user can search for printers with particular properties by using the **Search** option on the task bar's **Start** menu. The print folder publishes some, but not all, of the printer capabilities that are available to it from DriverCapabilities. Only capabilities that are considered useful for browsing purposes are published.

Printer drivers can add or modify a print queue object's property information. The print queue properties that can be published are identified by **SPLDS\_**-prefixed constants, defined in winspool.h. To add or modify printer properties, your driver must use these predefined property name identifiers.

To add or modify a print queue object's property information, carry out the following steps:

1.  Add property names and values to the registry, under the SPLDS\_DRIVER\_KEY, by calling the spooler's **SetPrinterDataEx** function.

2.  Call the spooler's **SetPrinter** function, with an input structure of PRINTER\_INFO\_7 (described in the Windows SDK documentation) and an action of DSPRINT\_UPDATE, to inform the spooler that it should update the published print queue object. (Drivers should not specify an action of DSPRINT\_PUBLISH.)

These steps should be implemented within the printer driver's [**DrvPrinterEvent**](https://msdn.microsoft.com/library/windows/hardware/ff548564) function, when the function receives a PRINTER\_EVENT\_INITIALIZE event.

If a driver must obtain the current values for a printer's published properties, it should call **GetPrinterDataEx** or **EnumPrinterDataEx** to obtain the information from the registry, which is spooler-maintained and always up to date. An alternative way is to call **GetPrinter** to obtain the print queue's object identifier and then to call ADSI functions to obtain the values of the published properties. This technique is not recommended, both because it is more resource intensive and because returned data might not always be current.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Printer%20Driver%20Support%20for%20Printer%20Directory%20Services%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


