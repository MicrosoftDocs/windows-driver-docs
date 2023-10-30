---
title: ACPI_ENUM_CHILD_LENGTH_FROM_CHILD macro
description: The ACPI_ENUM_CHILD_LENGTH_FROM_CHILD macro calculates the size, in bytes, of a variable-length ACPI_ENUM_CHILD structure.
keywords: 
- ACPI_ENUM_CHILD_LENGTH_FROM_CHILD macro ACPI Devices
ms.date: 03/17/2023
ms.topic: reference
---

# ACPI_ENUM_CHILD_LENGTH_FROM_CHILD macro

The ACPI_ENUM_CHILD_LENGTH_FROM_CHILD macro calculates the size, in bytes, of a variable-length [**ACPI_ENUM_CHILD**](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_enum_child) structure.

## Syntax

```cpp
void ACPI_ENUM_CHILD_LENGTH_FROM_CHILD(
    Child
);
```

## Parameters

*Child*
A pointer to a structure of type **ACPI_ENUM_CHILD** for which to calculate the size, in bytes, of the structure.

## Return value

The size, in bytes, of the **ACPI_ENUM_CHILD** structure that *Child* points to.

## Remarks

A driver can use this macro to calculate the size, in bytes, of the **ACPI_ENUM_CHILD** structures in an [**ACPI_ENUM_CHILDREN_OUTPUT_BUFFER**](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_enum_children_output_buffer) structure.

## Requirements

**Target platform:** Desktop

**Header:** acpiioct.h (include Acpiioct.h)

## See also

[**ACPI_ENUM_CHILD**](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_enum_child)

[**ACPI_ENUM_CHILDREN_OUTPUT_BUFFER**](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_enum_children_output_buffer)
