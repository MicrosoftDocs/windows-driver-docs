---
title: Introduction to Point and Print
description: Introduction to Point and Print
ms.assetid: 03902c64-29d7-4b59-a604-e282e4a2c7ae
keywords:
- Point and Print WDK , about Point and Print
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Introduction to Point and Print





*Point and Print* is a term that refers to the capability of allowing a user on a Windows 2000 and later client to create a connection to a remote printer without providing disks or other installation media. All necessary files and configuration information are automatically downloaded from the print server to the client.

Point and Print technology provides two methods by which you can specify files that should be sent from the print server to the client machine:

-   Files can be associated with a printer driver. These files are associated with every print queue that uses the driver.

-   Files can be associated with individual print queues.

For more information, see [Supporting Point and Print During Printer Installations](supporting-point-and-print-during-printer-installations.md).

When a user application calls the **AddPrinterConnection** function (described in the Microsoft Windows SDK documentation) to make a printer connection, the following operations are performed:

-   Driver-associated and queue-associated files are downloaded from the print server to the client.

-   Current values of the printer's configuration parameters, which are stored in the server's registry under the printer's key, are downloaded to the client.

For more information, see [Supporting Point and Print During Printer Connections](supporting-point-and-print-during-printer-connections.md).

 

 




