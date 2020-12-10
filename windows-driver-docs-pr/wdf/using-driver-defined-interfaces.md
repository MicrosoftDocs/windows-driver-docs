---
title: Using Driver-Defined Interfaces
description: Using Driver-Defined Interfaces
keywords:
- driver-defined interfaces WDK KMDF
- interfaces WDK KMDF
- one-way communication WDK KMDF
- two-way communication WDK KMDF
- reference counts WDK KMDF
- reference functions WDK KMDF
- dereference functions WDK KMDF
- no-op functions WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using Driver-Defined Interfaces


Drivers can define device-specific interfaces that other drivers can access. These *driver-defined interfaces* can consist of a set of callable routines, a set of data structures, or both. The driver typically provides pointers to these routines and structures in a driver-defined interface structure, which the driver makes available to other drivers.

For example, a bus driver might provide one or more routines that higher-level drivers can call to obtain information about a child device, if that information is not available in the child device's resource list.

For an example of a set of driver-defined interfaces that are documented in the WDK, see [USB Routines](/previous-versions/windows/hardware/drivers/ff540046(v=vs.85)). Also, see the framework-based version of the [toaster](sample-kmdf-drivers.md) sample.

### Creating an Interface

Each driver-defined interface is specified by:

-   A GUID

-   A version number

-   A driver-defined interface structure

-   Reference and dereference routines

To create an interface and make it available to other drivers, framework-based drivers can use the following steps:

1.  Define an interface structure.

    The first member of this driver-defined structure must be an [**INTERFACE**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_interface) header structure. Additional members might include interface data and pointers to additional structures or routines that anther driver can call.

    Your driver must provide a [**WDF\_QUERY\_INTERFACE\_CONFIG**](/windows-hardware/drivers/ddi/wdfqueryinterface/ns-wdfqueryinterface-_wdf_query_interface_config) structure, which describes the interface that you have defined.

2.  Call [**WdfDeviceAddQueryInterface**](/windows-hardware/drivers/ddi/wdfqueryinterface/nf-wdfqueryinterface-wdfdeviceaddqueryinterface).

    The [**WdfDeviceAddQueryInterface**](/windows-hardware/drivers/ddi/wdfqueryinterface/nf-wdfqueryinterface-wdfdeviceaddqueryinterface) method does the following:

    -   Stores information about the interface, such as its GUID, version number, and structure size, so the framework can recognize another driver's request for the interface.
    -   Registers an optional [*EvtDeviceProcessQueryInterfaceRequest*](/windows-hardware/drivers/ddi/wdfqueryinterface/nc-wdfqueryinterface-evt_wdf_device_process_query_interface_request) event callback function, which the framework calls when another driver asks for the interface.

Each instance of a driver-defined interface is associated with an individual device, so drivers typically call [**WdfDeviceAddQueryInterface**](/windows-hardware/drivers/ddi/wdfqueryinterface/nf-wdfqueryinterface-wdfdeviceaddqueryinterface) from within an [*EvtDriverDeviceAdd*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) or [*EvtChildListCreateDevice*](/windows-hardware/drivers/ddi/wdfchildlist/nc-wdfchildlist-evt_wdf_child_list_create_device) callback function.

### Accessing an Interface

If your driver has defined an interface, another framework-based driver can request access to the interface by calling [**WdfFdoQueryForInterface**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoqueryforinterface) and passing a GUID, version number, pointer to a structure, and the structure size. The framework creates an I/O request and sends it to the top of the driver stack.

A driver typically calls [**WdfFdoQueryForInterface**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoqueryforinterface) from within an [*EvtDriverDeviceAdd*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) callback function. Alternatively, if the driver must release the interface when the device is not in its working state, the driver can call **WdfFdoQueryForInterface** from within an [*EvtDevicePrepareHardware*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_prepare_hardware) callback function and call the interface's dereference routine from within an [*EvtDeviceReleaseHardware*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_release_hardware) callback function.

If driver A asks driver B for an interface that driver B has defined, the framework handles the request for driver B. The framework verifies that the GUID and version represent a supported interface, and that the structure size that driver A supplied is large enough to hold the interface.

When a driver calls [**WdfFdoQueryForInterface**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoqueryforinterface), the I/O request that the framework creates travels all the way to the bottom of the driver stack. If a simple driver stack consists of three drivers - A, B, and C - and if driver A asks for an interface, both driver B and driver C can support the interface. For example, driver B might fill in driver A's interface structure before passing the request down to driver C. Driver C can provide an [*EvtDeviceProcessQueryInterfaceRequest*](/windows-hardware/drivers/ddi/wdfqueryinterface/nc-wdfqueryinterface-evt_wdf_device_process_query_interface_request) callback function that examines the interface structure's contents and possibly modifies them.

If driver A needs to access driver B's interface, and driver B is a remote I/O target (that is, a driver that is in a different driver stack), driver A must call [**WdfIoTargetQueryForInterface**](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetqueryforinterface) instead of [**WdfFdoQueryForInterface**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoqueryforinterface).

### Using One-Way or Two-Way Communication

You can define an interface that provides one-way communication, or one that provides two-way communication. To specify two-way communication, your driver sets the **ImportInterface** member of its [**WDF\_QUERY\_INTERFACE\_CONFIG**](/windows-hardware/drivers/ddi/wdfqueryinterface/ns-wdfqueryinterface-_wdf_query_interface_config) structure to **TRUE**.

If the interface provides one-way communication, and if driver A asks for driver B's interface, interface data flows only from driver B to driver A. When the framework receives driver A's request for an interface that supports one-way communication, the framework copies the driver-defined interface values into the driver A's interface structure. It then calls driver B's [*EvtDeviceProcessQueryInterfaceRequest*](/windows-hardware/drivers/ddi/wdfqueryinterface/nc-wdfqueryinterface-evt_wdf_device_process_query_interface_request) callback function, if it exists, so it can examine and possibly modify the interface values.

If the interface provides two-way communication, the interface structure contains some members that driver A fills in before sending the request to driver B. Driver B can read the parameter values that driver A provided and make choices, based on those values, about which information to supply to driver A. When the framework receives driver A's request for an interface that supports two-way communication, the framework calls driver B's [*EvtDeviceProcessQueryInterfaceRequest*](/windows-hardware/drivers/ddi/wdfqueryinterface/nc-wdfqueryinterface-evt_wdf_device_process_query_interface_request) callback function so that it can examine received values and supply output values. For two-way communication, the callback function is required because the framework does not copy any interface values to driver A's interface structure.

### Maintaining a Reference Count

Each interface must include a reference function and a dereference function, which increment and decrement a reference count for the interface. The driver that defines the interface specifies the addresses of these functions in its [**INTERFACE**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_interface) structure.

When driver A asks driver B for an interface, the framework calls the interface's reference function before making the interface available to driver A. When driver A has finished using the interface, it must call the interface's dereference function.

The reference and dereference functions for most interfaces can be no-op functions that do nothing. The framework provides no-op reference count functions, [**WdfDeviceInterfaceReferenceNoOp**](/windows-hardware/drivers/ddi/wdfqueryinterface/nf-wdfqueryinterface-wdfdeviceinterfacereferencenoop) and [**WdfDeviceInterfaceDereferenceNoOp**](/windows-hardware/drivers/ddi/wdfqueryinterface/nf-wdfqueryinterface-wdfdeviceinterfacedereferencenoop), that most drivers can use.

The only time that drivers must keep track of an interface's reference count, and provide real reference and dereference functions, is when driver A requests an interface from a remote I/O target (that is, a driver that is in a different driver stack). In this case, driver B (in a different stack) must implement a reference count so that it can prevent its device from being removed while driver A is using driver B's interface.

If you are designing driver B, which defines an interface, you must decide whether your driver's interface will be accessed from a different driver stack. (Driver B cannot determine if a request for its interface is from the local driver stack or from a remote stack.) If your driver will support interface requests from a remote stack, the driver must implement a reference count.

If you are designing driver A, which accesses the interface on the remote I/O target, the driver must provide an [*EvtIoTargetQueryRemove*](/windows-hardware/drivers/ddi/wdfiotarget/nc-wdfiotarget-evt_wdf_io_target_query_remove) callback function that releases the interface when driver B's device is about to be removed, an [*EvtIoTargetRemoveComplete*](/windows-hardware/drivers/ddi/wdfiotarget/nc-wdfiotarget-evt_wdf_io_target_remove_complete) callback function that releases the interface when driver B's device is surprise-removed, and an [*EvtIoTargetRemoveCanceled*](/windows-hardware/drivers/ddi/wdfiotarget/nc-wdfiotarget-evt_wdf_io_target_remove_canceled) callback function that reacquires the interface if an attempt to remove the device was canceled.

 

