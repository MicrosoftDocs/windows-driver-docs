---
title: Synchronous I/O Programming
author: windows-driver-content
description: Synchronous I/O Programming
ms.assetid: ef021dd2-bd1d-4fb0-853f-014c62bda76b
---

# Synchronous I/O Programming


Synchronous programming simply waits for a call to return. This is fast and efficient from the programmer's point of view but in an environment like Windows where many programs are running at once, it can cause problems. Whenever possible, use [Asynchronous I/O Programming Techniques](asynchronous-i-o-programming.md).

**Note**  For driver developers using Microsoft Vista, this is not as serious a problem. For more information about synchronous programming in Vista, see [Restricting Waits in Vista](restricting-waits-in-vista.md).

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Synchronous%20I/O%20Programming%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


