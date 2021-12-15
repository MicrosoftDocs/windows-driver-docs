---
title: Multiple-Component Device, one or more Functional Power States
description: Supporting Multiple-Component Devices with Single or Multiple Functional Power States
ms.date: 04/20/2017
---

# Supporting Multiple-Component Devices with Single or Multiple Functional Power States


\[Applies to KMDF only\]

A KMDF driver for a multiple-component device can define one or more functional power states for each component.

In this case, the driver registers directly with the power management framework (PoFx). To specify that WDF should not register with PoFx, the driver calls [**WdfDeviceAssignS0IdleSettings**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceassigns0idlesettings) with the **IdleTimeoutType** member of the [**WDF\_DEVICE\_POWER\_POLICY\_IDLE\_SETTINGS**](/windows-hardware/drivers/ddi/wdfdevice/ns-wdfdevice-_wdf_device_power_policy_idle_settings) structure set to **DriverManagedIdleTimeout**. Typically, the driver calls this method from its [*EvtDriverDeviceAdd*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) callback function.

Next, the driver must register with PoFx. To do so, the driver calls [**PoFxRegisterDevice**](/windows-hardware/drivers/ddi/wdm/nf-wdm-pofxregisterdevice) and then [**PoFxStartDevicePowerManagement**](/windows-hardware/drivers/ddi/wdm/nf-wdm-pofxstartdevicepowermanagement). Your driver must register with PoFx only once, when the device is first started. One way to do this is by calling these routines from a driver-supplied [*EvtDeviceSelfManagedIoInit*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_init) function. *EvtDeviceSelfManagedIoInit* is called only the first time the device is started.

When the device is removed, the driver must call [**PoFxUnregisterDevice**](/windows-hardware/drivers/ddi/wdm/nf-wdm-pofxunregisterdevice) to unregister the device from PoFx. To unregister only once, we recommend the driver call this routine from a driver-supplied [*EvtDeviceSelfManagedIoFlush*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_flush) function. *EvtDeviceSelfManagedIoFlush* is called only when the device is being removed. By unregistering in *EvtDeviceSelfManagedIoFlush*, the driver retains power registration during sleep and rebalance transitions and does not have to maintain power references for I/O requests that remain pending during these transitions.

When the driver calls [*PoFxRegisterDevice*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_post_po_fx_register_device), it receives a power registration handle (POHANDLE) that it can use to interact directly with PoFx, as described in the following topics:

-   [Coordinating I/O Requests with Component Power State](coordinating-i-o-requests-with-component-power-state.md)
-   [Reporting Device Powered On When System Returns to S0](reporting-device-powered-on.md)
-   [Supporting Idle Power-Down on Multiple-Component Devices](supporting-idle-power-down-on-multiple-component-devices.md)

In addition, the driver can call [power framework routines](/windows-hardware/drivers/ddi/_kernel/#power-management-routines) directly to send power control requests and specify latency, residency, and wake requirements.

For more information about PoFx, see [Overview of the Power Management Framework](../kernel/overview-of-the-power-management-framework.md).

 

