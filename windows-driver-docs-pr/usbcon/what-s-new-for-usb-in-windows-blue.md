---
title: Windows 8.1 - What's New for USB
description: Here are the new features and improvements for Universal Serial Bus (USB) in Windows 8.1.
ms.date: 01/17/2024
---

# Windows 8.1: What's new for USB

Here are the new features and improvements for Universal Serial Bus (USB) in Windows 8.1.

## Windows Runtime USB API for developing UWP apps

Windows Runtime provides a new namespace: **[Windows.Devices.Usb](/uwp/api/Windows.Devices.Usb)** (see [Writing apps for USB devices (UWP apps using C#/VB/C++)](/previous-versions/windows/apps/dn263144(v=win.10)) for a brief overview). By using the namespace, you can write a UWP app that talks to a custom USB device.

For more information, see these articles:

- [Talking to USB devices, start to finish (UWP app)](talking-to-usb-devices-start-to-finish.md)
- [How to add USB device capabilities to the app manifest](updating-the-app-manifest-with-usb-device-capabilities.md)
- [How to connect to a USB device (UWP app)](how-to-connect-to-a-usb-device--uwp-app-.md)
- [How to send a USB control transfer (UWP app)](how-to-send-a-usb-control-transfer--uwp-app-.md)
- [How to send a USB interrupt transfer request (UWP app)](how-to-send-a-usb-interrupt-transfer--uwp-app-.md)
- [How to send a USB bulk transfer request (UWP app)](how-to-send-a-usb-bulk-transfer--uwp-app-.md)
- [How to get USB descriptors (UWP app)](how-to-get-usb-descriptors--uwp-app-.md)
- [How to select a USB interface setting (UWP app)](how-to-select-a-usb-interface-setting--uwp-app-.md)

These samples demonstrate the use of the **[Windows.Devices.Usb](/uwp/api/Windows.Devices.Usb)** namespace.

| UWP app sample | Description |
|---|---|
| [Custom USB device access sample](/samples/browse/) | This sample shows how to communicate with a USB device. The sample can communicate with the OSR USB FX2 learning kit and the SuperMUTT device. |
| [USB CDC Control sample](/samples/browse/) | This sample shows how to communicate with a USB CDC (Communications Device Class) device and sends and receives data through serial ports, such as a USB serial converter cable. |
| [Firmware Update USB Device sample](/samples/browse/) | This sample shows how a UWP app can update the firmware of a USB device. The update operation runs as a background task. |

## Microsoft OS 2.0 descriptors for improved device enumerations

Microsoft OS 2.0 descriptors improve device identification and driver installation experience.

MS OS 2.0 descriptors specification provides these improvements:

- Defines a new BOS device capability descriptor to allow devices to return platform-specific properties. The BOS descriptor is a standard descriptor defined by the standard USB specification for USB versions 2.1 and greater, so retrieval is a normal and an expected enumeration step that shouldn't lead to unintended device behavior.
- Allows descriptors to be scoped to an entire device, a specific configuration, or a function.
- Allows devices to return multiple descriptor sets where each set applies to a specific range of Windows version. This enables devices to enumerate differently depending on the version of Windows on the system to which it's attached.
- Faster Resume: Device can identify its resume time, which reduces time from suspend state.

For information about the specification, see [Microsoft OS Descriptors for USB Devices](microsoft-defined-usb-descriptors.md).

## Isochronous support for WinUSB

The Microsoft-provided WinUSB (kernel-mode driver) now supports transfers to and from isochronous endpoints of a USB device

The user-mode DLL, Winusb.dll, exposes these [WinUSB functions](using-winusb-api-to-communicate-with-a-usb-device.md) that a Windows desktop app can use to initiate such transfers.

- **[WinUsb\_RegisterIsochBuffer](/windows/win32/api/winusb/nf-winusb-winusb_registerisochbuffer)**
- **[WinUsb\_UnregisterIsochBuffer](/windows/win32/api/winusb/nf-winusb-winusb_unregisterisochbuffer)**
- **[WinUsb\_WriteIsochPipeAsap](/windows/win32/api/winusb/nf-winusb-winusb_writeisochpipeasap)**
- **[WinUsb\_ReadIsochPipeAsap](/windows/win32/api/winusb/nf-winusb-winusb_readisochpipeasap)**
- **[WinUsb\_WriteIsochPipe](/windows/win32/api/winusb/nf-winusb-winusb_writeisochpipe)**
- **[WinUsb\_ReadIsochPipe](/windows/win32/api/winusb/nf-winusb-winusb_readisochpipe)**
- **[WinUsb\_GetCurrentFrameNumber](/windows/win32/api/winusb/nf-winusb-winusb_getcurrentframenumber)**
- **[WinUsb\_GetAdjustedFrameNumber](/windows/win32/api/winusb/nf-winusb-winusb_getadjustedframenumber)**

## USB driver stack improvements

In Windows 8.1, the performance and reliability of both USB 3.0 and 2.0 driver stacks have been improved.

- For newer platforms that support InstantGo, the overall system power consumption in S0 can be low. For such a system, even the few milliwatts that a USB device consumes while in selective suspend, starts to matter. With the goal of optimizing power for the new systems, we have implemented D3cold for USB 2.0 stack and Usbccgp.sys and improved Windows 8 implementation of USB 3.0 driver stack.
- Better power management when no driver is installed. The USB driver stack now suspends a USB port that causes the hub to suspend if it's the only device connected to the controller.
- DPC performance has been improved to avoid watchdog timeout crashes.
- Devices can now recover faster than the default 10 millisecond specified in the USB 2.0 specification. Also, the host controller driver asserts resume signaling for less than the 20 milliseconds required in the USB 2.0 specification.
- USB 3.0 driver stack is now more reliable when performing control, bulk, and isochronous data transfers.

## USB tests in the Hardware Certification Kit (HCK)

- These USB tests in the Hardware Certification Kit (HCK) have been improved. The device enumeration tests now have a new parameter that reduces manual intervention during testing using simplified topologies. The suspend tests have been improved logging capabilities.

  - [USB Exposed Port Controller Test](/previous-versions/windows/hardware/hck/hh998021(v=vs.85))
  - [USB Hub Exposed Port Test USB](/previous-versions/windows/hardware/hck/jj123960(v=vs.85))
  - [Hub Selective Suspend Test](/previous-versions/windows/hardware/hck/jj124844(v=vs.85))
  - [USB Exposed Port System Test](/previous-versions/windows/hardware/hck/jj123655(v=vs.85))
  - [USB Selective Suspend Test (xHCI)](/previous-versions/windows/hardware/hck/jj124491(v=vs.85))
  - [USB 3.0 Suspend Test](/previous-versions/windows/hardware/hck/jj125210(v=vs.85))
- MUTT and SuperMUTT devices are now USB-IF compliance devices. The devices and the accompanying software package are integrated in to the HCK suite of USB tests. They provide automated testing that can be used during the development cycle of USB controllers, devices and systems, especially stress testing.

    MUTT hardware can be purchased from [JJG Technologies](http://www.jjgtechnologies.com/mutt.htm). The device doesn't have installed firmware installed. To install firmware, download the MUTT software package from [this Web site](./index.md) and run MUTTUtil.exe. For more information, see the documentation included with the package.

## Improved USB diagnostic tools and debugger extensions

- Kernel debugging extensions for USB 2.0 and 3.0 (USBKD.dll and USB3KD.dll) have been improved to have similar command pattern. Debugger extension for Usbccgp.sys is now available.
- USB events shown in the Message Analyzer (Netmon) are now more descriptive. The events can also be grouped and sorted by controller, hub, and so on.

## Related topics

- [Universal Serial Bus (USB)](../index.yml)
