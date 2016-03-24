---
title: Supporting System Wake-Up in UMDF Drivers
description: Supporting System Wake-Up in UMDF Drivers
ms.assetid: 945b1751-f3a1-4a29-8fb7-6690f91af7d9
keywords: ["power management WDK UMDF , system wake-up", "system wake-up WDK UMDF"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Supporting%20System%20Wake-Up%20in%20UMDF%20Drivers%20%20RELEASE:%20%283/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




