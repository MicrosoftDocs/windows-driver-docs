---
title: Top-level collections opened by Windows for system use
description: Top-level collections opened by Windows for system use
keywords:
- top-level collections WDK HID
ms.date: 07/14/2022
---

# Top-level collections opened by Windows for system use

Windows opens the following [top-level collections](top-level-collections.md) for system use:

| Usage page | Usage ID | Notes | Access mode |
| --- | --- | --- | --- |
| 0x0001 | 0x0001 - 0x0002 | [Mouse class driver and mapper driver](keyboard-and-mouse-class-drivers.md) | Exclusive |
| 0x0001 | 0x0004 - 0x0005 | Game controllers | Shared |
| 0x0001 | 0x0006 - 0x0007 | [Keyboard class driver and mapper driver](keyboard-and-mouse-class-drivers.md) | Exclusive |
| 0x0001 | 0x000C | Flight mode switch | Shared |
| 0x0001 | 0x0080 | System controls (power) | Shared |
| 0x000C | 0x0001 | Consumer controls | Shared |
| 0x000D | 0x0001 | External pen device | Exclusive |
| 0x000D | 0x0002 | Integrated pen device | Exclusive |
| 0x000D | 0x0004 | Touchscreen | Exclusive |
| 0x000D | 0x0005 | Precision touchpad (PTP) | Exclusive |
| 0x0020 | *Multiple | Sensors | Shared |
| 0x0084 | 0x0004 | HID UPS battery | Shared |
| 0x008C | 0x0002 | Barcode scanner (hidscanner.dll) | Shared |

*Multiple: Sensors usages from 0x00 – 0xFF are segmented for different purposes. For example 0x10 indicates a biometric sensor; 0x40 indicates a light sensor. Those allocations are not contiguous. For the list of sensor usages, see [USB-IF Device Class Definitions for HID](https://www.usb.org/document-library/device-class-definition-hid-111). For information about sensors usages that are supported in Windows, [HID Sensors Usages](windows-hardware/design/whitepapers/hid-sensors-usages).
