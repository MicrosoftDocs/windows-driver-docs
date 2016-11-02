---
title: Windows Pointer Device Overview
description: In Windows 8, a Windows pointer device refers to devices that support the pen, or touch, functionality.
ms.assetid: EC4BA3B0-F9B0-497C-9B71-97E415DFB45D
---

# Windows Pointer Device Overview


In Windows 8, a *Windows pointer device* refers to devices that support the pen, or touch, functionality. In the context of a Windows Pointer Device, a pen is a single contact point active stylus input, also known as tablet-pen that supports hovering. Touch functionality refers to a single finger contact point or two or more concurrent finger contacts.

## <span id="windows_pointer_devices"></span><span id="WINDOWS_POINTER_DEVICES"></span>Windows Pointer Devices


Windows pointer devices are expected to use the human interface device (HID) protocol in order to communicate with the host. The following documents include information about the protocol:

-   [Device Class Definition for Human Interface Devices (HID) Version 1.11](http://www.usb.org/developers/hidpage/HID1_11.pdf)

-   [HID Usage Tables](http://www.usb.org/developers/hidpage/Hut1_12v2.pdf)

-   [HID Over I2C Protocol Specification Version 1.0](http://msdn.microsoft.com/library/windows/hardware/hh852380)

Because Windows 8 includes an HID class driver and corresponding HID I2C and HID USB miniport drivers, you do not need to implement one. You only need to report the usages described in this white paper in the firmware for your pointer device. Windows will use your firmware and its own HID driver to enable touch and pointer capabilities for your device and furnish the Windows touch and pointer APIs with access to your device.

To report data for any type of integrated stylus, the input must be reported by using a pen Collection Application(CA) collection. Similarly, touch data should be reported by using a touch CA collection. External stylus devices should use the digitizer CA collection. Sample descriptors are included under [Implementing Top-Level Collections in Multi-touch Devices](implementing-top-level-collections-in-multitouch-devices.md) section for multi-touch devices.

## <span id="windows_hardware_certification"></span><span id="WINDOWS_HARDWARE_CERTIFICATION"></span>Windows Hardware Certification


As part of Windows 8 touch hardware certification, digitizers are required to appear to the Windows operating system as human interface device (HID) devices and follow the rules described in [Required HID Descriptors](required-descriptors.md#required_hid_descriptors).

 

 




