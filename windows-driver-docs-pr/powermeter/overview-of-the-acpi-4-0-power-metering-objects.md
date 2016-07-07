---
title: Overview of the ACPI 4.0 Power Metering Objects
description: Overview of the ACPI 4.0 Power Metering Objects
ms.assetid: 91488b88-bbdc-40e9-9095-2ea3fb7d69ad
keywords: ["Power Metering and Budgeting WDK , ACPI 4.0 power metering objects", "ACPI 4.0 Power Metering objects WDK"]
---

# Overview of the ACPI 4.0 Power Metering Objects


The ACPI Power Meter Interface (PMI) exposes the power metering and budgeting capabilities of the hardware platform to the drivers that provide the WDM PMI interface.

The ACPI PMI is provided by the ACPI 4.0 Power Metering objects. These objects provide an abstraction layer to the protocol that is used for power metering and budgeting by the hardware platform. This abstraction layer provides a consistent power supply and meter interface to the operating system across all hardware platforms.

The system firmware must implement the ACPI 4.0 Power Metering objects. The platform implementation details are proprietary and specific to the system.

Power supplies and meters that are PMI-compliant are identified through the ACPI hardware ID of "ACPI000D". In addition, the ACPI PMI defines control methods that are used to obtain static information, and query or set dynamic information. For example, an ACPI PMI control method is defined to read the current power draw from a PMI-compliant power meter.

PMI events, such as when power thresholds are exceeded, are signaled through a set of ACPI notify codes on the power meter device.

Each ACPI PMI namespace object has appropriate control methods that allow interactions between the operating system and the hardware platform. These control methods provide support for the following:

-   Query of power supply and power meter characteristics.

-   Query of runtime power consumption measurements.

-   Management of power budgeting by a power meter.

-   Event notification.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[powermeter\powermeter]:%20Overview%20of%20the%20ACPI%204.0%20Power%20Metering%20Objects%20%20RELEASE:%20%286/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


