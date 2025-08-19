---
title: HID Architecture
description: The architecture of the HID driver stack in Windows is built on the class driver named hidclass.sys.
ms.date: 06/26/2024
keywords:
- HID class driver
- hidclass.sys
- HID class driver for Windoows
ms.topic: concept-article
---

# HID architecture

The architecture of the HID driver stack in Windows is built on the class driver named *hidclass.sys*. Clients and transport minidrivers access the class driver from user-mode or kernel-mode.

## The HID class driver

The system-supplied HID class driver is the WDM function driver and bus driver for the HID device setup class (HIDClass). The executable component of the HID class driver is *hidclass.sys*. The HID class driver is the glue between HID clients and various transports, allowing a HID client to be written in an independent way from transports. This level of abstraction allows clients to continue to work (with little to no modifications) when a new standard, or a third-party transport is introduced.

The following diagram is a representation of the HID architecture.

![Diagram of a simplified HID driver stack showing HID clients, the HID class driver, and HID transport components.](images/hid-intro-simple.png)

The preceding diagram includes:

- HID clients – Identifies the Windows and third-party clients and their interfaces.
- HID class driver - The *hidclass.sys* executable.
- HID transport minidriver - Identifies the Windows and third-party transports and their interfaces.

Here's the device stack diagram of a generic HID client and transport.

![Diagram of a HID device stack for a generic HID client and transport.](images/hid-device-stacks-generic.png)

Here's another device stack diagram showing HID keyboard and mouse collections over USB.

![Diagram of a HID device stack for a keyboard and mouse over USB.](images/hid-device-stacks.png)

## HID clients

The HID Clients are drivers, services, or applications that communicate with *HIDClass.sys* and often represent a specific type of device (for example, sensor, keyboard, mouse, and so on). They identify the device via a hardware ID or a specific HID Collection and communicate with the HID Collection via the following guidance.

User-mode drivers and applications, and kernel-mode drivers, do the following to operate HID collections:

- User-mode drivers and applications use HIDClass support routines (HidD_Xxx) to obtain information about a HID collection.
- Kernel-mode drivers, user-mode drivers, and applications use HID parsing support routines (HidP_Xxx), and kernel-mode drivers use HID class driver IOCTLs to handle HID reports.

The following table simplifies the information.

| Mode | Drivers | Applications |
|--|--|--|
| User Mode | HidD_Xxx | HidP_Xxx |
| Kernel Mode | HidD_Xxx OR IOCTL_HID_xxx | N/A |

For more information, see [Opening HID collections](opening-hid-collections.md).

### HID clients supported in Windows

Windows supports the following top-level collections:

| Usage page | Usage | Notes | Access mode |
|--|--|--|--|
| 0x0001 | 0x0001 - 0x0002 | [Mouse class driver and mapper driver](keyboard-and-mouse-class-drivers.md) | Exclusive |
| 0x0001 | 0x0004 - 0x0005 | Game controllers | Shared |
| 0x0001 | 0x0006 - 0x0007 | [Keyboard / Keypad class driver and mapper driver](keyboard-and-mouse-class-drivers.md) | Exclusive |
| 0x0001 | 0x000C | Flight mode switch | Shared |
| 0x0001 | 0x0080 | System controls (Power) | Shared |
| 0x000C | 0x0001 | Consumer controls | Shared |
| 0x000D | 0x0001 | External pen device | Exclusive |
| 0x000D | 0x0002 | Integrated pen device | Exclusive |
| 0x000D | 0x0004 | Touchscreen | Exclusive |
| 0x000D | 0x0005 | Precision touchpad (PTP) | Exclusive |
| 0x0020 | *Multiple | Sensors | Shared |
| 0x0084 | 0x0004 | HID UPS battery | Shared |
| 0x008C | 0x0002 | Barcode scanner (hidscanner.dll) | Shared |

In the preceding table, the access mode for input HID clients is *exclusive* to prevent other HID clients from intercepting or receiving global input state when they aren't the target recipient of that input. For security reasons, Raw Input Manager (RIM) opens all such devices exclusively.

If RIM opens a device in *exclusive* mode, the user can still open a HID device interface without requesting read and write permissions and obtain HID device information via HIDClass support routines (HidD_GetXxx).

Sharing mode allows multiple applications to access a device. For example, multiple applications can access a barcode scanner to inquire about device capabilities and retrieve statistics. However, retrieving decoded data from a barcode scanner is done in *exclusive* mode. Usages are defined in the [USB-IF Usage Tables](https://usb.org/document-library/hid-usage-tables-121).

*Multiple: Sensors usages from 0x00 – 0xFF are segmented for different purposes. For example, 0x10 indicates a biometric sensor; 0x40 indicates a light sensor. Those allocations aren't contiguous. For the list of sensor usages, see [USB-IF Device Class Definitions for HID](https://www.usb.org/document-library/device-class-definition-hid-111). For information about sensors usages that are supported in Windows, see [HID Sensors Usages](/windows-hardware/design/whitepapers/hid-sensors-usages).

## The HID transport driver

The HID class driver is designed to use HID minidrivers to access a hardware input device. A HID minidriver abstracts the device-specific operation of the input devices that it supports. The HID minidriver binds its operation to the HID class driver by registering with the HID class driver. The HID class driver communicates with a HID minidriver by calling the minidriver's support routines. The HID minidriver, in turn, sends communications down the driver stack to an underlying bus or port driver.

### HID Transports Supported in Windows

For a list of supported HID transports, see the [HID Transport Overview](hid-transports.md).

[USB Generic HID Test](/windows-hardware/test/hlk/testref/f7949ab5-dd13-4c74-876f-6d54ff85e213) in the Windows Hardware Lab Kit (HLK) covers HidUsb and HidClass drivers. There's no HLK test for third-party HID minidrivers.
