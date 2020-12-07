---
title: Introduction to CD-ROM Drivers
description: CD-ROM Drivers
keywords:
- CD-ROM drivers WDK storage
- storage CD-ROM drivers WDK
- storage drivers WDK , CD-ROM
- IOCTLs WDK CD-ROM
ms.date: 12/15/2019
ms.localizationpriority: medium
---

# Introduction to CD-ROM drivers

When the operating system enumerates a CD-ROM device, it loads a native CD-ROM class driver (*Cdrom.sys*). This driver exposes an I/O control request (IOCTL) interface. All public I/O control codes for drivers of CD-ROM devices use buffered I/O. Consequently, the input or output data for these requests is at Irp->AssociatedIrp.SystemBuffer. For more info, see [CD-ROM I/O control codes](cd-rom-io-control-codes.md)

Class drivers for CD-ROM devices handle additional public I/O control codes, along with those described in this section. For more information about requirements for storage class drivers, see [General Storage I/O Control Codes](general-storage-io-control-codes.md).

The following topics explain some of the key features of the CD-ROM class driver IOCTL interface:

- [CD-ROM Exclusive Access](cd-rom-exclusive-access-mode.md)

- [CD-ROM Set Speed](cd-rom-set-speed.md)

- [CD-ROM Real-Time Streaming](cd-rom-real-time-streaming-.md)

- [ACLs and the Device Stack](acls-and-the-device-stack.md)
