---
title: HID over USB
description: USB was the first supported HID transport in the Windows operating system.
ms.assetid: F892C910-BA33-4795-A803-9D3FD55782BC
keywords:
- HID miniport driver
- USB
- USB 1.1
- USB 2.0
- USB 3.0
- USB, HID
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# HID over USB


USB was the first supported HID transport in the Windows operating system. The corresponding inbox driver was introduced in Windows 2000 and has been available in all operating systems since then.

Windows 8 continues to support HID over USB and has been enhanced to include new classes of HID devices from touchpads and keyboards to sensors and vendor specific device types.

HID over USB is also optimized to take advantage of selective suspend. (This feature requires a vendor provided INF or support via Microsoft operating-system descriptors.)

Recent updates to HID over USB also include:

-   Support for USB 1.1, USB 2.0 and USB 3.0.
-   A HID over USB driver is available on all client SKUs of Windows and is included in WinPE.

 

 




