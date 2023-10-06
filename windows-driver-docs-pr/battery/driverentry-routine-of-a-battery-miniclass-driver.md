---
title: "Battery miniclass driver: DriverEntry routine"
description: "Discover the DriverEntry routine in a battery miniclass driver and its role in the initialization process."
keywords:
- battery miniclass drivers WDK, routines
- DriverEntry WDK battery
ms.date: 10/05/2023
---

# Battery miniclass driver: DriverEntry routine

The [DriverEntry](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) routine initializes the miniclass driver.

## Driver-specific entry points

The miniclass driver's [DriverEntry](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) routine sets up the following driver-specific entry points:

- The [Unload](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_unload) routine in *DriverObject*->**DriverUnload**
- The driver's [AddDevice](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device) routine in *DriverObject*->**DriverExtension**->**AddDevice**
- The [DRIVER_DISPATCH](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) callback function in *DriverObject*->**MajorFunction**\[[IRP_MJ_POWER](../kernel/irp-mj-power.md)\]
- The [DRIVER_DISPATCH](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) callback function in *DriverObject*->**MajorFunction**\[[IRP_MJ_PNP](../kernel/irp-mj-pnp.md)\]
- The [DRIVER_DISPATCH](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) callback function in *DriverObject*->**MajorFunction**\[[IRP_MJ_CREATE](../kernel/irp-mj-create.md)\]
- The [DRIVER_DISPATCH](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) callback function in *DriverObject*->**MajorFunction**\[[IRP_MJ_CLOSE](../kernel/irp-mj-close.md)\]
- The [DRIVER_DISPATCH](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) callback function in *DriverObject*->**MajorFunction**\[[IRP_MJ_DEVICE_CONTROL](../kernel/irp-mj-device-control.md)\]
- The [DRIVER_DISPATCH](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) callback function in *DriverObject*->**MajorFunction**\[[IRP_MJ_SYSTEM_CONTROL](../kernel/irp-mj-system-control.md)\].

Here's a sample code that initializes these entry points for a hypothetical NewBatt miniclass driver:

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

Since battery-specific state information is unknown until the PnP Manager calls the miniclass driver's *AddDevice* routine, the [DriverEntry](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) routine doesn't initialize any such state. Device-specific initialization is performed in the *AddDevice* routine.

## Additional routine-specific requirements

For more information on routine-specific requirements, see the following topics:

- [AddDevice routine for battery miniclass drivers](adddevice-routine-of-a-battery-miniclass-driver.md)
- [Battery miniclass driver's DispatchDeviceControl routine](dispatchdevicecontrol-routine-of-a-battery-miniclass-driver.md)
- [DispatchSystemControl routine of a battery miniclass driver](dispatchsystemcontrol-routine-of-a-battery-miniclass-driver.md)
- [Unload routine of a battery miniclass driver](unload-routine-of-a-battery-miniclass-driver.md)
- [DispatchPower](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch)
- [DispatchPnP](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch)
- [DRIVER_DISPATCH](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch)
- [DispatchClose](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch)
