---
title: Multi-Tier Reset in Storport
author: windows-driver-content
description: Multi-Tier Reset in Storport
ms.assetid: 11c717b9-5154-43dd-b357-ff093cabec4b
keywords: ["Storport drivers WDK , errors", "errors WDK Storport"]
---

# Multi-Tier Reset in Storport


## <span id="ddk_multi_tier_reset_in_storport_kg"></span><span id="DDK_MULTI_TIER_RESET_IN_STORPORT_KG"></span>


The Storport driver implements a more advanced reset scheme than the SCSI Port driver. The SCSI Port technique of resetting the entire bus is an expensive operation, even on a SCSI bus. On high-performance buses, such as a fibre channel bus, a bus reset might not even be possible.

When possible, the Storport driver and related higher-level drivers attempt to reset the logical unit. If this fails, Storport attempts to reset the device. Finally, if this approach also fails, Storport resets the bus. This sequence generates significantly fewer bus-reset operations.

To address the more complex requirements of high performance buses, Storport implements a multitier reset operation that allows a greater variety of reset options. There are two types of reset that are sent via SRBs that can be requested, instead of one:

Finally, the bus reset operation is effected through a synchronous callback routine, [**HwStorResetBus**](https://msdn.microsoft.com/library/windows/hardware/ff557415).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Multi-Tier%20Reset%20in%20Storport%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


