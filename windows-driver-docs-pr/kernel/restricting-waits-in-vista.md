---
title: Restricting Waits in Vista
author: windows-driver-content
description: Restricting Waits in Vista
ms.assetid: edcc25d0-bcf6-48f0-832e-3f911bd42142
---

# Restricting Waits in Vista


Because many device driver developers use [Synchronous I/O Programming Techniques](synchronous-i-o-programming.md), Windows can slow down or "freeze up" while a device is taking time to respond. To reduce this problem, the I/O Manager in Vista will stop execution of programs that are "stuck" waiting for a device to respond after a few moments.

**Note**   It is strongly recommended that [Synchronous I/O Programming Techniques](synchronous-i-o-programming.md) are avoided in your device driver. If Vista stops execution of your driver code because your driver is waiting for a device, your device may be left in an unknown state.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Restricting%20Waits%20in%20Vista%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


