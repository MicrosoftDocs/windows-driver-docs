---
title: ACPI-defined devices
description: The ACPI 5.0 specification defines a number of device types to represent and control typical platform features.
ms.assetid: 10BD17C9-E8FE-41E0-BD8C-E622B60E6BB6
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# ACPI-defined devices


The [ACPI 5.0 specification](https://www.uefi.org/specifications) defines a number of device types to represent and control typical platform features. For example, ACPI defines a power button, a sleep button, and system indicators. For SoC-based platforms, Windows provides built-in drivers to support the ACPI-defined devices that are described in this article.

For more information, see section 9, "ACPI-Defined Devices and Device-Specific Objects", in the ACPI 5.0 specification.

## <a href="" id="lid"></a>Lid device


This device describes and reports the status of a clamshell device's lid. For more information, see section 9.4, "Control Method Lid Device", in the [ACPI 5.0 specification](https://www.uefi.org/specifications). Lid device implementations use the GPIO-signaled ACPI event mechanism, which is described in section 5.6.5, "GPIO-Signaled ACPI Events", in the ACPI 5.0 specification.

## <a href="" id="battery"></a>Control method battery device


This device describes, configures, and reports the status of the platform battery. For more information, see section 10.2, "Control Method Batteries", in the [ACPI 5.0 specification](https://www.uefi.org/specifications). Control Method Battery implementations on SoC platforms use the GPIO-signaled ACPI event mechanism, which is described in section 5.6.5, "GPIO-Signaled ACPI Events", in the ACPI 5.0 specification. Access to the battery and charging hardware is done by methods that operate through GPIO or SPB OpRegions, which are described in sections 5.5.2.4.4 and 5.5.2.4.5 of the ACPI 5.0 specification.

For more information about battery management in Windows, see [Windows Power and Battery Subsystem Requirements](https://msdn.microsoft.com/library/windows/hardware/mt614876).

**Battery Device-Specific Method (\_DSM)**

To support the passive thermal management of the battery by the platform, Microsoft defines a \_DSM method to communicate to the platform firmware the thermal throttling limit set by the battery's thermal zone. For more information, see the following:

-   [Battery Device-Specific Method](battery-device-specific-method.md)
-   [Thermal zones](#thermal)

## <a href="" id="time"></a>Control method time and alarm device


ACPI 5.0 defines the operation and definition of the optional control method-based Time and Alarm device, which provides a hardware-independent abstraction and a more robust alternative to the Real Time Clock (RTC). For more information, see section 9.15, "PC/AT RTC/CMOS Devices", and section 9.18, "Time and Alarm Device", in the [ACPI 5.0 specification](https://www.uefi.org/specifications). If the standard PC RTC either is not implemented or is used as the RTC hardware backing the Time and Alarm device, the "CMOS RTC Not Present" bit of the FADT's Boot Architecture flags field must be set.

The time capabilities of the Time and Alarm device are required for platforms that support the InstantGo feature (and the Connected Standby power mode). These capabilities maintain time-of-day information across system power transitions, and keep track of time even when the platform is turned off. It is expected that the time on the platform will be consistent when different firmware interfaces are used to query the platform time. For example, a UEFI call to get the time should return the same time that the operating system would get by using the Time and Alarm device.

The Time and Alarm device must be driven from the same time source as UEFI time services.

## <a href="" id="thermal"></a>Thermal zones


To support ACPI thermal management, the system designer logically partitions a hardware platform into one or more physical regions called thermal zones. Sensor devices track the temperature in each thermal zone. When a thermal zone starts to overheat, the operating system can take actions to cool down the devices in the zone. These actions can be categorized as either passive cooling or active cooling.

### Thermal management in Windows

The Windows thermal management model is based on ACPI's concept of thermal zones. This is a cooperative firmware/OS/driver model that abstracts the sensors and cooling devices from the central thermal management component through well-defined interfaces. For more information about thermal management, see the document titled "Thermal Management in Windows" on the [Microsoft Connect website](http://connect.microsoft.com/site1304/Downloads/DownloadDetails.aspx?DownloadID=48106).

### ACPI thermal zones

A thermal zone is defined to include child objects that do the following:

-   Identify the devices that are contained in the thermal zone:

    -   \_TZD to list the non-processor devices in the thermal zone.
    -   \_PSL to list the processors in the thermal zone.
-   Specify thermal thresholds at which actions must be taken:

    -   \_PSV to indicate the temperature at which the operating system starts passive cooling control.
    -   \_HOT to indicate the temperature at which the operating system hibernates.
    -   \_CRT to indicate the temperature at which the operating system shuts down.
-   Describe the thermal zone's passive cooling behavior:

    -   \_TC1, \_TC2 for thermal responsiveness.
    -   \_TSP for the appropriate temperature sampling interval for passive cooling of the thermal zone.
-   Report the thermal zone's temperature:

    -   \_TMP for firmware-reported temperature, or
    -   \_HID and \_CRS for loading a temperature sensor driver and allocating hardware resources to it.
-   Optionally, receive notifications of additional temperature threshold crossings:

    -   \_NTT for specifying additional threshold crossings to be notified of.
    -   \_DTI for receiving notifications of additional threshold crossings.
-   Optionally, describe the thermal zone's active cooling behavior:

    -   \_AL*x* for listing the fans in the thermal zone.
    -   \_AC*x* the temperature at which fan *x* must be turned on.

For more information about ACPI thermal zones, see chapter 11, "Thermal Management", in the [ACPI 5.0 specification](https://www.uefi.org/specifications).

### Logical processor idling as a thermal mitigation

The platform can indicate to the operating system that processor cores in the thermal zone should be idled (instead of throttled). This is done by including the Processor Aggregator device (ACPI000C) in one or more thermal zones. Windows will park a number of cores when the thermal zone's \_PSV is crossed. The number is either *(1 - &lt;zone passive limit&gt;) \* &lt;the number of cores in the thermal zone&gt;*, or the number of cores reported in \_PUR, whichever is greater. For more information, see section 8.5.1, "Logical Processor Idling", in the [ACPI 5.0 specification](https://www.uefi.org/specifications).

OEMs can include a Device-Specific Method (\_DSM) to support the Microsoft thermal extensions for Windows. For more information, see [Device-Specific Method for Microsoft Thermal Extensions](device-specific-method-for-microsoft-thermal-extensions.md).

 

 




