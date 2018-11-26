---
title: Using Power Manager Routines for Idle Detection
description: Using Power Manager Routines for Idle Detection
ms.assetid: 6a89b2eb-d987-4722-b521-9df93153d957
keywords: ["idle detection WDK power management", "PoRegisterDeviceForIdleDetection", "PoSetDeviceBusy", "power manager WDK kernel", "idle time-outs WDK power management", "time-outs WDK power management"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Using Power Manager Routines for Idle Detection





The power manager provides support for idle detection through the [**PoRegisterDeviceForIdleDetection**](https://msdn.microsoft.com/library/windows/hardware/ff559721) and [**PoSetDeviceBusy**](https://msdn.microsoft.com/library/windows/hardware/ff559755) routines.

To enable idle detection for its device, a device power policy owner calls **PoRegisterDeviceForIdleDetection** and specifies:

-   The idle time-out value to apply when the system optimizes for performance.

-   The idle time-out value to apply when the system optimizes for conservation.

-   The device power state to which the device should transition when idle.

**PoRegisterDeviceForIdleDetection** returns a pointer to an idle counter, which the driver uses later to disable idle detection. Callers of **PoRegisterDeviceForIdleDetection** must be running at IRQL &lt; DISPATCH\_LEVEL.

A driver can register its device for idle detection any time after the device has been started and is ready to handle device power IRPs. For example, a driver might enable idle detection as part of its *IoCompletion* routine for a PnP start-device IRP.

The time-out values for any given device should be proportional to the device's power-up latency and based on observed device behavior. For devices of certain types, a driver can specify conservation and performance time-out values of -1 to use the standard power policy time-outs for the device class. See the device-specific documentation for details.

When the device is in use, the driver must call [**PoSetDeviceBusy**](https://msdn.microsoft.com/library/windows/hardware/ff559755), passing the pointer returned by **PoRegisterDeviceForIdleDetection**. **PoSetDeviceBusy** resets the idle counter, thus restarting the idle countdown for the device. The driver should call **PoSetDeviceBusy** on every I/O operation.

To determine whether the device is idle, the power manager compares the value of the idle counter with the driver-specified idle time-out value for the current system power policy (either conservation or performance). See the Microsoft Windows SDK for functions pertaining to the system power policy.

When the device satisfies the time-out value, the power manager sends a device set-power IRP, specifying the device power state that the driver passed in its call to **PoRegisterDeviceForIdleDetection**. The power manager does not send a query IRP before sending the set-power IRP. The drivers in the stack handle the set-power IRP as they would handle any other; they must complete it in a timely manner and they cannot fail it. (See [Handling Device Power-Down IRPs](handling-device-power-down-irps.md).)

When the driver no longer requires idle detection or is not prepared to handle device power-down IRPs, it should call **PoRegisterDeviceForIdleDetection** again, passing zero for both time-out values. Setting the time-outs to zero disables idle detection for both conservation (battery) and performance (AC) power policies. The driver can quickly reenable idle detection; it simply calls **PoRegisterDeviceForIdleDetection** with nonzero time-out values. Once the driver has registered the device, it can enable and disable idle detection by changing the time-out values, even if the device has been powered down and reawakened.

 

 




