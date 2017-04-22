---
title: Introduction to Printer Interface DLLs
author: windows-driver-content
description: Introduction to Printer Interface DLLs
ms.assetid: 1993d818-9761-418e-96c3-e3c46965bef1
keywords:
- printer interface DLL WDK , about printer interface DLL
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Introduction to Printer Interface DLLs


## <a href="" id="ddk-introduction-to-printer-interface-dlls-gg"></a>


Printers typically provide users with a large number of modifiable configuration options that can be changed for each document that is printed. Options such as paper, tray and font selection, along with image resolution, size, color, and so on, must be accessible through user interfaces that can be invoked by applications.

A printer driver's *printer interface DLL*, which executes in user mode, is responsible for exporting a user interface to the printer's configuration options. Providing this interface involves [creating property sheet pages for printers](creating-property-sheet-pages-for-printers.md). Applications (such as the print folder) display the interface by calling Win32 functions exported by the print spooler, and the spooler, in turn, calls [functions defined by printer interface DLLs](functions-defined-by-printer-interface-dlls.md).

Providing a user interface to configuration options is not a printer interface DLL's only responsibility. The DLL also exports functions that the spooler can call to notify the driver of print-related system events, such as driver installations and upgrades, or printer additions and connections.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Introduction%20to%20Printer%20Interface%20DLLs%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


