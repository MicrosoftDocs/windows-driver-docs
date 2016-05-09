---
title: CD-ROM Drivers
author: windows-driver-content
description: CD-ROM Drivers
ms.assetid: 04b0a605-7816-4804-bfa8-39122a03ce16
keywords: ["CD-ROM drivers WDK storage", "storage CD-ROM drivers WDK", "storage drivers WDK , CD-ROM", "IOCTLs WDK CD-ROM"]
---

# CD-ROM Drivers


When the operating system enumerates a CD-ROM device, it loads a native CD-ROM class driver (*Cdrom.sys*). This driver exposes an I/O control request (IOCTL) interface that is described in the [CD-ROM I/O Control Codes](https://msdn.microsoft.com/library/windows/hardware/ff551394) section.

The following topics explain some of the key features of the IOCTL interface:

[CD-ROM Exclusive Access](cd-rom-exclusive-access-mode.md)

[CD-ROM Set Speed](cd-rom-set-speed.md)

[CD-ROM Real-Time Streaming](cd-rom-real-time-streaming-.md)

[ACLs and the Device Stack](acls-and-the-device-stack.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20CD-ROM%20Drivers%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


