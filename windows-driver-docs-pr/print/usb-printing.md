---
title: Microsoft USB printer driver (Usbprint.sys)
description: Usbprint.sys is the Microsoft-provided device driver for USB printers. Usbprint.sys works with Usbmon.dll to provide end-to-end connectivity between USB printers and high-level printer drivers.
keywords:
- printer drivers WDK, USB
- USB printers WDK
ms.date: 01/02/2024
---

# Microsoft USB printer driver (Usbprint.sys)

Usbprint.sys is the Microsoft-provided device driver for USB printers. Usbprint.sys works with Usbmon.dll to provide end-to-end connectivity between USB printers and high-level printer drivers.

Unlike some USB device class drivers, Usbprint.sys doesn't "drive" the printer. Instead, Usbprint.sys provides a communication conduit by which higher-level drivers can control the printer. As is true for parallel printers, USB printers require a printer driver to render print jobs, and might also require a language monitor to manage high-level communication with the printer.

During the installation of a USB printer, the system-supplied INF file, Usbprint.inf, obtains Usbprint.sys from the local file Driver.cab. Because Driver.cab was installed with the operating system, the printer installer typically doesn't need the original installation media to install Usbprint.sys.

For more information about Usbprint.inf, see [Printer connected to a USB port](printer-connected-to-a-usb-port.md). 

For more information about Driver.cab, see [Printer installation and the Plug and Play manager](printer-installation-and-the-plug-and-play-manager.md).

## In this section

[Programming considerations for USBPRINT](programming-considerations-for-usbprint.md)
