---
title: GUID_DEVICE_SYS_BUTTON
description: GUID_DEVICE_SYS_BUTTON
keywords: ["GUID_DEVICE_SYS_BUTTON Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_DEVICE_SYS_BUTTON
api_location:
- Poclass.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# GUID_DEVICE_SYS_BUTTON


The GUID_DEVICE_SYS_BUTTON [device interface class](./overview-of-device-interface-classes.md)is defined for Advanced Configuration and Power Interface (ACPI) system power button devices.

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
<td align="left"><p>GUID_DEVICE_SYS_BUTTON</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{4AFA3D53-74A7-11d0-be5e-00A0C9062857}</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The system-supplied [ACPI driver](../kernel/acpi-driver.md) registers an instance of this device interface class to notify the operating system and applications of the presence of system power button devices. I8042prt, the system-supplied driver for PS/2-style keyboard and mouse devices, also registers an instance of this class for a keyboard that supports a system power button.

For information about supplying WDM [function drivers](../kernel/function-drivers.md) for ACPI devices, see [Supporting ACPI Devices](../acpi/supporting-acpi-devices.md).

For information about PS/2-style keyboard and mouse devices, see [Non-HIDClass Keyboard and Mouse Devices](../hid/keyboard-and-mouse-class-drivers.md).

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

 

