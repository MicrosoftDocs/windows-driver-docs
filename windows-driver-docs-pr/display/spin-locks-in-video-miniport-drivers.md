---
title: Spin Locks in Video Miniport Drivers
description: Spin Locks in Video Miniport Drivers
ms.assetid: 89ec0139-c109-44b1-aadd-a909a19ca1ee
keywords: ["video miniport drivers WDK Windows 2000 , spin locks", "spin locks WDK video miniport", "locking WDK video miniport"]
---

# Spin Locks in Video Miniport Drivers


## <span id="ddk_spin_locks_in_video_miniport_drivers_gg"></span><span id="DDK_SPIN_LOCKS_IN_VIDEO_MINIPORT_DRIVERS_GG"></span>


The video port driver supports multiprocessor synchronization in the video miniport driver by providing spin lock functions to protect data when one or more miniport driver threads are running at or below IRQL DISPATCH\_LEVEL. The video port driver's spin lock functions enable miniport driver threads to create, acquire, release, and destroy spin locks. The video port driver provides these functions because video miniport driver writers must implement miniport drivers using functions provided exclusively by the video port driver. For a general discussion on spin locks, see [Spin Locks](https://msdn.microsoft.com/library/windows/hardware/ff563830).

Before a video miniport driver can use a spin lock, it must create the spin lock by calling [**VideoPortCreateSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff570289). After the spin lock has been created, a thread can attempt to acquire the spin lock by a call to either [**VideoPortAcquireSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff570175) or [**VideoPortAcquireSpinLockAtDpcLevel**](https://msdn.microsoft.com/library/windows/hardware/ff570176). The first function of this pair can be used when the miniport driver's thread is at or below IRQL DISPATCH\_LEVEL. The second function can be used only when the thread is running at IRQL DISPATCH\_LEVEL.

When the thread that is holding the spin lock has completed its task, the miniport driver should release the spin lock. If the thread acquired the spin lock in a call to **VideoPortAcquireSpinLock**, it should use [**VideoPortReleaseSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff570357) to release the spin lock. In the call to **VideoPortReleaseSpinLock**, the thread must pass the same value in the *NewIrql* parameter that it received in the *OldIrql* parameter of **VideoPortAcquireSpinLock** when that function returned. If the thread called **VideoPortAcquireSpinLockAtDpcLevel**, it should call [**VideoPortReleaseSpinLockFromDpcLevel**](https://msdn.microsoft.com/library/windows/hardware/ff570358) to release the spin lock.

When the miniport driver has no further use for the spin lock, it should destroy the spin lock by a call to [**VideoPortDeleteSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff570293).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Spin%20Locks%20in%20Video%20Miniport%20Drivers%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




