---
title: Sample KMDF Drivers
description: This topic lists the Kernel-Mode Driver Framework (KMDF) sample drivers that you can download from the Windows Dev Center - Hardware.
ms.assetid: 83d15b96-63b1-4584-8ef4-ccbdcc1522bb
keywords:
- kernel-mode drivers WDK KMDF , samples
- KMDF WDK , sample drivers
- Kernel-Mode Driver Framework WDK , sample drivers
- framework-based drivers WDK KMDF , samples
- sample drivers WDK KMDF
ms.date: 06/04/2018
ms.localizationpriority: medium
---

# Sample KMDF Drivers


This topic lists the Kernel-Mode Driver Framework (KMDF) sample drivers that you can download from the [Windows driver samples repository](https://github.com/Microsoft/Windows-driver-samples) on GitHub.




For information on building the samples, see [Building a Driver](https://msdn.microsoft.com/windows-drivers/develop/building_a_driver).

<a href="" id="echo"></a>ECHO
Demonstrates how to use the framework's queue and request objects and automatic synchronization.

For more information about this sample, see the [KMDF Echo Sample](https://github.com/Microsoft/Windows-driver-samples/tree/master/general/echo/kmdf).

<a href="" id="fakemodem"></a>FakeModem
Demonstrates a simple controllerless modem driver that sends and receives AT commands.

For more information about this sample, see the [Fakemodem Driver](https://github.com/Microsoft/Windows-driver-samples/tree/master/network/modem/fakemodem).

<a href="" id="firefly"></a>FIREFLY
Demonstrates programming a human input device (HID) device by using I/O control codes (IOCTLs), and provides a Windows Management Instrumentation (WMI) interface.

For more information about this sample, see the [FIREFLY - WDF filter driver for HID device](https://github.com/Microsoft/Windows-driver-samples/tree/master/hid/firefly).

<a href="" id="hidusbfx2"></a>HIDUSBFX2
Demonstrates how to write a minidriver for a HID device and how to map a non-HID USB device to a HID device. The device is contained in the OSR USB-FX2 Learning Kit.

For more information about this sample, see [HIDUSBFX2](https://github.com/Microsoft/Windows-driver-samples/tree/master/hid/hidusbfx2).

<a href="" id="kbfiltr"></a>KbFiltr
Demonstrates an upper device filter driver for a PS/2 keyboard.

For more information about this sample, see the [Keyboard Input WDF Filter Driver (Kbfiltr)](https://github.com/Microsoft/Windows-driver-samples/tree/master/input/kbfiltr).

<a href="" id="ndisprot"></a>NDISProt
Demonstrates a connection-less NDIS 5.0/5.1 and NDIS 6.0 protocol driver.

For more information about this sample, see [NDISProt Connection-less WDF Protocol](https://github.com/Microsoft/Windows-driver-samples/tree/master/network/ndis/ndisprot_kmdf).

<a href="" id="nonpnp"></a>NONPNP
Demonstrates a non-Plug and Play (PnP) driver that uses the framework.

For more information about this sample, see [NONPNP](https://github.com/Microsoft/Windows-driver-samples/tree/master/general/ioctl/kmdf).

<a href="" id="kmdf-fx2"></a>KMDF\_FX2
Demonstrates how to perform bulk and interrupt data transfers to the USB device that is contained in the OSR USB-FX2 Learning Kit.

For more information about this sample, see [kmdf\_fx2](https://github.com/Microsoft/Windows-driver-samples/tree/master/usb/kmdf_fx2).

<a href="" id="pcidrv"></a>PCIDRV
A fully functional framework-based driver for Intel 82557/82558-based PCI Ethernet adapters (10/100) and Intel compatibles.

For more information about this sample, see the [PCIDRV - WDF Driver for PCI Device](https://github.com/Microsoft/Windows-driver-samples/tree/master/general/pcidrv).

<a href="" id="plx9x5x"></a>PLX9x5x
Demonstrates how to write a driver for a generic PCI device that supports DMA and uses the PLX9656/9653RDK-LITE board.

For more information about this sample, see the [PLX9x5x PCI Driver](https://github.com/Microsoft/Windows-driver-samples/tree/master/general/PLX9x5x).

<a href="" id="serial"></a>Serial
A framework-based serial driver that is based on the WDM serial sample driver.

For more information about this sample, see the [Serial sample](https://github.com/Microsoft/Windows-driver-samples/tree/master/serial/serial).

<a href="" id="toaster"></a>Toaster
Framework-based versions of the WDM toaster sample drivers. The toaster sample includes a filter driver, a function driver, and a bus driver that create a single driver stack. The sample also includes an additional kernel-mode driver that uses a remote I/O target to communicate with the driver stack.

For more information about this sample, see [Toaster](https://github.com/Microsoft/Windows-driver-samples/tree/master/general/toaster/toastDrv).

<a href="" id="usbsamp"></a>UsbSamp
Demonstrates how to use the framework to perform bulk and isochronous data transfers to a USB device.

For more information about this sample, see the [Usbsamp Sample](https://github.com/Microsoft/Windows-driver-samples/tree/master/usb/usbsamp).

<a href="" id="wmisamp"></a>WmiSamp
Demonstrates how to register WMI providers and create provider instances for framework device objects and how to handle WMI queries that applications send to the device.

For more information about this sample, see the [WmiSamp WMI Provider](https://github.com/Microsoft/Windows-driver-samples/tree/master/wmi/wmisamp).


