---
title: Unload Routine of a Battery Miniclass Driver
description: Unload Routine of a Battery Miniclass Driver
ms.assetid: f0acbf94-95d1-4a9d-aafd-1f868c5560cc
keywords: ["battery miniclass drivers WDK , routines", "Unload routine", "verifying device unloads", "unloading devices"]
---

# Unload Routine of a Battery Miniclass Driver


## <span id="ddk_unload_routine_of_battery_miniclass_driver_dg"></span><span id="DDK_UNLOAD_ROUTINE_OF_BATTERY_MINICLASS_DRIVER_DG"></span>


The *Unload* routine for a battery miniclass driver ensures that all the driver's devices have been removed and frees any resources the miniclass driver has allocated.

The *Unload* routine should first check to ensure that all its devices have been removed and, if not, do the following for each remaining device:

1.  Call [**BatteryClassUnload**](https://msdn.microsoft.com/library/windows/hardware/ff536271) to inform the class driver that the miniclass driver is unloading the device.

2.  Disable any device notifications from lower drivers, such as the ACPI driver, using that driver's interface.

3.  Delete the device object for the device by calling [**IoDeleteDevice**](https://msdn.microsoft.com/library/windows/hardware/ff549083), as follows:

    ```
        IoDeleteDevice (NewBatt->DeviceObject);
    ```

After all the miniclass driver's devices are unloaded, the *Unload* routine should free any resources allocated by the miniclass driver.

The miniclass driver's *Unload* routine can be called at any time after all the driver's devices have been removed. The PnP Manager calls the *Unload* routine in the context of a system thread at IRQL = PASSIVE\_LEVEL.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[battery\battery]:%20Unload%20Routine%20of%20a%20Battery%20Miniclass%20Driver%20%20RELEASE:%20%286/7/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




