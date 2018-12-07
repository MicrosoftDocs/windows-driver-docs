---
title: Unload Routine of a Battery Miniclass Driver
description: Unload Routine of a Battery Miniclass Driver
ms.assetid: f0acbf94-95d1-4a9d-aafd-1f868c5560cc
keywords:
- battery miniclass drivers WDK , routines
- Unload routine
- verifying device unloads
- unloading devices
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Unload Routine of a Battery Miniclass Driver


## <span id="ddk_unload_routine_of_battery_miniclass_driver_dg"></span><span id="DDK_UNLOAD_ROUTINE_OF_BATTERY_MINICLASS_DRIVER_DG"></span>


The *Unload* routine for a battery miniclass driver ensures that all the driver's devices have been removed and frees any resources the miniclass driver has allocated.

The *Unload* routine should first check to ensure that all its devices have been removed and, if not, do the following for each remaining device:

1.  Call [**BatteryClassUnload**](https://msdn.microsoft.com/library/windows/hardware/ff536271) to inform the class driver that the miniclass driver is unloading the device.

2.  Disable any device notifications from lower drivers, such as the ACPI driver, using that driver's interface.

3.  Delete the device object for the device by calling [**IoDeleteDevice**](https://msdn.microsoft.com/library/windows/hardware/ff549083), as follows:

    ```cpp
        IoDeleteDevice (NewBatt->DeviceObject);
    ```

After all the miniclass driver's devices are unloaded, the *Unload* routine should free any resources allocated by the miniclass driver.

The miniclass driver's *Unload* routine can be called at any time after all the driver's devices have been removed. The PnP Manager calls the *Unload* routine in the context of a system thread at IRQL = PASSIVE\_LEVEL.

 

 




