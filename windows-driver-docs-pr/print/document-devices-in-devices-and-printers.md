---
title: Document Devices in Devices and Printers
author: windows-driver-content
description: Document Devices in Devices and Printers
ms.assetid: 6855d8fa-1354-4af9-8c00-486b6a643f85
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Document Devices in Devices and Printers


All printers that appear in the Printers folder in Windows Vista appear in the Devices and Printers view in Windows 7. These printers include the following:

-   Locally connected printers

-   Networked printers connected through TCP/IP

-   Point and Print connections

-   HTTP-connected printers

-   Printer connections redirected through the Remote Desktop Connection utility

-   Virtual printers (including the Microsoft Shared Fax and the Microsoft XPS Document Writer)

All scanners installed with a Windows Image Acquisition (WIA) driver appear in the Devices and Printers view. Only scanners that are connected by Plug and Play or PnP-X appear in this view.

MFPs that connect to the PC by Plug and Play or PnP-X will appear in the Devices and Printers view as a single, composite device instead of as separate printer and scanner devices. Network MFPs that connect to a PC by using TCP/IP only are recognized as separate print and scan devices. The manufacturer can still provide a custom device experience that includes custom icons and a Device Stage page, but the Devices and Printers view displays the printer and scanner functions in the MFP as separate devices.

An MFP appears in the Devices and Printers view only if both the printer and scanner functions in the MFP are installed. If only the printer function is installed, this function appears in the view as a stand-alone printer, and if only the scanner function is installed, this function appears as a stand-alone scanner.

The Devices and Printers user interface treats the fax queues that the Microsoft Shared Fax driver creates as print queues. All context menus and command bar menus that are available for print queues are available for these queues.

If third-party fax drivers appear as printers in the spooler, the Devices and Printers user interface treats them as print queues and provides printer context menus, command bar menus, and generic printer icons for them.

If an MFP has a fax queue that enumerates as a print queue, it will appear as part of MFP.

If an MFP has a fax function that does not enumerate as a print queue, the Devices and Printers user interface can identify the fax as part of the MFP only if a device container identifier (ContainerID) for the fax functional device instance can be found. Manufacturers must provide custom metadata to specify the tasks for such fax devices. For more information about ContainerIDs, see the Identifying Device Functions in MFPs section.

Device manufacturers may author Device Stage for printers, scanners, and multi-function printers. Both locally attached printers (such as a printer that has a USB connection) and network-connected printers can have customized device experiences.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Document%20Devices%20in%20Devices%20and%20Printers%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


