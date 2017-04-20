---
title: Print Ticket Compatibility with Win 32 Applications
author: windows-driver-content
description: Print Ticket Compatibility with Win 32 Applications
ms.assetid: 3e358f8a-e950-4da0-b8ef-4e350ea28091
keywords:
- Win32 applications WDK print
- Print Tickets WDK ,Win32 applications
- Print Tickets WDK , XPSDrv
- Print Tickets WDK , GDI-based print drivers
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Print Ticket Compatibility with Win 32 Applications


When you use Print Tickets in Microsoft Win32-based applications and GDI-based print drivers, you must consider the following compatibility scenarios:

<a href="" id="win32-based-applications-that-are-printing-to-xpsdrv-print-drivers"></a>Win32-based applications that are printing to XPSDrv print drivers  
When a Win32-based application that is not aware of Print Ticket documents prints to an XPSDrv print driver, the GDI-to-XPS conversion module creates an XPS spool file from the DDI calls that the Win32-based application makes. The Windows Vista print support also creates Print Tickets that are based on the DEVMODE structures that the Win32-based application uses and inserts them into the XPS spool file that is created for the document. The GDI-to-XPS conversion can convert only the public portion of the DEVMODE structure. The conversion embeds the private DEVMODE into the print ticket as a binary large object (BLOB), using appropriate XML binary encoding. You can restore the binary BLOB to the private part of the [**DEVMODEW**](https://msdn.microsoft.com/library/windows/hardware/ff552837) structure from the print ticket in the DEVMODEW-to-Print Ticket conversion.

To the XPSDrv print driver, a document that is sent from a Win32-based application is not different than a document that is sent from a Windows Presentation Foundation (WPF) application because both documents are spooled in the XPS spool file format.

<a href="" id="wpf-applications-that-are-printing-to-gdi-based-print-drivers"></a>WPF applications that are printing to GDI-based print drivers  
When a WPF application prints a document that contains Print Tickets to a GDI-based print driver that does not support Print Tickets, the Windows Vista print support converts the XPS Document that the WPF application passes to an [EMF](emf-data-type.md) file and converts each Print Ticket to a DEVMODE structure.

To the GDI print driver, the print job from a WPF application is not different than a print job that a Win32 application sends.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Print%20Ticket%20Compatibility%20with%20Win%2032%20Applications%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


