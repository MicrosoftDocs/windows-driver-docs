---
title: Printer Driver Architecture
description: Printer Driver Architecture
ms.assetid: 68a61007-8f0d-4fd4-b4a7-c8acbc101236
keywords:
- print jobs WDK , printer drivers
- jobs WDK print , printer drivers
- Windows printing architecture WDK
- printer driver architecture WDK
- printer drivers WDK , architecture
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Printer Driver Architecture





Print jobs are created by applications through calls to Microsoft Win32 GDI or, in Windows Vista, Windows Presentation Foundation (WPF) functions. The Win32 functions spool application data as [EMF](emf-data-type.md) records for later playback by the EMF [*print processor*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-print-processor), or they can immediately render a printable image for each document page. The WPF functions spool application data as an XPS spool file.

Prior to Windows Vista, applications communicated printer settings to the printer by using a [**DEVMODEW**](https://msdn.microsoft.com/library/windows/hardware/ff552837) structure. In Windows Vista, the Print Ticket and Print Capabilities technologies communicate printer settings so that printer settings are more compatible across printers and applications.

Image rendering, whether performed immediately or during print processing, is performed in the print driver:

-   A [GDI-based printer driver](gdi-printer-drivers.md) performs the image rendering during the playback of EMF records from the spool file and is controlled by the GDI rendering engine. During the rendering operation, the GDI rendering engine calls the appropriate Windows 2000 and later printer driver for assistance.

-   [XPSDrv print drivers](xpsdrv-printer-drivers.md) use a series of processing filters to process the XPS spool file content for output to the printer.

Windows 2000 and later GDI-based printer drivers must:

-   Assist GDI in rendering print jobs by providing printer-specific drawing capabilities that GDI cannot support.

-   Send the rendered image's data stream to the print spooler.

-   Provide a user interface to the modifiable configuration parameters that are associated with printers and print documents, such as which input and output trays are selected, the number of copies, image resolution and orientation, and so on.

XPSDrv printer drivers have the same user interface responsibility as the GDI-based drivers and are also responsible for processing the print job data and sending the data to the printer. XPSDrv printer drivers, however, do not need to use GDI to render the page images for the printer.

Windows 2000 and later printer drivers are made up of a set of [printer driver components](gdi-printer-drivers.md) that divide a driver's drawing and user interface operations into separate DLLs. XPSDrv printer drivers are also made up of components that divide the configuration and the drawing and rendering functions into separate objects.

This section is intended to help you understand the different types of printer drivers that the Windows 2000 and later operating systems support, but you should also remember that the following three printer drivers are shipped with the operating system:

[Microsoft Universal Printer Driver](microsoft-universal-printer-driver.md)

[Microsoft PostScript Printer Driver](microsoft-postscript-printer-driver.md)

[Microsoft Plotter Driver](microsoft-plotter-driver.md)

These three drivers support most printing devices that end-users can purchase today. You need to write a printer driver only if your printing device is not compatible with the appropriate Microsoft-supplied driver. You can support most new printers by simply adding a [printer data file](printer-data-files.md) to one of the Microsoft-supplied drivers. Devices that might require a new driver include those containing hardware drawing accelerators controlled by proprietary command sequences.

This section contains the following topics, which describe the Windows printing architecture.

[XPSDrv Printer Drivers](xpsdrv-printer-drivers.md)

[GDI Printer Drivers](gdi-printer-drivers.md)

[Print Ticket and Print Capabilities Technologies](print-ticket-and-print-capabilities-technologies.md)

[Writing 64-Bit Printer Drivers](writing-64-bit-printer-drivers.md)

 

 




