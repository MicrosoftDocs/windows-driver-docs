---
title: A User Unplugs a Device
description: A User Unplugs a Device
ms.assetid: 85e69401-0128-4641-aa0f-fd7c4f22f395
keywords:
- PnP WDK KMDF , unplugging devices
- Plug and Play WDK KMDF , unplugging devices
- orderly device removal WDK KMDF
- unplugging devices WDK KMDF
- surprise device removal WDK KMDF
- unexpected device removal WDK KMDF
- removing devices WDK KMDF
- ejecting devices WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# A User Unplugs a Device


While a system is running, a user can remove a device in one of two ways: by *orderly removal*, which means that the user informs the system that the device is about to be removed (for example, by using the Unplug or Eject Hardware program); or by *surprise removal*, which means that the user unplugs the device without informing the system. If the bus supports surprise removal (for example, USB), the device's drivers must be able to handle the device's sudden disappearance.

### <a href="" id="orderly-removal"></a> Orderly Removal

The user requests removal by using the system's Unplug or Eject Hardware program, by disabling the device by using Device Manager, or by pushing an [ejectable](supporting-ejectable-devices.md) device's eject button. The framework allows the device to be removed or disabled, unless the driver has:

-   Called [**WdfDeviceSetSpecialFileSupport**](https://msdn.microsoft.com/library/windows/hardware/ff546903) and a special file is open on the device.

-   Called [**WdfDeviceSetStaticStopRemove**](https://msdn.microsoft.com/library/windows/hardware/ff546915).

-   Supplied an [*EvtDeviceQueryRemove*](https://msdn.microsoft.com/library/windows/hardware/ff540883) callback function, and the callback function has vetoed the removal.

For each function and filter driver that supports the device, the framework does the following, in sequence, one driver at a time, starting with the driver that is highest in the driver stack:

1.  If the driver is using self-managed I/O, the framework calls the driver's [*EvtDeviceSelfManagedIoSuspend*](https://msdn.microsoft.com/library/windows/hardware/ff540907) callback function.

2.  The framework stops all of the driver's power-managed I/O queues.

3.  If the hardware and driver support DMA, the framework calls the driver's [*EvtDmaEnablerSelfManagedIoStop*](https://msdn.microsoft.com/library/windows/hardware/ff541677), [*EvtDmaEnablerFlush*](https://msdn.microsoft.com/library/windows/hardware/ff541655), and [*EvtDmaEnablerDisable*](https://msdn.microsoft.com/library/windows/hardware/ff540927) callback functions (if they exist) for each DMA channel that was created.

4.  The framework calls the driver's [*EvtDeviceD0ExitPreInterruptsDisabled*](https://msdn.microsoft.com/library/windows/hardware/ff540856) callback function (if it exists), and then calls the driver's [*EvtInterruptDisable*](https://msdn.microsoft.com/library/windows/hardware/ff541714) callback function (if it exists) for each interrupt so that the driver can disable device interrupts.

5.  The framework calls the driver's [*EvtDeviceD0Exit*](https://msdn.microsoft.com/library/windows/hardware/ff540855) callback function (if it exists).

6.  The framework calls the driver's [*EvtDeviceReleaseHardware*](https://msdn.microsoft.com/library/windows/hardware/ff540890) callback function (if it exists), passing it the list of hardware resources that the PnP manager has assigned to the device.

7.  If the driver is using self-managed I/O, the framework calls the driver's [*EvtDeviceSelfManagedIoFlush*](https://msdn.microsoft.com/library/windows/hardware/ff540901) callback function.

8.  If the driver is using self-managed I/O, the framework calls the driver's [*EvtDeviceSelfManagedIoCleanup*](https://msdn.microsoft.com/library/windows/hardware/ff540898) callback function.

The bus driver is the driver in the stack that is called last. When the framework calls the bus driver's [*EvtDeviceD0Exit*](https://msdn.microsoft.com/library/windows/hardware/ff540855) callback function, the callback function sets the power state of the device (a child device of the bus) to D3. The bus driver can control when the framework calls its [*EvtDeviceReleaseHardware*](https://msdn.microsoft.com/library/windows/hardware/ff540890) callback function by calling [**WdfDeviceInitSetReleaseHardwareOrderOnFailure**](https://msdn.microsoft.com/library/windows/hardware/hh706196).

### <a href="" id="surprise-removal"></a> Surprise Removal

A user unplugs a device unexpectedly. The bus driver for the device's bus discovers that the device is missing and calls [**WdfChildListUpdateChildDescriptionAsMissing**](https://msdn.microsoft.com/library/windows/hardware/ff545674).

For each function and filter driver that supports the device, the framework does the following, in sequence, one driver at a time, starting with the driver that is highest in the driver stack:

1.  The framework calls the driver's [*EvtDeviceSurpriseRemoval*](https://msdn.microsoft.com/library/windows/hardware/ff540913) callback function (if it exists).

2.  If the device was in its working (D0) state when it was unplugged, the framework stops all of the driver's power-managed I/O queues.

3.  If the device was in its working (D0) state when it was unplugged, and if the driver is using self-managed I/O, the framework calls the driver's [*EvtDeviceSelfManagedIoSuspend*](https://msdn.microsoft.com/library/windows/hardware/ff540907) callback function.

4.  If the hardware and driver support DMA, the framework calls the driver's [*EvtDmaEnablerSelfManagedIoStop*](https://msdn.microsoft.com/library/windows/hardware/ff541677), [*EvtDmaEnablerFlush*](https://msdn.microsoft.com/library/windows/hardware/ff541655), and [*EvtDmaEnablerDisable*](https://msdn.microsoft.com/library/windows/hardware/ff540927) callback functions (if they exist) for each DMA channel that was created.

5.  The framework calls the driver's [*EvtDeviceD0ExitPreInterruptsDisabled*](https://msdn.microsoft.com/library/windows/hardware/ff540856) and [*EvtInterruptDisable*](https://msdn.microsoft.com/library/windows/hardware/ff541714) callback functions (if they exist) so that the driver can disable device interrupts.

6.  The framework calls the driver's [*EvtDeviceD0Exit*](https://msdn.microsoft.com/library/windows/hardware/ff540855) callback function (if it exists).

7.  The framework calls the driver's [*EvtDeviceReleaseHardware*](https://msdn.microsoft.com/library/windows/hardware/ff540890) callback function (if it exists), passing the list of hardware resources that the PnP manager has assigned to the device.

8.  If the driver is using self-managed I/O, the framework calls the driver's [*EvtDeviceSelfManagedIoFlush*](https://msdn.microsoft.com/library/windows/hardware/ff540901) callback function.

9.  If the driver is using self-managed I/O, the framework calls the driver's [*EvtDeviceSelfManagedIoCleanup*](https://msdn.microsoft.com/library/windows/hardware/ff540898) callback function.

Note that a device can be unexpectedly removed at any time. Therefore, the framework might call the driver's [*EvtDeviceSurpriseRemoval*](https://msdn.microsoft.com/library/windows/hardware/ff540913) callback function at a time other than that shown in the previous steps. For example, if a user unexpectedly unplugs the device while it is [entering a low-power state](a-device-enters-a-low-power-state.md), the framework might call the [*EvtDeviceSurpriseRemoval*](https://msdn.microsoft.com/library/windows/hardware/ff540913) callback function after it calls the [*EvtDeviceReleaseHardware*](https://msdn.microsoft.com/library/windows/hardware/ff540890) callback function. You must not code an [*EvtDeviceSurpriseRemoval*](https://msdn.microsoft.com/library/windows/hardware/ff540913) callback function in a manner that assumes that it and other callback functions are called in a particular sequence.

In addition, the framework does not synchronize a device's [*EvtDeviceSurpriseRemoval*](https://msdn.microsoft.com/library/windows/hardware/ff540913) callback function with any of the callback functions listed in the previous steps for that device. Therefore, the [*EvtDeviceSurpriseRemoval*](https://msdn.microsoft.com/library/windows/hardware/ff540913) callback function might run while another of the previously listed callback functions is also running.

 

 





