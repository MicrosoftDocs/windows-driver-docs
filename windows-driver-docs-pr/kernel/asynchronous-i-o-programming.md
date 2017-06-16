---
title: Asynchronous I/O Programming
author: windows-driver-content
description: Asynchronous I/O Programming
ms.assetid: f50c98ab-3aae-43f6-be91-2ae587105767
---

# Asynchronous I/O Programming


Asynchronous programming does not force everyone else to wait. This is the preferred technique for programming Windows device drivers. Supporting asynchronous I/O is one of the design goals of WDM drivers. For more information about asynchronous I/O in drivers, see [Supporting Asynchronous I/O](supporting-asynchronous-i-o.md). For device drivers, using interrupts is the best way to program asynchronously. You simply send a request to your device and let the system take control. Then when your device wants to tell you something, it triggers an interrupt that the operating system processes by calling an interrupt handler in your driver. This communication is handled through IRPs. For more information about IRPS, see [Handling IRPs](handling-irps.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Asynchronous%20I/O%20Programming%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


