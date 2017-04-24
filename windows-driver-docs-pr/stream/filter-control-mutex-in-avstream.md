---
title: Filter Control Mutex in AVStream
author: windows-driver-content
description: Filter Control Mutex in AVStream
ms.assetid: 402795a0-e567-4e7e-a7d8-b2ce29ffb8fd
keywords:
- filter control mutex WDK AVStream
- AVStream mutexes WDK
- mutexes WDK AVStream
- synchronization WDK AVStream
- state transitions WDK AVStream
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Filter Control Mutex in AVStream


## <a href="" id="ddk-filter-control-mutex-in-avstream-ksg"></a>


Each AVStream filter instance has an associated filter control mutex. This mutex is used to synchronize access to the object hierarchy from the filter downward to individual pins. Creation and destruction of filters and pins are synchronized with this mutex.

The object hierarchy is guaranteed to be stable *only* from a specific filter instance downward while the filter control mutex is held. Accordingly, the minidriver must obtain the filter control mutex before traversing the object hierarchy below the filter level using the **Ks***Xxx***GetFirstChild***Xxx* and **Ks***Xxx***GetNextSibling***Xxx* functions.

The filter control mutex is also used to synchronize state transitions.

AVStream obtains the filter control mutex when it handles properties that require the hierarchy to remain stable, such as when performing descriptor modification.

Be aware that a single filter control mutex is used for the object hierarchy under each individual filter. This means that a pin object uses its parent's filter control mutex when a minidriver calls a function with a pin object.

AVStream holds the filter control mutex on behalf of the minidriver when it calls the following minidriver-supplied routines:

-   [*AVStrMiniFilterCreate*](https://msdn.microsoft.com/library/windows/hardware/ff556310)

-   [*AVStrMiniFilterClose*](https://msdn.microsoft.com/library/windows/hardware/ff556307)

-   [*AVStrMiniPinCreate*](https://msdn.microsoft.com/library/windows/hardware/ff556334)

-   [*AVStrMiniPinClose*](https://msdn.microsoft.com/library/windows/hardware/ff556329)

-   [*AVStrMiniPinConnect*](https://msdn.microsoft.com/library/windows/hardware/ff556332)

-   [*AVStrMiniPinDisconnect*](https://msdn.microsoft.com/library/windows/hardware/ff556337)

-   [*AVStrMiniPinSetDataFormat*](https://msdn.microsoft.com/library/windows/hardware/ff556355)

-   [*AVStrMiniPinSetDeviceState*](https://msdn.microsoft.com/library/windows/hardware/ff556359)

Similar to the device mutex, the filter control mutex must not be obtained recursively. If, for example, AVStream makes a callback to a minidriver for a *Create* dispatch in the context of thread A, and the minidriver later attempts to obtain the mutex from within thread A, thread A deadlocks with itself.

A deadlock can occur if you do either of the following actions:

-   Try to acquire the filter control mutex from within the process routine.

-   Try to obtain the filter control mutex from within either the Sleep or Wake callback.

To manipulate the filter control mutex, use the following functions:

[**KsAcquireControl**](https://msdn.microsoft.com/library/windows/hardware/ff560908), [**KsFilterAcquireControl**](https://msdn.microsoft.com/library/windows/hardware/ff562523), [**KsPinAcquireControl**](https://msdn.microsoft.com/library/windows/hardware/ff563485), [**KsReleaseControl**](https://msdn.microsoft.com/library/windows/hardware/ff566780), [**KsFilterReleaseControl**](https://msdn.microsoft.com/library/windows/hardware/ff562551), [**KsPinReleaseControl**](https://msdn.microsoft.com/library/windows/hardware/ff563526)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Filter%20Control%20Mutex%20in%20AVStream%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


