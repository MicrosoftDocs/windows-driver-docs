---
title: ACPI_METHOD_SET_ARGUMENT_INTEGER macro
description: The ACPI_METHOD_SET_ARGUMENT_INTEGER macro sets the members of an ACPI_METHOD_ARGUMENT structure for a single integer value.
keywords: 
- ACPI_METHOD_SET_ARGUMENT_INTEGER macro ACPI Devices
ms.date: 03/17/2023
ms.topic: reference
---

# ACPI_METHOD_SET_ARGUMENT_INTEGER macro

The ACPI_METHOD_SET_ARGUMENT_INTEGER macro sets the members of an [**ACPI_METHOD_ARGUMENT**](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_method_argument_v1) structure for a single integer value.

## Syntax

```cpp
void ACPI_METHOD_SET_ARGUMENT_INTEGER(
    MethodArgument,
    IntData
);
```

## Parameters

*MethodArgument*
A pointer to an **ACPI_METHOD_ARGUMENT** structure.

*IntData*
An integer value of type ULONG.

## Return value

This macro does not return a value.

## Remarks

A driver can use this macro to set the members of an **ACPI_METHOD_ARGUMENT** structure that supplies a single integer value of type ULONG.

## Requirements

**Target platform:** Desktop

**Header:** acpiioct.h (include Acpiioct.h)

## See also

[**ACPI_METHOD_ARGUMENT**](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_method_argument_v1)
