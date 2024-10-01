---
title: Overview of Microsoft-Provided USB Drivers
description: This article describes the class drivers, generic client driver, and the parent composite driver that are provided by Microsoft.
ms.date: 09/06/2024
---

# Overview of Microsoft-provided USB drivers

This article describes the class drivers, generic client driver, and the parent composite driver that are provided by Microsoft.

## Microsoft-provided USB drivers for controllers and hubs

Microsoft provides the following set of drivers:

- For USB host controllers and hubs, see [USB host-side drivers in Windows](usb-3-0-driver-stack-architecture.md). You can develop a custom host controller driver that communicates with the USB host controller extension (UCX) driver. For more information, see [Developing Windows drivers for USB host controllers](developing-windows-drivers-for-usb-host-controllers.md).

- For handling common function logic for USB devices, see [USB device-side drivers in Windows](usb-device-side-drivers-in-windows.md).

For supporting USB Type-C connectors, see [Type-C driver reference](/windows-hardware/drivers/ddi/_usbref/#type-c-driver-reference).

## Other Microsoft-provided USB drivers

| Device setup class | Microsoft-provided driver and INF | Windows support | Description |
|---|---|---|---|
| USB | Usbccgp.sys<br/><br/>Usb.inf | Windows 11<br/><br/>Windows 10 | Usbccgp.sys is a parent driver for composite devices that supports multiple functions. For more information, see [USB Generic Parent Driver (Usbccgp.sys)](usb-common-class-generic-parent-driver.md). |
| USBDevice | Winusb.sys<br/><br/>Winusb.inf | Windows 11<br/><br/>Windows 10 | Winusb.sys can be used as the USB device's function driver instead of implementing a driver. See [WinUSB](how-to-write-a-windows-desktop-app-that-communicates-with-a-usb-device.md). |

## Microsoft-provided USB device class drivers

Microsoft provides drivers for several USB device classes approved by USB-IF. The drivers and their installation files are included in Windows. They're available in the \\Windows\\System32\\DriverStore\\FileRepository folder. For more information, see [USB device class drivers included in Windows](supported-usb-classes.md).

Microsoft defines setup classes for most devices. IHVs and OEMs can define new device setup classes, but only if none of the existing classes apply. For more information, see [System-Defined Device Setup Classes Available to Vendors](../install/system-defined-device-setup-classes-available-to-vendors.md).

## USB driver frameworks

Microsoft provides a driver framework for some types of USB devices that do not have their own USB device class specification. Vendors who want to create these types of devices should develop a device driver that uses the specified framework for the device type.

Currently, Microsoft provides the following driver frameworks for the following USB devices:

- USB biometric devices

    Microsoft supports USB biometric devices (fingerprint readers) by providing the Windows Biometric Framework. For more information see [Biometric Framework overview](/windows/desktop/SecBioMet/biometric-framework-overview).

## See also

- [Universal Serial Bus (USB)](../index.yml)
- [USB Driver Development Guide](usb-driver-development-guide.md)
