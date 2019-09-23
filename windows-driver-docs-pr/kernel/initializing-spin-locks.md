---
title: Initializing Spin Locks
description: Initializing Spin Locks
ms.assetid: 7ed27e43-4406-4e64-b2c9-42b8a883efdb
keywords: ["initializing spin locks", "spin locks WDK kernel", "KeInitializeSpinLock", "executive spin locks WDK kernel", "interrupt spin locks WDK kernel", "queued spin locks WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Initializing Spin Locks





Before calling any support routine that requires access to a caller-supplied executive spin lock, a driver must call [**KeInitializeSpinLock**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-keinitializespinlock) to initialize the corresponding executive spin lock. Support routines that require an initialized executive spin lock include the following:

- [**KeAcquireSpinLock**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-keacquirespinlock) and, subsequently, [**KeReleaseSpinLock**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kereleasespinlock)

- [**KeAcquireSpinLockAtDpcLevel**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-keacquirespinlockatdpclevel) and, subsequently, [**KeReleaseSpinLockFromDpcLevel**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kereleasespinlockfromdpclevel)

- [**KeAcquireInStackQueuedSpinLock**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff551899(v=vs.85)) and, subsequently, [**KeReleaseInStackQueuedSpinLock**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kereleaseinstackqueuedspinlock)

- [**KeAcquireInStackQueuedSpinLockAtDpcLevel**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff551908(v=vs.85)) and, subsequently, [**KeReleaseInStackQueuedSpinLockFromDpcLevel**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kereleaseinstackqueuedspinlockfromdpclevel)

- An **ExInterlocked*Xxx*** routine

Before calling [**IoConnectInterrupt**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-ioconnectinterrupt) and [**KeSynchronizeExecution**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kesynchronizeexecution), a lowest-level driver must call [**KeInitializeSpinLock**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-keinitializespinlock) to initialize an interrupt spin lock for which it provides storage.

 

 




