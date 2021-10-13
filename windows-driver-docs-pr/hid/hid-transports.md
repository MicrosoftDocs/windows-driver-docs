---
title: HID Transport Overview
description: HID Transport Overview
keywords:
- HID Transports
- USB transport
- Bluetooth transport
- Bluetooth
- Bluetooth LE
- I2C
- transport minidriver
ms.date: 06/22/2021
ms.localizationpriority: medium
---

# HID Transport Overview

## HID transports supported in Windows

| Transport    | In-box minidriver | Version               |  Notes |
| ------------ | ----------------- | --------------------- | ---------- | 
| USB          | Hidusb.sys        | Windows 7 and later.  | Support for USB HID 1.11+ is provided on Windows operating systems dating back to Windows 2000.       |
| Bluetooth    | Hidbth.sys        | Windows 7 and later.  | Support for Bluetooth HID 1.1+ is provided on Windows operating systems dating back to Windows Vista. |
| Bluetooth LE | HidBthLE.dll      | Windows 8 and later.  | Windows 8 introduces support for HID over Bluetooth LE.                                               |
| I²C          | Hidi2c.sys        | Windows 8 and later.  | Windows 8 introduces support for HID over I2C.                                                        |
| GPIO         | Hidinterrupt.sys  | Windows 10 and later. | Windows 10 introduces support for general-purpose I/O (GPIO) buttons.                                 |
| SPI          | HidSpi.sys        | Windows 10 and later. | Windows 11 introduces support for HID over Serial Peripheral Interface (SPI).                         |

Microsoft recommends using the included drivers for transports listed in the preceding table.

If a device requires a transport other than USB, Bluetooth, Bluetooth LE, or I²C, a miniport driver as described in [Transport Minidrivers](transport-minidrivers.md) is recommended.

## HID transport limits

- **Report Descriptor Length**

    A transport minidriver submits report descriptors to Hidclass in a [**HID\_DESCRIPTOR**](/windows-hardware/drivers/ddi/hidport/ns-hidport-_hid_descriptor) structure. Regardless of the size defined by the transport protocol for transferring HID report descriptor with their devices, the actual report descriptor size is limited during the communication between Hidclass and HID minidrivers.

- **TLCs in a Report Descriptor**

    The Hidclass/Hidparse driver pair is aware of the number of TLCs in a Report Descriptor. HID miniport drivers do not have that information. Each TLC has at least 2 bytes to start a collection and 1 byte to end the collection.

- **Input/Output/Feature Report Length**

    The Hidclass/Hidparse driver pair defines lengths of HID Input, Output, and Feature Reports. The limit is 8 KB (minus 1 bit). Even if a HID minidriver can request a transfer of more than 8 KB for a report, only reports smaller than 8 KB are successfully transferred.

| In-box minidriver | Report Descriptor Length | TLCs in One Report Descriptor | Input/Output/Feature Report Length |
| ----------------- | ------------------------ | ----------------------------- | ---------------------------------- |
| Hidclass/Hidparse | 65535 bytes              | 21845                         | 8 KB - 1 bit                       |
| Hidusb            | 65535 bytes              | N/A                           | 64 KB                              |
| Hidbth            | 65535 bytes              | N/A                           | 64 KB                              |
| HidBthLE          | 65535 bytes              | N/A                           | 64 KB                              |
| Hidi2c            | 65535 bytes              | N/A                           | 64 KB                              |
| Hidspi            | 65535 bytes              | N/A                           | 64 KB                              |

## See Also

[USB Generic HID Test](/windows-hardware/test/hlk/testref/f7949ab5-dd13-4c74-876f-6d54ff85e213) in the Windows Hardware Lab Kit (HLK) covers HidUsb and HidClass drivers. There is no HLK test for third-party HID mini drivers.
