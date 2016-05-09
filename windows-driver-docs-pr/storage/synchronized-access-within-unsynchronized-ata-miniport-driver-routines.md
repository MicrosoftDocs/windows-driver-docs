---
title: Synchronized Access within Unsynchronized ATA Miniport Driver Routines
author: windows-driver-content
description: Synchronized Access within Unsynchronized ATA Miniport Driver Routines
ms.assetid: ed047579-9f22-4725-a4b0-3c44b8db89ef
keywords: ["ATA Port drivers WDK , synchronization", "synchronization WDK ATA Port driver", "unsynchronized processing WDK ATA Port driver"]
---

# Synchronized Access within Unsynchronized ATA Miniport Driver Routines


## <span id="ddk_synchronized_access_within_unsynchronized_ata_miniport_driver_rout"></span><span id="DDK_SYNCHRONIZED_ACCESS_WITHIN_UNSYNCHRONIZED_ATA_MINIPORT_DRIVER_ROUT"></span>


Even when an ATA miniport driver does unsynchronized processing of I/O requests in its [**IdeHwBuildIo**](https://msdn.microsoft.com/library/windows/hardware/ff557462) routine, it can synchronize access to critical system structures by calling [**AtaPortRequestSynchronizedRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff550223). This routine resembles the [**StorPortSynchronizeAccess**](https://msdn.microsoft.com/library/windows/hardware/ff567511) routine that is provided in the Storport I/O model. For more information about how Storport miniport drivers manage synchronized access of critical data structures, see [Synchronized Access within Unsynchronized Miniport Driver Routines](synchronized-access-within-unsynchronized-miniport-driver-routines.md).

When an ATA miniport driver calls **AtaPortRequestSynchronizedRoutine**, it must supply a pointer to a callback routine. The callback routine processes the part of the I/O request that must be synchronized with the interrupt handler. For better performance, write your driver to spend as little time as possible to execute the callback routine.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Synchronized%20Access%20within%20Unsynchronized%20ATA%20Miniport%20Driver%20Routines%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


