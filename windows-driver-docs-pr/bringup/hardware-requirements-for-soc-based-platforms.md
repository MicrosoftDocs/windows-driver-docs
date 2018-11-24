---
title: Hardware requirements for SoC-based platforms
description: The ACPI 5.0 specification introduces a new set of hardware requirements to support SoC-based platforms that run Windows.
ms.assetid: C8AA4EE1-D9A6-438E-801B-8EDDF8AA0560
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Hardware requirements for SoC-based platforms


The [ACPI 5.0 specification](https://www.uefi.org/specifications) introduces a new set of hardware requirements to support SoC-based platforms that run Windows. ACPI 5.0 supports hardware-reduced system designs to lower cost, and supports the connected standby power model to enable long battery life.

## Hardware-reduced ACPI platforms


To support SoCs, Windows does not require hardware platforms to implement any of the features that are described in chapter 4, "ACPI Hardware Specification" of the ACPI 5.0 specification. ACPI fixed hardware features such as the following are not required:

-   Power Management (PM) timer
-   Real Time Clock (RTC) wake alarm
-   System Control Interrupt (SCI)
-   Fixed Hardware register set (PMx\_\* event/control/status registers)
-   GPE block registers (GPEx\_\* event/control/status registers)
-   Embedded controller

Platforms that do not implement the ACPI Fixed Hardware interface are referred to as *hardware-reduced* ACPI platforms. To indicate that a platform is hardware-reduced, set the HW\_REDUCED\_ACPI flag in the Fixed ACPI Description Table (FADT).

On hardware-reduced ACPI platforms, fixed hardware features such as *power button*, *lid status*, and so on that have traditionally been implemented in ACPI-defined hardware, are replaced exclusively by their ACPI-defined software equivalents. For example, a Control Method Power Button is used instead of the Fixed Hardware equivalent.

## Connected standby


Platforms that implement the connected standby power model (a key feature of InstantGo devices) are exposed to Windows as platforms that provide the low-power S0-idle capability defined in ACPI 5.0. The "Low Power S0 Idle Capable" flag in the FADT must be set to indicate that the platform supports connected standby.

Windows supports platforms that have low-power S0-idle capability regardless of whether they implement hardware-reduced ACPI or full ACPI. However, as required by the ACPI 5.0 specification, Windows does not use traditional sleep/resume features on platforms that have low-power S0-idle capability, regardless of ACPI configuration.

For more information about the connected standby power model, see [Modern Standby](https://msdn.microsoft.com/library/windows/hardware/dn915061).

## ACPI events


As part of chapter 4, "ACPI Hardware Specification", of the ACPI 5.0 specification, a full-featured mechanism is defined for signaling hardware events. Windows supports many events defined in the specification, and this support carries over to SoC platforms. However, for hardware-reduced ACPI platforms, GPIO interrupts are used to signal the events, instead of the ACPI-defined GPE/SCI hardware. After an event is signaled however, event handling is identical between hardware-reduced and full ACPI platforms. In both cases, the ACPI-specified event-handling mechanism invokes the appropriate control method (handler) for the event, which ultimately sends an ACPI-defined notification to the appropriate device driver.

For more information about GPIO-signaled ACPI events, see section 5.6.5, "GPIO-Signaled ACPI Events", of the ACPI 5.0 specification. For more information about the ACPI software event handling, see section 5.6.4, "General Purpose Event Handling", of the ACPI 5.0 specification.

 

 




