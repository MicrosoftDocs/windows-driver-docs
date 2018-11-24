---
title: General-purpose I/O (GPIO)
description: System on a Chip (SoC) integrated circuits make extensive use of general-purpose I/O (GPIO) pins.
ms.assetid: 9EB4EFC3-B94E-42C9-9FC7-12DF4AD01622
ms.date: 07/09/2018
ms.localizationpriority: medium
---

# General-purpose I/O (GPIO)


System on a Chip (SoC) integrated circuits make extensive use of general-purpose I/O (GPIO) pins. For SoC-based platforms, Windows defines a general abstraction for GPIO hardware, and this abstraction requires support from the Advanced Configuration and Power Interface (ACPI) namespace.

The GPIO abstraction is supported by the [ACPI 5.0 Specification](https://www.uefi.org/specifications) definitions that are listed in this article.

To verify that your GPIO controller meets all Windows platform requirements, see [GPIO Controller Requirements Checklist](gpio-controller-requirements-checklist.md).

## GPIO controller devices


Windows supports GPIO controllers. GPIO controllers provide a variety of functions for peripheral devices, including interrupts, input signaling, and output signaling. GPIO capabilities are modeled as a GPIO controller device in the namespace. The [GPIO framework extension](https://docs.microsoft.com/windows-hardware/drivers/gpio/gpio-driver-support-overview) (GpioClx) models the GPIO controller device as being partitioned into some number of banks of pins. Each pin bank has 64 or fewer configurable pins. The banks in a GPIO controller are ordered relative to their pins' position within the controller-relative GPIO pin space. For example, bank 0 contains pins 0-31 on the controller, bank 1 contains pins 32-63, and so on. All banks have the same number of pins, except for the last bank, which might have fewer. Banks are significant for the ACPI firmware because the firmware must report the mapping of system interrupt resources to banks, as described in **GPIO namespace objects** section below.

Each pin on a bank has a set of parameters (for example, output, level-sensitive interrupt, de-bounced input, and so on) that describe how the pin is to be configured.

**GPIO controllers and ActiveBoth interrupts**

A feature of some GPIO controllers is the ability to generate interrupts on both edges of a signal (rising, or ActiveHigh edges, and falling, or ActiveLow edges). This is useful in a variety of applications, including the button interface, wherein both button-press events (one edge) and button-release events (the opposite edge) are meaningful. This feature is referred to as "ActiveBoth".

Logically, ActiveBoth signals have both an asserted and unasserted state, whether they are momentary assertions (for example, pushbuttons), or indefinitely long assertions (for example, headphone jack insertions). Edge detection for ActiveBoth interrupts might be implemented in the GPIO controller hardware (hardware ActiveBoth), or be emulated in the GPIO driver software (emulated ActiveBoth). Windows requires that GPIO controllers that implement ActiveBoth must use emulated ActiveBoth. This is required to ensure robust handling of double-edged interrupts for all scenarios. In support of ActiveBoth emulation, the following hardware requirements apply:

1.  GPIO controllers that support ActiveBoth interrupts must support level-mode interrupts, and must support re-programming the polarity of the interrupt dynamically at runtime.
2.  To minimize the risk of I/O errors, Windows prefers the use of memory-mapped GPIO controllers instead of SPB-connected GPIO controllers. In fact, for the Windows Button Array device (PNP0C40), it is required that the ActiveBoth GPIO interrupts for this device connect to a memory-mapped GPIO controller, and not to an SPB-connected one. To determine which button interrupts must be ActiveBoth, see the **Button devices** sectionin the [Other ACPI namespace objects](other-acpi-namespace-objects.md) topic.
3.  To establish a deterministic initial state for ActiveBoth interrupt signals, the Windows GPIO device stack guarantees that the first interrupt generated after connection of the interrupt by the driver will always be for the signal's asserted state. The stack further assumes that the asserted state of all ActiveBoth interrupt lines is logic level low (the ActiveLow edge) by default. If this is not the case on your platform, you can override the default by including the GPIO controller Device-Specific Method (\_DSM) in the controller's namespace. For more information about this method, see [GPIO Controller Device-Specific Method (\_DSM)](gpio-controller-device-specific-method---dsm-.md).

> [!NOTE]
> The third requirement in the preceding list implies that the driver for a device that uses ActiveBoth might receive an interrupt immediately after initializing (connecting to) the interrupt, if the signal at the GPIO pin is in the asserted state at that time. This is possible, and even likely for some devices (for example, headphones), and must be supported in the driver.

 

To support emulated ActiveBoth, the GPIO controller driver must enable ("opt-in to") ActiveBoth emulation by implementing a [*CLIENT\_ReconfigureInterrupt*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/gpioclx/nc-gpioclx-gpio_client_reconfigure_interrupt) callback function, and by setting the **EmulateActiveBoth** flag in the basic information structure that the driver's [*CLIENT\_QueryControllerBasicInformation*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/gpioclx/nc-gpioclx-gpio_client_query_controller_basic_information) callback function supplies to **GpioClx**. For more information, see [General-Purpose I/O (GPIO) Drivers](https://docs.microsoft.com/windows-hardware/drivers/gpio).

## GPIO namespace objects


GPIO controllers, and the peripherals that connect to them, are enumerated by ACPI. The connection between them is described using GPIO Connection Resource Descriptors. For more information, see section 6.4.3.8, "Connection Descriptors", of the ACPI 5.0 specification.

**Device identification and configuration objects**

A GPIO controller device's ACPI namespace includes the following:

-   A vendor-assigned ACPI-compliant Hardware ID (\_HID) object.
-   A set of resources consumed (\_CRS) object.
-   A Unique ID (\_UID) object, if there is more than one instance of the GPIO controller in the namespace (that is, two or more namespace nodes that have the same device identification objects).

The GPIO controller's \_CRS contains all of the resources (address space for registers, system interrupts, and so on) consumed by all of the banks in the GPIO controller. The interrupt resource-to-bank mapping is represented in the order in which the interrupt resources are listed in the \_CRS—that is, the first interrupt listed is assigned to bank 0, the next one listed is assigned to bank 1, and so on. Banks can share interrupt resources, in which case the interrupt is listed once for each bank connected to it, in bank order, and is configured as Shared.

**GPIO connection resource descriptors**

The relationship between peripherals and the GPIO pins to which they are connected is described to the operating system by GPIO connection resource descriptors. These resource descriptors can define two types of GPIO Connections: GPIO interrupt connections and GPIO I/O connections. Peripherals include GPIO connection descriptors in their \_CRS for all GPIO I/O and interrupt pins connected. If a connected interrupt is wake-capable (capable of waking the system from a low-power idle state, then it must be configured as ExclusiveAndWake or SharedAndWake; for more information, see [Device Power Management](device-power-management.md).

The descriptors are defined in section 6.4.3.8.1, "GPIO Connection Descriptor", of the ACPI 5.0 specification. The ASL Resource Template Macros for these descriptors are described in section 19.5.53, "GpioInt (GPIO Interrupt Connection Resource Descriptor Macro)", of the ACPI 5.0 specification.

**GPIO-signaled ACPI events**

ACPI defines a platform event model that enables hardware events in the platform to be signaled and communicated to the ACPI driver. Windows provides a notification service for communicating platform events to device drivers. A number of inbox drivers rely on this service to provide support for ACPI-defined devices, such as Control Method Power Button, LID device, Control Method Battery, Thermal Zone, and so on. For more information about notifications, see section 5.6.5, "GPIO-Signaled ACPI Events", of the ACPI specification.

For SoC platforms, GPIO interrupts are used to signal platform events. Any namespace device ("ACPI Event Source" device) that signals events to its driver using the ASL Notify operator requires the following:

-   The namespace node of the GPIO controller to which the ACPI event signal is connected must include a GpioInt resource for that pin in its ACPI Event Information (\_AEI) object (see section 2.4.2.3.1, "ACPI Event Information (\_AEI) Object", below). The GpioInt resource must be configured as non-shared (Exclusive).
-   The controller's node must also contain an Edge (\_Exx), Level (\_Lxx) or Event (\_EVT) control method for each pin listed in the \_AEI object.

The ACPI driver handles the listed GPIO interrupt and evaluates the Edge, Level or Event control method for it. The control method quiesces the hardware event, if necessary, and executes the required Notify operator on the event source device's namespace node. Windows then sends the notification to the device's driver. Multiple events can be signaled over the same GpioInt resource if the event control method can query the hardware to determine which event occurred. The method must then notify the correct device with the correct notification code.

*ACPI Event Information (\_AEI) object*

As previously mentioned, the GPIO controller's namespace must contain the \_AEI object in order to support ACPI events. The \_AEI object (see section 5.6.5.2 in the ACPI 5.0 specification) returns a Resource Template buffer containing only GpioInt descriptors that signal ACPI events via this GPIO controller. Each descriptor corresponds to one ACPI event source device and is dedicated to that device (not shared between devices).

**GeneralPurposeIO operation regions (OpRegions)**

GPIO controllers are often used by platform firmware to support any number of platform hardware features such as controlling power and clocks, or setting modes on devices. To support the use of GPIO I/O from ASL control methods, ACPI 5.0 defines a new OpRegion type, "GeneralPurposeIO".

GeneralPurposeIO OpRegions (see section 5.5.2.4.4 of the ACPI 5.0 specification) are declared within the namespace scope of the GPIO controller device whose driver will handle the I/O. GeneralPurposeIO Field declarations (see section 5.5.2.4.4.1 of the ACPI 5.0 specification) assign names to GPIO pins that are to be accessed within a GeneralPurposeIO OpRegion. GpioIO Connection Resources (see section 19.5.53 of the ACPI 5.0 specification) are used within the Field declaration to specify the pin number(s) and configuration for a particular Field reference. The total number of named field bits following a connection descriptor must equal the number of pins listed in the descriptor.

Fields in an OpRegion can be declared anywhere in the namespace and accessed from any method in the namespace. The direction of accesses to a GeneralPurposeIO OpRegion is determined by the first access (read or write) and cannot be changed.

> [!NOTE]
> Because OpRegion access is provided by the GPIO controller device driver (the "OpRegion Handler"), methods must take care not to access an OpRegion until the driver is available. ASL code can track the state of the OpRegion handler by including a Region (\_REG) method under the GPIO controller device (see section 6.5.4 of the ACPI 5.0 specification). Additionally, the OpRegion Dependencies (\_DEP) object (see section 6.5.8 of the ACPI 5.0 specification) can be used under any device that has a method accessing GPIO OpRegion fields, if needed. See the **Device dependencies** section in the [Device management namespace objects](device-management-namespace-objects.md) topic for a discussion of when to use \_DEP. It is important that drivers are not assigned GPIO I/O resources that are also assigned to GeneralPurposeIO OpRegions. Opregions are for the exclusive use of ASL control methods.

 
