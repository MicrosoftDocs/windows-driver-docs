---
title: Creating Device Objects in a Bus Driver
author: windows-driver-content
description: Creating Device Objects in a Bus Driver
ms.assetid: 36b4d24c-9f5e-4853-bf70-c94613e01f2b
keywords: ["PnP WDK KMDF , bus drivers", "Plug and Play WDK KMDF , bus drivers", "power management WDK KMDF , bus drivers", "bus drivers WDK KMDF", "physical device objects WDK KMDF", "PDOs WDK KMDF", "bus enumeration WDK KMDF", "enumeration WDK KMDF"]
---

# Creating Device Objects in a Bus Driver


Each [bus driver](https://msdn.microsoft.com/library/windows/hardware/ff540704) must create a framework device object when it discovers that a child device is connected to a parent device. The parent device is typically a bus, but it can also be a multifunction device for which each function requires a separate set of drivers (such as a sound card that supports digital audio and MIDI). The device objects that bus drivers create are called physical device objects (PDOs) because each represents an actual connection of one piece of hardware (the child) to another (the parent).

The process of identifying and reporting the devices that are connected to a bus is called *bus enumeration*.

-   If a bus driver performs [dynamic bus enumeration](dynamic-enumeration.md), its [*EvtChildListCreateDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540828) callback function receives a handle to a [**WDFDEVICE\_INIT**](https://msdn.microsoft.com/library/windows/hardware/ff546951) structure.

-   If a bus driver performs [static bus enumeration](static-enumeration.md), it must call [**WdfPdoInitAllocate**](https://msdn.microsoft.com/library/windows/hardware/ff548786) to obtain a handle to a WDFDEVICE\_INIT structure.

For more information about bus enumeration, see [Enumerating the Devices on a Bus](enumerating-the-devices-on-a-bus.md).

A bus driver can call a set of [framework device object initialization methods](https://msdn.microsoft.com/library/windows/hardware/dn265631#device-init-methods), which store information in the [**WDFDEVICE\_INIT**](https://msdn.microsoft.com/library/windows/hardware/ff546951) structure. Additionally, bus drivers can call [framework PDO initialization methods](https://msdn.microsoft.com/library/windows/hardware/dn265631#pdo-init-methods).

Creating a framework device object for an enumerated child device typically includes the following steps:

-   Registering bus driver-specific callback functions.

    Most bus drivers call [**WdfPdoInitSetEventCallbacks**](https://msdn.microsoft.com/library/windows/hardware/ff548805), because they must specify the system hardware resources that a device requires. For more information about specifying hardware resources, see [Hardware Resources for Framework-Based Drivers](hardware-resources-for-kmdf-drivers.md). Additional callback functions can be registered if the device and driver support ejection.

-   Reporting [device identification strings](https://msdn.microsoft.com/library/windows/hardware/ff541224).

    Bus drivers must report the device's identification strings by calling [**WdfPdoInitAssignDeviceID**](https://msdn.microsoft.com/library/windows/hardware/ff548797), [**WdfPdoInitAssignInstanceID**](https://msdn.microsoft.com/library/windows/hardware/ff548799), [**WdfPdoInitAddCompatibleID**](https://msdn.microsoft.com/library/windows/hardware/ff548776), and [**WdfPdoInitAddHardwareID**](https://msdn.microsoft.com/library/windows/hardware/ff548784) for each type of string that the device supports. In addition, bus drivers that use version 1.9 or later of the framework can call [**WdfPdoInitAssignContainerID**](https://msdn.microsoft.com/library/windows/hardware/ff548792).

-   Reporting whether the bus driver can support the device in raw mode.

    If the bus driver supports raw mode for the device, it must call [**WdfPdoInitAssignRawDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548802).

-   Providing displayable text that describes the device.

    Bus drivers call [**WdfPdoInitAddDeviceText**](https://msdn.microsoft.com/library/windows/hardware/ff548780) and [**WdfPdoInitSetDefaultLocale**](https://msdn.microsoft.com/library/windows/hardware/ff548803) to provide text that describes the device to users, in multiple languages.

-   Creating the device object.

    The final step in creating a device object is to call [**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926).

If the driver encounters an error while initializing the WDFDEVICE\_INIT structure that it obtained from [**WdfPdoInitAllocate**](https://msdn.microsoft.com/library/windows/hardware/ff548786), the driver must call [**WdfDeviceInitFree**](https://msdn.microsoft.com/library/windows/hardware/ff546050) instead of [**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926).

After the bus driver has created the device object, it typically calls [**WdfDeviceSetPnpCapabilities**](https://msdn.microsoft.com/library/windows/hardware/ff546898) and [**WdfDeviceSetPowerCapabilities**](https://msdn.microsoft.com/library/windows/hardware/ff546901) to report the device's Plug and Play and power capabilities.

Each bus driver is also the function driver for the bus adapter. Therefore, the driver must also provide an [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback function. This callback function creates a functional device object (FDO) for each bus adapter on the system. For more information about creating FDOs, see [Creating Device Objects in a Function Driver](creating-device-objects-in-a-function-driver.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Creating%20Device%20Objects%20in%20a%20Bus%20Driver%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




