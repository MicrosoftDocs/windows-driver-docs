---
title: Supporting Multiple-Component Devices with Single or Multiple Functional Power States
description: Supporting Multiple-Component Devices with Single or Multiple Functional Power States
ms.assetid: D601A0F6-A035-4161-879A-D495518E7EC6
---

# Supporting Multiple-Component Devices with Single or Multiple Functional Power States


\[Applies to KMDF only\]

A KMDF driver for a multiple-component device can define one or more functional power states for each component.

In this case, the driver registers directly with the power management framework (PoFx). To specify that WDF should not register with PoFx, the driver calls [**WdfDeviceAssignS0IdleSettings**](https://msdn.microsoft.com/library/windows/hardware/ff545903) with the **IdleTimeoutType** member of the [**WDF\_DEVICE\_POWER\_POLICY\_IDLE\_SETTINGS**](https://msdn.microsoft.com/library/windows/hardware/ff551270) structure set to **DriverManagedIdleTimeout**. Typically, the driver calls this method from its [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback function.

Next, the driver must register with PoFx. To do so, the driver calls [**PoFxRegisterDevice**](https://msdn.microsoft.com/library/windows/hardware/hh439521) and then [**PoFxStartDevicePowerManagement**](https://msdn.microsoft.com/library/windows/hardware/hh439551). Your driver must register with PoFx only once, when the device is first started. One way to do this is by calling these routines from a driver-supplied [*EvtDeviceSelfManagedIoInit*](https://msdn.microsoft.com/library/windows/hardware/ff540902) function. *EvtDeviceSelfManagedIoInit* is called only the first time the device is started.

When the device is removed, the driver must call [**PoFxUnregisterDevice**](https://msdn.microsoft.com/library/windows/hardware/hh439558) to unregister the device from PoFx. To unregister only once, we recommend the driver call this routine from a driver-supplied [*EvtDeviceSelfManagedIoFlush*](https://msdn.microsoft.com/library/windows/hardware/ff540901) function. *EvtDeviceSelfManagedIoFlush* is called only when the device is being removed. By unregistering in *EvtDeviceSelfManagedIoFlush*, the driver retains power registration during sleep and rebalance transitions and does not have to maintain power references for I/O requests that remain pending during these transitions.

When the driver calls [*PoFxRegisterDevice*](https://msdn.microsoft.com/library/windows/hardware/hh406408), it receives a power registration handle (POHANDLE) that it can use to interact directly with PoFx, as described in the following topics:

-   [Coordinating I/O Requests with Component Power State](coordinating-i-o-requests-with-component-power-state.md)
-   [Reporting Device Powered On When System Returns to S0](reporting-device-powered-on.md)
-   [Supporting Idle Power-Down on Multiple-Component Devices](supporting-idle-power-down-on-multiple-component-devices.md)

In addition, the driver can call [power framework routines](https://msdn.microsoft.com/library/windows/hardware/hh450961) directly to send power control requests and specify latency, residency, and wake requirements.

For more information about PoFx, see [Overview of the Power Management Framework](https://msdn.microsoft.com/library/windows/hardware/hh406637).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Supporting%20Multiple-Component%20Devices%20with%20Single%20or%20Multiple%20Functional%20Power%20States%20%20RELEASE:%20%283/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




