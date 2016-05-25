---
title: Handling PnP Start in a Storage Filter Driver
author: windows-driver-content
description: Handling PnP Start in a Storage Filter Driver
ms.assetid: 02a87fec-772d-4416-bd3a-5c7f98e8d55e
keywords: ["storage filter drivers WDK , PnP", "filter drivers WDK storage , PnP", "SFD WDK storage , PnP", "PnP WDK storage"]
---

# Handling PnP Start in a Storage Filter Driver


## <span id="ddk_handling_pnp_start_in_a_storage_filter_driver_kg"></span><span id="DDK_HANDLING_PNP_START_IN_A_STORAGE_FILTER_DRIVER_KG"></span>


A storage filter driver (SFD) performs device-specific initialization and sets up its device extension when the PnP manager calls its [*DispatchPnP*](https://msdn.microsoft.com/library/windows/hardware/ff543341) routine with a start request ([**IRP\_MJ\_PNP**](https://msdn.microsoft.com/library/windows/hardware/ff550772) with [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749)). An SFD handles a start request in much the same way as does a storage class driver.

For information about how a storage class driver handles a start request and sets up its device extension, see [Storage Class Drivers](storage-class-drivers.md). For general information about handling a PnP start request, see [Plug and Play](https://msdn.microsoft.com/library/windows/hardware/ff547125).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Handling%20PnP%20Start%20in%20a%20Storage%20Filter%20Driver%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


