---
title: GUID_DEVICE_APPLICATIONLAUNCH_BUTTON
description: GUID_DEVICE_APPLICATIONLAUNCH_BUTTON
keywords: ["GUID_DEVICE_APPLICATIONLAUNCH_BUTTON Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_DEVICE_APPLICATIONLAUNCH_BUTTON
api_location:
- Poclass.h
api_type:
- HeaderDef
ms.date: 10/17/2018
ms.topic: reference
---

# GUID_DEVICE_APPLICATIONLAUNCH_BUTTON


The GUID_DEVICE_APPLICATIONLAUNCH_BUTTON [device interface class](./overview-of-device-interface-classes.md) is defined for Advanced Configuration and Power Interface (ACPI) application start buttons.

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
<td align="left"><p>GUID_DEVICE_APPLICATIONLAUNCH_BUTTON</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{629758EE-986E-4D9E-8E47-DE27F8AB054D}</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The system-supplied [ACPI driver](../kernel/acpi-driver.md) registers an instance of this device interface class to notify the operating system and applications of the presence of ACPI application start buttons.

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

 

