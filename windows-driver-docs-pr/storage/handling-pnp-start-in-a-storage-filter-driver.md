---
title: Handling PnP Start in a Storage Filter Driver
description: Handling PnP Start in a Storage Filter Driver
ms.assetid: 02a87fec-772d-4416-bd3a-5c7f98e8d55e
keywords:
- storage filter drivers WDK , PnP
- filter drivers WDK storage , PnP
- SFD WDK storage , PnP
- PnP WDK storage
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling PnP Start in a Storage Filter Driver


## <span id="ddk_handling_pnp_start_in_a_storage_filter_driver_kg"></span><span id="DDK_HANDLING_PNP_START_IN_A_STORAGE_FILTER_DRIVER_KG"></span>


A storage filter driver (SFD) performs device-specific initialization and sets up its device extension when the PnP manager calls its [*DispatchPnP*](https://msdn.microsoft.com/library/windows/hardware/ff543341) routine with a start request ([**IRP\_MJ\_PNP**](https://msdn.microsoft.com/library/windows/hardware/ff550772) with [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749)). An SFD handles a start request in much the same way as does a storage class driver.

For information about how a storage class driver handles a start request and sets up its device extension, see [Storage Class Drivers](storage-class-drivers.md). For general information about handling a PnP start request, see [Plug and Play](https://msdn.microsoft.com/library/windows/hardware/ff547125).

 

 




