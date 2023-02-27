---
title: ACPI_METHOD_SET_ARGUMENT_STRING macro
description: The ACPI_METHOD_SET_ARGUMENT_STRING macro sets the members of an ACPI_METHOD_ARGUMENT structure for a string value.
keywords: 
- ACPI_METHOD_SET_ARGUMENT_STRING macro ACPI Devices
ms.date: 02/24/2023
ms.topic: reference
---

# ACPI_METHOD_SET_ARGUMENT_STRING macro

The ACPI_METHOD_SET_ARGUMENT_STRING macro sets the members of an [**ACPI_METHOD_ARGUMENT**](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_method_argument_v1) structure for a string value.

## Syntax

```cpp
void ACPI_METHOD_SET_ARGUMENT_STRING(
    Argument,
    StrData
);
```

## Parameters

*Argument*
A pointer to an **ACPI_METHOD_ARGUMENT** structure.

*StrData*
A pointer to a NULL-terminated ASCII string.

## Return value

This macro does not return a value.

## Remarks

A driver can use this macro to set the members of an **ACPI_METHOD_ARGUMENT** structure that supplies a NULL-terminated ASCII string.

## Requirements

**Target platform:** Desktop

**Header:** acpiioct.h (include Acpiioct.h)

## See also

[**ACPI_METHOD_ARGUMENT**](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_method_argument_v1)
