---
title: Print Capabilities in Unidrv and PScript5 Print Drivers
description: Print Capabilities in Unidrv and PScript5 Print Drivers
ms.assetid: 70f8b846-3e05-4345-baad-a3db6b8df620
keywords:
- Print Capabilities WDK , Unidrv
- Print Capabilities WDK , PScript5
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Print Capabilities in Unidrv and PScript5 Print Drivers


The Unidrv and PScript5 minidrivers provide the Print Ticket and Print Capabilities interfaces that are required to support the Print Capabilities feature. These print drivers provide Print Ticket and Print Capabilities support for the features that are described in the [generic printer description (GPD) file](introduction-to-gpd-files.md) or the PostScript printer description (PPD) file, as appropriate, whether the feature information is in the public or private portion of the [**DEVMODEW**](https://msdn.microsoft.com/library/windows/hardware/ff552837) structure.

[XPSDrv print drivers](xpsdrv-printer-drivers.md) can also use the Unidrv printer configuration DLL to provide the required support for both the GDI-based printer configuration interface and the [IPrintTicketProvider interface](https://msdn.microsoft.com/library/windows/hardware/ff554375). If you use the Unidrv configuration DLL, you can expedite the development of XPSDrv printer drivers for basic-functionality printers or pass-through print drivers.

 

 




