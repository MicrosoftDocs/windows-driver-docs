---
title: Print Ticket Compatibility with Win 32 Applications
description: Print Ticket Compatibility with Win 32 Applications
ms.assetid: 3e358f8a-e950-4da0-b8ef-4e350ea28091
keywords:
- Win32 applications WDK print
- Print Tickets WDK ,Win32 applications
- Print Tickets WDK , XPSDrv
- Print Tickets WDK , GDI-based print drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Print Ticket Compatibility with Win 32 Applications


When you use Print Tickets in Microsoft Win32-based applications and GDI-based print drivers, you must consider the following compatibility scenarios:

<a href="" id="win32-based-applications-that-are-printing-to-xpsdrv-print-drivers"></a>Win32-based applications that are printing to XPSDrv print drivers  
When a Win32-based application that is not aware of Print Ticket documents prints to an XPSDrv print driver, the GDI-to-XPS conversion module creates an XPS spool file from the DDI calls that the Win32-based application makes. The Windows Vista print support also creates Print Tickets that are based on the DEVMODE structures that the Win32-based application uses and inserts them into the XPS spool file that is created for the document. The GDI-to-XPS conversion can convert only the public portion of the DEVMODE structure. The conversion embeds the private DEVMODE into the print ticket as a binary large object (BLOB), using appropriate XML binary encoding. You can restore the binary BLOB to the private part of the [**DEVMODEW**](https://msdn.microsoft.com/library/windows/hardware/ff552837) structure from the print ticket in the DEVMODEW-to-Print Ticket conversion.

To the XPSDrv print driver, a document that is sent from a Win32-based application is not different than a document that is sent from a Windows Presentation Foundation (WPF) application because both documents are spooled in the XPS spool file format.

<a href="" id="wpf-applications-that-are-printing-to-gdi-based-print-drivers"></a>WPF applications that are printing to GDI-based print drivers  
When a WPF application prints a document that contains Print Tickets to a GDI-based print driver that does not support Print Tickets, the Windows Vista print support converts the XPS Document that the WPF application passes to an [EMF](emf-data-type.md) file and converts each Print Ticket to a DEVMODE structure.

To the GDI print driver, the print job from a WPF application is not different than a print job that a Win32 application sends.

 

 




