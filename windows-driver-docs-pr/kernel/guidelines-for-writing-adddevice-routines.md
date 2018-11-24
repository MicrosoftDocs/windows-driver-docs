---
title: Guidelines for Writing AddDevice Routines
description: Guidelines for Writing AddDevice Routines
ms.assetid: 8df36af5-158c-4c14-9fc2-2c3f997c2098
keywords: ["AddDevice routines WDK kernel , design guidelines"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Guidelines for Writing AddDevice Routines





Consider the following design guidelines when writing an [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine:

-   If a filter driver determines its *AddDevice* routine was called for a device it does not need to service, the filter driver must return STATUS\_SUCCESS to allow the rest of the device stack to be loaded for the device. The filter driver does not create a device object nor attach it to the device stack; the filter driver just returns success and allows the rest of the drivers to be added to the stack.

-   A driver must provide storage, usually in the device extension of a device object, for any kernel-defined objects and executive spin locks it uses. A driver also must provide storage for pointers to certain objects obtained from the I/O manager or other system components.

    You might decide to allocate additional system-space memory for the driver's needs, such as for long-term I/O buffers or a lookaside list. If so, an *AddDevice* routine can call the following routines:

    [**ExAllocatePoolWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff544520) for paged or nonpaged system-space memory

    [**ExInitializePagedLookasideList**](https://msdn.microsoft.com/library/windows/hardware/ff545309) or [**ExInitializeNPagedLookasideList**](https://msdn.microsoft.com/library/windows/hardware/ff545301) to initialize a paged or nonpaged lookaside list

-   If the driver has a device-dedicated thread or waits on any kernel-defined dispatcher objects, the *AddDevice* routine might initialize [kernel dispatcher objects](kernel-dispatcher-objects.md).

-   If the driver uses any executive spin locks or provides the storage for an interrupt spin lock, the *AddDevice* routine might initialize these spin locks. See [Spin Locks](spin-locks.md) for more information.

-   Tighten file-open security when calling [**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397).

    Specify the FILE\_DEVICE\_SECURE\_OPEN characteristic on the call to **IoCreateDevice**. This characteristic is supported on Windows NT 4.0 SP5 and later. It directs the I/O manager to perform security checks against the device object for all open requests. Vendors should specify this characteristic on calls to **IoCreateDevice** if the FILE\_DEVICE\_SECURE\_OPEN characteristic is not set in the device's class-installer INF or the device's INF and the drivers do not perform their own security checks on opens. (For more information, see [Controlling Device Namespace Access](controlling-device-namespace-access.md).)

    If a driver sets the FILE\_DEVICE\_SECURE\_OPEN characteristic when it calls **IoCreateDevice**, the I/O manager applies the security descriptor of the device object to any relative opens or trailing-filename opens. For example, if FILE\_DEVICE\_SECURE\_OPEN is set for \\Device\\foo, and if \\Device\\foo can only be opened by the administrator, then \\Device\\foo\\abc can also be opened by the administrator. The I/O manager, however, prevents a normal user from opening \\Device\\foo and \\Device\\foo\\abc.

    If one driver for a device sets this characteristic, the PnP manager propagates it to all the device objects for the device.

 

 




