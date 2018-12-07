---
title: CD-ROM Drivers
description: CD-ROM Drivers
ms.assetid: 04b0a605-7816-4804-bfa8-39122a03ce16
keywords:
- CD-ROM drivers WDK storage
- storage CD-ROM drivers WDK
- storage drivers WDK , CD-ROM
- IOCTLs WDK CD-ROM
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# CD-ROM Drivers


When the operating system enumerates a CD-ROM device, it loads a native CD-ROM class driver (*Cdrom.sys*). This driver exposes an I/O control request (IOCTL) interface that is described in the [CD-ROM I/O Control Codes](https://msdn.microsoft.com/library/windows/hardware/ff551394) section.

The following topics explain some of the key features of the IOCTL interface:

[CD-ROM Exclusive Access](cd-rom-exclusive-access-mode.md)

[CD-ROM Set Speed](cd-rom-set-speed.md)

[CD-ROM Real-Time Streaming](cd-rom-real-time-streaming-.md)

[ACLs and the Device Stack](acls-and-the-device-stack.md)

 

 




