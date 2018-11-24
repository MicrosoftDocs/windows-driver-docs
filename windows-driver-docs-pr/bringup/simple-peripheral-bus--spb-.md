---
title: Simple peripheral bus (SPB)
description: SoC integrated circuits make extensive use of simple, low-pin-count, and low-power serial interconnects for connecting to platform peripherals.
ms.assetid: E85BDD36-7ECE-47DB-A770-E28DA8383BA2
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Simple peripheral bus (SPB)


System on a Chip (SoC) integrated circuits make extensive use of simple, low-pin-count and low-power serial interconnects for connecting to platform peripherals. I²C, SPI and UARTs are examples. For SoC-based platforms, Windows provides a general abstraction for Simple Peripheral Bus (SPB) hardware, and this abstraction requires new support from the Advanced Configuration and Power Interface (ACPI) namespace.

## SPB controller devices


A SPB controller device is identified in the namespace together with a vendor-assigned Hardware ID (\_HID) and a set of resources that are consumed (\_CRS).

### SPB namespace objects

SPB controllers, and the peripherals that connect to them, are enumerated by ACPI. The connection between them is described using Serial Bus Connection Resource Descriptors. For more information, see section 6.4.3.8, "Connection Descriptors", of the [ACPI 5.0 specification](https://www.uefi.org/specifications).

### SPB resource descriptors

As is the case with GPIO connections, SPB connections are described to the operating system by the consuming device, via new resource descriptors. The Generic Serial Bus Resource Descriptor is used to declare I²C connections, SPI connections, and UART connections, and is extensible to support other serial bus types in the future.

Resource Template Macros for these descriptors are described in section 19.5.55, "I2CSerialBus (I2C Serial Bus Connection Resource Descriptor Macro) ", of the [ACPI 5.0 specification](https://www.uefi.org/specifications).

### GenericSerialBus OpRegions

Also similar to GPIO, ACPI 5.0 defines an OpRegion for use with SPB controllers, GenericSerialBus (section 5.5.2.4.5 of the ACPI 5.0 specification). Because SPBs are communication buses, GenericSerialBus OpRegions support various protocols for accessing SPB target devices. For more information, see section 5.5.2.4.5.3, "Using the GenericSerialBus Protocols", of the [ACPI 5.0 specification](https://www.uefi.org/specifications).

Often with SPBs, it is necessary for ASL control methods to share access to a SPB target device with the operating system driver for that device. To ensure synchronization of these accesses, ACPI 5.0 defines the Device Lock Mutex (\_DLM) object. For more information, see section 5.7.5 of the [ACPI 5.0 specification](https://www.uefi.org/specifications).

 

 




