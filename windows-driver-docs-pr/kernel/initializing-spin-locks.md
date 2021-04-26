---
title: Initializing Spin Locks
description: Initializing Spin Locks
keywords: ["initializing spin locks", "spin locks WDK kernel", "KeInitializeSpinLock", "executive spin locks WDK kernel", "interrupt spin locks WDK kernel", "queued spin locks WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Initializing Spin Locks





Before calling any support routine that requires access to a caller-supplied executive spin lock, a driver must call [**KeInitializeSpinLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keinitializespinlock) to initialize the corresponding executive spin lock. Support routines that require an initialized executive spin lock include the following:

- [**KeAcquireSpinLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keacquirespinlock) and, subsequently, [**KeReleaseSpinLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kereleasespinlock)

- [**KeAcquireSpinLockAtDpcLevel**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keacquirespinlockatdpclevel) and, subsequently, [**KeReleaseSpinLockFromDpcLevel**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kereleasespinlockfromdpclevel)

- [**KeAcquireInStackQueuedSpinLock**](/previous-versions/windows/hardware/drivers/ff551899(v=vs.85)) and, subsequently, [**KeReleaseInStackQueuedSpinLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kereleaseinstackqueuedspinlock)

- [**KeAcquireInStackQueuedSpinLockAtDpcLevel**](/previous-versions/windows/hardware/drivers/ff551908(v=vs.85)) and, subsequently, [**KeReleaseInStackQueuedSpinLockFromDpcLevel**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kereleaseinstackqueuedspinlockfromdpclevel)

- An **ExInterlocked*Xxx*** routine

Before calling [**IoConnectInterrupt**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioconnectinterrupt) and [**KeSynchronizeExecution**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kesynchronizeexecution), a lowest-level driver must call [**KeInitializeSpinLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keinitializespinlock) to initialize an interrupt spin lock for which it provides storage.

 

