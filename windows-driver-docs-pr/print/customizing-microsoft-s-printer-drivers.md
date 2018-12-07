---
title: Customizing Microsoft Printer Drivers
description: Customizing Microsoft Printer Drivers
ms.assetid: b7761209-1f6f-4288-af47-4ed855c2e629
keywords:
- printer driver customizing WDK
- customizing printer drivers WDK
- printer driver customizing WDK , about customizing printer drivers
- customizing printer drivers WDK , about customizing printer drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Customizing Microsoft Printer Drivers


The designs of the [Microsoft Universal Printer Driver](microsoft-universal-printer-driver.md) (Unidrv) and the [Microsoft PostScript Printer Driver](microsoft-postscript-printer-driver.md) (Pscript) are based on the NT-based operating system [printer driver architecture](printer-driver-architecture.md). Therefore, each is composed of two components--a [printer interface DLL](printer-interface-dll.md) and a [printer graphics DLL](printer-graphics-dll.md). This section explains how to customize these components.

To customize the printer interface DLL provided for Unidrv or Pscript, you must provide one or more [user interface plug-ins](user-interface-plug-ins.md). You can use these plug-ins to modify the driver's user interface and to provide extra processing for certain printer events. If you are using Unidrv from Windows Vista, you can replace the user interface completely.

To customize the printer graphics DLL provided for Unidrv or Pscript, you must provide one or more [rendering plug-ins](rendering-plug-ins.md). You can use these plug-ins to modify the data that is sent to the print spooler within a print job's data stream.

This section includes the following topics:

[User Interface Plug-Ins](user-interface-plug-ins.md)

[Rendering Plug-Ins](rendering-plug-ins.md)

[Implementing Printer Driver COM Interfaces](implementing-printer-driver-com-interfaces.md)

[Installing Customized Driver Components](installing-customized-driver-components.md)

[Common Property Sheet User Interface](common-property-sheet-user-interface.md)

[Color Management for Printers](color-management-for-printers.md)

[Adding Print Ticket Support to Print Drivers](adding-print-ticket-support-to-print-drivers.md)

[Device Stage for Document Devices](device-stage-for-document-devices.md)

 

 




