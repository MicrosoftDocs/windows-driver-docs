---
title: Power States
description: Power States
ms.assetid: 33043903-9db6-4c51-b33c-921ade237ccf
keywords: ["power management WDK kernel , power states", "power states WDK kernel", "states WDK power management", "system power states WDK kernel", "device power states WDK kernel", "power consumption levels WDK kernel", "consumption levels WDK power management", "computing activity WDK power management", "physical device objects WDK power management", "PDOs WDK power management", "functional device objects WDK power management", "FDOs WDK power management", "filter DOs WDK power management"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Power States





A power state indicates the level of power consumption—and thus the extent of computing activity—by the system or by a single device. The power manager sets the power state of the system as a whole. Device drivers set the power state of their individual devices.

The ACPI specification defines two sets of discrete power states: *system power states* and *device power states*. Each power state has a unique name.

[System power states](system-power-states.md) are named S*x*, where *x* is a state number between 0 and 5. [Device power states](device-power-states.md) are named D*x*, where *x* is a state number between 0 and 3. The state number is inversely related to power consumption: higher numbered states use less power. States S0 and D0 are the highest-powered, most functional, fully on states. States S5 and D3 are the lowest-powered states and have the longest wake-up latency.

These clearly defined power states allow many devices from various manufacturers to work together consistently and predictably. For example, when the power manager sets the system in state S3, it can rely upon drivers that support power management not only to put their devices in the corresponding device power state but also to return to the working state in a predictable fashion.

 

 




