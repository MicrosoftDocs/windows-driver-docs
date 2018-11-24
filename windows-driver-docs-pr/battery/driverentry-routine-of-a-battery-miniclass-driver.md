---
title: DriverEntry Routine of a Battery Miniclass Driver
description: DriverEntry Routine of a Battery Miniclass Driver
ms.assetid: dc7c9f75-835b-4646-b30b-24c9dcb6ed2d
keywords:
- battery miniclass drivers WDK , routines
- DriverEntry WDK battery
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DriverEntry Routine of a Battery Miniclass Driver


## <span id="ddk_driverentry_routine_of_battery_miniclass_driver_dg"></span><span id="DDK_DRIVERENTRY_ROUTINE_OF_BATTERY_MINICLASS_DRIVER_DG"></span>


The [*DriverEntry*](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine initializes the miniclass driver.

The miniclass driver's [*DriverEntry*](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine sets up the following driver-specific entry points:

-   The [*Unload*](https://msdn.microsoft.com/library/windows/hardware/ff564886) routine in *DriverObject*-&gt;**DriverUnload**

-   The driver's [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine in *DriverObject*-&gt;**DriverExtension**-&gt;**AddDevice**

-   The [*DRIVER_DISPATCH*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_dispatch) callback function in *DriverObject*-&gt;**MajorFunction**\[[**IRP\_MJ\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff550784)\]

-   The [*DRIVER_DISPATCH*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_dispatch) callback function in *DriverObject*-&gt;**MajorFunction**\[[**IRP\_MJ\_PNP**](https://msdn.microsoft.com/library/windows/hardware/ff550772)\]

-   The [*DRIVER_DISPATCH*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_dispatch) callback function in *DriverObject*-&gt;**MajorFunction**\[[**IRP\_MJ\_CREATE**](https://msdn.microsoft.com/library/windows/hardware/ff550729)\]

-   The [*DRIVER_DISPATCH*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_dispatch) callback function in *DriverObject*-&gt;**MajorFunction**\[[**IRP\_MJ\_CLOSE**](https://msdn.microsoft.com/library/windows/hardware/ff550720)\]

-   The [*DRIVER_DISPATCH*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_dispatch) callback function in *DriverObject*-&gt;**MajorFunction**\[[**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550744)\]

-   The [*DRIVER_DISPATCH*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_dispatch) callback function in *DriverObject*-&gt;**MajorFunction**\[[**IRP\_MJ\_SYSTEM\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550813)\].

The following sample code initializes these entry points for a hypothetical NewBatt miniclass driver:

```cpp
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

[*DRIVER_DISPATCH*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_dispatch)

[*DispatchClose*](https://msdn.microsoft.com/library/windows/hardware/ff543255)

 

 




