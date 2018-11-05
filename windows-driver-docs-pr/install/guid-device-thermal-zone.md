---
title: GUID_DEVICE_THERMAL_ZONE
description: GUID_DEVICE_THERMAL_ZONE
ms.assetid: bbb9abb8-aaff-4f1c-ba8d-96fc5b69676a
keywords: ["GUID_DEVICE_THERMAL_ZONE Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_DEVICE_THERMAL_ZONE
api_location:
- Poclass.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# GUID_DEVICE_THERMAL_ZONE


The GUID_DEVICE_THERMAL_ZONE [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for Advanced Configuration and Power Interface (ACPI) thermal zone devices.

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
<td align="left"><p>GUID_DEVICE_THERMAL_ZONE</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{4AFA3D51-74A7-11d0-be5e-00A0C9062857}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The system-supplied [ACPI driver](https://msdn.microsoft.com/library/windows/hardware/ff540493) registers an instance of this device interface class to notify the operating system and applications of the presence of thermal zone devices.

For information about supplying WDM [function drivers](https://msdn.microsoft.com/library/windows/hardware/ff546516) for ACPI devices, see [Supporting ACPI Devices](https://msdn.microsoft.com/library/windows/hardware/ff536161).

Requirements
------------

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

 

 





