---
title: Initializing Spin Locks
author: windows-driver-content
description: Initializing Spin Locks
ms.assetid: 7ed27e43-4406-4e64-b2c9-42b8a883efdb
keywords: ["initializing spin locks", "spin locks WDK kernel", "KeInitializeSpinLock", "executive spin locks WDK kernel", "interrupt spin locks WDK kernel", "queued spin locks WDK kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Initializing Spin Locks


## <a href="" id="ddk-initializing-spin-locks-kg"></a>


Before calling any support routine that requires access to a caller-supplied executive spin lock, a driver must call [**KeInitializeSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff552160) to initialize the corresponding executive spin lock. Support routines that require an initialized executive spin lock include the following:

-   [**KeAcquireSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551917) and, subsequently, [**KeReleaseSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff553145)

-   [**KeAcquireSpinLockAtDpcLevel**](https://msdn.microsoft.com/library/windows/hardware/ff551921) and, subsequently, [**KeReleaseSpinLockFromDpcLevel**](https://msdn.microsoft.com/library/windows/hardware/ff553150)

-   [**KeAcquireInStackQueuedSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551899) and, subsequently, [**KeReleaseInStackQueuedSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff553130)

-   [**KeAcquireInStackQueuedSpinLockAtDpcLevel**](https://msdn.microsoft.com/library/windows/hardware/ff551908) and, subsequently, [**KeReleaseInStackQueuedSpinLockFromDpcLevel**](https://msdn.microsoft.com/library/windows/hardware/ff553137)

-   An **ExInterlocked*Xxx*** routine

Before calling [**IoConnectInterrupt**](https://msdn.microsoft.com/library/windows/hardware/ff548371) and [**KeSynchronizeExecution**](https://msdn.microsoft.com/library/windows/hardware/ff553302), a lowest-level driver must call [**KeInitializeSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff552160) to initialize an interrupt spin lock for which it provides storage.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Initializing%20Spin%20Locks%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


