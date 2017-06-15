---
title: Using Power Manager Routines for Idle Detection
author: windows-driver-content
description: Using Power Manager Routines for Idle Detection
MS-HAID:
- 'PwrMgmt\_59061bc7-f6cd-470b-9388-58ad9849d955.xml'
- 'kernel.using\_power\_manager\_routines\_for\_idle\_detection'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 6a89b2eb-d987-4722-b521-9df93153d957
keywords: ["idle detection WDK power management", "PoRegisterDeviceForIdleDetection", "PoSetDeviceBusy", "power manager WDK kernel", "idle time-outs WDK power management", "time-outs WDK power management"]
---

# Using Power Manager Routines for Idle Detection


## <a href="" id="ddk-using-power-manager-routines-for-idle-detection-kg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Using%20Power%20Manager%20Routines%20for%20Idle%20Detection%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


