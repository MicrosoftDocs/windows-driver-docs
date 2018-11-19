---
title: Document Devices in Devices and Printers
description: Document Devices in Devices and Printers
ms.assetid: 6855d8fa-1354-4af9-8c00-486b6a643f85
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




