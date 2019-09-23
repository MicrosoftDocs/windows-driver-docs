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


The [*DriverEntry*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_initialize) routine initializes the miniclass driver.

The miniclass driver's [*DriverEntry*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_initialize) routine sets up the following driver-specific entry points:

-   The [*Unload*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_unload) routine in *DriverObject*-&gt;**DriverUnload**

-   The driver's [*AddDevice*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_add_device) routine in *DriverObject*-&gt;**DriverExtension**-&gt;**AddDevice**

-   The [*DRIVER_DISPATCH*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_dispatch) callback function in *DriverObject*-&gt;**MajorFunction**\[[**IRP\_MJ\_POWER**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mj-power)\]

-   The [*DRIVER_DISPATCH*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_dispatch) callback function in *DriverObject*-&gt;**MajorFunction**\[[**IRP\_MJ\_PNP**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mj-pnp)\]

-   The [*DRIVER_DISPATCH*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_dispatch) callback function in *DriverObject*-&gt;**MajorFunction**\[[**IRP\_MJ\_CREATE**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mj-create)\]

-   The [*DRIVER_DISPATCH*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_dispatch) callback function in *DriverObject*-&gt;**MajorFunction**\[[**IRP\_MJ\_CLOSE**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mj-close)\]

-   The [*DRIVER_DISPATCH*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_dispatch) callback function in *DriverObject*-&gt;**MajorFunction**\[[**IRP\_MJ\_DEVICE\_CONTROL**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mj-device-control)\]

-   The [*DRIVER_DISPATCH*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_dispatch) callback function in *DriverObject*-&gt;**MajorFunction**\[[**IRP\_MJ\_SYSTEM\_CONTROL**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mj-system-control)\].

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

Because battery-specific state information is not known until the PnP Manager calls the miniclass driver's *AddDevice* routine, the [*DriverEntry*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_initialize) routine does not initialize any such state. Device-specific initialization is performed in the *AddDevice* routine.

For additional routine-specific requirements, see the following topics:

[AddDevice Routine of a Battery Miniclass Driver](adddevice-routine-of-a-battery-miniclass-driver.md)

[DispatchDeviceControl Routine of a Battery Miniclass Driver](dispatchdevicecontrol-routine-of-a-battery-miniclass-driver.md)

[DispatchSystemControl Routine of a Battery Miniclass Driver](dispatchsystemcontrol-routine-of-a-battery-miniclass-driver.md)

[Unload Routine of a Battery Miniclass Driver](unload-routine-of-a-battery-miniclass-driver.md)

[*DispatchPower*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_dispatch)

[*DispatchPnP*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_dispatch)

[*DRIVER_DISPATCH*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_dispatch)

[*DispatchClose*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_dispatch)

 

 




