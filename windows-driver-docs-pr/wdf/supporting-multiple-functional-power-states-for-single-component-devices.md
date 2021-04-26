---
title: Single-Component Device, one or more Functional Power States
description: Describes how to implement Fx state support for a single-component device in a KMDF driver.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting Single-Component Devices with Single or Multiple Functional Power States


A KMDF driver for a single-component device can define one or more functional power states for the component and register callback functions that the power management framework (PoFx) calls when the Fx state of the component changes or its active/idle condition changes. Starting in UMDF version 2.0, a UMDF driver for a single-component device can define a single functional power state (F0).

For more information about PoFx, see [Overview of the Power Management Framework](../kernel/overview-of-the-power-management-framework.md).

To implement Fx state support for a single-component device, you must do the following in order before or during the first time a device starts.

1.  This step is for KMDF drivers only. Call [**WdfDeviceWdmAssignPowerFrameworkSettings**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicewdmassignpowerframeworksettings) to specify the power framework settings that WDF uses when registering with PoFx. In the [**WDF\_POWER\_FRAMEWORK\_SETTINGS**](/windows-hardware/drivers/ddi/wdfdevice/ns-wdfdevice-_wdf_power_framework_settings) structure that the driver provides when it calls **WdfDeviceWdmAssignPowerFrameworkSettings**, the driver can provide pointers to several callback functions. If the driver supports only a single functional power state (F0), this step is optional.
2.  This step applies to KMDF drivers and UMDF drivers. Call [**WdfDeviceAssignS0IdleSettings**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceassigns0idlesettings) and set the **IdleTimeoutType** field of the [**WDF\_DEVICE\_POWER\_POLICY\_IDLE\_SETTINGS**](/windows-hardware/drivers/ddi/wdfdevice/ns-wdfdevice-_wdf_device_power_policy_idle_settings) structure to **SystemManagedIdleTimeout** or **SystemManagedIdleTimeoutWithHint**. Doing so causes WDF to register with PoFx.

    For KMDF drivers, when registering with PoFx, the framework uses the information that the driver provided in [**WDF\_POWER\_FRAMEWORK\_SETTINGS**](/windows-hardware/drivers/ddi/wdfdevice/ns-wdfdevice-_wdf_power_framework_settings) when it called [**WdfDeviceWdmAssignPowerFrameworkSettings**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicewdmassignpowerframeworksettings).

Because a device can start more than once, for example in the event of resource rebalancing, a driver might perform the previous steps within the [*EvtDeviceSelfManagedIoInit*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_init) callback function. If the driver has registered an *EvtDeviceSelfManagedIoInit* callback function, the framework calls it once for each device, after the framework has called the driver's [*EvtDeviceD0Entry*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_entry) callback function for the first time.

The remainder of the information in this topic applies only to KMDF drivers.

## Powering Up


When the driver calls [**WdfDeviceWdmAssignPowerFrameworkSettings**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicewdmassignpowerframeworksettings), it can provide a pointer to a [*EvtDeviceWdmPostPoFxRegisterDevice*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_post_po_fx_register_device) callback function.

The framework calls the driver's [*EvtDeviceWdmPostPoFxRegisterDevice*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_post_po_fx_register_device) callback function after the framework has registered with PoFx. Here is an example of a typical power up sequence:

1.  [*EvtDevicePrepareHardware*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_prepare_hardware)
2.  [*EvtDeviceD0Entry*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_entry) (*PrevState* = **WdfPowerDeviceD3Final**)
3.  [*EvtInterruptEnable*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_enable)
4.  [*EvtDeviceWdmPostPoFxRegisterDevice*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_post_po_fx_register_device) // PoFx handle is available

The driver provides the [*EvtDeviceWdmPostPoFxRegisterDevice*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_post_po_fx_register_device) callback if it must perform any additional operations using the POHANDLE for the power framework registration. For example, it could specify latency, residency, and wake requirements. For more information about routines that use the POHANDLE, see [Device Power Management Routines](/windows-hardware/drivers/ddi/index).

Your driver can also use the POHANDLE to exchange power control requests with PoFx:

-   To send a power control request to PoFx, the driver provides a [*EvtDeviceWdmPostPoFxRegisterDevice*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_post_po_fx_register_device) callback function, and then uses the resulting POHANDLE to call [**PoFxPowerControl**](/windows-hardware/drivers/ddi/wdm/nf-wdm-pofxpowercontrol).
-   To perform power control operations requested by PoFx, the driver provides a [*PowerControlCallback*](/windows-hardware/drivers/ddi/wdm/nc-wdm-po_fx_power_control_callback) callback routine in its [**WDF\_POWER\_FRAMEWORK\_SETTINGS**](/windows-hardware/drivers/ddi/wdfdevice/ns-wdfdevice-_wdf_power_framework_settings) structure.

## Powering Down


WDF calls the [*EvtDeviceWdmPrePoFxUnregisterDevice*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_pre_po_fx_unregister_device) callback function before deleting a specified registration with PoFx.

