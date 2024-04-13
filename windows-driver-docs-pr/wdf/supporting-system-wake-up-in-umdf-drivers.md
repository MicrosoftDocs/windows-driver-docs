---
title: Supporting System Wake-Up in UMDF Drivers
description: Supporting System Wake-Up in UMDF Drivers
keywords:
- power management WDK UMDF , system wake-up
- system wake-up WDK UMDF
ms.date: 04/20/2017
---

# Supporting System Wake-Up in UMDF Drivers


[!include[UMDF 1 Deprecation](../includes/umdf-1-deprecation.md)]

While the system is in a low-power state, some devices can detect an external event, such as an incoming network packet, and then wake the system. For example, if a PCI device has a system wake-up capability, as indicated in the device's Power Management Capabilities (PMC) register, it wakes the system by raising the Power Management Event (PME) signal on the PCI bus.

If your device can wake the system from a system-wide low-power state, the [**IDriverEntry::OnDeviceAdd**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-idriverentry-ondeviceadd) callback function in the [power policy owner](power-policy-ownership-in-umdf.md) must perform the following two steps:

1.  Call [**IWDFDevice2::AssignSxWakeSettings**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice2-assignsxwakesettings) to specify:
    -   The low-power state that the device will enter
    -   Whether users can control the device's idle settings
    -   Whether the device's wake capability is enabled or disabled

2.  Implement the [IPowerPolicyCallbackWakeFromSx](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-ipowerpolicycallbackwakefromsx) interface and the following event callback functions, if you need them for your device:
    -   [**IPowerPolicyCallbackWakeFromSx::OnArmWakeFromSx**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ipowerpolicycallbackwakefromsx-onarmwakefromsx), which enable the device hardware to respond to an external wake-up event.
    -   [**IPowerPolicyCallbackWakeFromSx::OnDisarmWakeFromSx**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ipowerpolicycallbackwakefromsx-ondisarmwakefromsx), which disables the device's ability to respond to an external wake-up event.
    -   [**IPowerPolicyCallbackWakeFromSx::OnWakeFromSxTriggered**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ipowerpolicycallbackwakefromsx-onwakefromsxtriggered), which informs the driver that the bus detected a wake signal.

Bus drivers also participate in waking up the system. The kernel-mode driver for the device's bus does whatever is necessary on the bus adapter to enable and disable a device's ability to wake from a low-power state.

For information about registry entries that control a device's wake capabilities, see [User Control of Device Idle and Wake Behavior in UMDF](user-control-of-device-idle-and-wake-behavior-in-umdf.md).

 

