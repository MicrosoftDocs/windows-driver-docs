---
title: Supporting Idle Power-Down
description: Some devices can enter a low-power (Dx) state while the system remains in its working (S0) state.
ms.assetid: d0ce51db-eeb7-45ef-b823-248cd03ee2a9
keywords: ["idle power-down WDK KMDF", "power management WDK KMDF , idle power-down", "wake-up capabilities WDK KMDF", "sleep power management WDK KMDF", "low-power states WDK KMDF", "system sleeping states WDK KMDF"]
---

# Supporting Idle Power-Down


Some devices can enter a low-power (Dx) state while the system remains in its working (S0) state. Starting in Windows 8, devices can transition to a low-power functional power state (Fx) prior to entering a Dx state. For such devices, the framework initiates lowering power of the device or component after the device has been idle (not used) for a predetermined (and settable) amount of time.

Some of these devices can also trigger a wake-up signal on the bus when they detect an external event. The bus driver responds to this signal, and the driver stack restores the device to its working state. (Devices that do not detect external events remain in a low-power state until the framework asks the bus driver to initiate restoring the device to its working state.)

If your device or component can be powered down when it is idle, the [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback function in the [power policy owner](power-policy-ownership.md) must perform the following two steps:

1.  Call [**WdfDeviceAssignS0IdleSettings**](https://msdn.microsoft.com/library/windows/hardware/ff545903) to specify:

    -   The low-power state that the device will enter
    -   The amount of time that the device [must remain idle](#idle-conditions) before its power state is lowered
    -   Whether the device can detect an external event and trigger a wake-up signal on the bus
    -   Whether users can control the device's idle settings
    -   Whether the device's idle power-down capability is enabled or disabled
    -   Whether the device will return to its working (D0) state when the system returns to its working (S0) state
    -   Whether the idle timeout value for the device is determined by the power management framework (PoFx)
    -   Whether the framework can put the device in the D3cold power state when the idle timeout period expires

    For more information about these settings, see the [**WDF\_DEVICE\_POWER\_POLICY\_IDLE\_SETTINGS**](https://msdn.microsoft.com/library/windows/hardware/ff551270) structure, as well as [Supporting Functional Power States](supporting-functional-power-states.md).

2.  Call [**WdfDeviceInitSetPowerPolicyEventCallbacks**](https://msdn.microsoft.com/library/windows/hardware/ff546774) to register the following event callback functions, if you need them for your device:
    -   [*EvtDeviceArmWakeFromS0*](https://msdn.microsoft.com/library/windows/hardware/ff540843), which enables the device hardware (not the bus) to respond to an external wake-up event
    -   [*EvtDeviceDisarmWakeFromS0*](https://msdn.microsoft.com/library/windows/hardware/ff540860), which disables the device's ability (not the bus's ability) to respond to an external wake-up event
    -   [*EvtDeviceWakeFromS0Triggered*](https://msdn.microsoft.com/library/windows/hardware/ff540919), which informs the driver that the bus detected a wake signal.

## <a href="" id="idle-conditions"></a>


The framework considers the device to be idle, and starts counting idle time, when all of the following conditions are met:

-   None of the power-managed queues created for this device instance have any requests waiting in queue or dispatched to the driver. If a request was dispatched to the driver and the driver sent it to an I/O target, the request is still related to the queue. The device will not be considered idle, unless the driver used the [**send and forget option**](https://msdn.microsoft.com/library/windows/hardware/ff552462) to send the request. Requests in non-power managed queues are not counted toward device idle.
-   If the driver previously called [**WdfDeviceStopIdle**](https://msdn.microsoft.com/library/windows/hardware/ff546921), the driver has subsequently called [**WdfDeviceResumeIdle**](https://msdn.microsoft.com/library/windows/hardware/ff546838).
-   If the power policy owner is a bus driver, none of the child devices of the bus driver are in D0.

If your driver (or a user) enables idle power-down for your device, you might have to use the [**WdfDeviceStopIdle**](https://msdn.microsoft.com/library/windows/hardware/ff546921) method. If the device is in its working (D0) state, this method prevents the device from idling until the driver calls [**WdfDeviceResumeIdle**](https://msdn.microsoft.com/library/windows/hardware/ff546838). If the device is in a low-power state when the driver calls **WdfDeviceStopIdle**, and if the system is in its working (S0) state, the framework requests the bus driver to restore the device to its working (D0) state. Every successful call to **WdfDeviceStopIdle** must be matched by a call to **WdfDeviceResumeIdle**. For information about viewing the power reference count in the debugger, see [Debugging Power Reference Leaks in WDF](debugging-power-reference-leaks-in-wdf.md).

For more information about when your driver might have to call [**WdfDeviceStopIdle**](https://msdn.microsoft.com/library/windows/hardware/ff546921), see the method's reference page.

If the device can wake itself from a low-power state, the driver for the device's bus participates in waking the device. The bus driver typically provides [*EvtDeviceEnableWakeAtBus*](https://msdn.microsoft.com/library/windows/hardware/ff540866) and [*EvtDeviceDisableWakeAtBus*](https://msdn.microsoft.com/library/windows/hardware/ff540858) callback functions. These functions do whatever is necessary on the bus adapter to enable and disable a device's ability to wake from a low-power state.

For information about registry entries that control a device's idle capabilities, see [User Control of Device Idle and Wake Behavior](user-control-of-device-idle-and-wake-behavior.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Supporting%20Idle%20Power-Down%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




