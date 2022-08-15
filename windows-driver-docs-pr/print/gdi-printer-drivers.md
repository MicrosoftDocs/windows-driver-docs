---
title: GDI Printer Drivers
description: GDI Printer Drivers
keywords:
- GDI printer drivers WDK
- printer drivers WDK , GDI
- GDI printer drivers WDK , about GDI printer drivers
ms.date: 04/20/2017
---

# GDI Printer Drivers





All Windows 2000 and later printer drivers consist of the following components:

-   A [printer graphics DLL](printer-graphics-dll.md) that assists GDI in rendering a print job, and sends the rendered data stream to the print spooler.

-   A [printer interface DLL](printer-interface-dll.md) that provides both a user interface to the driver's configuration parameters, and an interface the spooler can call to notify the driver of print-related system events.

In addition, Microsoft-supplied printer drivers make use of [printer data files](printer-data-files.md).

 

 




