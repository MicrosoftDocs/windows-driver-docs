---
Description: Here are the new features and improvements for Universal Serial Bus (USB) in Windows 8.1.
title: Windows 8.1 - What's new for USB
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Windows 8.1: What's new for USB


Here are the new features and improvements for Universal Serial Bus (USB) in Windows 8.1.

-   [Windows Runtime USB API for developing UWP apps](#usb-sdk)
-   [Microsoft OS 2.0 descriptors for improved device enumeration](#microsoft-os-2-0-descriptors-for-improved-device-enumeration)
-   [Isochronous support for WinUSB](#usb-wdk)
-   [USB driver stack improvements](#usb-driver-stack-improvements)
-   [USB tests in the Hardware Certification Kit (HCK)](#usb-tests-in-the-hardware-certification-kit-hck)
-   [Improved USB diagnostic tools and debugger extensions](#improved-usb-diagnostic-tools-and-debugger-extensions-)
-   [Related topics](#related-topics)

## Windows Runtime USB API for developing UWP apps


Windows Runtime provides a new namespace: [**Windows.Devices.Usb**](https://msdn.microsoft.com/library/windows/apps/dn278466) (see [Writing apps for USB devices (UWP apps using C#/VB/C++)](https://msdn.microsoft.com/library/windows/apps/xaml/dn263144) for a brief overview). By using the namespace, you can write a UWP app that talks to a custom USB device.

For more information, see these topics:

-   [Talking to USB devices, start to finish (UWP app)](talking-to-usb-devices-start-to-finish.md)
-   [How to add USB device capabilities to the app manifest](updating-the-app-manifest-with-usb-device-capabilities.md)
-   [How to connect to a USB device (UWP app)](how-to-connect-to-a-usb-device--uwp-app-.md)
-   [How to send a USB control transfer (UWP app)](how-to-send-a-usb-control-transfer--uwp-app-.md)
-   [How to send a USB interrupt transfer request (UWP app)](how-to-send-a-usb-interrupt-transfer--uwp-app-.md)
-   [How to send a USB bulk transfer request (UWP app)](how-to-send-a-usb-bulk-transfer--uwp-app-.md)
-   [How to get USB descriptors (UWP app)](how-to-get-usb-descriptors--uwp-app-.md)
-   [How to select a USB interface setting (UWP app)](how-to-select-a-usb-interface-setting--uwp-app-.md)

These samples demonstrate the use of the [**Windows.Devices.Usb**](https://msdn.microsoft.com/library/windows/apps/dn278466) namespace.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>UWP app sample</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="" id="custom-usb-device-access-sample"></a><a href="http://go.microsoft.com/fwlink/p/?linkid=309716" data-raw-source="[Custom USB device access sample](http://go.microsoft.com/fwlink/p/?linkid=309716)">Custom USB device access sample</a></p></td>
<td><p>This sample shows how to communicate with a USB device. The sample can communicate with the OSR USB FX2 learning kit and the SuperMUTT device.</p></td>
</tr>
<tr class="even">
<td><p><a href="" id="usb-cdc-control-sample"></a><a href="http://go.microsoft.com/fwlink/p/?linkid=309716" data-raw-source="[USB CDC Control sample](http://go.microsoft.com/fwlink/p/?linkid=309716)">USB CDC Control sample</a></p></td>
<td><p>This sample shows how to communicate with a USB CDC (Communications Device Class) device and sends and receives data through serial ports, such as a USB serial converter cable.</p></td>
</tr>
<tr class="odd">
<td><p><a href="" id="firmware-update-usb-device-sample"></a><a href="http://go.microsoft.com/fwlink/p/?linkid=309716" data-raw-source="[Firmware Update USB Device sample](http://go.microsoft.com/fwlink/p/?linkid=309716)">Firmware Update USB Device sample</a></p></td>
<td><p>This sample shows how a UWP app can update the firmware of a USB device. The update operation runs as a background task.</p></td>
</tr>
</tbody>
</table>

## Microsoft OS 2.0 descriptors for improved device enumerations 
 
Microsoft OS 2.0 descriptors improve device identification and driver installation experience.

MS OS 2.0 descriptors specification provides these improvements:

-   Defines a new BOS device capability descriptor to allow devices to return platform-specific properties. The BOS descriptor is a standard descriptor defined by the standard USB specification for USB versions 2.1 and greater, so retrieval is a normal and an expected enumeration step that should not lead to unintended device behavior.
-   Allows descriptors to be scoped to an entire device, a specific configuration, or a function.
-   Allows devices to return multiple descriptor sets where each set applies to a specific range of Windows version. This enables devices to enumerate differently depending on the version of Windows on the system to which it is attached.
-   Faster Resume: Device can identify its resume time, which reduces time from suspend state.

For information about the specification, see [Microsoft OS Descriptors for USB Devices](microsoft-defined-usb-descriptors.md).

## Isochronous support for WinUSB


The Microsoft-provided WinUSB (kernel-mode driver) now supports transfers to and from isochronous endpoints of a USB device

The user-mode DLL, Winusb.dll, exposes these [WinUSB Functions](https://msdn.microsoft.com/library/windows/hardware/ff540046#winusb) that a Windows desktop app can use to initiate such transfers.

-   [**WinUsb\_RegisterIsochBuffer**](https://msdn.microsoft.com/library/windows/hardware/dn265566)
-   [**WinUsb\_UnregisterIsochBuffer**](https://msdn.microsoft.com/library/windows/hardware/dn265567)
-   [**WinUsb\_WriteIsochPipeAsap**](https://msdn.microsoft.com/library/windows/hardware/dn265569)
-   [**WinUsb\_ReadIsochPipeAsap**](https://msdn.microsoft.com/library/windows/hardware/dn265565)
-   [**WinUsb\_WriteIsochPipe**](https://msdn.microsoft.com/library/windows/hardware/dn265568)
-   [**WinUsb\_ReadIsochPipe**](https://msdn.microsoft.com/library/windows/hardware/dn265564)
-   [**WinUsb\_GetCurrentFrameNumber**](https://msdn.microsoft.com/library/windows/hardware/dn265549)
-   [**WinUsb\_GetAdjustedFrameNumber**](https://msdn.microsoft.com/library/windows/hardware/dn265548)

## USB driver stack improvements


In Windows 8.1, the performance and reliability of both USB 3.0 and 2.0 driver stacks have been improved.

-   For newer platforms that support InstantGo, the overall system power consumption in S0 can be extremely low. For such a system, even the few milliwatts that a USB device consumes while in selective suspend, starts to matter. With the goal of optimizing power for the new systems, we have implemented D3cold for USB 2.0 stack and Usbccgp.sys and improved Windows 8 implementation of USB 3.0 driver stack.
-   Better power management when no driver is installed. The USB driver stack now suspend a USB port that causes the hub to suspend if it's the only device connected to the controller.
-   DPC performance has been improved to avoid watchdog timeout crashes.
-   Devices can now recover faster than the default 10 millisecond specified in the USB 2.0 specification. Also, the host controller driver asserts resume signaling for less than the 20 milliseconds required in the USB 2.0 specification.
-   USB 3.0 driver stack is now more reliable when performing control, bulk, and isochronous data transfers.

## USB tests in the Hardware Certification Kit (HCK)

-   These USB tests in the Hardware Certification Kit (HCK) have been improved. The device enumeration tests now have a new parameter that reduces manual intervention during testing using simplified topologies. The suspend tests have been improved logging capabilities.

    -   [USB Exposed Port Controller Test](https://msdn.microsoft.com/library/windows/hardware/hh998021.aspx)
    -   [USB Hub Exposed Port Test USB](https://msdn.microsoft.com/library/windows/hardware/jj123960.aspx)
    -   [Hub Selective Suspend Test](https://msdn.microsoft.com/library/windows/hardware/jj124844.aspx)
    -   [USB Exposed Port System Test](https://msdn.microsoft.com/library/windows/hardware/jj123655.aspx)
    -   [USB Selective Suspend Test (xHCI)](https://msdn.microsoft.com/library/windows/hardware/jj124491.aspx)
    -   [USB 3.0 Suspend Test](https://msdn.microsoft.com/library/windows/hardware/jj125210.aspx)
-   MUTT and SuperMUTT devices are now USB-IF compliance devices. The devices and the accompanying software package are integrated in to the HCK suite of USB tests. They provide automated testing that can be used during the development cycle of USB controllers, devices and systems, especially stress testing.

    MUTT hardware can be purchased from [JJG Technologies](http://jjgtechnologies.com/mutt.md). The device does not have installed firmware installed. To install firmware, download the MUTT software package from [this Web site](https://msdn.microsoft.com/windows/hardware/jj590752) and run MUTTUtil.exe. For more information, see the documentation included with the package.

## Improved USB diagnostic tools and debugger extensions


-   Kernel debugging extensions for USB 2.0 and 3.0 (USBKD.dll and USB3KD.dll) have been improved to have similar command pattern. Debugger extension for Usbccgp.sys is now available.
-   USB events shown in the Message Analyzer (Netmon) are now more descriptive. The events can also be grouped and sorted by controller, hub, and so on.

## Related topics
[Universal Serial Bus (USB)](https://msdn.microsoft.com/library/windows/hardware/ff538930)  



