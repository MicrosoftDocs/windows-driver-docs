---
title: Supporting System Wake-Up in UMDF Drivers
author: windows-driver-content
description: Supporting System Wake-Up in UMDF Drivers
ms.assetid: 945b1751-f3a1-4a29-8fb7-6690f91af7d9
keywords:
- power management WDK UMDF , system wake-up
- system wake-up WDK UMDF
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Supporting System Wake-Up in UMDF Drivers


\[This topic applies to UMDF 1.*x*.\]

While the system is in a low-power state, some devices can detect an external event, such as an incoming network packet, and then wake the system. For example, if a PCI device has a system wake-up capability, as indicated in the device's Power Management Capabilities (PMC) register, it wakes the system by raising the Power Management Event (PME) signal on the PCI bus.

If your device can wake the system from a system-wide low-power state, the [**IDriverEntry::OnDeviceAdd**](https://msdn.microsoft.com/library/windows/hardware/ff554896) callback function in the [power policy owner](power-policy-ownership-in-umdf.md) must perform the following two steps:

1.  Call [**IWDFDevice2::AssignSxWakeSettings**](https://msdn.microsoft.com/library/windows/hardware/ff556923) to specify:
    -   The low-power state that the device will enter
    -   Whether users can control the device's idle settings
    -   Whether the device's wake capability is enabled or disabled

2.  Implement the [IPowerPolicyCallbackWakeFromSx](https://msdn.microsoft.com/library/windows/hardware/ff556825) interface and the following event callback functions, if you need them for your device:
    -   [**IPowerPolicyCallbackWakeFromSx::OnArmWakeFromSx**](https://msdn.microsoft.com/library/windows/hardware/ff556826), which enable the device hardware to respond to an external wake-up event.
    -   [**IPowerPolicyCallbackWakeFromSx::OnDisarmWakeFromSx**](https://msdn.microsoft.com/library/windows/hardware/ff556828), which disables the device's ability to respond to an external wake-up event.
    -   [**IPowerPolicyCallbackWakeFromSx::OnWakeFromSxTriggered**](https://msdn.microsoft.com/library/windows/hardware/ff556833), which informs the driver that the bus detected a wake signal.

Bus drivers also participate in waking up the system. The kernel-mode driver for the device's bus does whatever is necessary on the bus adapter to enable and disable a device's ability to wake from a low-power state.

For information about registry entries that control a device's wake capabilities, see [User Control of Device Idle and Wake Behavior in UMDF](user-control-of-device-idle-and-wake-behavior-in-umdf.md).

 

 





