---
title: Alternatives to Mutex Objects
author: windows-driver-content
description: Alternatives to Mutex Objects
ms.assetid: c3b78155-426a-449d-8678-5666a7a12cbd
keywords: ["kernel dispatcher objects WDK , mutex objects", "dispatcher objects WDK kernel , mutex objects", "mutex objects WDK kernel", "fast mutexes WDK kernel", "guarded mutexes WDK kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Alternatives to Mutex Objects


Fast mutexes and guarded mutexes can be used as a replacement for mutex objects. A fast mutex or guarded mutex can be acquired and released faster than a mutex object, but they have the following restrictions:

-   Drivers cannot use the [**KeWaitForSingleObject**](https://msdn.microsoft.com/library/windows/hardware/ff553350) or [**KeWaitForMultipleObjects**](https://msdn.microsoft.com/library/windows/hardware/ff553324) routines to wait for a fast or guarded mutex. Thus, a driver cannot wait for a fast or guarded mutex and a dispatcher object simultaneously.

-   Drivers cannot acquire a fast or guarded mutex recursively. If a driver tries to acquire a fast or guarded mutex that it has already acquired, the driver will deadlock. A mutex object, however, can be acquired recursively.

For more information about fast and guarded mutexes, see [Fast Mutexes and Guarded Mutexes](fast-mutexes-and-guarded-mutexes.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Alternatives%20to%20Mutex%20Objects%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


