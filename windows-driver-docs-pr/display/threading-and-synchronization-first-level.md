---
title: Threading and Synchronization First Level
description: Threading and Synchronization First Level
ms.assetid: 9fce6a18-2a66-4518-b05b-e85bdaa3951f
keywords: ["threading WDK display , first level", "synchronization WDK display , first level"]
---

# Threading and Synchronization First Level


The Windows Display Driver Model (WDDM) categorizes calls into the display miniport driver that are made under the first level of threading and synchronization into the following nonreentrancy classes. No reentrancy is permitted within a particular class. That is, only one thread can enter the driver within a particular class; however, calls from multiple classes and [zero-level](threading-and-synchronization-zero-level.md) calls can be entered simultaneously.

**Note**   Although two or more threads from different classes and threads from [zero-level](threading-and-synchronization-zero-level.md) calls can be running in the driver at the same time, no two threads can belong to a single process.

 

**Note**   The child I/O class functions are synchronized per child device (that is, simultaneous calls to multiple child devices are allowed). However, if internal dependencies exist between child devices, the display miniport driver must block calls as required.

 

-   [Pointer Class](pointer-class.md)

-   [GPU Scheduler Class](gpu-scheduler-class.md)

-   [Swizzling Range Class](swizzling-range-class.md)

-   [Overlay Class](overlay-class.md)

-   [Child I/O Class](child-i-o-class.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Threading%20and%20Synchronization%20First%20Level%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




