---
title: Spin Locks in Video Miniport Drivers
description: Spin Locks in Video Miniport Drivers
keywords:
- video miniport drivers WDK Windows 2000 , spin locks
- spin locks WDK video miniport
- locking WDK video miniport
ms.date: 04/20/2017
---

# Spin Locks in Video Miniport Drivers


## <span id="ddk_spin_locks_in_video_miniport_drivers_gg"></span><span id="DDK_SPIN_LOCKS_IN_VIDEO_MINIPORT_DRIVERS_GG"></span>


The video port driver supports multiprocessor synchronization in the video miniport driver by providing spin lock functions to protect data when one or more miniport driver threads are running at or below IRQL DISPATCH\_LEVEL. The video port driver's spin lock functions enable miniport driver threads to create, acquire, release, and destroy spin locks. The video port driver provides these functions because video miniport driver writers must implement miniport drivers using functions provided exclusively by the video port driver. For a general discussion on spin locks, see [Spin Locks](../kernel/introduction-to-spin-locks.md).

Before a video miniport driver can use a spin lock, it must create the spin lock by calling [**VideoPortCreateSpinLock**](/windows-hardware/drivers/ddi/video/nf-video-videoportcreatespinlock). After the spin lock has been created, a thread can attempt to acquire the spin lock by a call to either [**VideoPortAcquireSpinLock**](/previous-versions/ff570175(v=vs.85)) or [**VideoPortAcquireSpinLockAtDpcLevel**](/previous-versions/ff570176(v=vs.85)). The first function of this pair can be used when the miniport driver's thread is at or below IRQL DISPATCH\_LEVEL. The second function can be used only when the thread is running at IRQL DISPATCH\_LEVEL.

When the thread that is holding the spin lock has completed its task, the miniport driver should release the spin lock. If the thread acquired the spin lock in a call to **VideoPortAcquireSpinLock**, it should use [**VideoPortReleaseSpinLock**](/previous-versions/ff570357(v=vs.85)) to release the spin lock. In the call to **VideoPortReleaseSpinLock**, the thread must pass the same value in the *NewIrql* parameter that it received in the *OldIrql* parameter of **VideoPortAcquireSpinLock** when that function returned. If the thread called **VideoPortAcquireSpinLockAtDpcLevel**, it should call [**VideoPortReleaseSpinLockFromDpcLevel**](/previous-versions/ff570358(v=vs.85)) to release the spin lock.

When the miniport driver has no further use for the spin lock, it should destroy the spin lock by a call to [**VideoPortDeleteSpinLock**](/windows-hardware/drivers/ddi/video/nf-video-videoportdeletespinlock).

 

