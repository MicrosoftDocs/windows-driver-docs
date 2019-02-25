---
title: Single-Component Device, one or more Functional Power States
description: Describes how to implement Fx state support for a single-component device in a KMDF driver.
ms.assetid: C7EFD71F-E101-4160-9703-E1DBD507698C
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting Single-Component Devices with Single or Multiple Functional Power States


A KMDF driver for a single-component device can define one or more functional power states for the component and register callback functions that the power management framework (PoFx) calls when the Fx state of the component changes or its active/idle condition changes. Starting in UMDF version 2.0, a UMDF driver for a single-component device can define a single functional power state (F0).

For more information about PoFx, see [Overview of the Power Management Framework](https://msdn.microsoft.com/library/windows/hardware/hh406637).

To implement Fx state support for a single-component device, you must do the following in order before or during the first time a device starts.

1.  This step is for KMDF drivers only. Call [**WdfDeviceWdmAssignPowerFrameworkSettings**](https://msdn.microsoft.com/library/windows/hardware/hh451097) to specify the power framework settings that WDF uses when registering with PoFx. In the [**WDF\_POWER\_FRAMEWORK\_SETTINGS**](https://msdn.microsoft.com/library/windows/hardware/hh406489) structure that the driver provides when it calls **WdfDeviceWdmAssignPowerFrameworkSettings**, the driver can provide pointers to several callback functions. If the driver supports only a single functional power state (F0), this step is optional.
2.  This step applies to KMDF drivers and UMDF drivers. Call [**WdfDeviceAssignS0IdleSettings**](https://msdn.microsoft.com/library/windows/hardware/ff545903) and set the **IdleTimeoutType** field of the [**WDF\_DEVICE\_POWER\_POLICY\_IDLE\_SETTINGS**](https://msdn.microsoft.com/library/windows/hardware/ff551270) structure to **SystemManagedIdleTimeout** or **SystemManagedIdleTimeoutWithHint**. Doing so causes WDF to register with PoFx.

    For KMDF drivers, when registering with PoFx, the framework uses the information that the driver provided in [**WDF\_POWER\_FRAMEWORK\_SETTINGS**](https://msdn.microsoft.com/library/windows/hardware/hh406489) when it called [**WdfDeviceWdmAssignPowerFrameworkSettings**](https://msdn.microsoft.com/library/windows/hardware/hh451097).

Because a device can start more than once, for example in the event of resource rebalancing, a driver might perform the previous steps within the [*EvtDeviceSelfManagedIoInit*](https://msdn.microsoft.com/library/windows/hardware/ff540902) callback function. If the driver has registered an *EvtDeviceSelfManagedIoInit* callback function, the framework calls it once for each device, after the framework has called the driver's [*EvtDeviceD0Entry*](https://msdn.microsoft.com/library/windows/hardware/ff540848) callback function for the first time.

The remainder of the information in this topic applies only to KMDF drivers.

## Powering Up


When the driver calls [**WdfDeviceWdmAssignPowerFrameworkSettings**](https://msdn.microsoft.com/library/windows/hardware/hh451097), it can provide a pointer to a [*EvtDeviceWdmPostPoFxRegisterDevice*](https://msdn.microsoft.com/library/windows/hardware/hh406408) callback function.

The framework calls the driver's [*EvtDeviceWdmPostPoFxRegisterDevice*](https://msdn.microsoft.com/library/windows/hardware/hh406408) callback function after the framework has registered with PoFx. Here is an example of a typical power up sequence:

1.  [*EvtDevicePrepareHardware*](https://msdn.microsoft.com/library/windows/hardware/ff540880)
2.  [*EvtDeviceD0Entry*](https://msdn.microsoft.com/library/windows/hardware/ff540848) (*PrevState* = **WdfPowerDeviceD3Final**)
3.  [*EvtInterruptEnable*](https://msdn.microsoft.com/library/windows/hardware/ff541730)
4.  [*EvtDeviceWdmPostPoFxRegisterDevice*](https://msdn.microsoft.com/library/windows/hardware/hh406408) // PoFx handle is available

The driver provides the [*EvtDeviceWdmPostPoFxRegisterDevice*](https://msdn.microsoft.com/library/windows/hardware/hh406408) callback if it must perform any additional operations using the POHANDLE for the power framework registration. For example, it could specify latency, residency, and wake requirements. For more information about routines that use the POHANDLE, see [Device Power Management Routines](https://msdn.microsoft.com/library/windows/hardware/hh450961).

Your driver can also use the POHANDLE to exchange power control requests with PoFx:

-   To send a power control request to PoFx, the driver provides a [*EvtDeviceWdmPostPoFxRegisterDevice*](https://msdn.microsoft.com/library/windows/hardware/hh406408) callback function, and then uses the resulting POHANDLE to call [**PoFxPowerControl**](https://msdn.microsoft.com/library/windows/hardware/hh439518).
-   To perform power control operations requested by PoFx, the driver provides a [*PowerControlCallback*](https://msdn.microsoft.com/library/windows/hardware/hh439564) callback routine in its [**WDF\_POWER\_FRAMEWORK\_SETTINGS**](https://msdn.microsoft.com/library/windows/hardware/hh406489) structure.

## Powering Down


WDF calls the [*EvtDeviceWdmPrePoFxUnregisterDevice*](https://msdn.microsoft.com/library/windows/hardware/hh406411) callback function before deleting a specified registration with PoFx.

The driver can provide a pointer to a [*ComponentIdleStateCallback*](https://msdn.microsoft.com/library/windows/hardware/hh450931) routine in the [**WDF\_POWER\_FRAMEWORK\_SETTINGS**](https://msdn.microsoft.com/library/windows/hardware/hh406489) structure that it provides to [**WdfDeviceWdmAssignPowerFrameworkSettings**](https://msdn.microsoft.com/library/windows/hardware/hh451097). PoFx calls this routine to notify the driver of a pending change to the Fx power state of the specified component. In this callback routine, the driver can perform hardware-specific operations related to the functional state change.

For example, before transitioning a component into a low-power Fx state, a driver might save hardware state and disable interrupts and DMA. The driver calls [**WdfInterruptReportInactive**](https://msdn.microsoft.com/library/windows/hardware/hh439277) to inform the system that the interrupt is no longer active. Turning off interrupts during F-state transitions may reduce overall system power consumption.

The driver can also provide a pointer to a [*ComponentIdleConditionCallback*](https://msdn.microsoft.com/library/windows/hardware/hh406420) routine in its [**WDF\_POWER\_FRAMEWORK\_SETTINGS**](https://msdn.microsoft.com/library/windows/hardware/hh406489) structure. PoFx calls this routine to notify the driver that a component has become idle. In this routine, the driver begins the process of stopping its power-managed queues and self-managed I/O operations:

1.  Call [**WdfIoQueueStop**](https://msdn.microsoft.com/library/windows/hardware/ff548482) once for each of the device’s power-managed queues. In each call to **WdfIoQueueStop**, supply a [*EvtIoQueueState*](https://msdn.microsoft.com/library/windows/hardware/ff541771) callback. Typically, the driver calls **WdfIoQueueStop** from within [*ComponentIdleConditionCallback*](https://msdn.microsoft.com/library/windows/hardware/hh406420).
2.  Ensure that requests that are dispatched to the driver from each of the power-managed queues are completed quickly. Depending on the driver, this may involve some or all of the following:
    -   If the driver does not hold requests for an extended time and does not forward them to an I/O target that does so, continue to step 3.
    -   If the driver holds certain requests for an extended time, requeue these requests to a manual queue. In its [*ComponentActiveConditionCallback*](https://msdn.microsoft.com/library/windows/hardware/hh406416) routine, the driver can then retrieve the requests.
    -   If the driver forwards certain requests to an I/O target that holds them for an extended time, cancel these requests. Resubmit the requests in [*ComponentActiveConditionCallback*](https://msdn.microsoft.com/library/windows/hardware/hh406416).

3.  When each queue has been stopped, the framework calls [*EvtIoQueueState*](https://msdn.microsoft.com/library/windows/hardware/ff541771). If the driver is stopping multiple power-managed queues, the framework calls *EvtIoQueueState* multiple times, once for each queue.

    The driver must call [**PoFxCompleteIdleCondition**](https://msdn.microsoft.com/library/windows/hardware/hh406658) after the last [*EvtIoQueueState*](https://msdn.microsoft.com/library/windows/hardware/ff541771) function has been called. For example, the driver could make this call from within the last *EvtIoQueueState*.

    In order to determine which call is last, the driver might use a counter to track the number of times that the framework has called [*EvtIoQueueState*](https://msdn.microsoft.com/library/windows/hardware/ff541771). The Singlecomp sample illustrates this technique. This sample is available beginning in the Windows 8 WDK.

Here is an example of a typical power down sequence:

1.  [*ComponentIdleConditionCallback*](https://msdn.microsoft.com/library/windows/hardware/hh406420)
2.  [*ComponentIdleStateCallback*](https://msdn.microsoft.com/library/windows/hardware/hh450931)
3.  [*EvtInterruptDisable*](https://msdn.microsoft.com/library/windows/hardware/ff541714)
4.  [*EvtDeviceD0Exit*](https://msdn.microsoft.com/library/windows/hardware/ff540855)

Restart power-managed queues and self-managed I/O operations in [*ComponentActiveConditionCallback*](https://msdn.microsoft.com/library/windows/hardware/hh406416).

If the driver previously called [**WdfInterruptReportInactive**](https://msdn.microsoft.com/library/windows/hardware/hh439277), re-enable inactive interrupts by calling [**WdfInterruptReportActive**](https://msdn.microsoft.com/library/windows/hardware/hh439273) from either [*ComponentActiveConditionCallback*](https://msdn.microsoft.com/library/windows/hardware/hh406416) or [*ComponentIdleStateCallback*](https://msdn.microsoft.com/library/windows/hardware/hh450931).

 

 





