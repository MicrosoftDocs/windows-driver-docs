---
title: Overview of developing Windows applications for USB devices
description: This article provides guidelines for deciding whether you should write a UWP app or a Windows desktop app to communicate with a USB device.
ms.date: 02/06/2023
---

# Overview of developing Windows applications for USB devices

Summary:

- Guidelines for choosing the right programming model
- UWP app and desktop app developer experience

Important APIs:

- **[Windows.Devices.Usb](/uwp/api/Windows.Devices.Usb)**
- [WinUSB Functions](using-winusb-api-to-communicate-with-a-usb-device.md)

This article provides guidelines for deciding whether you should write a UWP app or a Windows desktop app to communicate with a USB device.

Windows provides API sets that you can use to write apps that talk to custom USB devices. The API performs common USB-related tasks such as, finding the device, data transfers.

Custom device in this context means, a device for which Microsoft doesn't provide an in-box class driver. Instead, you can install WinUSB (Winusb.sys) as the device driver.

## Choosing a programming model

If you install [Winusb.sys](winusb-installation.md), here are the programming model options:

- [UWP app for a USB device](writing-usb-device-companion-apps-for-microsoft-store.md)

  Windows 8.1 provides the **[Windows.Devices.Usb](/uwp/api/Windows.Devices.Usb)** namespace that can't be used in earlier versions of Windows. For other Microsoft Store resources, see the [Universal Windows Platform documentation](/windows/uwp/).

