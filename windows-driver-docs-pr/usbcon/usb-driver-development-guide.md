---
title: Overview of developing Windows client drivers for USB devices
description: This article describes Universal Serial Bus (USB) support in the Windows operating system, so that you can develop USB device drivers that are interoperable with Windows.
ms.date: 01/17/2023
---

# Overview of developing Windows client drivers for USB devices

This article describes Universal Serial Bus (USB) support in the Windows operating system, so that you can develop USB device drivers that are interoperable with Windows.

USB devices are peripherals, such as mouse devices and keyboards, that are connected to a computer through a single port. A USB client driver is the software installed on the computer that communicates with the hardware to make the device function. If the device belongs to a device class supported by Microsoft, Windows loads one of the [Microsoft-provided USB drivers](system-supplied-usb-drivers.md) (in-box class drivers) for the device. Otherwise, a custom client driver must be provided by the hardware manufacturer or a third party vendor. The user installs the client driver for the device when the device is first detected by Windows. After successful installation, Windows loads the client driver every time the device is attached and unloads the driver when the device is detached from the host computer.

You can develop a custom client driver for a USB device by using the [Windows Driver Frameworks](../wdf/index.md) (WDF) or the [Windows Driver Model](../kernel/writing-wdm-drivers.md) (WDM). Instead of communicating with the hardware directly, most client drivers send their requests to the Microsoft-provided USB driver stack that makes hardware abstraction layer (HAL) function calls to send the client driver's request to the hardware. The topics in this section describe the typical requests that a client driver can send and the device driver interfaces (DDIs) that the client driver must call to create those requests.

## Developer audience

A client driver for a USB device is a WDF or WDM driver that communicates with the device through DDIs exposed by the USB driver stack. This section is intended for use by C/C++ programmers who are familiar with WDM. Before you use this section, you should understand basic driver development. For more information, see [Getting Started with Windows Drivers](../gettingstarted/index.md). For WDF drivers, the client driver can use [Kernel-Mode Driver Framework](../debugger/kernel-mode-driver-framework-debugging.md) (KMDF) or [User-Mode Driver Framework](../wdf/index.md) (UMDF) interfaces designed specifically to work with USB targets. For more information about the USB-specific interfaces, see [WDF USB Reference](/windows-hardware/drivers/ddi/wdfusb/) and [UMDF USB I/O Target Interfaces](/windows-hardware/drivers/ddi/wudfddi/).

## Development tools

The Windows Driver Kit (WDK) contains resources that are required for driver development, such as headers, libraries, tools, and samples.

- [Download the Windows Driver Kit (WDK)](../download-the-wdk.md)

## USB programming reference

Gives specifications for I/O requests, support routines, structures, and interfaces used by USB client drivers. Those routines and related data structures are defined in the WDK headers.

- [Universal Serial Bus (USB) programming reference](/windows-hardware/drivers/ddi/_usbref/#common-usb-client-driver-reference)

## USB driver samples

Use these samples to get started with USB client driver programming.

- [Usbsamp Generic USB Driver](/samples/microsoft/windows-driver-samples/usbsamp-generic-usb-driver/)
- [Sample KMDF Function Driver for OSR USB-FX2](/samples/microsoft/windows-driver-samples/sample-kmdf-function-driver-for-osr-usb-fx2/)
- [Sample UMDF Function Driver for OSR USB-FX2 (UMDF Version 1)](../wdf/user-mode-driver-framework-design-guide.md)
- [Sample Function Driver for OSR USB-FX2 (UMDF Version 2)](/samples/microsoft/windows-driver-samples/sample-function-driver-for-osr-usb-fx2-umdf-version-2/)

## Related standards and specifications

You can download official USB specifications from the [Universal Serial Bus Document Library](https://www.usb.org/documents) website. This website contains links to various revisions of Universal Serial Bus specifications.

## Documentation sections

- [Getting started with USB client driver development](getting-started-with-usb-client-driver-development.md)<br/>Introduces you to USB driver development. Provides information about choosing the most appropriate model for providing a USB driver for your device. Write, build, and install your first skeleton user-mode and kernel-mode USB drivers by using the USB templates included with Microsoft Visual Studio.

- [USB host-side drivers in Windows](usb-3-0-driver-stack-architecture.md)<br/>Provides an overview of the USB driver stack architecture.

- [About USB Block Requests (URBs)](communicating-with-a-usb-device.md)<br/>Learn how a client driver builds a variable-length data structure called a USB Request Block (URB) to submit requests to the USB driver stack.

- [USB descriptors](usb-descriptors.md)<br/>Learn how a client driver builds a variable-length data structure called a USB Request Block (URB) to submit requests to the USB driver stack.

- [Selecting a USB configuration in USB drivers](configuring-usb-devices.md)<br/>Device configuration refers to the tasks that the client driver performs to select a USB configuration and an alternate interface in each interface. The section shows the method calls required to select a USB configuration.

- [Sending USB data transfers in USB client drivers](usb-device-i-o.md)<br/>Describes USB pipes, URBs for I/O requests, and how a client driver can use the device driver interfaces (DDIs) to transfer data to and from a USB device.

- [Implementing power management in USB client drivers](usb-power-management.md)<br/>Use the power management abilities of USB devices that comply with the Universal Serial Bus (USB) specification have a rich and complex set of power management features.

## Related topics

- [Universal Serial Bus (USB)](../index.yml)