---
title: Storage Filter Driver's AddDevice Routine
description: Storage Filter Driver's AddDevice Routine
ms.assetid: 7970fb3e-4e4c-4ff7-9738-e09454a864c4
keywords:
- storage filter drivers WDK , AddDevice
- filter drivers WDK storage , AddDevice
- SFD WDK storage , AddDevice
- AddDevice routine WDK storage
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Storage Filter Driver's AddDevice Routine


## <span id="ddk_storage_filter_driver_s_adddevice_routine_kg"></span><span id="DDK_STORAGE_FILTER_DRIVER_S_ADDDEVICE_ROUTINE_KG"></span>


The PnP manager calls the [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine of a storage filter driver when it detects a device controlled by that driver. The *AddDevice* routine of an storage filter driver (SFD) is similar to that of a storage class driver, except that it must not attempt to claim the device (SRB\_FUNCTION\_CLAIM\_DEVICE).

For information about a storage class driver's [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine, see [Storage Class Drivers](storage-class-drivers.md). For general information about a PnP driver's *AddDevice* routine, see [Plug and Play](https://msdn.microsoft.com/library/windows/hardware/ff547125).

 

 




