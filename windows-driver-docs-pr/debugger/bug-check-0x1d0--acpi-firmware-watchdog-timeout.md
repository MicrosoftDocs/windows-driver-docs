---
title: Bug Check 0x1D0 ACPI_FIRMWARE_WATCHDOG_TIMEOUT  
description: The ACPI_FIRMWARE_WATCHDOG_TIMEOUT bug check has a value of 0x000001D0.
keywords: ["Bug Check 0x1D0 ACPI_FIRMWARE_WATCHDOG_TIMEOUT",  "ACPI_FIRMWARE_WATCHDOG_TIMEOUT"]
ms.date: 04/19/2018
topic_type:
- apiref
ms.topic: reference
api_name:
- ACPI_FIRMWARE_WATCHDOG_TIMEOUT 
api_type:
- NA
---

# Bug Check 0x1D0: ACPI\_FIRMWARE\_WATCHDOG\_TIMEOUT 


> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


The ACPI_FIRMWARE_WATCHDOG_TIMEOUT bug check has a value of 0x000001D0. 

ACPI driver failed to complete an operation in expected alloted time.

## ACPI\_FIRMWARE\_WATCHDOG\_TIMEOUT Parameters

The following parameters are displayed on the blue screen.

Parameter | Description 
|---------|--------------|
1 | Pointer to AMLI Context
2 | Pointer to Unicode Name of the Aml Context
3 | Pointer to ACPI Device Extension.
4 | Pointer to ACPI Triage Block.