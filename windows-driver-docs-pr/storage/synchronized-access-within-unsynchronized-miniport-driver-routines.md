---
title: Synchronized Access within Unsynchronized Miniport Driver Routines
description: Synchronized Access within Unsynchronized Miniport Driver Routines
ms.assetid: a1bc3bff-b109-4a52-8466-48a0be7611b7
---

# Synchronized Access within Unsynchronized Miniport Driver Routines


## <span id="ddk_synchronized_access_within_unsynchronized_miniport_driver_routines"></span><span id="DDK_SYNCHRONIZED_ACCESS_WITHIN_UNSYNCHRONIZED_MINIPORT_DRIVER_ROUTINES"></span>


Even when a miniport driver executes in full-duplex mode or does unsynchronized processing of SRBs in an [**HwStorBuildIo**](https://msdn.microsoft.com/library/windows/hardware/ff557369) routine, it might still require synchronized access to its device extension. The library of support routines provided by the Storport driver includes [**StorPortSynchronizeAccess**](https://msdn.microsoft.com/library/windows/hardware/ff567511), a routine that allows miniport drivers to synchronize access to critical data structures such as the device extension.

When the miniport driver calls **StorPortSynchronizeAccess**, it must supply the routine with a pointer to a callback routine. The callback routine contains the part of the SRB's processing that must be synchronized with the host bus adapter's interrupt handler. For better performance, write your driver to spend as little time as possible executing the callback routine.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Synchronized%20Access%20within%20Unsynchronized%20Miniport%20Driver%20Routines%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




