---
title: Supporting Idle Power-Down in UMDF Drivers
description: Supporting Idle Power-Down in UMDF Drivers
ms.assetid: 128f009e-1847-493e-90e3-2fe8c141b158
keywords:
- power management WDK UMDF , idle power-down
- idle power-down WDK UMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting Idle Power-Down in UMDF Drivers


[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

Some devices can enter a sleeping state while the system remains in its working state. For such devices, the framework initiates lowering the device's power after the device has been idle (not used) for a predetermined (and settable) amount of time.

Some of these devices can also trigger a wake-up signal on the bus when they detect an external event. The bus driver responds to this signal, and the driver stack restores the device to its working state. (Devices that do not detect external events remain in a low-power state until the framework asks the bus driver to initiate restoring the device to its working state.)

If your device can be powered down when it is idle, the [power policy owner](power-policy-ownership-in-umdf.md) must perform the following two steps:

1.  Call [**IWDFDevice2::AssignS0IdleSettings**](https://msdn.microsoft.com/library/windows/hardware/ff556920) or [**IWDFDevice3::AssignS0IdleSettingsEx**](https://msdn.microsoft.com/library/windows/hardware/hh451202) to specify:
    -   The low-power state that the device will enter
    -   The amount of time that the device must remain idle before its power state is lowered
    -   Whether the device can detect an external event and trigger a wake-up signal on the bus
    -   Whether users can control the device's idle settings
    -   Whether the framework can put the device in the D3cold power state when the idle timeout period expires

    If your driver was built with version 1.11 or later of the framework, you can call **IWDFDevice3::AssignS0IdleSettingsEx** instead of **IWDFDevice2::AssignS0IdleSettings**. In addition to the above functionality, **IWDFDevice3::AssignS0IdleSettingsEx** allows the driver to specify:
    -   Whether the device's idle power-down capability is enabled or disabled
    -   Whether the device will return to its working (D0) state when the system returns to its working (S0) state

2.  Implement the [IPowerPolicyCallbackWakeFromS0](https://msdn.microsoft.com/library/windows/hardware/ff556815) interface and the following event callback functions, if you need them for your device:
    -   [**IPowerPolicyCallbackWakeFromS0::OnArmWakeFromS0**](https://msdn.microsoft.com/library/windows/hardware/ff556817), which enables the device hardware (not the bus) to respond to an external wake-up event.
    -   [**IPowerPolicyCallbackWakeFromS0::OnDisarmWakeFromS0**](https://msdn.microsoft.com/library/windows/hardware/ff556819), which disables the device's ability (not the bus's ability) to respond to an external wake-up event.
    -   [**IPowerPolicyCallbackWakeFromS0::OnWakeFromS0Triggered**](https://msdn.microsoft.com/library/windows/hardware/ff556822), which informs the driver that the bus detected a wake signal.




The framework considers the device to be idle, and starts counting idle time, when all of the following conditions are met:

-   None of the power-managed queues created for this device instance have any requests waiting in queue or dispatched to the driver. If a request was dispatched to the driver and the driver sent it to an I/O target, the request is still related to the queue and the device will not be considered idle. Requests in non-power–managed queues are not counted toward device idle.
-   If the driver previously called [**IWDFDevice2::StopIdle**](https://msdn.microsoft.com/library/windows/hardware/ff556948), the driver has subsequently called [**IWDFDevice2::ResumeIdle**](https://msdn.microsoft.com/library/windows/hardware/ff556943).
-   If the power policy owner is a bus driver, none of the child devices of the bus driver are in D0.

If your driver (or a user) enables idle power-down for your device, you might have to use the [**IWDFDevice2::StopIdle**](https://msdn.microsoft.com/library/windows/hardware/ff556948) method. If the device is in its working (D0) state, this method prevents the device from idling until the driver calls [**IWDFDevice2::ResumeIdle**](https://msdn.microsoft.com/library/windows/hardware/ff556943). If the device is in a low-power state when the driver calls **IWDFDevice2::StopIdle**, and if the system is in its working (S0) state, the framework requests the bus driver to restore the device to its working (D0) state. For more information about when your driver might have to call **IWDFDevice2::StopIdle**, see the method's reference page.

If the device can wake itself from a low-power state, the driver for the device's bus participates in waking the device. The kernel-mode bus driver does whatever is necessary on the bus adapter to enable and disable a device's ability to wake from a low-power state.

For information about registry entries that control a device's idle capabilities, see [User Control of Device Idle and Wake Behavior in UMDF](user-control-of-device-idle-and-wake-behavior-in-umdf.md).

 

 





