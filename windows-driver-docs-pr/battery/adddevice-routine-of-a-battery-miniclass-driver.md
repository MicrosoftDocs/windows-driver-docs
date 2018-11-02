---
title: AddDevice Routine of a Battery Miniclass Driver
description: AddDevice Routine of a Battery Miniclass Driver
ms.assetid: 1b34e223-e238-4547-bd44-754be2e6749c
keywords:
- AddDevice routine WDK battery
- battery miniclass drivers WDK , routines
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# AddDevice Routine of a Battery Miniclass Driver


## <span id="ddk_adddevice_routine_of_battery_miniclass_driver_dg"></span><span id="DDK_ADDDEVICE_ROUTINE_OF_BATTERY_MINICLASS_DRIVER_DG"></span>


Every battery miniclass driver must have an [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine, which initializes battery-specific state. The PnP Manager calls the *AddDevice* routine for each battery device controlled by this miniclass driver.

In addition to the tasks required of a PnP *AddDevice* routine, the *AddDevice* routine for a battery miniclass driver must also do the following:

1.  Create an FDO for the battery and attach the FDO to the device stack for the controller.

2.  Initialize the [**BATTERY\_MINIPORT\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff536287) structure and call [**BatteryClassInitializeDevice**](https://msdn.microsoft.com/library/windows/hardware/ff536266) to register the miniclass driver with the battery class driver.

3.  Perform any other initialization required for the device.

 

 




