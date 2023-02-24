---
title: ACPI_ENUM_CHILD_NEXT macro
description: The ACPI_ENUM_CHILD_NEXT macro calculates a pointer to the next ACPI_ENUM_CHILD structure in an array of variable length ACPI_ENUM_CHILD structures.
keywords: 
- ACPI_ENUM_CHILD_NEXT macro ACPI Devices
ms.date: 02/24/2023
ms.topic: reference
---

# ACPI_ENUM_CHILD_NEXT macro

The ACPI_ENUM_CHILD_NEXT macro calculates a pointer to the next [**ACPI_ENUM_CHILD**](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_enum_child) structure in an array of variable length **ACPI_ENUM_CHILD** structures.

## Syntax

```cpp
void ACPI_ENUM_CHILD_NEXT(
    Child
);
```

## Parameters

*Child*
A pointer to a variable of type **ACPI_ENUM_CHILD** for which to return a nonaligned pointer to the next **ACPI_ENUM_CHILD** structure in an array of variable-length ACPI_ENUM_CHILD structures.

## Return value

A pointer to the next **ACPI_ENUM_CHILD** structure in an array of variable-length **ACPI_ENUM_CHILD** structures.

## Remarks

After a driver uses an [**IOCTL_ACPI_ENUM_CHILDREN**](/windows-hardware/drivers/ddi/acpiioct/ni-acpiioct-ioctl_acpi_enum_children) request to retrieve an array of child device names in an [**ACPI_ENUM_CHILDREN_OUTPUT_BUFFER**](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_enum_children_output_buffer) request, the driver can use this macro to determine a sequence of pointers to the variable-length **ACPI_ENUM_CHILD** structures in the **Children** array that the output buffer contains.

## Requirements

**Target platform:** Desktop

**Header:** acpiioct.h (include Acpiioct.h)

## See also

[**ACPI_ENUM_CHILD**](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_enum_child)

[**ACPI_ENUM_CHILDREN_OUTPUT_BUFFER**](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_enum_children_output_buffer)

[**IOCTL_ACPI_ENUM_CHILDREN**](/windows-hardware/drivers/ddi/acpiioct/ni-acpiioct-ioctl_acpi_enum_children)
