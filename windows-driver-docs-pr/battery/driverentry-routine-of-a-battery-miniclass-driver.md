---
title: DriverEntry Routine of a Battery Miniclass Driver
description: DriverEntry Routine of a Battery Miniclass Driver
ms.assetid: dc7c9f75-835b-4646-b30b-24c9dcb6ed2d
keywords: ["battery miniclass drivers WDK , routines", "DriverEntry WDK battery"]
---

# DriverEntry Routine of a Battery Miniclass Driver


## <span id="ddk_driverentry_routine_of_battery_miniclass_driver_dg"></span><span id="DDK_DRIVERENTRY_ROUTINE_OF_BATTERY_MINICLASS_DRIVER_DG"></span>


The [*DriverEntry*](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine initializes the miniclass driver.

The miniclass driver's [*DriverEntry*](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine sets up the following driver-specific entry points:

-   The [*Unload*](https://msdn.microsoft.com/library/windows/hardware/ff564886) routine in *DriverObject*-&gt;**DriverUnload**

-   The driver's [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine in *DriverObject*-&gt;**DriverExtension**-&gt;**AddDevice**

-   The [*DispatchPower*](https://msdn.microsoft.com/library/windows/hardware/ff543354) routine in *DriverObject*-&gt;**MajorFunction**\[[**IRP\_MJ\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff550784)\]

-   The [*DispatchPnP*](https://msdn.microsoft.com/library/windows/hardware/ff543341) routine in *DriverObject*-&gt;**MajorFunction**\[[**IRP\_MJ\_PNP**](https://msdn.microsoft.com/library/windows/hardware/ff550772)\]

-   The [*DispatchCreate*](https://msdn.microsoft.com/library/windows/hardware/ff543266) routine in *DriverObject*-&gt;**MajorFunction**\[[**IRP\_MJ\_CREATE**](https://msdn.microsoft.com/library/windows/hardware/ff550729)\]

-   The [*DispatchClose*](https://msdn.microsoft.com/library/windows/hardware/ff543255) routine in *DriverObject*-&gt;**MajorFunction**\[[**IRP\_MJ\_CLOSE**](https://msdn.microsoft.com/library/windows/hardware/ff550720)\]

-   The [*DispatchDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff543287) routine in *DriverObject*-&gt;**MajorFunction**\[[**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550744)\]

-   The [*DispatchSystemControl*](https://msdn.microsoft.com/library/windows/hardware/ff543412) routine in *DriverObject*-&gt;**MajorFunction**\[[**IRP\_MJ\_SYSTEM\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550813)\].

The following sample code initializes these entry points for a hypothetical NewBatt miniclass driver:

```
DriverObject->DriverUnload = NewBattUnload;
DriverObject->DriverExtension->AddDevice = NewBattAddDevice; 
DriverObject->MajorFunction[IRP_MJ_DEVICE_CONTROL] = NewBattDispatchDeviceControl;
DriverObject->MajorFunction[IRP_MJ_CREATE] = NewBattDispatchCreate;
DriverObject->MajorFunction[IRP_MJ_CLOSE] = NewBattDispatchClose;
DriverObject->MajorFunction[IRP_MJ_PNP] = NewBattDispatchPnp;
DriverObject->MajorFunction[IRP_MJ_POWER] = NewBattDispatchPower;
DriverObject->MajorFunction[IRP_MJ_SYSTEM_CONTROL] = NewBattSystemControl;
```

Because battery-specific state information is not known until the PnP Manager calls the miniclass driver's *AddDevice* routine, the [*DriverEntry*](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine does not initialize any such state. Device-specific initialization is performed in the *AddDevice* routine.

For additional routine-specific requirements, see the following topics:

[AddDevice Routine of a Battery Miniclass Driver](adddevice-routine-of-a-battery-miniclass-driver.md)

[DispatchDeviceControl Routine of a Battery Miniclass Driver](dispatchdevicecontrol-routine-of-a-battery-miniclass-driver.md)

[DispatchSystemControl Routine of a Battery Miniclass Driver](dispatchsystemcontrol-routine-of-a-battery-miniclass-driver.md)

[Unload Routine of a Battery Miniclass Driver](unload-routine-of-a-battery-miniclass-driver.md)

[*DispatchPower*](https://msdn.microsoft.com/library/windows/hardware/ff543354)

[*DispatchPnP*](https://msdn.microsoft.com/library/windows/hardware/ff543341)

[*DispatchCreate*](https://msdn.microsoft.com/library/windows/hardware/ff543266)

[*DispatchClose*](https://msdn.microsoft.com/library/windows/hardware/ff543255)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[battery\battery]:%20DriverEntry%20Routine%20of%20a%20Battery%20Miniclass%20Driver%20%20RELEASE:%20%286/7/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


