---
title: AddDevice Routine of a Battery Miniclass Driver
description: AddDevice Routine of a Battery Miniclass Driver
ms.assetid: 1b34e223-e238-4547-bd44-754be2e6749c
keywords: ["AddDevice routine WDK battery", "battery miniclass drivers WDK , routines"]
---

# AddDevice Routine of a Battery Miniclass Driver


## <span id="ddk_adddevice_routine_of_battery_miniclass_driver_dg"></span><span id="DDK_ADDDEVICE_ROUTINE_OF_BATTERY_MINICLASS_DRIVER_DG"></span>


Every battery miniclass driver must have an [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine, which initializes battery-specific state. The PnP Manager calls the *AddDevice* routine for each battery device controlled by this miniclass driver.

In addition to the tasks required of a PnP *AddDevice* routine, the *AddDevice* routine for a battery miniclass driver must also do the following:

1.  Create an FDO for the battery and attach the FDO to the device stack for the controller.

2.  Initialize the [**BATTERY\_MINIPORT\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff536287) structure and call [**BatteryClassInitializeDevice**](https://msdn.microsoft.com/library/windows/hardware/ff536266) to register the miniclass driver with the battery class driver.

3.  Perform any other initialization required for the device.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[battery\battery]:%20AddDevice%20Routine%20of%20a%20Battery%20Miniclass%20Driver%20%20RELEASE:%20%286/7/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




