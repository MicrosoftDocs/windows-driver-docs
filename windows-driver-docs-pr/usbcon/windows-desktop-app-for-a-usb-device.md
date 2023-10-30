---
description: Learn about how an application can call WinUSB Functions to communicate with a USB device.
title: Windows desktop app for a USB device
ms.date: 10/28/2022
---

# Windows desktop app for a USB device

In this article, you'll learn about how an application can call [WinUSB functions](using-winusb-api-to-communicate-with-a-usb-device.md) to communicate with a USB device. For such an application, [WinUSB](winusb.md) (Winusb.sys) must be installed as the device's function driver. WinUSB in the device's kernel-mode stack. This driver is included in Windows in the \\Windows\\System32\\drivers folder.

If you're using Winusb.sys as a USB device's function driver, you can call [WinUSB functions](using-winusb-api-to-communicate-with-a-usb-device.md) from an application to communicate with the device. These functions, exposed by the user-mode DLL Winusb.dll, simplify the communication process. Instead of constructing device I/O control requests to perform standard USB operations (such as configuring the device, sending control requests, and transferring data to or from the device), applications call the equivalent WinUSB function.

Winusb.dll uses the application-supplied data to construct the appropriate device I/O control request, and then sends the request to Winusb.sys for processing. To communicate with the USB stack, the WinUSB function calls the [**DeviceIoControl**](/windows/desktop/api/ioapiset/nf-ioapiset-deviceiocontrol) function with the appropriate IOCTL that correlates to the application's request. When the request is complete, the WinUSB function passes any information returned by Winusb.sys (such as data from a read request) back to the calling process. If the call to **DeviceIoControl** is successful, it returns a nonzero value. If the call fails or is pending (not processed immediately), **DeviceIoControl** returns a zero value. If an error occurs, the application can call [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror) for a more detailed error message.

It's simpler to use WinUSB functions to communicate with a device than to implement a driver. However, note the following limitations:

- WinUSB functions allow one application at a time to communicate with the device. If you require more than one application to communicate concurrently with a device, you must implement a function driver.

- Before Windows 8.1, WinUSB functions don't support streaming data to or from isochronous endpoints.

- WinUSB functions don't support devices that already have kernel-mode support. Examples of such devices include modems and network adapters, which are supported by the telephony API (TAPI) and NDIS, respectively.

- For multifunction devices, you can use the device's INF file to specify either an in-box kernel-mode driver or Winusb.sys for each USB function separately. However, you can specify only one of these options for a particular function, not both.

> [!NOTE]
> WinUSB functions require Windows XP or later. You can use these functions in your C/C++ application to communicate with your USB device. To write a UWP app that uses WinUSB APIs, see [UWP app for a USB device](writing-usb-device-companion-apps-for-microsoft-store.md).

## Getting started

1. Get the tools required to write a Windows desktop app for devices

    - Follow the instructions at [Downloading the Windows Driver Kit](../download-the-wdk.md).

2. Get a test USB device and its hardware specification.

    - Use the specification to determine the functionality of the app and the related design decisions.

    - Microsoft USB Test Tool (MUTT) devices are available from [JJG Technologies](http://www.jjgtechnologies.com/Mutt20.htm). This device requires firmware from Microsoft available at [Download MUTT Software Package](./mutt-software-package.md#download-mutt-software-package).

3. Write a skeleton app that obtains a handle to the device.

    There are two approaches for writing the first application:

    - Write based on the WinUSB template included in Visual Studio. For more information, see [Write a Windows desktop app based on the WinUSB template](how-to-write-a-windows-desktop-app-that-communicates-with-a-usb-device.md).

    - Call [SetupAPI](../install/setupapi.md) routines to get a handle to the device and open it by calling [WinUsb_Initialize](/windows/desktop/api/winusb/nf-winusb-winusb_initialize). For more information, see [How to Access a USB Device by Using WinUSB Functions](using-winusb-api-to-communicate-with-a-usb-device.md).

4. Install Winusb.sys for your device.

    If using Visual Studio, install the driver package on the target computer by using Visual Studio deployment. For instructions see [Write a Windows desktop app based on the WinUSB template](how-to-write-a-windows-desktop-app-that-communicates-with-a-usb-device.md). Otherwise manually install the driver in Device Manager by writing a custom INF. For more information, see [WinUSB (Winusb.sys) Installation](winusb-installation.md).

5. Get information about your device and view its descriptors.

    For conceptual information, see [Concepts for all USB developers](usb-concepts-for-all-developers.md). Get information about your device capabilities by reading the configuration descriptor, interface descriptors for each supported alternate settings, and their endpoint descriptors. For more information, see [Query the Device for USB Descriptors](using-winusb-api-to-communicate-with-a-usb-device.md#step-2-query-the-device-for-usb-descriptors).

6. Send a USB control transfer.

    Send standard control requests and vendor commands to your device. For more information, see [Send Control Transfer to the Default Endpoint](using-winusb-api-to-communicate-with-a-usb-device.md#step-3-send-control-transfer-to-the-default-endpoint).

7. Send bulk or interrupt transfers.

    Perform read and write operations to and from the bulk, interrupt, and isochronous endpoints supported by your device. For more information, see [Issue I/O Requests](using-winusb-api-to-communicate-with-a-usb-device.md#step-4-issue-io-requests).

8. Send isochronous transfers.

    Send isochronous read and write requests, mostly used for streaming data. This feature is only available on Windows 8.1 and later. For more information, see [Sending USB isochronous transfers from a WinUSB desktop app](getting-set-up-to-use-windows-devices-usb.md).

## See also

[Developing Windows applications for USB devices](developing-windows-applications-that-communicate-with-a-usb-device.md)  

[Universal Serial Bus (USB)](../index.yml)
