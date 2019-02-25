---
title: Multiple-Component Device, one or more Functional Power States
description: Supporting Multiple-Component Devices with Single or Multiple Functional Power States
ms.assetid: D601A0F6-A035-4161-879A-D495518E7EC6
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





