---
title: UWP App for a USB Device
description: The Windows.Devices.Usb namespace provides APIs to communicate with an external USB device.
ms.date: 01/17/2024
---

# UWP app for a USB device

The **[Windows.Devices.Usb](/uwp/api/Windows.Devices.Usb)** namespace provides a way for a Windows app to communicate with an external USB device that uses WinUSB (Winusb.sys) as the device driver.

## In this section

| Article | Description |
|---|---|
| [Talking to USB devices, start to finish (UWP app)](talking-to-usb-devices-start-to-finish.md) | Use the Windows Runtime APIs, introduced in Windows 8.1, to write UWP apps that give users access to their peripheral USB device. Such apps can connect to a device based on user-specified criteria, get information about the device, send data to the device and conversely get data steams from the device, and poll the device for interrupt data. |
| [How to add USB device capabilities to the app manifest](updating-the-app-manifest-with-usb-device-capabilities.md) | This article describes the device capabilities that are required for a Windows app that uses the **[Windows.Devices.Usb](/uwp/api/Windows.Devices.Usb)** namespace. |
| [How to connect to a USB device (UWP app)](how-to-connect-to-a-usb-device--uwp-app-.md) | In Windows 8.1, you can write a UWP app that interacts with a USB device. The app can send control commands, get device information, and read and write data to/from bulk and interrupt endpoints. Before you can do all that, you must find the device and establish connection.<br><br>In this part, you learn how to use the **[DeviceWatcher](/uwp/api/Windows.Devices.Enumeration.DeviceWatcher)** object to find the device and then open it to start communicating from your app. You also learn how to close the device when you're finished using it. |
| [How to send a USB control transfer (UWP app)](how-to-send-a-usb-control-transfer--uwp-app-.md) | An app that communicates with a USB device usually sends several control transfers requests. Those requests get information about the device and send control commands defined by the hardware vendor. In this article, you learn about control transfers and how to format and send them in your UWP app. |
| [How to send a USB interrupt transfer request (UWP app)](how-to-send-a-usb-interrupt-transfer--uwp-app-.md) | A USB device can support interrupt endpoints so that it can send or receive data at regular intervals. To accomplish that, the host polls the device at regular intervals and data is transmitted each time the host polls the device. Interrupt transfers are mostly used for getting interrupt data from the device. This article describes how a UWP app can get continuous interrupt data from the device. |
| [How to send a USB bulk transfer request (UWP app)](how-to-send-a-usb-bulk-transfer--uwp-app-.md) | In this article, you learn about a USB bulk transfer and how to initiate a transfer request from your UWP app that communicates with a USB device. |
| [How to get USB descriptors (UWP app)](how-to-get-usb-descriptors--uwp-app-.md) | One of the main tasks of interacting with a USB device is to get information about it. All USB devices provide information in the form of several data structures called descriptors. This article describes how a UWP app can get descriptors from the device at the endpoint, interface, configuration, and device level. |
| [How to select a USB interface setting (UWP app)](how-to-select-a-usb-interface-setting--uwp-app-.md) | In this article, you learn about changing a setting within a USB interface. You use the **[UsbInterfaceSetting](/uwp/api/Windows.Devices.Usb.UsbInterfaceSetting)** object to get the current setting and set a setting in the interface. |

## USB samples

- [Custom USB device access sample](/samples/browse/)
- [USB CDC Control sample](/samples/browse/)
- [Firmware Update USB Device sample](/samples/browse/)

## What are the limitations of the namespace?

You *can't* use **[Windows.Devices.Usb](/uwp/api/Windows.Devices.Usb)** in these cases:

- If the device driver isn't Winusb.sys.

- You want to communicate with USB isochronous endpoints of the device.

- You want to communicate streams of a SuperSpeed bulk endpoint. For those endpoints, the USB Windows Runtime classes for bulk transfers can only send or receive data from the first stream of the endpoint.

- You allow multiple apps to concurrently access the device.

- Your USB device is an internal device.

    > [!NOTE]
    > The APIs are primarily designed for accessing peripheral devices. The API can also access PC internal USB devices. However access to PC internal USB devices from a UWP app is limited to a privileged app that is explicitly declared by the OEM for that PC.

- The kernel-mode device stack has a filter driver above Winusb.sys.

    > [!NOTE]
    > This scenario is available to privileged apps only.

- Your device has multiple USB configurations, and you want to select a configuration, other than the first. **[Windows.Devices.Usb](/uwp/api/Windows.Devices.Usb)** selects the first configuration by default.

## Related topics

- **[Windows.Devices.Usb](/uwp/api/Windows.Devices.Usb)**