The driver can provide a pointer to a [*ComponentIdleStateCallback*](/windows-hardware/drivers/ddi/wdm/nc-wdm-po_fx_component_idle_state_callback) routine in the [**WDF\_POWER\_FRAMEWORK\_SETTINGS**](/windows-hardware/drivers/ddi/wdfdevice/ns-wdfdevice-_wdf_power_framework_settings) structure that it provides to [**WdfDeviceWdmAssignPowerFrameworkSettings**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicewdmassignpowerframeworksettings). PoFx calls this routine to notify the driver of a pending change to the Fx power state of the specified component. In this callback routine, the driver can perform hardware-specific operations related to the functional state change.

For example, before transitioning a component into a low-power Fx state, a driver might save hardware state and disable interrupts and DMA. The driver calls [**WdfInterruptReportInactive**](/windows-hardware/drivers/ddi/wdfinterrupt/nf-wdfinterrupt-wdfinterruptreportinactive) to inform the system that the interrupt is no longer active. Turning off interrupts during F-state transitions may reduce overall system power consumption.

The driver can also provide a pointer to a [*ComponentIdleConditionCallback*](/windows-hardware/drivers/ddi/wdm/nc-wdm-po_fx_component_idle_condition_callback) routine in its [**WDF\_POWER\_FRAMEWORK\_SETTINGS**](/windows-hardware/drivers/ddi/wdfdevice/ns-wdfdevice-_wdf_power_framework_settings) structure. PoFx calls this routine to notify the driver that a component has become idle. In this routine, the driver begins the process of stopping its power-managed queues and self-managed I/O operations:

1.  Call [**WdfIoQueueStop**](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuestop) once for each of the device’s power-managed queues. In each call to **WdfIoQueueStop**, supply a [*EvtIoQueueState*](/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_state) callback. Typically, the driver calls **WdfIoQueueStop** from within [*ComponentIdleConditionCallback*](/windows-hardware/drivers/ddi/wdm/nc-wdm-po_fx_component_idle_condition_callback).
2.  Ensure that requests that are dispatched to the driver from each of the power-managed queues are completed quickly. Depending on the driver, this may involve some or all of the following:
    -   If the driver does not hold requests for an extended time and does not forward them to an I/O target that does so, continue to step 3.
    -   If the driver holds certain requests for an extended time, requeue these requests to a manual queue. In its [*ComponentActiveConditionCallback*](/windows-hardware/drivers/ddi/wdm/nc-wdm-po_fx_component_active_condition_callback) routine, the driver can then retrieve the requests.
    -   If the driver forwards certain requests to an I/O target that holds them for an extended time, cancel these requests. Resubmit the requests in [*ComponentActiveConditionCallback*](/windows-hardware/drivers/ddi/wdm/nc-wdm-po_fx_component_active_condition_callback).

3.  When each queue has been stopped, the framework calls [*EvtIoQueueState*](/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_state). If the driver is stopping multiple power-managed queues, the framework calls *EvtIoQueueState* multiple times, once for each queue.

    The driver must call [**PoFxCompleteIdleCondition**](/windows-hardware/drivers/ddi/wdm/nf-wdm-pofxcompleteidlecondition) after the last [*EvtIoQueueState*](/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_state) function has been called. For example, the driver could make this call from within the last *EvtIoQueueState*.

    In order to determine which call is last, the driver might use a counter to track the number of times that the framework has called [*EvtIoQueueState*](/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_state). The Singlecomp sample illustrates this technique. This sample is available beginning in the Windows 8 WDK.

Here is an example of a typical power down sequence:

1.  [*ComponentIdleConditionCallback*](/windows-hardware/drivers/ddi/wdm/nc-wdm-po_fx_component_idle_condition_callback)
2.  [*ComponentIdleStateCallback*](/windows-hardware/drivers/ddi/wdm/nc-wdm-po_fx_component_idle_state_callback)
3.  [*EvtInterruptDisable*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_disable)
4.  [*EvtDeviceD0Exit*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_exit)

Restart power-managed queues and self-managed I/O operations in [*ComponentActiveConditionCallback*](/windows-hardware/drivers/ddi/wdm/nc-wdm-po_fx_component_active_condition_callback).

If the driver previously called [**WdfInterruptReportInactive**](/windows-hardware/drivers/ddi/wdfinterrupt/nf-wdfinterrupt-wdfinterruptreportinactive), re-enable inactive interrupts by calling [**WdfInterruptReportActive**](/windows-hardware/drivers/ddi/wdfinterrupt/nf-wdfinterrupt-wdfinterruptreportactive) from either [*ComponentActiveConditionCallback*](/windows-hardware/drivers/ddi/wdm/nc-wdm-po_fx_component_active_condition_callback) or [*ComponentIdleStateCallback*](/windows-hardware/drivers/ddi/wdm/nc-wdm-po_fx_component_idle_state_callback).

 

