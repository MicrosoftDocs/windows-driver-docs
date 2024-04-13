---
title: ACPI_METHOD_SET_ARGUMENT_BUFFER Macro
description: The ACPI_METHOD_SET_ARGUMENT_BUFFER macro sets the members of an ACPI_METHOD_ARGUMENT structure for custom data that is supplied in a data buffer.
keywords: 
- ACPI_METHOD_SET_ARGUMENT_BUFFER macro ACPI Devices
ms.date: 03/17/2023
ms.topic: reference
---

# ACPI_METHOD_SET_ARGUMENT_BUFFER macro

The ACPI_METHOD_SET_ARGUMENT_BUFFER macro sets the members of an [**ACPI_METHOD_ARGUMENT**](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_method_argument_v1) structure for custom data that is supplied in a data buffer.

## Syntax

```cpp
void ACPI_METHOD_SET_ARGUMENT_BUFFER(
    Argument,
    BuffData,
    BuffLength
);
```

## Parameters

*Argument*
A pointer to an **ACPI_METHOD_ARGUMENT** structure.

*BuffData*
A pointer to a data buffer that contains custom data.

*BuffLength*
The size, in bytes, of the custom data.

## Return value

This macro does not return a value.

## Remarks

A driver can use this macro to set the members of an **ACPI_METHOD_ARGUMENT** structure that supplies custom data.

## Requirements

**Target platform:** Desktop

**Header:** acpiioct.h (include Acpiioct.h)

## See also

[**ACPI_METHOD_ARGUMENT**](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_method_argument_v1)
