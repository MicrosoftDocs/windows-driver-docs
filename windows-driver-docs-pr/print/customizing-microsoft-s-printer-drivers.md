---
title: Customizing Microsoft's Printer Drivers
author: windows-driver-content
description: Customizing Microsoft's Printer Drivers
MS-HAID:
- 'custdrvr\_22633c3f-a67a-4695-b560-6cfcbb87400e.xml'
- 'print.customizing\_microsoft\_s\_printer\_drivers'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: b7761209-1f6f-4288-af47-4ed855c2e629
keywords: ["printer driver customizing WDK", "customizing printer drivers WDK", "printer driver customizing WDK , about customizing printer drivers", "customizing printer drivers WDK , about customizing printer drivers"]
---

# Customizing Microsoft's Printer Drivers


## <a href="" id="ddk-customizing-microsofts-printer-drivers-gg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Customizing%20Microsoft's%20Printer%20Drivers%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


