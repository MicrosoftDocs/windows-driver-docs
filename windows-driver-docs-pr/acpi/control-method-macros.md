---
title: Control Method Macros
description: Provides information about control method macros
keywords:
- ACPI control methods WDK, macros
ms.date: 08/17/2021
ms.localizationpriority: medium
---

# Control Method Macros

A driver can use the following macros to set input arguments that are used with the ACPI IOCTLs that [evaluate control methods](evaluating-acpi-control-methods.md):

[**ACPI_METHOD_SET_ARGUMENT_INTEGER**](acpi-method-set-argument-integer.md)

[**ACPI_METHOD_SET_ARGUMENT_STRING**](acpi-method-set-argument-string.md)

[**ACPI_METHOD_SET_ARGUMENT_BUFFER**](acpi-method-set-argument-buffer.md)

The ACPI IOCTLs that evaluate control methods return output arguments in the **Argument** member of an [**ACPI_EVAL_OUTPUT_BUFFER**](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_eval_output_buffer_v1) structure, where the **Argument** member is an array of [**ACPI_METHOD_ARGUMENT**](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_method_argument_v1) structures. A driver can use the following macros to help process an array of ACPI_METHOD_ARGUMENT structures:

[**ACPI_METHOD_ARGUMENT_LENGTH**](acpi-method-argument-length.md)

[**ACPI_METHOD_ARGUMENT_LENGTH_FROM_ARGUMENT**](acpi-method-argument-length-from-argument.md)

[**ACPI_METHOD_NEXT_ARGUMENT**](acpi-method-next-argument.md)

An [**IOCTL_ACPI_ENUM_CHILDREN**](/windows-hardware/drivers/ddi/acpiioct/ni-acpiioct-ioctl_acpi_enum_children) request retrieves the path and name of child objects in the namespace of the device to which the request is sent. The ACPI driver returns the full path and name of the enumerated object beginning with the root of the ACPI namespace. The path and name of the child objects are returned in the **Children** member of an [**ACPI_ENUM_CHILDREN_OUTPUT_BUFFER**](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_enum_children_output_buffer) structure, where the **Children** member is an array of [**ACPI_ENUM_CHILD**](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_enum_child) structures. A driver can use the following macros to help process an array of ACPI_ENUM_CHILD structures:

[**ACPI_ENUM_CHILD_NEXT**](acpi-enum-child-next.md)

[**ACPI_ENUM_CHILD_LENGTH_FROM_CHILD**](acpi-enum-child-length-from-child.md)
