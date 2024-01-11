---
title: HID Over USB Overview
description: USB was the first supported HID transport in the Windows operating system.
keywords:
- HID miniport driver
- USB
- USB 1.1
- USB 2.0
- USB 3.0
- USB, HID
ms.date: 01/11/2024
---

# HID over USB Overview

USB was the first supported HID transport in Windows. The corresponding in-box driver was introduced in Windows 2000 and has been available in all operating systems since then. This driver has been enhanced to include new classes of HID devices from touchpads and keyboards to sensors and vendor specific device types. HID over USB is also optimized to take advantage of selective suspend. (This feature requires a vendor provided INF or support via Microsoft operating-system descriptors.)

Recent updates to HID over USB also include:

- Support for USB 1.1, USB 2.0 and USB 3.0.
- A HID over USB driver is available on all client SKUs of Windows and is included in WinPE.

## See also

- [HID USB homepage](https://www.usb.org/hid)
- [HID USB specification](https://www.usb.org/sites/default/files/documents/hid1_11.pdf)
- [HID Usage Tables](https://www.usb.org/sites/default/files/documents/hut1_12v2.pdf)
