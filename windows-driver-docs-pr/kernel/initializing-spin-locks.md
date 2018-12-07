---
title: Initializing Spin Locks
description: Initializing Spin Locks
ms.assetid: 7ed27e43-4406-4e64-b2c9-42b8a883efdb
keywords: ["initializing spin locks", "spin locks WDK kernel", "KeInitializeSpinLock", "executive spin locks WDK kernel", "interrupt spin locks WDK kernel", "queued spin locks WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Initializing Spin Locks





Before calling any support routine that requires access to a caller-supplied executive spin lock, a driver must call [**KeInitializeSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff552160) to initialize the corresponding executive spin lock. Support routines that require an initialized executive spin lock include the following:

- [**KeAcquireSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551917) and, subsequently, [**KeReleaseSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff553145)

- [**KeAcquireSpinLockAtDpcLevel**](https://msdn.microsoft.com/library/windows/hardware/ff551921) and, subsequently, [**KeReleaseSpinLockFromDpcLevel**](https://msdn.microsoft.com/library/windows/hardware/ff553150)

- [**KeAcquireInStackQueuedSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551899) and, subsequently, [**KeReleaseInStackQueuedSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff553130)

- [**KeAcquireInStackQueuedSpinLockAtDpcLevel**](https://msdn.microsoft.com/library/windows/hardware/ff551908) and, subsequently, [**KeReleaseInStackQueuedSpinLockFromDpcLevel**](https://msdn.microsoft.com/library/windows/hardware/ff553137)

- An **ExInterlocked*Xxx*** routine

Before calling [**IoConnectInterrupt**](https://msdn.microsoft.com/library/windows/hardware/ff548371) and [**KeSynchronizeExecution**](https://msdn.microsoft.com/library/windows/hardware/ff553302), a lowest-level driver must call [**KeInitializeSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff552160) to initialize an interrupt spin lock for which it provides storage.

 

 




