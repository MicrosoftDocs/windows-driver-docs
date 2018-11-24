---
title: Threading and Synchronization First Level
description: Threading and Synchronization First Level
ms.assetid: 9fce6a18-2a66-4518-b05b-e85bdaa3951f
keywords:
- threading WDK display , first level
- synchronization WDK display , first level
ms.date: 04/20/2017
ms.localizationpriority: medium
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

-   [Display Class](display-class.md)

 





