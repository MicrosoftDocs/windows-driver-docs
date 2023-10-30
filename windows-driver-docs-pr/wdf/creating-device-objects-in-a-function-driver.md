---
title: Creating Device Objects in a Function Driver
description: Creating Device Objects in a Function Driver
keywords:
- PnP WDK KMDF , function drivers
- Plug and Play WDK KMDF , function drivers
- power management WDK KMDF , function drivers
- function drivers WDK KMDF
- functional device objects WDK KMDF
- FDOs WDK KMDF
ms.date: 04/20/2017
---

# Creating Device Objects in a Function Driver


Each [function driver](../kernel/function-drivers.md) creates a framework device object for each of its supported devices that exists on the system. Because these device objects are created by function drivers, they are called functional device objects (FDOs). Each FDO is a function driver's representation of a device.

A function driver must create a framework device object each time the framework calls the driver's [*EvtDriverDeviceAdd*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) callback function. The framework calls this callback function to inform the driver that one of its supported devices exists on the system.

The driver's [*EvtDriverDeviceAdd*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) callback function receives a pointer to a [**WDFDEVICE\_INIT**](./wdfdevice_init.md) structure. The driver can call a set of [framework device object initialization methods](/windows-hardware/drivers/ddi/wdfdevice/#device-init-methods), which store information in the WDFDEVICE\_INIT structure. Additionally, function drivers can call [framework FDO initialization methods](/windows-hardware/drivers/ddi/wdfdevice/#fdo-init-methods).

Creating a framework device object in a function driver typically includes the following steps:

-   Registering PnP, power, and power policy callback functions.

    Most function drivers call [**WdfDeviceInitSetPnpPowerEventCallbacks**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetpnppowereventcallbacks) to register PnP and power callback functions. For more information about these callback functions, see [Supporting PnP and Power Management in Function Drivers](supporting-pnp-and-power-management-in-function-drivers.md).

    If the device supports low-power idle or has wake-up capabilities, the function driver typically also calls [**WdfDeviceInitSetPowerPolicyEventCallbacks**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetpowerpolicyeventcallbacks) to register power policy callback functions. For more information about these callback functions, see [Power Policy Ownership](power-policy-ownership.md).

-   Registering function driver-specific callback functions.

    Some function drivers call [**WdfFdoInitSetEventCallbacks**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoinitseteventcallbacks), if they must participate in specifying the system hardware resources that a device requires. For more information about hardware resources, see [Hardware Resources for Framework-Based Drivers](./introduction-to-hardware-resources.md).

-   Registering file event callback functions.

    If your driver must respond when an application opens or closes a file on a device, the driver must call [**WdfDeviceInitSetFileObjectConfig**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetfileobjectconfig) to register callback functions for the framework file object. For more information, see [Using Framework File Objects](framework-file-objects.md).

-   Setting I/O request attributes.

    If your driver will receive I/O requests from framework queue objects, the driver can call [**WdfDeviceInitSetRequestAttributes**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetrequestattributes) to set up context memory that the framework will assign to a device's request objects. For more information, see [Using Request Object Context](using-request-object-context.md).

-   Setting device characteristics.

    Typically, a function driver calls some of the following methods to specify a device's characteristics:

    -   [**WdfDeviceInitSetDeviceType**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetdevicetype), to identify the type of hardware that the driver supports.
    -   [**WdfDeviceInitSetIoType**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetiotype), to identify a method for accessing data buffers, if the driver handles I/O requests from applications.
    -   [**WdfDeviceInitSetCharacteristics**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetcharacteristics), to set device characteristics, such as whether the device is read-only or supports removable media.
    -   [**WdfDeviceInitSetExclusive**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetexclusive), if the device requires exclusive access by one application at a time.
    -   [**WdfDeviceInitSetPowerInrush**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetpowerinrush), if the device requires an inrush of current when it transitions from a low-power state to its working (D0) state.
    -   [**WdfDeviceInitSetPowerPageable**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetpowerpageable) or [**WdfDeviceInitSetPowerNotPageable**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetpowernotpageable), to indicate whether the driver must access pageable data while the system is transitioning between a sleeping state and the working (S0) state.
    -   [**WdfDeviceInitAssignName**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitassignname), to assign a name to the device object.
    -   [**WdfDeviceInitAssignSDDLString**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitassignsddlstring), to assign a security descriptor to the device object.
    -   [**WdfDeviceInitSetDeviceClass**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetdeviceclass), to identify the device's setup class.
-   Obtaining device properties.

    Sometimes function drivers must obtain information about the device properties that the driver for the device's bus, or other lower-level driver, has set. The driver can call [**WdfFdoInitQueryProperty**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoinitqueryproperty) or [**WdfFdoInitAllocAndQueryProperty**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoinitallocandqueryproperty) to obtain this information. New drivers targeting Windows 8.1 and later can call [**WdfFdoInitQueryPropertyEx**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoinitquerypropertyex) and [**WdfFdoInitAllocAndQueryPropertyEx**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoinitallocandquerypropertyex).

-   Accessing the device's registry key.

    Some function drivers must obtain information about the device or driver that another driver, a user, or an installation package has placed in the registry. The driver can call [**WdfFdoInitOpenRegistryKey**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoinitopenregistrykey) to open the device or driver's registry key. For more information, see [Using the Registry in Framework-Based Drivers](./introduction-to-registry-keys-for-drivers.md).

-   Creating a default child list configuration to use for dynamic enumeration.

    If you are writing a function driver for a bus, and if your driver will perform dynamic enumeration of child devices that are connected to the bus, the driver must call [**WdfFdoInitSetDefaultChildListConfig**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoinitsetdefaultchildlistconfig). For more information, see [Enumerating the Devices on a Bus](enumerating-the-devices-on-a-bus.md).

-   Creating the device object.

    The final step in creating a device object is to call [**WdfDeviceCreate**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicecreate).