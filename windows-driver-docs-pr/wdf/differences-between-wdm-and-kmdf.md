---
title: Differences Between WDM and WDF
description: The WDM model is closely tied to the operating system.
ms.assetid: 4D35F0AB-44CE-49CA-8AB7-3922871567B0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Differences Between WDM and WDF


The WDM model is closely tied to the operating system. Drivers interact directly with the operating system by calling system service routines and manipulating operating system structures. Because WDM drivers are trusted kernel-mode components, the system provides limited checks on driver input.

In comparison, the Windows Driver Frameworks (WDF) model focuses on the driver’s requirements, and the framework library handles the majority of the interactions with the system.

The framework intercepts I/O requests, takes default actions where appropriate, and invokes the driver’s callbacks as required. The WDF model is object based and event driven. Objects represent common driver constructs, such as a device, a lock, or a queue. A Kernel-Mode Driver Framework (KMDF) or User-Mode Driver Framework (UMDF) driver contains an entry point ([**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff540807)), the event-related callback functions that are required to service the device and support I/O, and any additional internal utility functions on which the implementation depends.

This section describes important differences between WDM and WDF in the following areas:

-   [Driver Structure](#drv-struct)
-   [Device Objects and Driver Roles](#roles)
-   [Object Model](#obj-model)
-   [Object Creation](#creation)
-   [Object Context Area](#context)
-   [Supported IRP Types](#irp)
-   [I/O Queues](#queue)
-   [Synchronization and Concurrency](#sync)
-   [Driver Installation](#install)

## Driver Structure


Both WDM and WDF drivers contain a [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff540807) routine, a number of routines that are called to handle particular I/O requests, and various support routines.

In a WDM driver, the I/O dispatch routines map to particular major IRP codes. The dispatch routines receive IRPs from the I/O manager, parse them, and respond accordingly.

In a WDF driver, the framework registers its own dispatch routines, which receive IRPs from the I/O manager, parse them, and then invoke the driver’s event callback functions to handle them. The event callback functions typically perform a more specific task than the general I/O dispatch routines of the WDM driver.

A typical WDF driver for a Plug and Play device contains:

-   A [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff540807) routine.
-   An [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) routine, which is similar in function to a WDM AddDevice routine.
-   One or more I/O queues.
-   One or more I/O event callback functions, which are similar in function to a WDM driver’s I/O *DispatchXxx* routines.
-   Callbacks to handle the Plug and Play and power events that the driver supports.
-   Callbacks to handle the WMI requests that the driver supports. (KMDF-only)
-   Additional callbacks, as appropriate, for object cleanup, file creation, and I/O targets, and so on.

## Device Objects and Driver Roles


Both WDM and WDF drivers create one or more device objects. Each device object represents a driver role that is the target of I/O requests. A physical device object (PDO) represents a bus driver, a functional device object (FDO) represents a function driver, and a filter device object (filter DO) represents a filter driver.

In WDM drivers, these driver roles are implicit, so the driver must keep track of which role each device object represents and respond to IRPs appropriately.

WDF drivers, however, indicate explicitly whether a device object represents a PDO (KMDF only), FDO, or filter DO and register event callbacks that are specific to that role. For example, PDOs are the target of [resource requirements queries](creating-a-resource-requirements-list.md) and [device ejection requests](supporting-ejectable-devices.md), whereas FDOs and filter DOs do not handle such requests.

A WDF driver configures each device object to receive certain types of I/O requests. The framework calls the driver to handle only those I/O requests and performs a default action for all other requests. If the device object represents a filter driver, the framework passes all other requests to the next lower driver. If the device object represents a bus or function driver, the framework fails all other request types.

For Plug and Play and power requests, the framework calls the KMDF or UMDF driver only for the requests that are appropriate for each device object—and at the appropriate time. For example, an FDO must respond to certain requests after the underlying PDO has already responded. In a WDM driver, the FDO must set an I/O completion routine, pass the IRP down the stack, and process it after lower drivers. A WDF driver simply implements the corresponding callback routine, and the framework calls it after lower drivers have completed processing.

For information on how to create framework device objects, see [Creating a Framework Device Object](creating-a-framework-device-object.md).

Some drivers also handle certain I/O requests that are independent of Plug and Play. A WDM driver creates a DEVICE\_OBJECT as the target for such requests, but does not attach it to the Plug and Play device stack. To accomplish the same result, a KMDF driver [creates a control device object](using-control-device-objects.md). Some framework-based drivers use control device objects to implement “sideband” I/O mechanisms so that they can receive certain types of I/O requests regardless of device state.

## Object Model


WDF supports a coherent object model in which objects are opaque to drivers, provide driver-configurable context areas, and are referenced by a handle. WDM objects are system-wide objects that are accessible to drivers and are referenced by pointers. A driver that corrupts a WDM object can corrupt the entire system. Corrupting a WDF object is not only more difficult—because the framework validates the data that the driver supplies—but also causes system-wide problems much less often.

For information about the naming convention for KMDF objects, see [WDF Architecture](kernel-mode-driver-framework-architecture.md).

The framework maintains a reference count for each object, which thus provides some control over its lifetime. For more information, see [Framework Object Life Cycle](framework-object-life-cycle.md).

Although many of the WDF objects correspond to WDM objects, the WDF objects support features that would require additional code in a WDM driver. All WDF objects support driver-definable object context areas so that a driver can store information that is related to a particular instance of an object with the object itself. Objects typically track state as well. For example, WDFQUEUE objects are more than just a list of I/O requests; they support several types of dispatching, automatic synchronization with Plug and Play, and request cancellation. For WDFMEMORY objects, the framework-managed reference count helps prevent memory leaks and premature release of resources.

## Object Creation


WDF drivers follow a regular pattern to create all types of objects:

1.  Initialize the configuration structure for the object, if one exists.
2.  Optionally initialize the attributes structure for the object.
3.  Call the creation method to create the object.

The configuration structure and the attributes structure supply basic information about the object and how the driver uses it. All object types use [**WDF\_OBJECT\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552400) as the attributes structure, but the configuration structure for each type of object is different and some objects do not have one. For example, there is a [**WDF\_DRIVER\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff551300) structure but not a **WDF\_DEVICE\_CONFIG** structure.

The configuration structure holds pointers to object-specific information, such as the driver’s event callback functions for the object. The driver fills in this structure and then passes it to the framework when it calls the object creation method. For example, a call to [**WdfDriverCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547175) includes a pointer to a [**WDF\_DRIVER\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff551300) structure that contains a pointer to the driver’s [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback function.

The framework defines functions that are named WDF\_*Object*\_CONFIG\_INIT to initialize the configuration structures, where *Object* represents the name of the object type. The [**WDF\_OBJECT\_ATTRIBUTES\_INIT**](https://msdn.microsoft.com/library/windows/hardware/ff552402) function initializes a driver's [**WDF\_OBJECT\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552400) structure.

## Object Context Area


Every instance of an object can have one or more object context areas. The object context area is a storage area for data that is related to that particular instance, such as a driver-allocated event object. The driver determines the size and layout of the object context area. For a device object, the object context area is the equivalent of the WDM device extension. For information about defining and initializing a context area, see [Framework Object Context Space](framework-object-context-space.md).

## Supported IRP Types


WDF supports a subset of Windows IRPs. For a summary of the major WDM IRP types and the corresponding WDF event callback functions, see [WDM IRPs and WDF Event Callback Functions](wdm-irps-and-kmdf-event-callback-functions.md).

Even if your driver receives IRPs other than those listed in the table, you can port it to KMDF. KMDF provides a mechanism through which a driver can receive “raw” WDM IRPs but also use the KMDF features for other types of IRPs. For more information, see [Handling WDM IRPs Outside of the Framework](handling-wdm-irps-outside-of-the-framework.md).

## I/O Queues


Nearly all drivers queue I/O requests. WDM drivers typically use one of the following approaches:

-   Implement a [*StartIo*](https://msdn.microsoft.com/library/windows/hardware/ff563858) function and call [**IoStartPacket**](https://msdn.microsoft.com/library/windows/hardware/ff550370) and [**IoStartNextPacket**](https://msdn.microsoft.com/library/windows/hardware/ff550358) to use the system’s device queue for I/O requests.
-   Use the **IoCsqXxx** or other list-management functions to implement its own internal I/O queues.
-   Use the **KeXxxDeviceQueue** functions to initialize and manage a queue that is protected by a spin lock.

A WDF driver creates a WDF queue object (WDFQUEUE) to represent an I/O queue. The WDF queue object is similar to a cancel-safe queue but provides additional features.

When you port a WDM driver to WDF, you can use the WDF queuing mechanism regardless of the mechanism that the WDM driver uses. For more information about queues, see [Framework Queue Objects](framework-queue-objects.md).

## Synchronization and Concurrency


WDF drivers benefit from some built-in synchronization support that is not available to WDM drivers. Although this support does not mean that the driver can ignore concurrency and synchronous access to data, WDF drivers nevertheless require significantly fewer locks and less synchronization code than do WDM drivers.

For more information about the synchronization features that the framework provides, see [Synchronization Techniques](synchronization-techniques-for-wdf-drivers.md).

## Driver Installation


Like WDM drivers, KMDF and UMDF drivers are installed by using INF files. However, WDF driver installation sometimes requires a framework co-installer that is provided with the Windows Driver Kit (WDK). The co-installer ensures that a compatible version of the framework library is present on the target system. For information about installation, see [Building and Loading a WDF Driver](building-and-loading-a-kmdf-driver.md).

 

 





