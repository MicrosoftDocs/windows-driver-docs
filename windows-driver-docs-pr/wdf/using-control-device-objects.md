---
title: Using Control Device Objects
description: Using Control Device Objects
ms.assetid: 6367954f-6916-46df-a5a0-e80f045b69e5
keywords:
- control device objects WDK KMDF
- device objects WDK KMDF
- framework objects WDK KMDF , control device objects
- legacy hardware devices WDK KMDF
- software-only virtual devices WDK KMDF
- system shutdown notifications WDK KMDF
- shutdown notifications WDK KMDF
- notifications WDK KMDF
- names WDK KMDF
- names WDK KMDF , device objects
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using Control Device Objects


A *control device object* is a framework device object that does not support Plug and Play (PnP) or power management operations. Drivers can use control device objects to represent software-only virtual devices or *legacy hardware devices* (that is, devices that do not provide PnP or power management capabilities).

A driver that creates a control device object also typically creates a symbolic link for the device object. Applications can send I/O requests to the control device object by passing the symbolic link name to an API element, such as the Microsoft Win32 [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) function.

The framework does not attach control device objects to a [device stack](wdm-concepts-for-kmdf-drivers.md#device-stacks). Therefore, when an application sends an I/O request to a control device object, the I/O manager delivers the request directly to the driver that created the control device object, instead of to the driver at the top of the stack. (However, an additional driver can call [**IoAttachDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548294) to attach a device object above the control device object. In this case, the additional driver receives the I/O request first.)

### Uses of Control Device Objects

Two typical uses for control devices are:

1.  A filter driver for a PnP device, if the driver supports a set of custom I/O control codes for applications to use.

    If an application attempted to send the custom I/O control codes to the top of the driver stack (by using, for example, the symbolic link name of a [device interface](using-device-interfaces.md)), a driver above the filter driver might fail the I/O request if the driver did not recognize the custom I/O control codes. To avoid this problem, the filter driver can create a control device object. Applications can use the control device object's symbolic link name to send I/O control codes directly to the filter driver.

    (Note that a better way for the filter driver to avoid the problem is to act as a bus driver and [enumerate](enumerating-the-devices-on-a-bus.md) child devices that operate in raw mode. In other words, for each device that the filter driver supports, the driver can create a physical device object (PDO) that does not require a function driver. The driver calls [**WdfPdoInitAssignRawDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548802) and [**WdfDeviceInitAssignName**](https://msdn.microsoft.com/library/windows/hardware/ff546029) for each of these devices, and the application can identify a device by name when it sends a custom I/O control code.)

2.  A driver for a device that does not support PnP.

    Such a driver must use control device objects, because the device objects for such devices do not reside in a device stack and do not provide PnP capabilities. For more information about supporting non-PnP devices, see [Using Kernel-Mode Driver Framework with Non-PnP Drivers](using-kernel-mode-driver-framework-with-non-pnp-drivers.md).

### Creating a Control Device Object

To create a control device object, a driver must:

1.  Call [**WdfControlDeviceInitAllocate**](https://msdn.microsoft.com/library/windows/hardware/ff545841) to obtain a [**WDFDEVICE\_INIT**](https://msdn.microsoft.com/library/windows/hardware/ff546951) structure.

2.  Call object initialization methods, as needed, to initialize the WDFDEVICE\_INIT structure. The driver can call only the following initialization methods:
    -   [**WdfControlDeviceInitSetShutdownNotification**](https://msdn.microsoft.com/library/windows/hardware/ff545847)
    -   [**WdfDeviceInitAssignName**](https://msdn.microsoft.com/library/windows/hardware/ff546029)
    -   [**WdfDeviceInitAssignSDDLString**](https://msdn.microsoft.com/library/windows/hardware/ff546035)
    -   [**WdfDeviceInitAssignWdmIrpPreprocessCallback**](https://msdn.microsoft.com/library/windows/hardware/ff546043)
    -   [**WdfDeviceInitSetCharacteristics**](https://msdn.microsoft.com/library/windows/hardware/ff546074)
    -   [**WdfDeviceInitSetDeviceClass**](https://msdn.microsoft.com/library/windows/hardware/ff546084)
    -   [**WdfDeviceInitSetExclusive**](https://msdn.microsoft.com/library/windows/hardware/ff546097)
    -   [**WdfDeviceInitSetFileObjectConfig**](https://msdn.microsoft.com/library/windows/hardware/ff546107)
    -   [**WdfDeviceInitSetIoInCallerContextCallback**](https://msdn.microsoft.com/library/windows/hardware/ff546119)
    -   [**WdfDeviceInitSetIoType**](https://msdn.microsoft.com/library/windows/hardware/ff546128)
    -   [**WdfDeviceInitSetRequestAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff546786)

3.  Call [**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926), which uses the contents of the WDFDEVICE\_INIT structure to create a framework device object.

4.  Complete the following initialization operations:
    -   [Create a default I/O queue](creating-i-o-queues.md) for the device, if one is needed.
    -   Call [**WdfDeviceConfigureRequestDispatching**](https://msdn.microsoft.com/library/windows/hardware/ff545920), if needed.
    -   Call [**WdfDeviceCreateSymbolicLink**](https://msdn.microsoft.com/library/windows/hardware/ff545939) to create a symbolic link name that applications can use to access the control device.

5.  Call [**WdfControlFinishInitializing**](https://msdn.microsoft.com/library/windows/hardware/ff545854).

### Rules for Using Control Device Objects

Drivers that create control device objects must obey the following rules:

-   Drivers cannot pass the control device object's handle to framework methods that [enumerate child devices](enumerating-the-devices-on-a-bus.md).

-   Drivers cannot pass the control device object's handle to framework methods that support [device interfaces](using-device-interfaces.md).

-   Drivers can create I/O queues and register request handlers for the queues, but the framework does not allow the queues to be [power-managed](using-power-managed-i-o-queues.md).

-   Drivers can create [file objects](framework-file-objects.md) for control device objects.

### Naming a Control Device Object

All control device objects must be named. Typically, your driver will call [**WdfDeviceInitAssignName**](https://msdn.microsoft.com/library/windows/hardware/ff546029) to assign a device name and then call [**WdfDeviceCreateSymbolicLink**](https://msdn.microsoft.com/library/windows/hardware/ff545939) to create a symbolic link name that applications can use to access the object.

If your driver does not call [**WdfDeviceInitAssignName**](https://msdn.microsoft.com/library/windows/hardware/ff546029) to assign a device name, the framework automatically generates a name for control devices--but your driver cannot call [**WdfDeviceCreateSymbolicLink**](https://msdn.microsoft.com/library/windows/hardware/ff545939).

Your driver can call [**WdfDeviceInitSetDeviceClass**](https://msdn.microsoft.com/library/windows/hardware/ff546084) to specify a [device setup class](https://msdn.microsoft.com/library/windows/hardware/ff541509) for a control device. The device setup class identifies a section of the registry that contains administrator-supplied information about devices that belong to the setup class. For more information about calling [**WdfDeviceInitSetDeviceClass**](https://msdn.microsoft.com/library/windows/hardware/ff546084), see [Controlling Device Access in Framework-Based Drivers](controlling-device-access-in-kmdf-drivers.md).

### Receiving Notification of System Shutdown

Because control device objects do not support PnP, your driver cannot register callback functions that inform the driver when a device's power state changes. However, the driver can call [**WdfControlDeviceInitSetShutdownNotification**](https://msdn.microsoft.com/library/windows/hardware/ff545847) to register an [*EvtDeviceShutdownNotification*](https://msdn.microsoft.com/library/windows/hardware/ff540911) callback function. This callback function informs the driver when the system is about to lose its power.

### Deleting a Control Device Object

Some drivers have to delete their control device objects before the driver unloads, as follows:

-   If your driver creates control device objects (which do not support PnP or power management), and if the driver also creates framework device objects that support PnP and power management, the driver must eventually call [**WdfObjectDelete**](https://msdn.microsoft.com/library/windows/hardware/ff548734) at IRQL = PASSIVE\_LEVEL to delete the control device objects.

    If the driver creates both types of device objects, the operating system cannot unload your driver until the driver has deleted the control device objects.

    However, the driver must not delete the control device objects until after the framework has deleted the other device objects. To determine when the framework has deleted the other device objects, your driver should provide [*EvtCleanupCallback*](https://msdn.microsoft.com/library/windows/hardware/ff540840) functions for those objects.

-   If your driver creates control device objects but does not create framework device objects that support PnP and power management, the driver does not have to delete the control device objects.

    In this case, the framework deletes the control device objects after the driver's [*EvtDriverUnload*](https://msdn.microsoft.com/library/windows/hardware/ff541694) callback function returns.

 

 





