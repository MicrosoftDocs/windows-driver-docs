---
title: Supporting System Wake-Up
description: Supporting System Wake-Up
ms.assetid: 519dcd1a-9975-48b1-a032-04348b903ac5
keywords:
- system wake-up WDK KMDF
- power management WDK KMDF , wake-up capabilities
- wake-up capabilities WDK KMDF
- sleep power management WDK KMDF
- low-power states WDK KMDF
- Power Management Event WDK KMDF
- PME WDK KMDF
- Power Management Capabilities WDK KMDF
- PMC WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting System Wake-Up


While the system is in a low-power state, some devices can detect an external event, such as an incoming network packet, and then wake the system. For example, if a PCI device has a system wakeup capability, as indicated in the device's Power Management Capabilities (PMC) register, it wakes the system by raising the Power Management Event (PME) signal on the PCI bus.

If your device can wake the system from a system-wide low-power state, the [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback function in the [power policy owner](power-policy-ownership.md) must perform the following two steps:

1.  Call [**WdfDeviceAssignSxWakeSettings**](https://msdn.microsoft.com/library/windows/hardware/ff545909) to specify:

    -   The low-power state that the device will enter
    -   Whether users can control the device's idle settings
    -   Whether the device's wake capability is enabled or disabled

    For more information about these settings, see the [**WDF\_DEVICE\_POWER\_POLICY\_WAKE\_SETTINGS**](https://msdn.microsoft.com/library/windows/hardware/ff551277) structure.

2.  Call [**WdfDeviceInitSetPowerPolicyEventCallbacks**](https://msdn.microsoft.com/library/windows/hardware/ff546774) to register the following event callback functions, if you need them for your device:
    -   [*EvtDeviceArmWakeFromSx*](https://msdn.microsoft.com/library/windows/hardware/ff540844) or [*EvtDeviceArmWakeFromSxWithReason*](https://msdn.microsoft.com/library/windows/hardware/ff540846), which enable the device hardware to respond to an external wake-up event.
    -   [*EvtDeviceDisarmWakeFromSx*](https://msdn.microsoft.com/library/windows/hardware/ff540862), which disables the device's ability to respond to an external wake-up event.
    -   [*EvtDeviceWakeFromSxTriggered*](https://msdn.microsoft.com/library/windows/hardware/ff540923), which informs the driver that the bus detected a wake signal.

Bus drivers also participate in waking up the system. The driver for the device's bus typically provides [*EvtDeviceEnableWakeAtBus*](https://msdn.microsoft.com/library/windows/hardware/ff540866) and [*EvtDeviceDisableWakeAtBus*](https://msdn.microsoft.com/library/windows/hardware/ff540858) callback functions. These functions do whatever is necessary on the bus adapter to enable and disable a device's ability to wake from a low-power state.

When a bus driver determines that a device has triggered a wake signal, it must call [**WdfDeviceIndicateWakeStatus**](https://msdn.microsoft.com/library/windows/hardware/ff546025) to inform the framework that the device's power should be restored. The framework then passes this information to the rest of the drivers in the driver stack.

For information about registry entries that control a device's wake capabilities, see [User Control of Device Idle and Wake Behavior](user-control-of-device-idle-and-wake-behavior.md).

 

 





