---
title: Hardware requirements for SoC-based platforms
description: The ACPI 5.0 specification introduces a new set of hardware requirements to support SoC-based platforms that run Windows.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: C8AA4EE1-D9A6-438E-801B-8EDDF8AA0560
---

# Hardware requirements for SoC-based platforms


The [ACPI 5.0 specification](http://www.acpi.info) introduces a new set of hardware requirements to support SoC-based platforms that run Windows. ACPI 5.0 supports hardware-reduced system designs to lower cost, and supports the connected standby power model to enable long battery life.

## <a href="" id="hw"></a>Hardware-reduced ACPI platforms


To support SoCs, Windows does not require hardware platforms to implement any of the features that are described in chapter 4, "ACPI Hardware Specification" of the ACPI 5.0 specification. ACPI fixed hardware features such as the following are not required:

-   Power Management (PM) timer
-   Real Time Clock (RTC) wake alarm
-   System Control Interrupt (SCI)
-   Fixed Hardware register set (PMx\_\* event/control/status registers)
-   GPE block registers (GPEx\_\* event/control/status registers)
-   Embedded controller

Platforms that do not implement the ACPI Fixed Hardware interface are referred to as *hardware-reduced* ACPI platforms. To indicate that a platform is hardware-reduced, set the HW\_REDUCED\_ACPI flag in the Fixed ACPI Description Table (FADT).

On hardware-reduced ACPI platforms, fixed hardware features such as *power button*, *lid status*, and so on that have traditionally been implemented in ACPI-defined hardware, are replaced exclusively by their ACPI-defined software equivalents. For example, a Control Method Power Button is used instead of the Fixed Hardware equivalent.

## <a href="" id="cs"></a>Connected standby


Platforms that implement the connected standby power model (a key feature of InstantGo devices) are exposed to Windows as platforms that provide the low-power S0-idle capability defined in ACPI 5.0. The "Low Power S0 Idle Capable" flag in the FADT must be set to indicate that the platform supports connected standby.

Windows supports platforms that have low-power S0-idle capability regardless of whether they implement hardware-reduced ACPI or full ACPI. However, as required by the ACPI 5.0 specification, Windows does not use traditional sleep/resume features on platforms that have low-power S0-idle capability, regardless of ACPI configuration.

For more information about the connected standby power model, see [Modern Standby](https://msdn.microsoft.com/library/windows/hardware/dn915061).

## <a href="" id="acpi"></a>ACPI events


As part of chapter 4, "ACPI Hardware Specification", of the ACPI 5.0 specification, a full-featured mechanism is defined for signaling hardware events. Windows supports many events defined in the specification, and this support carries over to SoC platforms. However, for hardware-reduced ACPI platforms, GPIO interrupts are used to signal the events, instead of the ACPI-defined GPE/SCI hardware. After an event is signaled however, event handling is identical between hardware-reduced and full ACPI platforms. In both cases, the ACPI-specified event-handling mechanism invokes the appropriate control method (handler) for the event, which ultimately sends an ACPI-defined notification to the appropriate device driver.

For more information about GPIO-signaled ACPI events, see section 5.6.5, "GPIO-Signaled ACPI Events", of the ACPI 5.0 specification. For more information about the ACPI software event handling, see section 5.6.4, "General Purpose Event Handling", of the ACPI 5.0 specification.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20Hardware%20requirements%20for%20SoC-based%20platforms%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




