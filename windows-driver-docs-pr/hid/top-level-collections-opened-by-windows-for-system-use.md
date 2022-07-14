---
title: Top-level collections opened by Windows for system use
description: Top-level collections opened by Windows for system use
keywords:
- top-level collections WDK HID
ms.date: 07/14/2022
---

# Top-level collections opened by Windows for system use

Windows opens the following [top-level collections](top-level-collections.md) for system use:

| Usage Page | Usage | Windows 7 | Windows 8 | Windows 10 | Notes | Access Mode |
| --- | --- | --- | --- | --- | --- | --- |
| 0x0001 | 0x0001 - 0x0002 | Yes | Yes | Yes | [Mouse class driver and mapper driver](keyboard-and-mouse-class-drivers.md) | Exclusive |
| 0x0001 | 0x0004 - 0x0005 | Yes | Yes | Yes | Game Controllers | Shared |
| 0x0001 | 0x0006 - 0x0007 | Yes | Yes | Yes | [Keyboard / Keypad class driver and mapper driver](keyboard-and-mouse-class-drivers.md) | Exclusive |
| 0x0001 | 0x000C | No | Yes | Yes | Flight Mode Switch | Shared |
| 0x0001 | 0x0080 | Yes | Yes | Yes | System Controls (Power) | Shared |
| 0x000C | 0x0001 | Yes | Yes | Yes (For both Windows 10 and Windows 10 Mobile) | Consumer Controls | Shared (For both Windows 10 and Windows 10 Mobile) |
| 0x000D | 0x0001 | Yes | Yes | Yes | External Pen Device | Exclusive |
| 0x000D | 0x0002 | Yes | Yes | Yes | Integrated Pen Device | Exclusive |
| 0x000D | 0x0004 | Yes | Yes | Yes | Touchscreen | Exclusive |
| 0x000D | 0x0005 | No | Yes | Yes | Precision Touchpad (PTP) | Exclusive |
| 0x0020 | *Multiple | No | Yes | Yes | Sensors | Shared |
| 0x0084 | 0x0004 | Yes | Yes | Yes | HID UPS Battery | Shared |
| 0x008C | 0x0002 | No | Yes (Windows 8.1 and later) | Yes | Barcode Scanner (hidscanner.dll) | Shared |

*Multiple: Sensors usages from 0x00 – 0xFF are segmented for different purposes. For example 0x10 indicates a biometric sensor; 0x40 indicates a light sensor. Those allocations are not contiguous. For the list of sensor usages, see [USB-IF Device Class Definitions for HID](https://www.usb.org/document-library/device-class-definition-hid-111). For information about sensors usages that are supported in Windows, [HID Sensors Usages](windows-hardware/design/whitepapers/hid-sensors-usages).
