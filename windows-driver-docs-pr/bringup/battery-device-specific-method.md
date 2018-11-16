---
title: Battery Device-Specific Method
description: This topic describes _DSM control method and parameters for passive thermal battery management.
ms.assetid: 622803F4-2548-4E8A-A330-179ABDF374AD
ms.date: 05/16/2018
ms.localizationpriority: medium
---

# Battery Device-Specific Method


To support the passive thermal management of the battery by the platform, Microsoft defines a \_DSM method to communicate to the platform firmware the thermal throttling limit set by the battery's thermal zone.

For more information, see the **Thermal zones** section in the [ACPI defined devices](acpi-defined-devices.md#thermal) topic.

## Function 1: Battery thermal limit


The \_DSM control method parameters for the battery charging thermal limit function are as follows:

### Arguments

-   **Arg0:** UUID = 4c2067e3-887d-475c-9720-4af1d3ed602e
-   **Arg1:** Revision = 0
-   **Arg2:** Function index = 1
-   **Arg3:** Thermal limit (integer value from 0 to 100)

### Return

None. Firmware is responsible for taking the current thermal limit into account when engaging charging.
 

 




