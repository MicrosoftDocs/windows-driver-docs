---
title: Supporting Idle Power-Down on Multiple-Component Devices
description: Supporting Idle Power-Down on Multiple-Component Devices
ms.date: 04/20/2017
---

# Supporting Idle Power-Down on Multiple-Component Devices


\[Applies to KMDF only\]

A KMDF driver for a multiple-component device can support [idle power-down](supporting-idle-power-down.md) and functional power states. Because in this case the driver registers directly with the power management framework (PoFx), the driver must coordinate the resulting Dx state changes with PoFx.

## Providing Device Power Policy Idle Settings


When it calls [**WdfDeviceAssignS0IdleSettings**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceassigns0idlesettings), the driver must set **IdleTimeoutType** to **DriverManagedIdleTimeout** in the [**WDF\_DEVICE\_POWER\_POLICY\_IDLE\_SETTINGS**](/windows-hardware/drivers/ddi/wdfdevice/ns-wdfdevice-_wdf_device_power_policy_idle_settings) structure. In addition, the driver must set **PowerUpIdleDeviceOnSystemWake** to **WdfTrue**, and **IdleCaps** to [**IdleCannotWakeFromS0**](/windows-hardware/drivers/ddi/wdfdevice/ne-wdfdevice-_wdf_power_policy_s0_idle_capabilities), as shown in the following example.

```ManagedCPlusPlus
WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS s0IdleSettings;

WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS_INIT(&s0IdleSettings, 
                                           IdleCannotWakeFromS0);
s0IdleSettings.IdleTimeoutType = DriverManagedIdleTimeout;
s0IdleSettings.PowerUpIdleDeviceOnSystemWake = WdfTrue;
s0IdleSettings.IdleTimeout = 1;
status = WdfDeviceAssignS0IdleSettings(device, &s0IdleSettings);
```

## Transitioning from Working (D0) to Low-Power (Dx) State


In [*EvtDeviceSelfManagedIoInit*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_init), the driver calls [**WdfDeviceStopIdle**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicestopidle) to take a power reference, which prevents WDF from putting the device in a low-power state.

The driver releases the power reference by calling [**WdfDeviceResumeIdle**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceresumeidle) from its [*DevicePowerRequiredCallback*](/windows-hardware/drivers/ddi/wdm/nc-wdm-po_fx_device_power_required_callback) callback routine.

The driver typically specifies a very short idle timeout so that WDF puts the device into a low-power state soon after all power references are released.

## Transitioning from Low-Power (Dx) to Working (D0) State


In [*DevicePowerRequiredCallback*](/windows-hardware/drivers/ddi/wdm/nc-wdm-po_fx_device_power_required_callback), the driver must bring the device to its working (D0) state. To do so, it must defer to a worker thread a call to [**WdfDeviceStopIdle**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicestopidle) with the *WaitForD0* parameter set to TRUE. This blocking call to **WdfDeviceStopIdle** must *not be made* from within *DevicePowerRequiredCallback*.

Instead, the driver must defer the blocking call to a worker thread that is running at passive level and is guaranteed not to make the [**WdfDeviceStopIdle**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicestopidle) call in the context of a power-managed queue’s I/O dispatch routine.

If the driver has previously called [**WdfDeviceInitSetPowerPageable**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetpowerpageable) (meaning it can access pageable data during power transitions), the driver can call [**WdfWorkItemCreate**](/windows-hardware/drivers/ddi/wdfworkitem/nf-wdfworkitem-wdfworkitemcreate) to create a framework work item. If the driver has not set power-pageable, the driver must create its own system thread. For more information, see [**PsCreateSystemThread**](/windows-hardware/drivers/ddi/wdm/nf-wdm-pscreatesystemthread).

After [**WdfDeviceStopIdle**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicestopidle) returns, even if the method returns an error, the driver must call [**PoFxReportDevicePoweredOn**](/windows-hardware/drivers/ddi/wdm/nf-wdm-pofxreportdevicepoweredon).

 

