---
title: ACPI_METHOD_NEXT_ARGUMENT macro
description: The ACPI_METHOD_NEXT_ARGUMENT structure returns a pointer to the next ACPI_METHOD_ARGUMENT structure in an array of ACPI_METHOD_ARGUMENT structures.
keywords: 
- ACPI_METHOD_NEXT_ARGUMENT macro ACPI Devices
ms.date: 08/17/2021
ms.localizationpriority: medium
---

# ACPI_METHOD_NEXT_ARGUMENT macro

The ACPI_METHOD_NEXT_ARGUMENT macro returns a pointer to the next [**ACPI_METHOD_ARGUMENT**](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_method_argument_v1) structure in an array of **ACPI_METHOD_ARGUMENT** structures.

## Syntax

```cpp
 ACPI_METHOD_NEXT_ARGUMENT(
    Argument
);
```

## Parameters

*Argument*
A pointer to an **ACPI_METHOD_ARGUMENT** structure in an array of **ACPI_METHOD_ARGUMENT** structures.

## Return value

A pointer to the next **ACPI_METHOD_ARGUMENT** structure in an array of **ACPI_METHOD_ARGUMENT** structures.

## Remarks

Given a pointer to an **ACPI_METHOD_ARGUMENT** structure in an array of such structures, a driver can use this macro to calculate a pointer to the next structure in the array, if one exists.

## Requirements

**Target platform:** Desktop

**Header:** acpiioct.h (include Acpiioct.h)

## See also

[**ACPI_METHOD_ARGUMENT**](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_method_argument_v1)
