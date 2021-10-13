---
title: Creating Device Objects in a Bus Driver
description: Creating Device Objects in a Bus Driver
keywords:
- PnP WDK KMDF , bus drivers
- Plug and Play WDK KMDF , bus drivers
- power management WDK KMDF , bus drivers
- bus drivers WDK KMDF
- physical device objects WDK KMDF
- PDOs WDK KMDF
- bus enumeration WDK KMDF
- enumeration WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating Device Objects in a Bus Driver


Each [bus driver](../kernel/bus-drivers.md) must create a framework device object when it discovers that a child device is connected to a parent device. The parent device is typically a bus, but it can also be a multifunction device for which each function requires a separate set of drivers (such as a sound card that supports digital audio and MIDI). The device objects that bus drivers create are called physical device objects (PDOs) because each represents an actual connection of one piece of hardware (the child) to another (the parent).

The process of identifying and reporting the devices that are connected to a bus is called *bus enumeration*.

-   If a bus driver performs [dynamic bus enumeration](dynamic-enumeration.md), its [*EvtChildListCreateDevice*](/windows-hardware/drivers/ddi/wdfchildlist/nc-wdfchildlist-evt_wdf_child_list_create_device) callback function receives a handle to a [**WDFDEVICE\_INIT**](./wdfdevice_init.md) structure.

-   If a bus driver performs [static bus enumeration](static-enumeration.md), it must call [**WdfPdoInitAllocate**](/windows-hardware/drivers/ddi/wdfpdo/nf-wdfpdo-wdfpdoinitallocate) to obtain a handle to a WDFDEVICE\_INIT structure.

For more information about bus enumeration, see [Enumerating the Devices on a Bus](enumerating-the-devices-on-a-bus.md).

A bus driver can call a set of [framework device object initialization methods](/windows-hardware/drivers/ddi/wdfdevice/#device-init-methods), which store information in the [**WDFDEVICE\_INIT**](./wdfdevice_init.md) structure. Additionally, bus drivers can call [framework PDO initialization methods](/windows-hardware/drivers/ddi/wdfdevice/#pdo-init-methods).

Creating a framework device object for an enumerated child device typically includes the following steps:

-   Registering bus driver-specific callback functions.

    Most bus drivers call [**WdfPdoInitSetEventCallbacks**](/windows-hardware/drivers/ddi/wdfpdo/nf-wdfpdo-wdfpdoinitseteventcallbacks), because they must specify the system hardware resources that a device requires. For more information about specifying hardware resources, see [Hardware Resources for Framework-Based Drivers](hardware-resources-for-kmdf-drivers.md). Additional callback functions can be registered if the device and driver support ejection.

-   Reporting [device identification strings](../install/device-identification-strings.md).

    Bus drivers must report the device's identification strings by calling [**WdfPdoInitAssignDeviceID**](/windows-hardware/drivers/ddi/wdfpdo/nf-wdfpdo-wdfpdoinitassigndeviceid), [**WdfPdoInitAssignInstanceID**](/windows-hardware/drivers/ddi/wdfpdo/nf-wdfpdo-wdfpdoinitassigninstanceid), [**WdfPdoInitAddCompatibleID**](/windows-hardware/drivers/ddi/wdfpdo/nf-wdfpdo-wdfpdoinitaddcompatibleid), and [**WdfPdoInitAddHardwareID**](/windows-hardware/drivers/ddi/wdfpdo/nf-wdfpdo-wdfpdoinitaddhardwareid) for each type of string that the device supports. In addition, bus drivers that use version 1.9 or later of the framework can call [**WdfPdoInitAssignContainerID**](/windows-hardware/drivers/ddi/wdfpdo/nf-wdfpdo-wdfpdoinitassigncontainerid).

-   Reporting whether the bus driver can support the device in raw mode.

    If the bus driver supports raw mode for the device, it must call [**WdfPdoInitAssignRawDevice**](/windows-hardware/drivers/ddi/wdfpdo/nf-wdfpdo-wdfpdoinitassignrawdevice).

-   Providing displayable text that describes the device.

    Bus drivers call [**WdfPdoInitAddDeviceText**](/windows-hardware/drivers/ddi/wdfpdo/nf-wdfpdo-wdfpdoinitadddevicetext) and [**WdfPdoInitSetDefaultLocale**](/windows-hardware/drivers/ddi/wdfpdo/nf-wdfpdo-wdfpdoinitsetdefaultlocale) to provide text that describes the device to users, in multiple languages.

-   Creating the device object.

    The final step in creating a device object is to call [**WdfDeviceCreate**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicecreate).

If the driver encounters an error while initializing the WDFDEVICE\_INIT structure that it obtained from [**WdfPdoInitAllocate**](/windows-hardware/drivers/ddi/wdfpdo/nf-wdfpdo-wdfpdoinitallocate), the driver must call [**WdfDeviceInitFree**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitfree) instead of [**WdfDeviceCreate**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicecreate).

After the bus driver has created the device object, it typically calls [**WdfDeviceSetPnpCapabilities**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicesetpnpcapabilities) and [**WdfDeviceSetPowerCapabilities**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicesetpowercapabilities) to report the device's Plug and Play and power capabilities.

Each bus driver is also the function driver for the bus adapter. Therefore, the driver must also provide an [*EvtDriverDeviceAdd*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) callback function. This callback function creates a functional device object (FDO) for each bus adapter on the system. For more information about creating FDOs, see [Creating Device Objects in a Function Driver](creating-device-objects-in-a-function-driver.md).

 

