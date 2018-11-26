---
title: Multi-Tier Reset in Storport
description: Multi-Tier Reset in Storport
ms.assetid: 11c717b9-5154-43dd-b357-ff093cabec4b
keywords:
- Storport drivers WDK , errors
- errors WDK Storport
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Multi-Tier Reset in Storport


## <span id="ddk_multi_tier_reset_in_storport_kg"></span><span id="DDK_MULTI_TIER_RESET_IN_STORPORT_KG"></span>


The Storport driver implements a more advanced reset scheme than the SCSI Port driver. The SCSI Port technique of resetting the entire bus is an expensive operation, even on a SCSI bus. On high-performance buses, such as a fibre channel bus, a bus reset might not even be possible.

When possible, the Storport driver and related higher-level drivers attempt to reset the logical unit. If this fails, Storport attempts to reset the device. Finally, if this approach also fails, Storport resets the bus. This sequence generates significantly fewer bus-reset operations.

To address the more complex requirements of high performance buses, Storport implements a multitier reset operation that allows a greater variety of reset options. There are two types of reset that are sent via SRBs that can be requested, instead of one:

Finally, the bus reset operation is effected through a synchronous callback routine, [**HwStorResetBus**](https://msdn.microsoft.com/library/windows/hardware/ff557415).

 

 