- [Windows desktop app for a USB device](windows-desktop-app-for-a-usb-device.md)

  Before Windows 8.1, apps that were communicating through [Winusb.sys](winusb-installation.md), were desktop apps written by using [WinUSB Functions](using-winusb-api-to-communicate-with-a-usb-device.md). In Windows 8.1, the API set was extended. For more information on Windows app development, see [Develop for Windows](https://developer.microsoft.com/windows/).

The strategy for choosing the best programming model depends on various factors.

- **Will your app communicate with an internal USB device?**

  The APIs are primarily designed for accessing peripheral devices. The API can also access PC internal USB devices. However access to PC internal USB devices from a UWP app is limited to a privileged app that is explicitly declared in device metadata by the OEM for that PC.

- **Will your app communicate with USB isochronous endpoints?**

  If your app transmits data to or from isochronous endpoints of the device, you must write a Windows desktop app. In Windows 8.1, new [WinUSB Functions](using-winusb-api-to-communicate-with-a-usb-device.md) have been added to the API set that allows a desktop app to send data to and receive data from isochronous endpoints.

- **Is your app a "control panel" type of app?**

  UWP apps are per-user apps and don't have the ability to make changes outside the scope of each app. For these types of apps, you must write a Windows desktop app.

- **Is the USB device class supported classes by UWP apps?**

  Write a UWP app if your device belongs to one these device classes.

  - `name:cdcControl,           classId:02 * *`
  - `name:physical,             classId:05 * *`
  - `name:personalHealthcare,   classId:0f 00 00`
  - `name:activeSync,           classId:ef 01 01`
  - `name:palmSync,             classId:ef 01 02`
  - `name:deviceFirmwareUpdate, classId:fe 01 01`
  - `name:irda,                 classId:fe 02 00`
  - `name:measurement,          classId:fe 03 *`
  - `name:vendorSpecific,       classId:ff * *`

   > [!NOTE]
   > If your device belongs to DeviceFirmwareUpdate class, your app must be a privileged app.

If your device doesn't belong to one the preceding device classes, write a Windows desktop app.

## Driver requirement

| Driver requirement | UWP app | Windows desktop app |
|---|---|---|
| Function driver | Microsoft-provided [Winusb.sys](winusb-installation.md) (kernel-mode driver). | Microsoft-provided [Winusb.sys](winusb-installation.md) (kernel-mode driver). |
| Filter driver | If filter drivers are present, access is limited to privileged apps. The app is declared as privileged apps in device metadata by the OEM. | Filter driver can be present in the kernel mode device stack as long as it doesn't block access to [Winusb.sys](winusb-installation.md). |

## Code samples

| Sample | UWP app | Windows desktop app |
|---|---|---|
| Get started with these samples | <ul><li>[Custom USB device access sample](/samples/browse/)</li><li>[USB CDC Control sample](/samples/browse/)</li><li>[Firmware Update USB Device sample](/samples/browse/)</li></ul> | <ul><li>Start with the **WinUsb Application** template included with Microsoft Visual Studio (Ultimate or Professional)</li><li>Extend the template by using code examples shown in [How to Access a USB Device by Using WinUSB Functions](using-winusb-api-to-communicate-with-a-usb-device.md).</li></ul> |

## Development tools

| Development tools | UWP app | Windows desktop app |
|---|---|---|
| Developer environment | Microsoft Visual Studio 2013<br/><br/>Microsoft Windows Software Development Kit (SDK) for Windows 8.1 | Use **WinUSB Application** template included with Visual Studio (Ultimate or Professional) and Windows Driver Kit (WDK) 8 or later. <br/><br/>For isochronous transfers, Visual Studio 2013 with Windows Driver Kit (WDK) 8.1 or later. |
| Programming languages | C#, VB.NET, C++, JavaScript | C/C++ |

## Feature implementation

| Key scenario | UWP app | Windows desktop app |
|---|---|---|
| Device discovery | Use **[Windows.Devices.Enumeration](/uwp/api/Windows.Devices.Enumeration)** namespace to get a **[UsbDevice](/uwp/api/Windows.Devices.Usb.UsbDevice)**. | Use [SetupAPI](../install/setupapi.md) and **[WinUsb_Initialize](/windows/win32/api/winusb/nf-winusb-winusb_initialize)** to get a WINUSB_INTERFACE_HANDLE. |
| USB control transfer | **[UsbSetupPacket](/uwp/api/Windows.Devices.Usb.UsbSetupPacket)**<br/>**[UsbControlRequestType](/uwp/api/Windows.Devices.Usb.UsbControlRequestType)**<br/>**[UsbDevice.SendControlInTransferAsync](/uwp/api/Windows.Devices.Usb.UsbDevice#Windows_Devices_Usb_UsbDevice_SendControlInTransferAsync_Windows_Devices_Usb_UsbSetupPacket_Windows_Storage_Streams_IBuffer_)**<br/>**[UsbDevice.SendControlOutTransferAsync](/uwp/api/Windows.Devices.Usb.UsbDevice#Windows_Devices_Usb_UsbDevice_SendControlOutTransferAsync_Windows_Devices_Usb_UsbSetupPacket_)** | **[WINUSB_SETUP_PACKET](/windows/win32/api/winusb/ns-winusb-winusb_setup_packet)**<br/>**[WinUsb_ControlTransfer](/windows/win32/api/winusb/nf-winusb-winusb_controltransfer)** |
| Getting USB descriptors | **[UsbDevice.DeviceDescriptor](/uwp/api/Windows.Devices.Usb.UsbDevice#Windows_Devices_Usb_UsbDevice_DeviceDescriptor)**<br/>**[UsbConfiguration.Descriptors](/uwp/api/Windows.Devices.Usb.UsbConfiguration#Windows_Devices_Usb_UsbConfiguration_Descriptors)**<br/>**[UsbInterface.Descriptors](/uwp/api/Windows.Devices.Usb.UsbInterface#Windows_Devices_Usb_UsbInterface_Descriptors)**<br/>**[UsbEndpointDescriptor](/uwp/api/Windows.Devices.Usb.UsbEndpointDescriptor)** | **[WinUsb_GetDescriptor](/windows/win32/api/winusb/nf-winusb-winusb_getdescriptor)** |
| Sending USB bulk transfer | **[UsbBulkInPipe](/uwp/api/Windows.Devices.Usb.UsbBulkInPipe)**<br/>**[UsbBulkOutPipe](/uwp/api/Windows.Devices.Usb.UsbBulkOutPipe)** | **[WinUsb_ReadPipe](/windows/win32/api/winusb/nf-winusb-winusb_readpipe)**<br/>**[WinUsb_WritePipe](/windows/win32/api/winusb/nf-winusb-winusb_writepipe)** |
| Sending USB interrupt transfer | **[UsbInterruptInPipe](/uwp/api/Windows.Devices.Usb.UsbInterruptInPipe)**<br/>**[UsbInterruptOutPipe](/uwp/api/Windows.Devices.Usb.UsbInterruptOutPipe)** | **[WinUsb_ReadPipe](/windows/win32/api/winusb/nf-winusb-winusb_readpipe)**<br/>**[WinUsb_WritePipe](/windows/win32/api/winusb/nf-winusb-winusb_writepipe)** |
| Sending USB isochronous transfer | Not supported. | **[WinUsb_ReadIsochPipe](/windows/win32/api/winusb/nf-winusb-winusb_readisochpipe)**<br/>**[WinUsb_ReadIsochPipeAsap](/windows/win32/api/winusb/nf-winusb-winusb_readisochpipeasap)**<br/>**[WinUsb_WriteIsochPipe](/windows/win32/api/winusb/nf-winusb-winusb_writeisochpipe)**<br/>**[WinUsb_WriteIsochPipeAsap](/windows/win32/api/winusb/nf-winusb-winusb_writeisochpipeasap)** |
| Closing the device | **[UsbDevice.Close](/uwp/api/Windows.Devices.Usb.UsbDevice#Windows_Devices_Usb_UsbDevice_Close)** | **[WinUsb_Free](/windows/win32/api/winusb/nf-winusb-winusb_free)** |

## Documentation

| Documentation | UWP app | Windows desktop app |
|---|---|---|
| Programming guide | [Talking to USB devices, start to finish](talking-to-usb-devices-start-to-finish.md) | [How to Access a USB Device by Using WinUSB Functions](using-winusb-api-to-communicate-with-a-usb-device.md) |
| API reference | [**Windows.Devices.Usb**](/uwp/api/Windows.Devices.Usb) | [WinUSB Functions](using-winusb-api-to-communicate-with-a-usb-device.md) |

## Related topics

- [Universal Serial Bus (USB)](../index.yml)
