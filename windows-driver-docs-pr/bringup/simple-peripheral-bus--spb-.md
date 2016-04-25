---
title: Simple peripheral bus (SPB)
description: System on a Chip (SoC) integrated circuits make extensive use of simple, low-pin-count and low-power serial interconnects for connecting to platform peripherals.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: E85BDD36-7ECE-47DB-A770-E28DA8383BA2
---

# Simple peripheral bus (SPB)


System on a Chip (SoC) integrated circuits make extensive use of simple, low-pin-count and low-power serial interconnects for connecting to platform peripherals. I²C, SPI and UARTs are examples. For SoC-based platforms, Windows provides a general abstraction for Simple Peripheral Bus (SPB) hardware, and this abstraction requires new support from the Advanced Configuration and Power Interface (ACPI) namespace.

## SPB controller devices


A SPB controller device is identified in the namespace together with a vendor-assigned Hardware ID (\_HID) and a set of resources that are consumed (\_CRS).

### SPB namespace objects

SPB controllers, and the peripherals that connect to them, are enumerated by ACPI. The connection between them is described using Serial Bus Connection Resource Descriptors. For more information, see section 6.4.3.8, "Connection Descriptors", of the [ACPI 5.0 specification](http://www.acpi.info).

### SPB resource descriptors

As is the case with GPIO connections, SPB connections are described to the operating system by the consuming device, via new resource descriptors. The Generic Serial Bus Resource Descriptor is used to declare I²C connections, SPI connections, and UART connections, and is extensible to support other serial bus types in the future.

Resource Template Macros for these descriptors are described in section 19.5.55, "I2CSerialBus (I2C Serial Bus Connection Resource Descriptor Macro) ", of the [ACPI 5.0 specification](http://www.acpi.info).

### GenericSerialBus OpRegions

Also similar to GPIO, ACPI 5.0 defines an OpRegion for use with SPB controllers, GenericSerialBus (section 5.5.2.4.5 of the ACPI 5.0 specification). Because SPBs are communication buses, GenericSerialBus OpRegions support various protocols for accessing SPB target devices. For more information, see section 5.5.2.4.5.3, "Using the GenericSerialBus Protocols", of the [ACPI 5.0 specification](http://www.acpi.info).

Often with SPBs, it is necessary for ASL control methods to share access to a SPB target device with the operating system driver for that device. To ensure synchronization of these accesses, ACPI 5.0 defines the Device Lock Mutex (\_DLM) object. For more information, see section 5.7.5 of the [ACPI 5.0 specification](http://www.acpi.info).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20Simple%20peripheral%20bus%20%28SPB%29%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




