---
title: Providing Storage for Spin Locks and Protected Data
author: windows-driver-content
description: Providing Storage for Spin Locks and Protected Data
ms.assetid: bde18474-10c3-4d9a-b120-6cbd5fc675cc
keywords: ["storage WDK spin locks", "storing spin-lock-protected data", "spin locks WDK kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Providing Storage for Spin Locks and Protected Data


## <a href="" id="ddk-providing-storage-for-spin-locks-and-protected-data-kg"></a>


As part of device start-up, a driver must allocate resident storage for any spin-lock-protected data or resources and for corresponding spin locks in one of the following places:

-   The device extension of a device object that the driver sets up by calling [**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397)

-   The controller extension of a controller object that the driver sets up by calling [**IoCreateController**](https://msdn.microsoft.com/library/windows/hardware/ff548395)

-   Nonpaged, system-space memory that the driver obtains by calling [**ExAllocatePoolWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff544520)

Attempting to access pageable data while holding a spin lock causes a fatal page fault if that page is not present. Referencing a spin lock that is invalid (because it was stored in pageable memory and is currently paged out) also causes a fatal page fault.

A driver must provide the storage for each of the following kinds of executive spin lock it might use:

-   Any spin lock that the driver explicitly acquires and releases using any of the **Ke*Xxx*** spin lock routines.

-   Any spin lock used as a parameter to any of the **ExInterlocked*Xxx*** routines.

While a driver can make calls to the **ExInterlocked*Xxx*** routines from its ISR or [*SynchCritSection*](https://msdn.microsoft.com/library/windows/hardware/ff563928) routines, it cannot use any of the **Ke*Xxx*** routines to acquire and release spin locks at any IRQL greater than DISPATCH\_LEVEL. Consequently, any driver that reuses a spin lock between calls to the **Ke*Xxx*SpinLock** and **ExInterlocked*Xxx*** routines must make every call while running at IRQL &lt;= DISPATCH\_LEVEL.

A driver can pass the same spin lock to **ExInterlockedInsertHeadList** as it does to another **ExInterlocked*Xxx*** routine, as long as both routines use the spin lock at the same IRQL. For more information about how spin lock usage affects performance, see [Using Spin Locks: An Example](using-spin-locks--an-example.md).

In addition to the storage for its executive spin locks, a device driver must provide the storage for another spin lock to be associated with its interrupt objects if it has a multivector ISR or more than one ISR.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Providing%20Storage%20for%20Spin%20Locks%20and%20Protected%20Data%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


