---
title: Universal Serial Bus (USB)
description: Learn to develop Windows drivers for USB devices.
ms.date: 10/28/2022
ms.topic: article
---

# Universal Serial Bus (USB)

Universal Serial Bus (USB) provides an expandable, hot-pluggable Plug and Play serial interface that ensures a standard, low-cost connection for peripheral devices such as keyboards, mice, joysticks, printers, scanners, storage devices, modems, and video conferencing cameras. Migration to USB is recommended for all peripheral devices that use legacy ports such as PS/2, serial, and parallel ports.

The USB-IF is a Special Interest Groups (SIGs) that maintains the [Official USB Specification](https://www.usb.org/documents), test specifications and tools.

Windows operating systems include native support for USB host controllers, hubs, and devices and systems that comply with the official USB specification. Windows also provides programming interfaces that you can use to develop [device drivers](usb-driver-development-guide.md) and [applications](developing-windows-applications-that-communicate-with-a-usb-device.md) that communicate with a USB device.

[![USB for device builders icon](images/icon-dev.png)](building-usb-devices-for-windows.md)[![USB for driver developers icon](images/icon-driver.png)](usb-driver-development-guide.md)[![USB for app developers icon](images/icon-app.png)](developing-windows-applications-that-communicate-with-a-usb-device.md)[![USB HCK certification icon](images/icon-cert.png)](windows-hardware-certification-kit-tests-for-usb.md)

## USB in Windows

- [Windows 10: What's new for USB](windows-10--what-s-new-for-usb.md): Overview of new features and improvements in USB in Windows 10.

- [USB FAQ](usb-faq--introductory-level.yml): Frequently asked questions from driver developers about the USB stack and features that are supported in USB.

- [Microsoft OS Descriptors for USB Devices](microsoft-defined-usb-descriptors.md): Windows defines MS OS descriptors that allows better enumeration when connected to system running Windows operating system.

## Development tools

- [Download the Windows Driver Kit (WDK)](../download-the-wdk.md)

## USB samples

- [UWP app samples for USB](https://github.com/Microsoft/Windows-universal-samples)
- [Windows driver samples for USB](https://go.microsoft.com/fwlink/p/?linkid=618021)

## Create a USB driver or app for Windows

Introduces you to USB driver development. Provides information about choosing the most appropriate model for providing a USB driver for your device.

### Write a USB client driver (KMDF, UMDF)

This section includes tutorials about writing your first user-mode and kernel-mode USB drivers by using the USB templates included with Microsoft Visual Studio.

- [Getting started with USB client driver development](getting-started-with-usb-client-driver-development.md)
- [USB device driver programming reference](/windows-hardware/drivers/ddi/_usbref/)

### Write a USB host controller driver

If you're developing an xHCI host controller that isn't compliant with the specification or developing a custom non-xHCI hardware (such as a virtual host controller), you can write a host controller driver that communicates with UCX. For example, consider a wireless dock that supports USB devices. The PC communicates with USB devices through the wireless dock by using USB over TCP as a transport.

- [Developing Windows drivers for USB host controllers](developing-windows-drivers-for-usb-host-controllers.md)

- USB host controller (UCX) reference
  - [Ucxclass.h](/windows-hardware/drivers/ddi/ucxclass/)
  - [Ucxcontroller.h](/windows-hardware/drivers/ddi/ucxcontroller/)
  - [Ucxroothub.h](/windows-hardware/drivers/ddi/ucxroothub/)
  - [Ucxusbdevice.h](/windows-hardware/drivers/ddi/ucxusbdevice/)
  - [Ucxendpoint.h](/windows-hardware/drivers/ddi/ucxendpoint/)
  - [Ucxsstreams.h](/windows-hardware/drivers/ddi/ucxsstreams/)

### Write a function controller driver for a USB device

You can develop a controller driver that handles all USB data transfers and commands sent by the host to the device. This driver communicates with the Microsoft-provided USB function controller extension (UFX).

[Developing Windows drivers for USB function controllers](developing-windows-drivers-for-usb-function-controllers.md)

USB function class extension (UFX) reference

- [Ufxbase.h](/windows-hardware/drivers/ddi/ufxbase/)
- [Ufxclient.h](/windows-hardware/drivers/ddi/ufxclient/)
- [Ufxproprietarycharger.h](/windows-hardware/drivers/ddi/ufxproprietarycharger/)

### Write a USB Type-C connector driver

Windows 10 introduces support for the new USB connector: USB Type-C. You can write a driver for the connector that communicates with the Microsoft-provided class extension module: UcmCx to handle scenarios related to Type-C connectors such as, which ports support Type-C, which ports support power delivery.

[Developing Windows drivers for USB Type-C connectors](developing-windows-drivers-for-usb-type-c-connectors.md)

USB connector manager class extension (UcmCx) reference

- [Ucmmanager.h](/windows-hardware/drivers/ddi/ucmmanager/)

### Write a USB dual-role controller driver

USB Dual Role controllers are now supported in Windows 10. Windows includes in-box client drivers for ChipIdea and Synopsis controllers. For other controllers, Microsoft provides a set of programming interfaces that allow the dual-role class extension (UrsCx) and its client driver to communicate with each other to handle the role-switching capability of a dual-role controller.

For more information about this feature, see:

[USB Dual Role Driver Stack Architecture](usb-dual-role-driver-stack-architecture.md)

USB dual-role controller driver programming reference

- [Ursdevice.h](/windows-hardware/drivers/ddi/ursdevice/)

### Write a USB driver for emulated devices

You can develop an emulated Universal Serial Bus (USB) host controller driver and a connected virtual USB device. Both components are combined into a single KMDF driver that communicates with the Microsoft-provided USB device emulation class extension (UdeCx).

[Developing Windows drivers for emulated USB devices (UDE)](developing-windows-drivers-for-emulated-usb-host-controllers-and-devices.md)

Emulated USB host controller driver programming reference

- [Udecxusbdevice.h](/windows-hardware/drivers/ddi/udecxusbdevice/)
- [Udecxusbendpoint.h](/windows-hardware/drivers/ddi/udecxusbendpoint/)
- [Udecxwdfdevice.h](/windows-hardware/drivers/ddi/udecxwdfdevice/)
- [Udecxurb.h](/windows-hardware/drivers/ddi/udecxurb/)

### WDF extension for developing USB drivers

- USB connector manager class extension (UcmCx) reference
  - [Ucmmanager.h](/windows-hardware/drivers/ddi/ucmmanager/)
- USB host controller (UCX) reference
  - [Ucxclass.h](/windows-hardware/drivers/ddi/ucxclass/)
  - [Ucxcontroller.h](/windows-hardware/drivers/ddi/ucxcontroller/)
  - [Ucxroothub.h](/windows-hardware/drivers/ddi/ucxroothub/)
  - [Ucxusbdevice.h](/windows-hardware/drivers/ddi/ucxusbdevice/)
  - [Ucxendpoint.h](/windows-hardware/drivers/ddi/ucxendpoint/)
  - [Ucxsstreams.h](/windows-hardware/drivers/ddi/ucxsstreams/)
- USB function class extension (UFX) reference
  - [Ufxbase.h](/windows-hardware/drivers/ddi/ufxbase/)
  - [Ufxclient.h](/windows-hardware/drivers/ddi/ufxclient/)
  - [Ufxproprietarycharger.h](/windows-hardware/drivers/ddi/ufxproprietarycharger/)

### Write a UWP app

- [Talk to USB devices, start to finish](talking-to-usb-devices-start-to-finish.md): Provides step-by-step instructions about implementing USB features in a UWP app. To write such an app for a USB device, you need Visual Studio and Microsoft Windows Software Development Kit (SDK).

- [Windows.Devices.Usb](/uwp/api/Windows.Devices.Usb): UWP namespace programming reference.

### Write a Windows desktop app

- [Write a WinUSB application](how-to-write-a-windows-desktop-app-that-communicates-with-a-usb-device.md): Describes how an application can call WinUSB Functions to communicate with a USB device.

- WinUSB functions
  - [Winusb.h](/windows/win32/api/winusb/)
  - [Usbioctl.h](/windows-hardware/drivers/ddi/usbioctl/)

- [Common programming scenarios](wdk-resources-for-usb-driver-development.md): List of common tasks that a driver or an app performs in order to communicate with a USB device. Get quick info about the programming interfaces you need for each task.

## Testing USB devices with Windows

[Overview of Microsoft USB Test Tool (MUTT) devices](./microsoft-usb-test-tool--mutt--devices.md)

Get information about the tools that you can use to test your USB hardware or software, capture traces of operations and other system events, and observe how the USB driver stack responds to a request sent by a client driver or an application.

Read an overview of tests in the Hardware Certification Kit that enable hardware vendors and device manufacturers to prepare their USB devices and host controllers for Windows Hardware Certification submission.

## Other Resources for USB

- [Official USB Specification](https://www.usb.org/documents): Provides complete technical details for the USB protocol.

- [Microsoft Windows USB Core Team Blog](https://techcommunity.microsoft.com/t5/Microsoft-USB-Blog/bg-p/MicrosoftUSBBlog): Check out posts written by the Microsoft USB Team. The blog focuses on the Windows USB driver stack that works with various USB Host controllers and USB hubs found in Windows PC. A useful resource for USB client driver developers and USB hardware designers to understand the driver stack implementation, resolve common issues, and explain how to use tools for gathering traces and log files.

- [OSR Online Lists - ntdev](https://community.osr.com/categories/ntdev): Discussion list managed by [OSR Online](https://www.osronline.com/index.cfm) for kernel-mode driver developers.

- [Windows Hardware Dev Center](https://developer.microsoft.com/windows/hardware/): Miscellaneous resources based on frequently asked questions from developers who are new to developing USB devices and drivers that work with Windows operating systems.

## USB-related videos

- [Understanding USB 3.0 in Windows 8](/events/build-build2011/hw-256t)
- [Building great USB 3.0 devices](/events/build-build2011/hw-773t)
- [USB Debugging Innovations in Windows 8 (Part I, II, & III)](/events/build-build2011/hw-258p)

## USB hardware for learning

- [MUTT devices](microsoft-usb-test-tool--mutt--devices.md): MUTT and SuperMUTT devices and the accompanying software package are integrated into the HCK suite of USB tests. They provide automated testing that can be used during the development cycle of USB controllers, devices and systems, especially stress testing.

- [OSR USB FX2 Learning Kit](https://www.osronline.com/index.cfm): If you're new to USB driver development. The kit is the most suitable to study USB samples included in this documentation set. You can get the learning kit from OSR Online Store.

## Learn about Microsoft-provided USB drivers

- [USB device-side drivers in Windows](usb-device-side-drivers-in-windows.md): Describes the architecture of the USB function stack.

- [USB host-side drivers in Windows](usb-3-0-driver-stack-architecture.md): Provides an overview of the Universal Serial Bus (USB) driver stack architecture. Microsoft provides a core stack of drivers that interoperate with devices that are connected to EHCI and xHCI controllers.

- [USB-IF device class drivers](supported-usb-classes.md): Lists the Microsoft-provided drivers for the supported USB device classes. Windows provides in-box device class drivers for many USB-IF approved device classes, audio, mass storage, and so on.

- [USB generic function driver–WinUSB](winusb.md): WinUSB is a generic driver for USB devices that is included with all versions of Windows since Windows Vista. Windows provides Winusb.sys that can be loaded as a function driver for a custom device and a function of a composite device.

- [USB generic parent driver for composite devices–Usbccgp](usb-common-class-generic-parent-driver.md): Parent driver for USB devices with multiple functions. Usbccgp creates physical device objects (PDOs) for each of those functions. Those individual PDOs are managed by their respective USB function drivers, which could be the Winusb.sys driver or a USB device class driver.