---
title: Types of WDM Drivers
author: windows-driver-content
description: There are three kinds of WDM drivers bus drivers, function drivers, and filter drivers.
MS-HAID:
- 'WDMIntro\_5355eedf-05d0-4d2b-8dae-e19df53a5da8.xml'
- 'kernel.types\_of\_wdm\_drivers'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 86acc77e-816e-46c8-b63c-2bb10920acd6
keywords: ["WDM drivers WDK kernel , types", "WDM drivers WDK kernel , layered drivers", "layered drivers WDK kernel", "driver layers WDK WDM", "bus drivers WDK WDM", "function drivers WDK WDM", "filter drivers WDK WDM", "WDM bus drivers WDK", "WDM function drivers WDK", "WDM filter drivers WDK"]
---

# Types of WDM Drivers


There are three kinds of WDM drivers: bus drivers, function drivers, and filter drivers.

## <a href="" id="ddk-types-of-wdm-drivers-kg"></a>


-   A [bus driver](bus-drivers.md) drives an individual I/O bus device and provides per-slot functionality that is device-independent. Bus drivers also detect and report child devices that are connected to the bus.
-   A [function driver](function-drivers.md) drives an individual device.
-   A [filter driver](filter-drivers.md) filters I/O requests for a device, a class of devices, or a bus.

In this context, a *bus* is any device to which other physical, logical, or virtual devices are attached; a bus includes traditional buses such as SCSI and PCI, as well as parallel ports, serial ports, and i8042 ports.

It is important for driver developers to understand the different kinds of WDM drivers and to know which kind of driver they are writing. For example, whether a driver handles each [Plug and Play](implementing-plug-and-play.md) IRP and how to handle such IRPs depends on what kind of driver is being written (bus driver, function driver, or filter driver).

### <a href="" id="possible-driver-layers"></a>

The following figure shows the relationship between the bus driver, function driver, and filter drivers for a device.

![diagram illustrating possible driver layers](images/drvlyr.png)

Each device typically has a bus driver for the parent I/O bus, a function driver for the device, and zero or more filter drivers for the device. A driver design that requires many filter drivers does not yield optimal performance.

The drivers in the previous figure are the following:

1.  A *bus driver* services a bus controller, adapter, or bridge. Bus drivers are required drivers; there is one bus driver for each type of bus on a machine. Microsoft provides bus drivers for most common buses. IHVs and OEMs can provide other bus drivers.

2.  A *bus filter driver* typically adds value to a bus and is supplied by Microsoft or a system OEM. There can be any number of bus filter drivers for a bus.

3.  *Lower-level filter drivers* typically modify the behavior of device hardware. They are optional and are typically supplied by IHVs. There can be any number of lower-level filter drivers for a device.

4.  A *function driver* is the main driver for a device. A function driver is typically written by the device vendor and is required (unless the device is being used in [*raw mode*](https://msdn.microsoft.com/library/windows/hardware/ff556331#wdkgloss-raw-mode)).

5.  *Upper-level filter drivers* typically provide added-value features for a device. They are optional and are typically provided by IHVs.

The following topics describe the three general types of WDM drivers—bus drivers, function drivers, filter drivers—in detail. Also included is an example of WDM driver layering that uses sample USB drivers.

## In this section


-   [Bus Drivers](bus-drivers.md)
-   [Function Drivers](function-drivers.md)
-   [Filter Drivers](filter-drivers.md)
-   [WDM Driver Layers: An Example](wdm-driver-layers---an-example.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Types%20of%20WDM%20Drivers%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


