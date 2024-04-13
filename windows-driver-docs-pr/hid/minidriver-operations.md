---
title: Minidrivers and the HID Class Driver
description: Minidrivers and the HID class driver
ms.date: 01/11/2024
---

# Minidrivers and the HID class driver

This article describes minidrivers and the HID class driver.

For more information, see [Creating WDF HID minidrivers](../wdf/creating-umdf-hid-minidrivers.md).

## Operational features of the HID class driver

The HID class driver does the following operations:

- Provides and manages the upper-level interface that kernel-mode drivers and user-mode applications use to access the [HID collections](hid-collections.md) that an input device supports.

    The HID class driver transparently manages and routes all communication between upper-level drivers and applications and the underlying input devices that support HID collections. It manages the different data protocols that are used by different input devices and input queues that support more than one open file on the same HID collection.

    The upper-level interface to HID collections consists of the [HID class driver IOCTLs](/windows-hardware/drivers/ddi/_hid/#hid-class-driver-ioctls), the [HIDClass support routines](/windows-hardware/drivers/ddi/_hid/#hidclass-support-routines), and the [HIDClass structures](/windows-hardware/drivers/ddi/_hid/#structures).

- Communicates with a HID minidriver by calling the minidriver's standard driver routines.

- Creates a functional device object (*FDO*) for HIDClass input devices enumerated by a lower-level bus or port driver.

    For example, the HID class driver creates and manages the operations of an FDO that represents a USB HID device enumerated by the system-supplied USB driver stack.

- Provides the functionality of a bus driver for the child devices (HID collections) supported by an underlying input device.

    The HID class driver creates a physical device object (*PDO*) for each HID collection supported by an input device and manages the collection's operation.

## Binding a minidriver to HIDClass

A HID minidriver binds its operation to the HID class driver by calling **[HidRegisterMinidriver](/windows-hardware/drivers/ddi/hidport/nf-hidport-hidregisterminidriver)** to register itself with the HID class driver. The registration operation:

- Saves a copy of the entry points (pointers) to the HID minidriver's standard driver routines in the HID class driver's device extension.

    A HID minidriver sets its entry points in the driver object that the minidriver receives as input to its **[DRIVER_INITIALIZE](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize)** routine. The HID minidriver sets these entry points before it registers with the HID class driver.

- Resets the entry points in the minidriver's driver object to the entry points for the standard driver routines supplied by the HID class driver.

The HID class driver supplies the following standard driver routines:

- **[DRIVER_ADD_DEVICE](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device)** and **[DRIVER_UNLOAD](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_unload)** routines

- Dispatch routines for the following I/O requests:

    **[IRP_MJ_CREATE](../kernel/irp-mj-create.md)**

    **[IRP_MJ_CLOSE](../kernel/irp-mj-close.md)**

    **[IRP_MJ_DEVICE_CONTROL](../kernel/irp-mj-device-control.md)**

    **[IRP_MJ_INTERNAL_DEVICE_CONTROL](../kernel/irp-mj-internal-device-control.md)**

    **[IRP_MJ_PNP](../kernel/irp-mj-pnp.md)**

    **[IRP_MJ_SYSTEM_CONTROL](../kernel/irp-mj-system-control.md)**

The registration process also allocates memory for the HID mind river device extension. Although the memory is allocated by the HID class driver, only the HID minidriver uses this device extension.

## Communicating with a HID minidriver

The HID class driver communicates with a HID minidriver by calling the HID minidriver's **[DRIVER_ADD_DEVICE](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device)**, **[DRIVER_UNLOAD](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_unload)**, and dispatch routines as follows:

### Calling the AddDevice routine

When the HID class driver's **AddDevice** routine is called to create a functional device object (*FDO*), the HID class driver creates the FDO, initializes it, and calls the HID minidriver **AddDevice** routine. The HID minidriver **AddDevice** routine does internal device-specific initialization and, if successful, returns STATUS_SUCCESS. If the HID minidriver **AddDevice** routine isn't successful, the HID class driver deletes the FDO and returns the status returned by the HID minidriver **AddDevice** routine.

### Calling the Unload routine

When the HID class driver **Unload** routine is called, the HID class driver completes releasing all resources associated with FDO and calls the HID minidriver's **Unload** routine.

### Calling the Dispatch routines

To operate a device, the HID class driver primarily calls the HID minidriver dispatch routine for internal device control requests.

When the I/O manager sends requests to the HID class driver, the HID class driver processes the request, and calls the HID minidriver's corresponding dispatch routine.

The HID class driver doesn't send the following requests to the HID minidriver: create, close, or device control.

## Operation of a HID minidriver

A HID transport minidriver abstracts the operation of a hardware bus or port that your input device attaches to.

HID minidrivers can be built using one of the following frameworks:

- UMDF – User Mode Driver Framework
- KDMF – Kernel Mode Driver Framework
- WDF - Windows Driver Framework
- WDM – Windows Driver Model (legacy)

Microsoft recommends using a Frameworks based solution (KMDF or UMDF). For more information on each of the driver models, visit the following sections:

- KMDF-based HID minidriver, see Creating Framework-based HID Minidrivers
- UMDF-based HID minidriver, see [Creating WDF HID Minidrivers](../wdf/creating-umdf-hid-minidrivers.md)

The following section talks about registering a WDM based HID minidriver but much of it's pertinent to a KMDF based Frameworks driver also. All HID minidriver must register with the HID class driver, and the HID class driver communicates with the minidriver by calling the minidriver's standard driver routines.

For more information about the functionality that a HID minidriver must support in its standard driver routines, see the following sections:

- [Registering a HID minidriver](#registering-a-hid-minidriver)
- [HID minidriver extension](#hid-minidriver-extension)
- [Using the HID_DEVICE_EXTENSION structure](#using-the-hid_device_extension-structure)
- [Standard minidriver routines](#standard-minidriver-routines)

For more information about the HID class driver, see [Operation of the HID minidriver](#operation-of-a-hid-minidriver).

## Registering a HID minidriver

After a HID minidriver completes all other driver initialization in its **[DRIVER_INITIALIZE](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize)** routine, the HID minidriver binds its operation to the HID class driver by calling **[HidRegisterMinidriver](/windows-hardware/drivers/ddi/hidport/nf-hidport-hidregisterminidriver)**.

When the HID minidriver registers with the HID class driver, it uses a **[HID_MINIDRIVER_REGISTRATION](/windows-hardware/drivers/ddi/hidport/ns-hidport-_hid_minidriver_registration)** structure. The structure specifies:

- The HID revision
- The HID minidriver driver object
- The size of a HID minidriver device extension
- Whether devices are polled

## HID minidriver extension

A HID minidriver device extension is device-specific, and is only used by a HID minidriver. The HID class driver allocates the memory for the minidriver device extension when the class driver creates its device extension for a functional device object (*FDO*). The HID minidriver specifies the size of its device extension when it registers the minidriver with the HID class driver. The size is specified by the **DeviceExtensionSize** member of a **[HID_MINIDRIVER_REGISTRATION](/windows-hardware/drivers/ddi/hidport/ns-hidport-_hid_minidriver_registration)** structure.

### Using the HID_DEVICE_EXTENSION structure

A HID minidriver must use a **[HID_DEVICE_EXTENSION](/windows-hardware/drivers/ddi/hidport/ns-hidport-_hid_device_extension)** structure as the layout for the device extension created by the HID class driver for a functional device object (*FDO*). The HID class driver sets the members of this structure when it initializes the FDO. A HID minidriver must not change the information in this structure.

A HID_DEVICE_EXTENSION structure contains the following members:

- **PhysicalDeviceObject** is a pointer to the physical device object (PDO) that represents the underlying input device.

- **NextDeviceObject** is a pointer to the top of the device stack beneath the FDO.

- **MiniDeviceExtension** is a pointer to the HID minidriver device extension.

Given a pointer to the FDO of an input device, the following GET_MINIDRIVER_DEVICE_EXTENSION macro returns a pointer to a HID minidriver extension:

```cpp
#define GET_MINIDRIVER_DEVICE_EXTENSION(DO) ((PDEVICE_EXTENSION) (((PHID_DEVICE_EXTENSION)(DO)->DeviceExtension)->MiniDeviceExtension))
```

PDEVICE_EXTENSION is a pointer to a device-specific device extension declared by a HID minidriver.

Similarly, a HID minidriver can obtain a pointer to the input device's PDO and the top of the device stack beneath the input device's FDO.

When a HID minidriver sends an IRP down the device stack, it should use **NextDeviceObject** as the target device object.

## Standard minidriver routines

A HID minidriver must provide the following standard driver support routines:

- HID minidriver DriverEntry routine
- HID minidriver AddDevice routine
- HID minidriver Unload routine

A HID minidriver must also support the dispatch routines described in Dispatch routines Provided by a HID minidriver.

### DriverEntry routine

The **[DRIVER_INITIALIZE](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize)** routine in a HID minidriver does the following:

- Creates a driver object for the linked pair of drivers (HID class driver and a HID minidriver).

- Sets the required driver entry points in the HID minidriver driver object.

- Calls **[HidRegisterMinidriver](/windows-hardware/drivers/ddi/hidport/nf-hidport-hidregisterminidriver)** to register the HID minidriver with the HID class driver.

- Does device-specific configurations that are only used by the HID minidriver.

### AddDevice routine

The HID class driver handles creating and initializing the functional device object (*FDO*) for an underlying input device. The HID class driver also operates the FDO from the perspective of the upper-level interface to the underlying device and its child devices (HID collections).

The HID class driver **[DRIVER_ADD_DEVICE](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device)** routine calls the HID minidriver *AddDevice* routine so that the minidriver can do internal device-specific initialization.

The parameters that are passed to the HID minidriver **[DRIVER_ADD_DEVICE](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device)** routine are the minidriver driver object and the FDO. The HID class driver passes the FDO to the minidriver *AddDevice* routine, not to the physical device object for the underlying input device.

The HID minidriver **[DRIVER_ADD_DEVICE](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device)** routine obtains a pointer to the minidriver device extension from the FDO.

- Typically, the HID minidriver **[DRIVER_ADD_DEVICE](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device)** routine does the following:

- Initializes the minidriver device extension. The device extension is only used by the minidriver.

- Returns STATUS_SUCCESS. If the minidriver returns an error status, the HID class driver deletes the FDO and returns the error status to the Plug and Play manager.

### Unload routine

The Unload routine of the HID class driver calls the HID minidriver **[DRIVER_UNLOAD](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_unload)** routine. A HID minidriver releases any internal resources allocated by the minidriver.

## Dispatch routines

A HID minidriver must supply the following dispatch routines: create, close, internal device control, system control, Plug and Play, and power management. Except for internal device control requests, most of these dispatch routines provide minimal function. When the HID class driver calls these dispatch routines, it passes the minidriver driver object and the functional device object (*FDO*).

### IRP_MJ_CREATE

In compliance with WDM requirements, the HID class driver and a HID minidriver provide a dispatch routine for create requests. However, the FDO can't be opened. The HID class driver returns STATUS_UNSUCCESSFUL.

A HID minidriver only needs to provide a stub. The create dispatch routine is never called.

### IRP_MJ_CLOSE

In compliance with WDM requirements, the HID class driver and a HID minidriver must provide a dispatch routine for close requests. However, the FDO can't be opened. The HID class driver returns STATUS_INVALID_PARAMETER_1.

A HID minidriver only needs to provide a stub. The close dispatch routine is never called.

### IRP_MJ_DEVICE_CONTROL

A HID minidriver doesn't need a dispatch routine for device control requests. The HID class driver doesn't pass device control requests to a minidriver.

### IRP_MJ_INTERNAL_DEVICE_CONTROL

A HID minidriver must provide a dispatch routine for internal device control requests that supports the requests described in [HID minidriver IOCTLs](/windows-hardware/drivers/ddi/_hid/#hid-minidriver-ioctls).

The HID class driver primarily uses internal device control requests to access the underlying input device.

The HID minidriver handles these requests in a device-specific way.

### IRP_MJ_SYSTEM_CONTROL

A HID minidriver must provide a dispatch routine for system control requests. However, a HID minidriver is only required to pass system control requests down the device stack as follows:

- Skip the current IRP stack location

- Send the request down the FDO's device stack

### IRP_MJ_PNP

A HID minidriver must supply a dispatch routine for Plug and Play requests.

The HID class driver does all the Plug and Play processing associated with the FDO. When the HID class driver processes a Plug and Play request, it calls the HID minidriver's Plug and Play dispatch routine.

A HID minidriver Plug and Play dispatch routine:

- Handles sending the request down the FDO's device stack and completing the request on the way backup the device stack, as appropriate for each type of request.

- Does device-specific processing associated with certain requests to update information about the state of the FDO.

    For example, the minidriver might update the Plug and Play state of the FDO (in particular, whether the FDO is started, stopped, or in the process of being removed).

### IRP_MJ_POWER

The HID minidriver must supply a dispatch routine for power requests. However, the HID class driver handles the power processing for the FDO.

In compliance with WDM requirements, a HID minidriver sends power requests down the FDO's device stack in this way:

- Skips the current IRP stack location

- Starts the next power IRP

- Sends the power IRP down the FDO's device stack

Typically, the HID minidriver passes power requests down the device stack without extra processing.
