---
title: Printer Driver Support for Printer Directory Services
description: Printer Driver Support for Printer Directory Services
ms.assetid: 6b0b3cda-a9e5-458d-b5e2-89667059bde4
keywords:
- Directory Services WDK printer
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Printer Driver Support for Printer Directory Services





Printer drivers are not responsible for publishing a print queue to Directory Services. The Microsoft Windows 2000 and later print folder creates a print queue object (by calling the spooler's **SetPrinter** function) during the process of installing the printer. (See [Publishing Print Queues](print-spooler-support-for-printer-directory-services.md#ddk-publishing-print-queues-gg).)

Print queue properties are published so that a user can search for printers with particular properties by using the **Search** option on the task bar's **Start** menu. The print folder publishes some, but not all, of the printer capabilities that are available to it from DriverCapabilities. Only capabilities that are considered useful for browsing purposes are published.

Printer drivers can add or modify a print queue object's property information. The print queue properties that can be published are identified by **SPLDS\_**-prefixed constants, defined in winspool.h. To add or modify printer properties, your driver must use these predefined property name identifiers.

To add or modify a print queue object's property information, carry out the following steps:

1.  Add property names and values to the registry, under the SPLDS\_DRIVER\_KEY, by calling the spooler's **SetPrinterDataEx** function.

2.  Call the spooler's **SetPrinter** function, with an input structure of PRINTER\_INFO\_7 (described in the Windows SDK documentation) and an action of DSPRINT\_UPDATE, to inform the spooler that it should update the published print queue object. (Drivers should not specify an action of DSPRINT\_PUBLISH.)

These steps should be implemented within the printer driver's [**DrvPrinterEvent**](https://msdn.microsoft.com/library/windows/hardware/ff548564) function, when the function receives a PRINTER\_EVENT\_INITIALIZE event.

If a driver must obtain the current values for a printer's published properties, it should call **GetPrinterDataEx** or **EnumPrinterDataEx** to obtain the information from the registry, which is spooler-maintained and always up to date. An alternative way is to call **GetPrinter** to obtain the print queue's object identifier and then to call ADSI functions to obtain the values of the published properties. This technique is not recommended, both because it is more resource intensive and because returned data might not always be current.

 

 




