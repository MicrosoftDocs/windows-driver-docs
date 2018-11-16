---
title: Handling IRP_MN_SET_POWER for Device Power States
description: Handling IRP_MN_SET_POWER for Device Power States
ms.assetid: b4a19995-7933-41f7-b951-15ce0e4627da
keywords: ["IRP_MN_SET_POWER", "device power states WDK kernel", "set-power IRPs WDK kernel", "DispatchPower routine", "passing IRPs down device stack WDK", "device set power IRPs WDK kernel", "power IRPs WDK kernel , device changes", "dispatch routines WDK power management"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Handling IRP\_MN\_SET\_POWER for Device Power States





A device set-power IRP requests a change of state for a single device and is sent to all the drivers in the stack for the device. Such an IRP specifies **DevicePowerState** in the **Power.Type** member of the I/O stack location.

Drivers handle power-down IRPs as they travel down the stack. For power-up IRPs, drivers set [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routines as the IRPs travel down the stack, and then handle the IRPs in the *IoCompletion* routines as the IRPs travel back up the stack. The drivers in a typical device stack handle a device set-power IRP as follows:

-   Most filter drivers should simply call [**IoMarkIrpPending**](https://msdn.microsoft.com/library/windows/hardware/ff549422), pass the IRP to the next-lower driver (see [Passing Power IRPs](passing-power-irps.md)), and return STATUS\_PENDING from the [*DispatchPower*](https://msdn.microsoft.com/library/windows/hardware/ff543354) routine. Some filter drivers, however, might first need to perform device-specific tasks, such as queuing incoming IRPs or saving device power state.

-   A function driver calls **IoMarkIrpPending**, performs device-specific tasks (such as completing pending I/O requests, queuing incoming I/O requests, saving device context, or changing device power), sets an *IoCompletion* routine if necessary, and passes the device power IRP to the next-lower driver (see [Passing Power IRPs](passing-power-irps.md)). It returns STATUS\_PENDING from its *DispatchPower* routine.

-   The bus driver changes device power if it is capable of doing so and then calls [**PoSetPowerState**](https://msdn.microsoft.com/library/windows/hardware/ff559765) to notify the power manager of the new device power state. In Windows Server 2003, Windows XP, and Windows 2000 only, the driver must also call [**PoStartNextPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559776) to start the next power IRP after it sets the power state. The driver then completes the IRP, specifying IO\_NO\_INCREMENT. If the driver cannot complete the IRP immediately, it calls [**IoMarkIrpPending**](https://msdn.microsoft.com/library/windows/hardware/ff549422), returns STATUS\_PENDING from its *DispatchPower* routine, and completes the IRP later.

Even if the target device is already in the requested power state, each function or filter driver must pass the IRP down to the next-lower driver. Every set-power IRP must travel all the way down the device stack to the bus driver, which completes it.

Function and filter drivers that are located above a bus driver must not fail a device set power IRP. The bus driver can fail a device power-up IRP if the device is removed or in the process of being removed.

Each driver (function, filter, and bus driver) in a driver stack must call [**PoSetPowerState**](https://msdn.microsoft.com/library/windows/hardware/ff559765) to inform the power manager of a change in the power state of its corresponding device object.

Like other driver tasks associated with device power-up and power-down, the call to **PoSetPowerState** must occur after the device powers on (if the new state is D0) or before the device powers off (if the new state is any other state).

Each driver should keep track of the power state of its device. The power manager does not supply this information to drivers.

While handling an [**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744) request for a device power state, a driver should return from the *DispatchPower* routine as quickly as possible. A driver must not wait in its *DispatchPower* routine for a kernel event signaled by code that handles the same IRP. Because power IRPs are synchronized throughout the system, a deadlock might occur.

To ensure the highest level of system performance, especially for multimedia applications, a driver should perform time-consuming operations at an interrupt request level (IRQL) equal to PASSIVE\_LEVEL. To perform operations at IRQL= PASSIVE\_LEVEL, a driver can use a [dedicated thread](device-dedicated-threads.md) or a [system worker thread](system-worker-threads.md). For guidelines on optimizing driver performance for multimedia platforms, see the [Streaming Media Devices Design Guide](https://msdn.microsoft.com/library/windows/hardware/ff568270).

The exact steps a driver must take to handle a power IRP depend upon whether the device is powering up or down, as described in the following sections:

[Handling Device Power-Down IRPs](handling-device-power-down-irps.md)

[Handling Device Power-Up IRPs](handling-device-power-up-irps.md)

 

 




