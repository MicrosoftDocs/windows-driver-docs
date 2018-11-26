---
title: Minidrivers and the HID class driver
description: Operation of the HID class driver
ms.assetid: 3A8F5545-F8EB-47E2-989D-7DE83E32110E
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Minidrivers and the HID class driver


The section includes the following topics about the operation of the HID class driver:

-   Operational features of the HID class driver
-   Binding the operation of the HID class driver to a HID minidriver
-   Communicating with a HID minidriver

See [Creating WDF HID minidrivers](https://docs.microsoft.com/windows-hardware/drivers/wdf/creating-umdf-hid-minidrivers) for more information.

### Operational features of the HID class driver

The HID class driver does the following:

-   Provides and manages the upper-level interface that kernel-mode drivers and user-mode applications use to access the [HID collections](hid-collections.md) that an input device supports.

    The HID class driver transparently manages and routes all communication between upper-level drivers and applications and the underlying input devices that support HID collections. It manages the different data protocols that are used by different input devices and input queues that support more than one open file on the same HID collection.

    The upper-level interface to HID collections consists of the [HID class driver IOCTLs](https://msdn.microsoft.com/library/windows/hardware/ff539849), the [HIDClass support routines](https://msdn.microsoft.com/library/windows/hardware/ff538865), and the [HIDClass structures](https://msdn.microsoft.com/library/windows/hardware/ff538854).

-   Communicates with a HID minidriver by calling the minidriver's standard driver routines.

-   Creates a functional device object ([*FDO*](https://msdn.microsoft.com/library/windows/hardware/ff556280#wdkgloss-fdo)) for HIDClass input devices enumerated by a lower-level bus or port driver.

    For example, the HID class driver creates and manages the operations of an FDO that represents a USB HID device enumerated by the system-supplied USB driver stack.

-   Provides the functionality of a bus driver for the child devices (HID collections) supported by an underlying input device.

    The HID class driver creates a physical device object ([*PDO*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-pdo)) for each HID collection supported by an input device and manages the collection's operation.

### Binding a minidriver to HIDClass

A HID minidriver binds its operation to the HID class driver by calling [**HidRegisterMinidriver**](https://msdn.microsoft.com/library/windows/hardware/ff539835) to register itself with the HID class driver. The registration operation does the following:

-   Saves a copy of the entry points (pointers) to the HID minidriver's standard driver routines in the HID class driver's device extension.

    A HID minidriver sets its entry points in the driver object that the minidriver receives as input to its [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine. The HID minidriver sets these entry points before it registers with the HID class driver.

-   Resets the entry points in the minidriver's driver object to the entry points for the standard driver routines supplied by the HID class driver.

The HID class driver supplies the following standard driver routines:

-   [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) and [*Unload*](https://msdn.microsoft.com/library/windows/hardware/ff564886) routines

-   Dispatch routines for the following I/O requests:

    [**IRP\_MJ\_CREATE**](https://msdn.microsoft.com/library/windows/hardware/ff550729)

    [**IRP\_MJ\_CLOSE**](https://msdn.microsoft.com/library/windows/hardware/ff550720)

    [**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550744)

    [**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550766)

    [**IRP\_MJ\_PNP**](https://msdn.microsoft.com/library/windows/hardware/ff550772)

    [**IRP\_MJ\_SYSTEM\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550813)

The registration process also allocates memory for the HID mindriver device extension. Although the memory is allocated by the HID class driver, only the HID minidriver uses this device extension.

### Communicating with a HID minidriver

The HID class driver communicates with a HID minidriver by calling the HID minidriver's [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521), [*Unload*](https://msdn.microsoft.com/library/windows/hardware/ff564886), and dispatch routines as follows:

### Calling the AddDevice Routine

When the HID class driver's **AddDevice** routine is called to create a functional device object ([*FDO*](https://msdn.microsoft.com/library/windows/hardware/ff556280#wdkgloss-fdo)), the HID class driver creates the FDO, initializes it, and calls the HID minidriver **AddDevice** routine. The HID minidriver **AddDevice** routine does internal device-specific initialization and, if successful, returns STATUS\_SUCCESS. If the HID minidriver **AddDevice** routine is not successful, the HID class driver deletes the FDO and returns the status returned by the HID minidriver **AddDevice** routine.

### Calling the Unload Routine

When the HID class driver **Unload** routine is called, the HID class driver completes releasing all resources associated with FDO and calls the HID minidriver's **Unload** routine.

### Calling the Dispatch Routines

To operate a device, the HID class driver primarily calls the HID minidriver dispatch routine for internal device control requests.

In addition, when the I/O manager sends Plug and Play, power, or system control requests to the HID class driver for an FDO, the HID class driver processes the request, and calls the HID minidriver's corresponding dispatch routine.

The HID class driver does not send the following requests to the HID minidriver: create, close, or device control.

### Operation of a HID minidriver

A HID transport minidriver abstracts the operation of a hardware bus or port that your input device attaches to.

HID minidrivers can be built using one of the following frameworks:

-   UMDF – User Mode Driver Framework
-   KDMF – Kernel Mode Driver Framework
-   WDM – Legacy Windows Driver Model

Microsoft recommends using a Frameworks based solution (KMDF or UMDF (on Windows 8 only)). For more information on each of the driver models, please visit the following sections:

-   KMDF-based HID minidriver, see Creating Framework-based HID Minidrivers
-   UMDF-based HID minidriver, see Creating UMDF-based HID Minidrivers

The following section talks about registering a WDM based HID Minidriver but much of it is pertinent to a KMDF based Frameworks driver also. All HID minidriver must register with the HID class driver, and the HID class driver communicates with the minidriver by calling the minidriver's standard driver routines.

For more information about the functionality that a HID minidriver must support in its standard driver routines, see the following topics:

-   Registering a HID Minidriver
-   HID Minidriver Driver Extension
-   Using the HID\_DEVICE\_EXTENSION Structure
-   Standard Driver Routines Provided by a HID Minidriver

For more information about the HID class driver, see Operation of the HID Class Driver

### Registering a HID minidriver

After a HID minidriver completes all other driver initialization in its [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine, the HID minidriver binds its operation to the HID class driver by calling [**HidRegisterMinidriver**](https://msdn.microsoft.com/library/windows/hardware/ff539835).

When the HID minidriver registers with the HID class driver, it uses a [**HID\_MINIDRIVER\_REGISTRATION**](https://msdn.microsoft.com/library/windows/hardware/ff539929) structure to specify the following: HID revision, the HID minidriver driver object, the size of a HID minidriver device extension, and whether devices are polled or not.

### HID minidriver extension

A HID minidriver device extension is device-specific, and is only used by a HID minidriver. The HID class driver allocates the memory for the minidriver device extension when the class driver creates its device extension for a functional device object ([*FDO*](https://msdn.microsoft.com/library/windows/hardware/ff556280#wdkgloss-fdo)). The HID minidriver specifies the size of its device extension when it registers the minidriver with the HID class driver. The size is specified by the **DeviceExtensionSize** member of a [**HID\_MINIDRIVER\_REGISTRATION**](https://msdn.microsoft.com/library/windows/hardware/ff539929) structure.

### <a href="" id="using-the-hid-device-extension-structure"></a>Using the HID\_DEVICE\_EXTENSION structure

A HID minidriver must use a [**HID\_DEVICE\_EXTENSION**](https://msdn.microsoft.com/library/windows/hardware/ff539896) structure as the layout for the device extension created by the HID class driver for a functional device object ([*FDO*](https://msdn.microsoft.com/library/windows/hardware/ff556280#wdkgloss-fdo)). The HID class driver sets the members of this structure when it initializes the FDO. A HID minidriver must not change the information in this structure.

A HID\_DEVICE\_EXTENSION structure contains the following members:

-   **PhysicalDeviceObject** is a pointer to the physical device object (PDO) that represents the underlying input device.

-   **NextDeviceObject** is a pointer to the top of the device stack beneath the FDO.

-   **MiniDeviceExtension** is a pointer to the HID minidriver device extension.

Given a pointer to the FDO of an input device, the following GET\_MINIDRIVER\_DEVICE\_EXTENSION macro returns a pointer to a HID minidriver extension:

```cpp
#define GET_MINIDRIVER_DEVICE_EXTENSION(DO) ((PDEVICE_EXTENSION) (((PHID_DEVICE_EXTENSION)(DO)->DeviceExtension)->MiniDeviceExtension))
```

PDEVICE\_EXTENSION is a pointer to a device-specific device extension declared by a HID minidriver.

Similarly, a HID minidriver can obtain a pointer to the input device's PDO and the top of the device stack beneath the input device's FDO.

When a HID minidriver sends an IRP down the device stack, it should use **NextDeviceObject** as the target device object.

### Standard minidriver routines

A HID minidriver must provide the following standard driver support routines:

-   HID Minidriver DriverEntry Routine
-   HID Minidriver AddDevice Routine
-   HID Minidriver Unload Routine

A HID minidriver must also support the dispatch routines described in Dispatch Routines Provided by a HID Minidriver.

### DriverEntry routine

The [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine in a HID minidriver does the following:

-   Creates a driver object for the linked pair of drivers (HID class driver and a HID minidriver).

-   Sets the required driver entry points in the HID minidriver driver object.

-   Calls [**HidRegisterMinidriver**](https://msdn.microsoft.com/library/windows/hardware/ff539835) to register the HID minidriver with the HID class driver.

-   Does device-specific configurations that are only used by the HID minidriver.

### AddDevice routine

The HID class driver handles creating and initializing the functional device object ([*FDO*](https://msdn.microsoft.com/library/windows/hardware/ff556280#wdkgloss-fdo)) for an underlying input device. The HID class driver also operates the FDO from the perspective of the upper-level interface to the underlying device and its child devices (HID collections).

The HID class driver [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine calls the HID minidriver *AddDevice* routine so that the minidriver can do internal device-specific initialization.

The parameters that are passed to the HID minidriver [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine are the minidriver driver object and the FDO. (Note that the HID class driver passes the FDO to the minidriver *AddDevice* routine, not to the physical device object for the underlying input device.)

The HID minidriver [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine obtains a pointer to the minidriver device extension from the FDO.

-   Typically, the HID minidriver [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine does the following:

-   Initializes the minidriver device extension. The device extension is only used by the minidriver.

-   Returns STATUS\_SUCCESS. If the minidriver returns an error status, the HID class driver deletes the FDO and returns the error status to the Plug and Play manager.

### Unload routine

The Unload routine of the HID class driver calls the HID minidriver Unload routine. A HID minidriver releases any internal resources allocated by the minidriver.

### Dispatch routines

A HID minidriver must supply the following dispatch routines: create, close, internal device control, system control, Plug and Play, and power management. Except for internal device control requests, most of these dispatch routines provide minimal function. When the HID class driver calls these dispatch routines, it passes the minidriver driver object and the functional device object ([*FDO*](https://msdn.microsoft.com/library/windows/hardware/ff556280#wdkgloss-fdo)).

### <a href="" id="irp-mj-create"></a>IRP\_MJ\_CREATE

In compliance with WDM requirements, the HID class driver and a HID minidriver provide a dispatch routine for create requests. However, the FDO cannot be opened. The HID class driver returns STATUS\_UNSUCCESSFUL.

A HID minidriver only needs to provide a stub. The create dispatch routine is never called.

### <a href="" id="irp-mj-close"></a>IRP\_MJ\_CLOSE

In compliance with WDM requirements, the HID class driver and a HID minidriver must provide a dispatch routine for close requests. However, the FDO cannot be opened. The HID class driver returns STATUS\_INVALID\_PARAMETER\_1.

A HID minidriver only needs to provide a stub. The close dispatch routine is never called.

### <a href="" id="irp-mj-device-control"></a>IRP\_MJ\_DEVICE\_CONTROL

A HID minidriver does not need a dispatch routine for device control requests. The HID class driver does not pass device control requests to a minidriver.

### <a href="" id="irp-mj-internal-device-control"></a>IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL

A HID minidriver must provide a dispatch routine for internal device control requests that supports the requests described in [HID MinidriverIOCTLs](https://msdn.microsoft.com/library/windows/hardware/ff539926).

The HID class driver primarily uses internal device control requests to access the underlying input device.

The HID minidriver handles these requests in a device-specific way.

### <a href="" id="irp-mj-system-control"></a>IRP\_MJ\_SYSTEM\_CONTROL

A HID minidriver must provide a dispatch routine for system control requests. However, a HID minidriver is only required to pass system control requests down the device stack as follows:

-   Skip the current IRP stack location

-   Send the request down the FDO's device stack

### <a href="" id="irp-mj-pnp"></a>IRP\_MJ\_PNP

A HID minidriver must supply a dispatch routine for Plug and Play requests.

The HID class driver does all the Plug and Play processing associated with the FDO. When the HID class driver processes a Plug and Play request, it calls the HID minidriver Plug and Play dispatch routine.

A HID minidriver Plug and Play dispatch routine does the following:

-   Handles sending the request down the FDO's device stack and completing the request on the way back up the device stack, as appropriate for each type of request.

-   Does device-specific processing associated with certain requests to update information about the state of the FDO.

    For example, the minidriver might update the Plug and Play state of the FDO (in particular, whether the FDO is started, stopped, or in the process of being removed).

### <a href="" id="irp-mj-power"></a>IRP\_MJ\_POWER

The HID minidriver must supply a dispatch routine for power requests. However, the HID class driver handles the power processing for the FDO.

In compliance with WDM requirements, a HID minidriver sends power requests down the FDO's device stack in the following way:

-   Skips the current IRP stack location

-   Starts the next power IRP

-   Sends the power IRP down the FDO's device stack

Typically, the HID minidriver passes power requests down the device stack without additional processing.

 

 




