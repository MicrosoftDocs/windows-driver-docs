---
title: Control Method Input Buffer Structures
description: Provides information about control method input buffer structures
ms.date: 08/17/2021
ms.localizationpriority: medium
---

# Control Method Input Buffer Structures

The ACPI driver supports the [**IOCTL_ACPI_EVAL_METHOD**](/windows-hardware/drivers/ddi/acpiioct/ni-acpiioct-ioctl_acpi_eval_method) request. A driver for a device can use this request to evaluate a control method that is an immediate child object in the ACPI namespace of the device to which the request is sent. The **IOCTL_ACPI_EVAL_METHOD** request supports the following input structures:

| Input structure | Description |
|--|--|
| [**ACPI_EVAL_INPUT_BUFFER**](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_eval_input_buffer_v1) | Supplies the signature of the buffer and the name of a control method that does not take an input argument. |
| [**ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER**](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_eval_input_buffer_simple_integer_v1) | Supplies the signature of the structure, the name of a control method, and a single input argument value of type ULONG. |
| [**ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING**](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_eval_input_buffer_simple_string_v1) | Supplies the signature of the structure, the name of a control method, and an input argument that is a NULL-terminated ASCII string. |
| [**ACPI_EVAL_INPUT_BUFFER_COMPLEX**](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_eval_input_buffer_complex_v1) | Supplies the signature of the structure, the name of a control method, and an input array of [**ACPI_METHOD_ARGUMENT**](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_method_argument_v1) structures. The array can contain a maximum number of seven such structures. An ACPI_METHOD_ARGUMENT structure can contain a ULONG integer, an ASCII string, an ACPI package description, or an array of custom data. |

Windows also supports the [**IOCTL_ACPI_EVAL_METHOD_EX**](/windows-hardware/drivers/ddi/acpiioct/ni-acpiioct-ioctl_acpi_eval_method_ex) request. A driver for a device can use this request to evaluate a control method that is a descendant child object in the ACPI namespace of the device to which the request is sent. The **IOCTL_ACPI_EVAL_METHOD_EX** request supports the following input structures:

| Input structure | Description |
|--|--|
| [**ACPI_EVAL_INPUT_BUFFER_EX**](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_eval_input_buffer_v1_ex) | supplies the signature of the structure and the path and name of a control method that does not take an input argument. |
| [**ACPI_EVAL_INPUT_BUFFER_SIMPLE_INTEGER_EX**](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_eval_input_buffer_simple_integer_v1_ex) | supplies the signature of the structure and the path and name of a control method that takes a single integer of type ULONG64 as an input argument. |
| [**ACPI_EVAL_INPUT_BUFFER_SIMPLE_STRING_EX**](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_eval_input_buffer_simple_string_v1_ex) | supplies the signature of the structure and the path and name of a control method that takes a single NULL-terminated ASCII string as an input argument. |
| [**ACPI_EVAL_INPUT_BUFFER_COMPLEX_EX**](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_eval_input_buffer_complex_v1_ex) | supplies the signature of the structure and the path and name of a control method that takes an array of **ACPI_METHOD_ARGUMENT** structures as input. The array can contain a maximum number of seven such structures. An **ACPI_METHOD_ARGUMENT** structure can contain a ULONG integer, an ASCII string, an ACPI package description, or an array of custom data. |

To obtain the path and name of child objects in the ACPI namespace of a device, a driver for a device can use an [**IOCTL_ACPI_ENUM_CHILDREN**](/windows-hardware/drivers/ddi/acpiioct/ni-acpiioct-ioctl_acpi_enum_children) request, as described in [Enumerating Child Devices and Control Methods](enumerating-child-devices-and-control-methods.md).
