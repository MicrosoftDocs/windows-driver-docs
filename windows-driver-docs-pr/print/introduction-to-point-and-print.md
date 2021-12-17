---
title: Introduction to Point and Print
description: Introduction to Point and Print
keywords:
- Point and Print WDK , about Point and Print
ms.date: 12/16/2021
ms.custom: contperf-fy22q2
---

# Introduction to Point and Print

*Point and Print* refers to the capability of allowing a user to create a connection to a remote printer without providing disks or other installation media. All necessary files and configuration information are automatically downloaded from the print server to the client.

Point and Print technology provides two methods by which you can specify files that should be sent from the print server to the client machine:

- Files can be associated with a printer driver. These files are associated with every print queue that uses the driver.

- Files can be associated with individual print queues.

When a user application calls the [**AddPrinterConnection**](/windows/win32/printdocs/addprinterconnection) function to make a printer connection, the following operations are performed:

- Driver-associated and queue-associated files are downloaded from the print server to the client.

- Current values of the printer's configuration parameters, which are stored in the server's registry under the printer's key, are downloaded to the client.

## See also

[Supporting Point and Print During Printer Installations](supporting-point-and-print-during-printer-installations.md)

[**AddPrinterConnection**](/windows/win32/printdocs/addprinterconnection)
