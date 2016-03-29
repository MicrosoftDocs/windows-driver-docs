---
title: Introduction to Point and Print
description: Introduction to Point and Print
ms.assetid: 03902c64-29d7-4b59-a604-e282e4a2c7ae
keywords: ["Point and Print WDK , about Point and Print"]
---

# Introduction to Point and Print


## <a href="" id="ddk-introduction-to-point-and-print-gg"></a>


*Point and Print* is a term that refers to the capability of allowing a user on a Windows 2000 and later client to create a connection to a remote printer without providing disks or other installation media. All necessary files and configuration information are automatically downloaded from the print server to the client.

Point and Print technology provides two methods by which you can specify files that should be sent from the print server to the client machine:

-   Files can be associated with a printer driver. These files are associated with every print queue that uses the driver.

-   Files can be associated with individual print queues.

For more information, see [Supporting Point and Print During Printer Installations](supporting-point-and-print-during-printer-installations.md).

When a user application calls the **AddPrinterConnection** function (described in the Microsoft Windows SDK documentation) to make a printer connection, the following operations are performed:

-   Driver-associated and queue-associated files are downloaded from the print server to the client.

-   Current values of the printer's configuration parameters, which are stored in the server's registry under the printer's key, are downloaded to the client.

For more information, see [Supporting Point and Print During Printer Connections](supporting-point-and-print-during-printer-connections.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Introduction%20to%20Point%20and%20Print%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




