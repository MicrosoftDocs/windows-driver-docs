---
title: Top-level collections opened by Windows for system use
description: Top-level collections opened by Windows for system use
keywords:
- top-level collections WDK HID
ms.date: 07/14/2022
---

# Top-level collections opened by Windows for system use

Windows opens the following [top-level collections](top-level-collections.md) for system use:

| Device type              | Usage page | Usage ID  | Windows client                                      | Access mode |
|--------------------------|:----------:|:---------:|-----------------------------------------------------|-------------|
| Pointer                  | 0x0001     | 0x0001    | Windows subsystem                                   | Exclusive   |
| Mouse                    | 0x0001     | 0x0002    | Windows subsystem                                   | Exclusive   |
| Joystick                 | 0x0001     | 0x0004    | DirectInput                                         | Shared      |
| Game pad                 | 0x0001     | 0x0005    | DirectInput                                         | Shared      |
| Keyboard                 | 0x0001     | 0x0006    | Windows subsystem                                   | Exclusive   |
| Keypad                   | 0x0001     | 0x0007    | Windows subsystem                                   | Exclusive   |
| System control           | 0x0001     | 0x0080    | Windows subsystem                                   | Shared      |
| Consumer control         | 0x000C     | 0x0001    | hidserv.exe                                         | Shared      |
| External pen device      | 0x000D     | 0x0001    | DirectInput                                         | Exclusive   |
| Integrated pen device    | 0x000D     | 0x0002    | Windows subsystem                                   | Exclusive   |
| Touchscreen              | 0x000D     | 0x0004    | Windows subsystem                                   | Exclusive   |
| Precision Touchpad (PTP) | 0x000D     | 0x0005    | DirectInput                                         | Exclusive   |
| Sensors                  | 0x0020     | *Multiple | Sensor HID class driver (SensorsHIDClassDriver.dll) | Shared      |
| HID UPS battery          | 0x0084     | 0x0004    | Windows subsystem                                   | Shared      |
| Barcode scanner          | 0x008C     | 0x0002    | hidscanner.dll                                      | Shared      |

*Multiple: Sensors usages from 0x00 – 0xFF are segmented for different purposes. For example 0x10 indicates a biometric sensor; 0x40 indicates a light sensor. Those allocations are not contiguous. For the list of sensor usages, see [USB-IF Device Class Definitions for HID](https://www.usb.org/document-library/device-class-definition-hid-111). For information about sensors usages that are supported in Windows, [HID Sensors Usages](windows-hardware/design/whitepapers/hid-sensors-usages).
