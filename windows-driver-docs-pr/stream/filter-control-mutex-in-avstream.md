---
title: Filter Control Mutex in AVStream
description: Filter Control Mutex in AVStream
keywords:
- filter control mutex WDK AVStream
- AVStream mutexes WDK
- mutexes WDK AVStream
- synchronization WDK AVStream
- state transitions WDK AVStream
ms.date: 04/20/2017
---

# Filter Control Mutex in AVStream





Each AVStream filter instance has an associated filter control mutex. This mutex is used to synchronize access to the object hierarchy from the filter downward to individual pins. Creation and destruction of filters and pins are synchronized with this mutex.

The object hierarchy is guaranteed to be stable *only* from a specific filter instance downward while the filter control mutex is held. Accordingly, the minidriver must obtain the filter control mutex before traversing the object hierarchy below the filter level using the **Ks***Xxx***GetFirstChild***Xxx* and **Ks***Xxx***GetNextSibling***Xxx* functions.

The filter control mutex is also used to synchronize state transitions.

AVStream obtains the filter control mutex when it handles properties that require the hierarchy to remain stable, such as when performing descriptor modification.

Be aware that a single filter control mutex is used for the object hierarchy under each individual filter. This means that a pin object uses its parent's filter control mutex when a minidriver calls a function with a pin object.

AVStream holds the filter control mutex on behalf of the minidriver when it calls the following minidriver-supplied routines:

-   [*AVStrMiniFilterCreate*](/windows-hardware/drivers/ddi/ks/nc-ks-pfnksfilterirp)

-   [*AVStrMiniFilterClose*](/previous-versions/ff556307(v=vs.85))

-   [*AVStrMiniPinCreate*](/windows-hardware/drivers/ddi/ks/nc-ks-pfnkspinirp)

-   [*AVStrMiniPinClose*](/previous-versions/ff556329(v=vs.85))

-   [*AVStrMiniPinConnect*](/previous-versions/ff556332(v=vs.85))

-   [*AVStrMiniPinDisconnect*](/windows-hardware/drivers/ddi/ks/nc-ks-pfnkspinvoid)

-   [*AVStrMiniPinSetDataFormat*](/windows-hardware/drivers/ddi/ks/nc-ks-pfnkspinsetdataformat)

-   [*AVStrMiniPinSetDeviceState*](/windows-hardware/drivers/ddi/ks/nc-ks-pfnkspinsetdevicestate)

Similar to the device mutex, the filter control mutex must not be obtained recursively. If, for example, AVStream makes a callback to a minidriver for a *Create* dispatch in the context of thread A, and the minidriver later attempts to obtain the mutex from within thread A, thread A deadlocks with itself.

A deadlock can occur if you do either of the following actions:

-   Try to acquire the filter control mutex from within the process routine.

-   Try to obtain the filter control mutex from within either the Sleep or Wake callback.

To manipulate the filter control mutex, use the following functions:

[**KsAcquireControl**](/windows-hardware/drivers/ddi/ks/nf-ks-ksacquirecontrol), [**KsFilterAcquireControl**](/windows-hardware/drivers/ddi/ks/nf-ks-ksfilteracquirecontrol), [**KsPinAcquireControl**](/windows-hardware/drivers/ddi/ks/nf-ks-kspinacquirecontrol), [**KsReleaseControl**](/windows-hardware/drivers/ddi/ks/nf-ks-ksreleasecontrol), [**KsFilterReleaseControl**](/windows-hardware/drivers/ddi/ks/nf-ks-ksfilterreleasecontrol), [**KsPinReleaseControl**](/windows-hardware/drivers/ddi/ks/nf-ks-kspinreleasecontrol)

 

