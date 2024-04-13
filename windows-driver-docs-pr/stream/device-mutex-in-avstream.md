---
title: Device Mutex in AVStream
description: Device Mutex in AVStream
keywords:
- AVStream mutexes WDK
- mutexes WDK AVStream
- device mutex WDK AVStream
- synchronization WDK AVStream
ms.date: 04/20/2017
---

# Device Mutex in AVStream





Use the device mutex to synchronize objects in the hierarchy from the device down to the filters. Each AVStream device has a single associated device mutex. Creation and destruction of both filter factories and filters are synchronized with this mutex. Certain Plug and Play and power management operations are also synchronized with this mutex. The minidriver focuses on two main issues with regard to the device mutex.

The object hierarchy is guaranteed to be stable *only* from the device down to individual filters if the device mutex is held. As a result, the minidriver must obtain the device mutex before manually creating filter factories by calling [**KsCreateFilterFactory**](/windows-hardware/drivers/ddi/ks/nf-ks-kscreatefilterfactory). The minidriver must also obtain the device mutex before traversing the object hierarchy by calling the **Ks***Xxx***GetFirstChild***Xxx* and **Ks***Xxx***GetNextSibling***Xxx* functions.

AVStream holds the device mutex on behalf of the minidriver when it receives the following requests:

-   [**IRP\_MN\_QUERY\_STOP\_DEVICE**](../kernel/irp-mn-query-stop-device.md)

-   [**IRP\_MN\_QUERY\_REMOVE\_DEVICE**](../kernel/irp-mn-query-remove-device.md)

-   [*PostStart dispatch*](/windows-hardware/drivers/ddi/ks/nc-ks-pfnksdevice)

-   [**IRP\_MN\_START\_DEVICE**](../kernel/irp-mn-start-device.md)

-   [**IRP\_MN\_QUERY\_POWER**](../kernel/irp-mn-query-power.md)

-   [**IRP\_MN\_SET\_POWER**](../kernel/irp-mn-set-power.md)

-   Sleep and wake notifications on filters and pins. See [**KsFilterRegisterPowerCallbacks**](/windows-hardware/drivers/ddi/ks/nf-ks-ksfilterregisterpowercallbacks) and [**KsPinRegisterPowerCallbacks**](/windows-hardware/drivers/ddi/ks/nf-ks-kspinregisterpowercallbacks).

It is important to note that the device mutex cannot be obtained recursively. Consider the following example. AVStream receives a sleep notification. As described above, it takes the device mutex on behalf of the minidriver. If AVStream then calls a minidriver-provided callback routine in the context of thread A, the minidriver must not subsequently attempt to obtain the device mutex in thread A. Doing so causes thread A to deadlock with itself.

AVStream often obtains filter control mutexes while the device mutex is already held. Consequently, as a general rule, a thread that has taken a filter control mutex should not subsequently take the device mutex.

To manipulate the device mutex, use the following functions:

[**KsAcquireDevice**](/windows-hardware/drivers/ddi/ks/nf-ks-ksacquiredevice), [**KsReleaseDevice**](/windows-hardware/drivers/ddi/ks/nf-ks-ksreleasedevice)

 

