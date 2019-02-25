---
title: Storage Driver's Return from DriverEntry
description: Storage Driver's Return from DriverEntry
ms.assetid: a5772e9c-ec7b-4570-aaae-d2879f7e0bc7
keywords:
- return values WDK SCSI
- ScsiPortInitialize
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Storage Driver's Return from DriverEntry


## <span id="ddk_storage_driver_s_return_from_driverentry_kg"></span><span id="DDK_STORAGE_DRIVER_S_RETURN_FROM_DRIVERENTRY_KG"></span>


When [**ScsiPortInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff564645) returns control, the [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff552654) routine propagates the return value of **ScsiPortInitialize** when **DriverEntry** itself returns control.

If a miniport driver calls **ScsiPortInitialize** more than once, its **DriverEntry** routine *must propagate thelowest value* returned by **ScsiPortInitialize**. A miniport driver writer cannot make any assumptions about the values returned by **ScsiPortInitialize**.

 

 




