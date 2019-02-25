---
title: Autoconfiguration Flow for GPD in Windows Vista
description: Autoconfiguration Flow for GPD in Windows Vista
ms.assetid: 41468218-fa05-4431-a57d-3056449f2e2e
keywords:
- GPD files WDK GDL extensions , autoconfiguration flow
- in-box autoconfiguration support WDK printer , sequence of steps
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Autoconfiguration Flow for GPD in Windows Vista


Autoconfiguration follows the following sequence:

1.  Port Monitor sends to the spooler a notification that contains any values that formerly were not in the cache or that changed.

2.  The spooler responds to the notification from the port monitor by calling [**DrvPrinterEvent**](https://msdn.microsoft.com/library/windows/hardware/ff548564).

3.  Printer\_Event\_Configuration is passed to the driver that contains any and all new values. The driver is notified that the value of an attribute has changed, and the registry is also updated.

4.  If the notification is too big, Reduced Schema Event is called.

5.  The PPD file is parsed, including all GDL file extensions and GDL content within the PPD. All GDL content in either GDL file extensions or throughout the PPD file must be surrounded with **\*Ifdef**: GDL\_Enabled and **\*Endif**: GDL\_Enabled.

6.  Your plug-in will retrieve the value for **\*MSBidiValue**, which will be based on the current string value for **\*QueryString**. For example, a **\*QueryString** value of "\\Printer.Configuration.DuplexUnit:Installed" will represent a **\*BidiValue** value of BOOL(TRUE).

7.  Your plug-in will update the driver UI according to the latest configuration.

 

 




