---
title: Alternatives to Mutex Objects
description: Alternatives to Mutex Objects
keywords: ["kernel dispatcher objects WDK , mutex objects", "dispatcher objects WDK kernel , mutex objects", "mutex objects WDK kernel", "fast mutexes WDK kernel", "guarded mutexes WDK kernel"]
ms.date: 06/16/2017
---

# Alternatives to Mutex Objects


Fast mutexes and guarded mutexes can be used as a replacement for mutex objects. A fast mutex or guarded mutex can be acquired and released faster than a mutex object, but they have the following restrictions:

-   Drivers cannot use the [**KeWaitForSingleObject**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kewaitforsingleobject) or [**KeWaitForMultipleObjects**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kewaitformultipleobjects) routines to wait for a fast or guarded mutex. Thus, a driver cannot wait for a fast or guarded mutex and a dispatcher object simultaneously.

-   Drivers cannot acquire a fast or guarded mutex recursively. If a driver tries to acquire a fast or guarded mutex that it has already acquired, the driver will deadlock. A mutex object, however, can be acquired recursively.

For more information about fast and guarded mutexes, see [Fast Mutexes and Guarded Mutexes](fast-mutexes-and-guarded-mutexes.md).

 

