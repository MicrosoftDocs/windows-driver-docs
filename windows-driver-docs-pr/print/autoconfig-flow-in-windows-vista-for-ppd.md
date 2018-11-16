---
title: Autoconfig Flow in Windows Vista for PPD
description: Autoconfig Flow in Windows Vista for PPD
ms.assetid: 60675cd3-fe98-4772-aa1b-a73529480d8a
keywords:
- PPD files WDK autoconfiguration , sequence of steps
- in-box autoconfiguration support WDK printer , sequence of steps
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Autoconfig Flow in Windows Vista for PPD


Autoconfig follows the following sequence:

1.  Port Monitor sends to the spooler a notification containing any values that formerly were not in the cache or that changed.

2.  Spooler responds to the notification from the port monitor by calling DrvPrinterEvent.

3.  Printer\_Event\_Configuration is passed to the driver containing any and all new values. The driver is notified that the value of an attribute has changed. The registry is also updated.

4.  If the notification is too big, a Reduced Schema Event is called.

5.  The PPD file is parsed including all GDL file extensions and GDL content within the PPD. All GDL content in either GDL file extensions or throughout the PPD file must be surrounded with `*Ifdef: GDL_Enabled` and `*Endif: GDL_Enabled`.

6.  The IHV plug-in will retrieve the value for **\*MSBidiValue** which will be based on the current string value for **\*QueryString**. For example, a **\*QueryString** value of \\Printer.Configuration.DuplexUnit:Installed will represent a **\*BidiValue** value of BOOL(TRUE).

7.  The IHV plug-in will update the driver UI according to the latest configuration.

 

 




