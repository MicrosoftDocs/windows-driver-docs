---
title: GUID_DEVICE_LID
description: GUID_DEVICE_LID
keywords: ["GUID_DEVICE_LID Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_DEVICE_LID
api_location:
- Poclass.h
api_type:
- HeaderDef
ms.date: 10/17/2018
ms.topic: reference
---

# GUID_DEVICE_LID


The GUID_DEVICE_LID [device interface class](./overview-of-device-interface-classes.md) is defined for Advanced Configuration and Power Interface (ACPI) lid devices.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Attribute</th>
<th align="left">Setting</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Identifier</p></td>
<td align="left"><p>GUID_DEVICE_LID</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{4AFA3D52-74A7-11d0-be5e-00A0C9062857}</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The system-supplied [ACPI driver](../kernel/acpi-driver.md) registers instances of this device interface class to notify the operating system and applications of the presence of ACPI lid devices.

For information about supplying WDM [function drivers](../kernel/function-drivers.md) for ACPI devices, see [Supporting ACPI Devices](../acpi/supporting-acpi-devices.md).

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Poclass.h (include Poclass.h)</td>
</tr>
</tbody>
</table>

 

