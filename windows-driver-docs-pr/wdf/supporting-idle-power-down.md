---
title: Supporting Idle Power-Down
description: Some devices can enter a low-power (Dx) state while the system remains in its working (S0) state.
keywords:
- idle power-down WDK KMDF
- power management WDK KMDF , idle power-down
- wake-up capabilities WDK KMDF
- sleep power management WDK KMDF
- low-power states WDK KMDF
- system sleeping states WDK KMDF
ms.date: 04/20/2017
---

# Supporting Idle Power-Down


Some devices can enter a low-power (Dx) state while the system remains in its working (S0) state. Starting in Windows 8, devices can transition to a low-power functional power state (Fx) prior to entering a Dx state. For such devices, the framework initiates lowering power of the device or component after the device has been idle (not used) for a predetermined (and settable) amount of time.

Some of these devices can also trigger a wake-up signal on the bus when they detect an external event. The bus driver responds to this signal, and the driver stack restores the device to its working state. (Devices that do not detect external events remain in a low-power state until the framework asks the bus driver to initiate restoring the device to its working state.)

If your device or component can be powered down when it is idle, the [*EvtDriverDeviceAdd*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) callback function in the [power policy owner](power-policy-ownership.md) must perform the following two steps:

1.  Call [**WdfDeviceAssignS0IdleSettings**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceassigns0idlesettings) to specify:

    -   The low-power state that the device will enter
    -   The amount of time that the device [must remain idle](#idle-conditions) before its power state is lowered
    -   Whether the device can detect an external event and trigger a wake-up signal on the bus
    -   Whether users can control the device's idle settings
    -   Whether the device's idle power-down capability is enabled or disabled
    -   Whether the device will return to its working (D0) state when the system returns to its working (S0) state
    -   Whether the idle timeout value for the device is determined by the power management framework (PoFx)
    -   Whether the framework can put the device in the D3cold power state when the idle timeout period expires

    For more information about these settings, see the [**WDF\_DEVICE\_POWER\_POLICY\_IDLE\_SETTINGS**](/windows-hardware/drivers/ddi/wdfdevice/ns-wdfdevice-_wdf_device_power_policy_idle_settings) structure, as well as [Supporting Functional Power States](supporting-functional-power-states.md).

2.  Call [**WdfDeviceInitSetPowerPolicyEventCallbacks**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetpowerpolicyeventcallbacks) to register the following event callback functions, if you need them for your device:
    -   [*EvtDeviceArmWakeFromS0*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_arm_wake_from_s0), which enables the device hardware (not the bus) to respond to an external wake-up event
    -   [*EvtDeviceDisarmWakeFromS0*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_disarm_wake_from_s0), which disables the device's ability (not the bus's ability) to respond to an external wake-up event
    -   [*EvtDeviceWakeFromS0Triggered*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_wake_from_s0_triggered), which informs the driver that the bus detected a wake signal.


## Idle Conditions

The framework considers the device to be idle, and starts counting idle time, when all of the following conditions are met:

-   None of the power-managed queues created for this device instance have any requests waiting in queue or dispatched to the driver. If a request was dispatched to the driver and the driver sent it to an I/O target, the request is still related to the queue. The device will not be considered idle, unless the driver used the [**send and forget option**](/windows-hardware/drivers/ddi/wdfrequest/ne-wdfrequest-_wdf_request_forward_options_flags) to send the request. Requests in non-power managed queues are not counted toward device idle.
-   If the driver previously called [**WdfDeviceStopIdle**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicestopidle), the driver has subsequently called [**WdfDeviceResumeIdle**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceresumeidle).
-   If the power policy owner is a bus driver, none of the child devices of the bus driver are in D0.

If your driver (or a user) enables idle power-down for your device, you might have to use the [**WdfDeviceStopIdle**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicestopidle) method. If the device is in its working (D0) state, this method prevents the device from idling until the driver calls [**WdfDeviceResumeIdle**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceresumeidle). If the device is in a low-power state when the driver calls **WdfDeviceStopIdle**, and if the system is in its working (S0) state, the framework requests the bus driver to restore the device to its working (D0) state. Every successful call to **WdfDeviceStopIdle** must be matched by a call to **WdfDeviceResumeIdle**. For information about viewing the power reference count in the debugger, see [Debugging Power Reference Leaks in WDF](debugging-power-reference-leaks-in-wdf.md).

For more information about when your driver might have to call [**WdfDeviceStopIdle**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicestopidle), see the method's reference page.

If the device can wake itself from a low-power state, the driver for the device's bus participates in waking the device. The bus driver typically provides [*EvtDeviceEnableWakeAtBus*](/windows-hardware/drivers/ddi/wdfpdo/nc-wdfpdo-evt_wdf_device_enable_wake_at_bus) and [*EvtDeviceDisableWakeAtBus*](/windows-hardware/drivers/ddi/wdfpdo/nc-wdfpdo-evt_wdf_device_disable_wake_at_bus) callback functions. These functions do whatever is necessary on the bus adapter to enable and disable a device's ability to wake from a low-power state.

For information about registry entries that control a device's idle capabilities, see [User Control of Device Idle and Wake Behavior](user-control-of-device-idle-and-wake-behavior.md).

 

