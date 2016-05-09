---
title: Storage Filter Driver's AddDevice Routine
author: windows-driver-content
description: Storage Filter Driver's AddDevice Routine
ms.assetid: 7970fb3e-4e4c-4ff7-9738-e09454a864c4
keywords: ["storage filter drivers WDK , AddDevice", "filter drivers WDK storage , AddDevice", "SFD WDK storage , AddDevice", "AddDevice routine WDK storage"]
---

# Storage Filter Driver's AddDevice Routine


## <span id="ddk_storage_filter_driver_s_adddevice_routine_kg"></span><span id="DDK_STORAGE_FILTER_DRIVER_S_ADDDEVICE_ROUTINE_KG"></span>


The PnP manager calls the [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine of a storage filter driver when it detects a device controlled by that driver. The *AddDevice* routine of an storage filter driver (SFD) is similar to that of a storage class driver, except that it must not attempt to claim the device (SRB\_FUNCTION\_CLAIM\_DEVICE).

For information about a storage class driver's [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine, see [Storage Class Drivers](storage-class-drivers.md). For general information about a PnP driver's *AddDevice* routine, see [Plug and Play](https://msdn.microsoft.com/library/windows/hardware/ff547125).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Storage%20Filter%20Driver's%20AddDevice%20Routine%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


