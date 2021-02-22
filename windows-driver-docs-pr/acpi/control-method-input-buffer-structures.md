---
title: Control Method Input Buffer Structures
description: Control Method Input Buffer Structures
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Control Method Input Buffer Structures


The ACPI driver supports the [**IOCTL\_ACPI\_EVAL\_METHOD**](/windows-hardware/drivers/ddi/acpiioct/ni-acpiioct-ioctl_acpi_eval_method) request. A driver for a device can use this request to evaluate a control method that is an immediate child object in the ACPI namespace of the device to which the request is sent. The IOCTL\_ACPI\_EVAL\_METHOD request supports the following input structures:

<a href="" id="acpi-eval-input-buffer"></a>[**ACPI\_EVAL\_INPUT\_BUFFER**](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_eval_input_buffer_v1)  
This structure supplies the signature of the buffer and the name of a control method that does not take an input argument.

<a href="" id="acpi-eval-input-buffer-simple-integer"></a>[**ACPI\_EVAL\_INPUT\_BUFFER\_SIMPLE\_INTEGER**](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_eval_input_buffer_simple_integer_v1)  
This structure supplies the signature of the structure, the name of a control method, and a single input argument value of type ULONG.

<a href="" id="acpi-eval-input-buffer-simple-string"></a>[**ACPI\_EVAL\_INPUT\_BUFFER\_SIMPLE\_STRING**](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_eval_input_buffer_simple_string_v1)  
This structure supplies the signature of the structure, the name of a control method, and an input argument that is a NULL-terminated ASCII string.

<a href="" id="acpi-eval-input-buffer-complex"></a>[**ACPI\_EVAL\_INPUT\_BUFFER\_COMPLEX**](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_eval_input_buffer_complex_v1)  
This structure supplies the signature of the structure, the name of a control method, and an input array of [**ACPI\_METHOD\_ARGUMENT**](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_method_argument_v1) structures. The array can contain a maximum number of seven such structures. An ACPI\_METHOD\_ARGUMENT structure can contain a ULONG integer, an ASCII string, an ACPI package description, or an array of custom data.

Windows also supports the [**IOCTL\_ACPI\_EVAL\_METHOD\_EX**](/windows-hardware/drivers/ddi/acpiioct/ni-acpiioct-ioctl_acpi_eval_method_ex) request. A driver for a device can use this request to evaluate a control method that is a descendant child object in the ACPI namespace of the device to which the request is sent. The IOCTL\_ACPI\_EVAL\_METHOD\_EX request supports the following input structures:

<a href="" id="acpi-eval-input-buffer-ex"></a>[**ACPI\_EVAL\_INPUT\_BUFFER\_EX**](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_eval_input_buffer_v1_ex)  
This structure supplies the signature of the structure and the path and name of a control method that does not take an input argument.

<a href="" id="acpi-eval-input-buffer-simple-integer-ex"></a>[**ACPI\_EVAL\_INPUT\_BUFFER\_SIMPLE\_INTEGER\_EX**](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_eval_input_buffer_simple_integer_v1_ex)  
This structure supplies the signature of the structure and the path and name of a control method that takes a single integer of type ULONG64 as an input argument.

<a href="" id="acpi-eval-input-buffer-simple-string-ex"></a>[**ACPI\_EVAL\_INPUT\_BUFFER\_SIMPLE\_STRING\_EX**](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_eval_input_buffer_simple_string_v1_ex)  
This structure supplies the signature of the structure and the path and name of a control method that takes a single NULL-terminated ASCII string as an input argument.

<a href="" id="acpi-eval-input-buffer-complex-ex"></a>[**ACPI\_EVAL\_INPUT\_BUFFER\_COMPLEX\_EX**](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_eval_input_buffer_complex_v1_ex)  
This structure supplies the signature of the structure and the path and name of a control method that takes an array of ACPI\_METHOD\_ARGUMENT structures as input. The array can contain a maximum number of seven such structures. An ACPI\_METHOD\_ARGUMENT structure can contain a ULONG integer, an ASCII string, an ACPI package description, or an array of custom data.

To obtain the path and name of child objects in the ACPI namespace of a device, a driver for a device can use an [**IOCTL\_ACPI\_ENUM\_CHILDREN**](/windows-hardware/drivers/ddi/acpiioct/ni-acpiioct-ioctl_acpi_enum_children) request, as described in [Enumerating Child Devices and Control Methods](enumerating-child-devices-and-control-methods.md).
