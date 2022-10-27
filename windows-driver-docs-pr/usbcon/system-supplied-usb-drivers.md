---
title: Overview of Microsoft-provided USB drivers
description: This topics in this section describe the class drivers, generic client driver, and the parent composite driver that are provided by Microsoft.
ms.date: 10/27/2022
---

# Overview of Microsoft-provided USB drivers

This topics in this section describe the class drivers, generic client driver, and the parent composite driver that are provided by Microsoft.

## Microsoft-provided USB drivers for controllers and hubs

Microsoft provides these set of drivers:

- For USB host controllers and hubs. For more information, see [USB host-side drivers in Windows](usb-3-0-driver-stack-architecture.md). You can develop a custom host controller driver that communicates with the USB host controller extension (UCX) driver. For more information, see [Developing Windows drivers for USB host controllers](developing-windows-drivers-for-usb-host-controllers.md).

- For handling common function logic for USB devices. For more information, see [USB device-side drivers in Windows](usb-device-side-drivers-in-windows.md).

- For supporting Type-C connectors. For more information, see [USB connector manager class extension (UcmCx)](/previous-versions/windows/hardware/drivers/mt188011(v=vs.85)).

## Other Microsoft-provided USB drivers

|Device setup class|Microsoft-provided driver and INF|Windows support|Description|
|--- |--- |--- |--- |
|USB|Usbccgp.sys</br></br>Usb.inf|Windows 11</br></br>Windows 10</br></br>Windows 8.1|Usbccgp.sys is a parent driver for composite devices that supports multiple functions. For more information, see [USB Generic Parent Driver (Usbccgp.sys)](usb-common-class-generic-parent-driver.md).|
|Biometric|WudfUsbBID.dll</br></br>WudfUsbBIDAdvanced.inf|Windows 8.1|Microsoft supports USB biometric devices by providing the [Windows Biometric Framework](/windows/win32/secbiomet/biometric-service-api-portal).|
|USBDevice|Winusb.sys</br></br>Winusb.inf|Windows 11</br></br>Windows 10</br></br>Windows 8.1|Winusb.sys can be used as the USB device's function driver instead of implementing a driver. See [WinUSB](how-to-write-a-windows-desktop-app-that-communicates-with-a-usb-device.md).|


## Microsoft-provided USB device class drivers

Microsoft provides drivers for several USB device classes approved by USB-IF. These drivers and their installation files are included in Windows. They are available in the \\Windows\\System32\\DriverStore\\FileRepository folder.

See, [USB device class drivers included in Windows](supported-usb-classes.md).

## Related topics

- [Universal Serial Bus (USB)](../index.yml)  
- [USB Driver Development Guide](usb-driver-development-guide.md)
