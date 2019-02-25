---
title: Using Self-Managed I/O
description: Using Self-Managed I/O
ms.assetid: 539b3618-44bb-41fd-a9f2-ed6a377c94e2
keywords:
- PnP WDK KMDF , self-managed I/O
- Plug and Play WDK KMDF , self-managed I/O
- power management WDK KMDF , self-managed I/O
- self-managed I/O WDK KMDF
- I/O self management WDK KMDF
- surprise device removal WDK KMDF
- unexpected device removal WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using Self-Managed I/O


Most framework-based drivers take advantage of the framework's PnP and power management capabilities for the devices they support. In other words, most framework-based drivers let the framework manage a device's PnP and power states by doing all of the following:

-   Supplying [*EvtDeviceD0Entry*](https://msdn.microsoft.com/library/windows/hardware/ff540848) and [*EvtDeviceD0Exit*](https://msdn.microsoft.com/library/windows/hardware/ff540855) callback functions.

-   Supplying [*EvtDevicePrepareHardware*](https://msdn.microsoft.com/library/windows/hardware/ff540880) and [*EvtDeviceReleaseHardware*](https://msdn.microsoft.com/library/windows/hardware/ff540890) callback functions.

-   Using power-managed queues for I/O requests that require the device to be in its working state, and using queues that are not power-managed for all other requests.

However, a few framework-based drivers will require greater knowledge of the state of their devices, including drivers in the following situations:

-   The operations that a driver performs are not determined by a set of I/O requests that the driver receives from framework I/O queues.

-   A driver communicates with older, non-framework drivers and deals directly with WDM interfaces.

-   The I/O requests that a driver receives cannot be divided into two groups: those that require the device to be in its working state and those that do not.

Most drivers are not in one of the preceding situations, but if your driver is, it might need to have more direct control over the device's PnP and power management operations. Such drivers can use *self-managed I/O*. Using self-managed I/O means that the driver is notified (by means of a set of callback functions) whenever one if its devices is plugged in or unplugged, and whenever the device is temporarily stopped.

Note that a driver can use self-managed I/O and still use the framework's I/O queues, either as power-managed queues or not. For example, a driver can use the framework's I/O queues, not power-managed, with a set of self-managed I/O callback functions.

To use self-managed I/O, the driver registers an extra set of event callback functions when it calls [**WdfDeviceInitSetPnpPowerEventCallbacks**](https://msdn.microsoft.com/library/windows/hardware/ff546135). These event callback functions are:

-   [*EvtDeviceSelfManagedIoInit*](https://msdn.microsoft.com/library/windows/hardware/ff540902), which initializes and starts the device's I/O operations.

-   [*EvtDeviceSelfManagedIoSuspend*](https://msdn.microsoft.com/library/windows/hardware/ff540907), which suspends I/O operations.

-   [*EvtDeviceSelfManagedIoRestart*](https://msdn.microsoft.com/library/windows/hardware/ff540905), which restarts the device's I/O operations after they have been suspended.

-   [*EvtDeviceSelfManagedIoFlush*](https://msdn.microsoft.com/library/windows/hardware/ff540901), which removes unserviced I/O requests.

-   [*EvtDeviceSelfManagedIoCleanup*](https://msdn.microsoft.com/library/windows/hardware/ff540898), which deallocates resources that were allocated by [*EvtDeviceSelfManagedIoInit*](https://msdn.microsoft.com/library/windows/hardware/ff540902).

When your device enters its working (D0) state for the first time, the framework calls your driver's [*EvtDeviceSelfManagedIoInit*](https://msdn.microsoft.com/library/windows/hardware/ff540902) callback function. This happens each time a user plugs your device into the system and each time the system is restarted.

There are three circumstances in which a driver must stop a device's I/O operations: the device is about to enter a low-power state, it is about to be removed, or it has already been removed unexpectedly. The following list examines each of these circumstances in detail:

-   The device is about to enter a low-power state and will eventually return to its working state.

    When your device is about to enter a low-power state (because either your device has been idle, the entire system is entering a low-power state, or the PnP manager is [redistributing system hardware resources](handling-requests-to-stop-a-device.md#redistributing-resources)), the framework calls your driver's [*EvtDeviceSelfManagedIoSuspend*](https://msdn.microsoft.com/library/windows/hardware/ff540907) callback function. After the device reenters its working state, the framework calls your driver's [*EvtDeviceSelfManagedIoRestart*](https://msdn.microsoft.com/library/windows/hardware/ff540905) callback function.

-   The device is about to be removed.

    To handle [user-requested device removal](handling-requests-to-stop-a-device.md#a-user-removes-or-disables-a-device), the framework calls your driver's [*EvtDeviceSelfManagedIoSuspend*](https://msdn.microsoft.com/library/windows/hardware/ff540907) callback function before stopping the device. After stopping the device, the framework calls your driver's [*EvtDeviceSelfManagedIoFlush*](https://msdn.microsoft.com/library/windows/hardware/ff540901) callback function. After the device has been removed, the framework calls the [*EvtDeviceSelfManagedIoCleanup*](https://msdn.microsoft.com/library/windows/hardware/ff540898) callback function.

-   The device has already been removed unexpectedly (surprise removal).

    If the driver for the device's bus determines that the device is no longer present, or if another driver in the stack determines that the device is not responding, the driver that discovered the problem informs the PnP manager. The PnP manager then informs the rest of the drivers that the device is gone. For framework-based drivers, the framework receives the PnP manager's message and calls your driver's [*EvtDeviceSelfManagedIoSuspend*](https://msdn.microsoft.com/library/windows/hardware/ff540907), [*EvtDeviceSelfManagedIoFlush*](https://msdn.microsoft.com/library/windows/hardware/ff540901), and [*EvtDeviceSelfManagedIoCleanup*](https://msdn.microsoft.com/library/windows/hardware/ff540898) callback functions.

    (Your driver can also register an [*EvtDeviceSurpriseRemoval*](https://msdn.microsoft.com/library/windows/hardware/ff540913) callback function. If the device was in its working (D0) state when removed, the framework calls *EvtDeviceSurpriseRemoval* before it calls the self-managed I/O callback functions. If the device was in a low-power state when removed, *EvtDeviceSurpriseRemoval* is called after [*EvtDeviceSelfManagedIoSuspend*](https://msdn.microsoft.com/library/windows/hardware/ff540907))

For more information about the order in which the framework calls a driver's event callback functions, see [PnP and Power Management Scenarios](pnp-and-power-management-scenarios.md).

Although rarely necessary, the framework allows drivers to have even more control over a device's PnP and power states, by accessing the [state machines in the framework](state-machines-in-the-framework.md).

 

 





