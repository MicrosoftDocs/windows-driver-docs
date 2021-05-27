---
title: ACPI_ENUM_CHILD_LENGTH_FROM_CHILD macro
description: The ACPI_ENUM_CHILD_LENGTH_FROM_CHILD macro calculates the size, in bytes, of a variable-length ACPI_ENUM_CHILD structure.
keywords: 
- ACPI_ENUM_CHILD_LENGTH_FROM_CHILD macro ACPI Devices
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# ACPI\_ENUM\_CHILD\_LENGTH\_FROM\_CHILD macro


The ACPI\_ENUM\_CHILD\_LENGTH\_FROM\_CHILD macro calculates the size, in bytes, of a variable-length [**ACPI\_ENUM\_CHILD**](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_enum_child) structure.

## Syntax

```cpp
void ACPI_ENUM_CHILD_LENGTH_FROM_CHILD(
    Child
);
```

## Parameters

*Child*   
A pointer to a structure of type ACPI\_ENUM\_CHILD for which to calculate the size, in bytes, of the structure.

## Return value

The size, in bytes, of the ACPI\_ENUM\_CHILD structure that *Child* points to.

## Remarks

A driver can use this macro to calculate the size, in bytes, of the ACPI\_ENUM\_CHILD structures in an [**ACPI\_ENUM\_CHILDREN\_OUTPUT\_BUFFER**](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_enum_children_output_buffer) structure.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr>
<td><p>Target platform</p></td>
<td>Desktop</td>
</tr>
<tr>
<td><p>Header</p></td>
<td>Acpiioct.h (include Acpiioct.h)</td>
</tr>
</tbody>
</table>

## See also


[**ACPI\_ENUM\_CHILD**](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_enum_child)

[**ACPI\_ENUM\_CHILDREN\_OUTPUT\_BUFFER**](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_enum_children_output_buffer)

 

