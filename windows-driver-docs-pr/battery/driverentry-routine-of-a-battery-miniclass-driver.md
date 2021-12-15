---
title: DriverEntry Routine of a Battery Miniclass Driver
description: DriverEntry Routine of a Battery Miniclass Driver
keywords:
- battery miniclass drivers WDK , routines
- DriverEntry WDK battery
ms.date: 04/20/2017
---

# DriverEntry Routine of a Battery Miniclass Driver


## <span id="ddk_driverentry_routine_of_battery_miniclass_driver_dg"></span><span id="DDK_DRIVERENTRY_ROUTINE_OF_BATTERY_MINICLASS_DRIVER_DG"></span>


The [*DriverEntry*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) routine initializes the miniclass driver.

The miniclass driver's [*DriverEntry*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) routine sets up the following driver-specific entry points:

-   The [*Unload*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_unload) routine in *DriverObject*-&gt;**DriverUnload**

-   The driver's [*AddDevice*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device) routine in *DriverObject*-&gt;**DriverExtension**-&gt;**AddDevice**

-   The [*DRIVER_DISPATCH*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) callback function in *DriverObject*-&gt;**MajorFunction**\[[**IRP\_MJ\_POWER**](../kernel/irp-mj-power.md)\]

-   The [*DRIVER_DISPATCH*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) callback function in *DriverObject*-&gt;**MajorFunction**\[[**IRP\_MJ\_PNP**](../kernel/irp-mj-pnp.md)\]

-   The [*DRIVER_DISPATCH*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) callback function in *DriverObject*-&gt;**MajorFunction**\[[**IRP\_MJ\_CREATE**](../kernel/irp-mj-create.md)\]

-   The [*DRIVER_DISPATCH*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) callback function in *DriverObject*-&gt;**MajorFunction**\[[**IRP\_MJ\_CLOSE**](../kernel/irp-mj-close.md)\]

-   The [*DRIVER_DISPATCH*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) callback function in *DriverObject*-&gt;**MajorFunction**\[[**IRP\_MJ\_DEVICE\_CONTROL**](../kernel/irp-mj-device-control.md)\]

-   The [*DRIVER_DISPATCH*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) callback function in *DriverObject*-&gt;**MajorFunction**\[[**IRP\_MJ\_SYSTEM\_CONTROL**](../kernel/irp-mj-system-control.md)\].

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

Because battery-specific state information is not known until the PnP Manager calls the miniclass driver's *AddDevice* routine, the [*DriverEntry*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) routine does not initialize any such state. Device-specific initialization is performed in the *AddDevice* routine.

For additional routine-specific requirements, see the following topics:

[AddDevice Routine of a Battery Miniclass Driver](adddevice-routine-of-a-battery-miniclass-driver.md)

[DispatchDeviceControl Routine of a Battery Miniclass Driver](dispatchdevicecontrol-routine-of-a-battery-miniclass-driver.md)

[DispatchSystemControl Routine of a Battery Miniclass Driver](dispatchsystemcontrol-routine-of-a-battery-miniclass-driver.md)

[Unload Routine of a Battery Miniclass Driver](unload-routine-of-a-battery-miniclass-driver.md)

[*DispatchPower*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch)

[*DispatchPnP*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch)

[*DRIVER_DISPATCH*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch)

[*DispatchClose*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch)

 

