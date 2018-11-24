---
title: Introduction to Printing
description: Introduction to Printing
ms.assetid: 8a2e0151-6d40-493d-9757-42350a9e6220
keywords:
- printing WDK
- rendering component WDK print
- configuration component WDK print
- components WDK printing
- architecture WDK print
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Introduction to Printing

The Microsoft Windows printing architecture consists of a print spooler and a set of printer drivers. By calling device-independent functions, applications can create print jobs and send them to many devices. This includes laser printers, vector plotters, raster printers, and fax machines.

Printer drivers include a rendering component and a configuration component. The *rendering component* converts the graphics commands from the application into a data format that the printer uses to render the image on the page. The *configuration component* contains a user interface component that enables users to control a printer's selectable options and a program interface that communicates the printer's configuration and features to an application.

When a Microsoft Win32 GDI application prints, it calls GDI functions in the Win32 API. These functions pass the information to the GDI graphics engine. The GDI graphics engine either spools the drawing instructions as an [*enhanced metafile (EMF)*](https://msdn.microsoft.com/library/windows/hardware/ff556279#wdkgloss-enhanced-metafile--emf-) file or, together with a printer driver, renders a printable image that can be sent to the spooler. Spooler components interpret EMF files, and they can insert page layout information and job control instructions into the data stream. The spooler then sends the data stream to the serial, parallel, or network port driver associated with the target printer's I/O port. In addition, if printing to an XPS device, the GDI print commands are converted through the GDI to XPS conversion component, and the print job is sent down the XPS print path.

In the XPS print path, printer drivers are based on the XML Paper Specification (XPS). When a Microsoft Win32 XPS application prints, the application calls XPS functions in the XPS Print API. When it prints to queues with [XPSDrv printer drivers](xpsdrv-printer-drivers.md), the spooler passes the XPS spool file straight to the device for rendering and output. When the XPS file is printed to a GDI device, it is converted to an EMF file through the XPS to GDI Conversion Module. It is then sent through the GDI print path in a manner similar to Win32 GDI applications.

Windows Presentation Foundation (WPF) applications call WPF print support functions to spool XPS documents to the spooler in the XPS spool file format. As when printing from Win32 XPS applications, when the spooler prints to print queues with XPSDrv printer drivers, the spooler passes the spooled file in its original format to the XPSDrv printer driver for rendering and output to the printer. When the spooler prints to printers that have GDI-based, version 3 printer drivers, the spooler sends the data in the XPS spool file format to the GDI Conversion Module for conversion to an EMF file. It then sends the data to the GDI-based printer driver for printing. For more information about these data paths, see [Windows Print Path Overview](windows-print-path-overview.md). For more information about XPS, see the [XML Paper Specification Overview](https://msdn.microsoft.com/library/windows/hardware/dn641615).

Spooler and driver components are replaceable, so hardware vendors can easily add support for new hardware. For more information about print spooler and driver components, see the following sections:

[Print Spooler Architecture](print-spooler-architecture.md)

[Printer Driver Architecture](printer-driver-architecture.md)

Support for a new printer usually requires only creating new data files for use with one of the Microsoft-supplied printer drivers. For more information about Microsoft printer drivers, see [Printer Driver Overview](printer-driver-overview.md).

You can customize the behavior of the Microsoft Universal Printer Driver and the Microsoft Postscript Printer Driver. For more information, see [Customizing Microsoft's Printer Drivers](customizing-microsoft-s-printer-drivers.md). You can also customize the print spooler. For more information, see [Customizing Print Spooler Components](print-spooler-components.md).

Other sections cover the following topics:

[Terminal Server Printing](terminal-server-printing.md)

[USB Printing](usb-printing.md)

[Bluetooth Printing](bluetooth-printing.md)

[Printer Driver Testing and Debugging](printer-driver-testing-and-debugging.md)
