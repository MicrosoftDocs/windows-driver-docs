---
title: Enumerating Child Devices and Control Methods
description: Provides information about enumerating child devices and control methods.
keywords:
- ACPI devices WDK , enumerating child devices
- ACPI devices WDK , enumerating control methods
- ACPI namespaces WDK
- ACPI control methods WDK , enumerating
ms.date: 08/17/2021
ms.localizationpriority: medium
---

# Enumerating Child Devices and Control Methods

In an ACPI namespace, an object that is a device--for example, a device named 'ABCD'--can have child objects that are child devices of the device or that are control methods that are supported by the device. Any child object that is a child device of a parent device can, in turn, recursively have child objects that are child devices or control methods.

For example, in the following simplified ACPI namespace, the root of the ACPI namespace is designated by '\\' and the object 'ABCD' is a device that is an immediate child of the root of the ACPI namespace. In addition, device 'ABCD' has two immediate child devices named 'CHL1' and 'CHL2' and a child object that is a control method named '_FOO.' In addition, the child device 'CHL2' has a child device named 'CHL3' and device "CHL3" has a child object that is a control method named '_FOO.'

```syntax
\     root of ACPI namespace
 ABCD            parent device 
    CHL1         child device of ABCD
    CHL2         child device of ABCD
       CHL3      child device of CHL2
          _FOO   control method
 _FOO            control method
```

To use [**IOCTL_ACPI_EVAL_METHOD_EX**](/windows-hardware/drivers/ddi/acpiioct/ni-acpiioct-ioctl_acpi_eval_method_ex) or [**IOCTL_ACPI_ASYNC_EVAL_METHOD_EX**](/windows-hardware/drivers/ddi/acpiioct/ni-acpiioct-ioctl_acpi_async_eval_method_ex), a driver for a device supplies the path and name of the control method in an ACPI namespace. To help obtain the path and name of a device and child objects of a device, Windows supports the [**IOCTL_ACPI_ENUM_CHILDREN**](/windows-hardware/drivers/ddi/acpiioct/ni-acpiioct-ioctl_acpi_enum_children) request. Referring to the simplified ACPI namespace provided in this section as an example, a driver in the device stack of device 'ABCD' can use this request to do the following:

- Enumerate device 'ABCD' and the immediate child devices of 'ABCD.' For example, the request can be used to return '\\ABCD,' '\\ABCD.CHL1,' and '\\ABCD.CHL2.'

- Recursively enumerate all the devices in the namespace of 'ABCD.' For example, the request can be used to return '\\ABCD,' '\\ABCD.CHL1,' '\\ABCD.CHL2,' and '\\ABCD.CHL2.CHL3.'

- Recursively enumerate all descendant child objects of 'ABCD' of a supplied name. The supplied name acts as a filter so that only those child objects that have the same name are enumerated. For example, for a supplied name '_FOO,' the request can be used to return '\\ABCD._FOO' and '\\ABCD.CHL2.CHL3._FOO.'

After a driver obtains the path and name of a control method, it can supply the path and name as input to **IOCTL_ACPI_EVAL_METHOD_EX** or **IOCTL_ACPI_ASYNC_EVAL_METHOD_EX**, as described in [Evaluating ACPI Control Methods Synchronously](evaluating-acpi-control-methods-synchronously.md).

An **IOCTL_ACPI_ENUM_CHILDREN** request takes as input a driver-allocated variable-length [**ACPI_ENUM_CHILDREN_INPUT_BUFFER**](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_enum_children_input_buffer) structure that contains the following members:

`Signature`

The signature of the input buffer, which must be set to ACPI_ENUM_CHILDREN_INPUT_BUFFER_SIGNATURE.

`Flags`

A flag that determines which objects in the ACPI namespace of a device that the ACPI driver enumerates. The ACPI driver returns the full path and name of the enumerated object beginning with the root of the ACPI namespace. The flag must be set to one of the following values:

| Flag | Description |
|--|--|
| ENUM_CHILDREN_IMMEDIATE_ONLY | Enumerates the device and enumerates the immediate child devices of the device. |
| ENUM_CHILDREN_MULTILEVEL | Enumerates the device and recursively enumerates all child devices of the device. |
| ENUM_CHILDREN_NAME_IS_FILTER | A bitwise OR of ENUM_CHILDREN and ENUM_CHILDREN_NAME_IS_FILTER enumerates the device's child objects whose name is identical to that supplied by the **Name** member. |

`NameLength`

The number of ASCII characters that the **Name** array contains.

`Name`

A NULL-terminated four-character ASCII array that contains the name of a child object that the ACPI driver uses to restrict the enumeration of child objects to those objects that have the same name.

The **IOCTL_ACPI_ENUM_CHILDREN** request returns the path and name of child objects in a driver-allocated variable-length [**ACPI_ENUM_CHILDREN_OUTPUT_BUFFER**](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_enum_children_output_buffer) that contains the following members:

`Signature`

The signature of the output buffer, which must be set to ACPI_ENUM_CHILDREN_OUTPUT_BUFFER_SIGNATURE.

`NumberOfChildren`

The number of elements of type [**ACPI_ENUM_CHILD**](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_enum_child) in the **Children** array.

`Children`

An array of elements of type **ACPI_ENUM_CHILD**. The **Name** member of an ACPI_ENUM_CHILD structure contains the path and name of the child object, and the **Flags** member indicates whether the child object has child objects.

If the output buffer that the driver allocates is not large enough to return all the enumerated child names, the ACPI driver returns no child names and sets the **Status** member of the IO_STATUS_BLOCK for the request to STATUS_BUFFER_OVERFLOW. In this case, if the size, in bytes, of the output buffer is at least **sizeof**(ACPI_ENUM_CHILDREN_OUTPUT_BUFFER_SIGNATURE), the ACPI driver also sets **NumberOfChildren** to the size, in bytes, that is required to retrieve the requested paths and names.

## See also

[Sending an IOCTL_ACPI_ENUM_CHILDREN Request](sending-an-ioctl-acpi-enum-children-request.md).
