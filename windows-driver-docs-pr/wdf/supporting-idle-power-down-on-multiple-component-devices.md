---
title: Supporting Idle Power-Down on Multiple-Component Devices
description: Supporting Idle Power-Down on Multiple-Component Devices
ms.assetid: 81C80E30-DAF4-4EE4-AA29-AB40A6827C26
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting Idle Power-Down on Multiple-Component Devices


\[Applies to KMDF only\]

A KMDF driver for a multiple-component device can support [idle power-down](supporting-idle-power-down.md) and functional power states. Because in this case the driver registers directly with the power management framework (PoFx), the driver must coordinate the resulting Dx state changes with PoFx.

## Providing Device Power Policy Idle Settings


When it calls [**WdfDeviceAssignS0IdleSettings**](https://msdn.microsoft.com/library/windows/hardware/ff545903), the driver must set **IdleTimeoutType** to **DriverManagedIdleTimeout** in the [**WDF\_DEVICE\_POWER\_POLICY\_IDLE\_SETTINGS**](https://msdn.microsoft.com/library/windows/hardware/ff551270) structure. In addition, the driver must set **PowerUpIdleDeviceOnSystemWake** to **WdfTrue**, and **IdleCaps** to [**IdleCannotWakeFromS0**](https://msdn.microsoft.com/library/windows/hardware/ff552429), as shown in the following example.

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


In [*EvtDeviceSelfManagedIoInit*](https://msdn.microsoft.com/library/windows/hardware/ff540902), the driver calls [**WdfDeviceStopIdle**](https://msdn.microsoft.com/library/windows/hardware/ff546921) to take a power reference, which prevents WDF from putting the device in a low-power state.

The driver releases the power reference by calling [**WdfDeviceResumeIdle**](https://msdn.microsoft.com/library/windows/hardware/ff546838) from its [*DevicePowerRequiredCallback*](https://msdn.microsoft.com/library/windows/hardware/hh450949) callback routine.

The driver typically specifies a very short idle timeout so that WDF puts the device into a low-power state soon after all power references are released.

## Transitioning from Low-Power (Dx) to Working (D0) State


In [*DevicePowerRequiredCallback*](https://msdn.microsoft.com/library/windows/hardware/hh450949), the driver must bring the device to its working (D0) state. To do so, it must defer to a worker thread a call to [**WdfDeviceStopIdle**](https://msdn.microsoft.com/library/windows/hardware/ff546921) with the *WaitForD0* parameter set to TRUE. This blocking call to **WdfDeviceStopIdle** must *not be made* from within *DevicePowerRequiredCallback*.

Instead, the driver must defer the blocking call to a worker thread that is running at passive level and is guaranteed not to make the [**WdfDeviceStopIdle**](https://msdn.microsoft.com/library/windows/hardware/ff546921) call in the context of a power-managed queue’s I/O dispatch routine.

If the driver has previously called [**WdfDeviceInitSetPowerPageable**](https://msdn.microsoft.com/library/windows/hardware/ff546766) (meaning it can access pageable data during power transitions), the driver can call [**WdfWorkItemCreate**](https://msdn.microsoft.com/library/windows/hardware/ff551201) to create a framework work item. If the driver has not set power-pageable, the driver must create its own system thread. For more information, see [**PsCreateSystemThread**](https://msdn.microsoft.com/library/windows/hardware/ff559932).

After [**WdfDeviceStopIdle**](https://msdn.microsoft.com/library/windows/hardware/ff546921) returns, even if the method returns an error, the driver must call [**PoFxReportDevicePoweredOn**](https://msdn.microsoft.com/library/windows/hardware/hh439526).

 

 





