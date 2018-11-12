---
title: Overview of the ACPI 4.0 Power Metering Objects
description: Overview of the ACPI 4.0 Power Metering Objects
ms.assetid: 91488b88-bbdc-40e9-9095-2ea3fb7d69ad
keywords:
- Power Metering and Budgeting WDK , ACPI 4.0 power metering objects
- ACPI 4.0 Power Metering objects WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




