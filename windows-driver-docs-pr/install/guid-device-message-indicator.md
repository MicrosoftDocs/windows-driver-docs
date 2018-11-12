---
title: GUID_DEVICE_MESSAGE_INDICATOR
description: GUID_DEVICE_MESSAGE_INDICATOR
ms.assetid: 6f48dbc7-dca7-4373-b5ff-83ebb5f5c266
keywords: ["GUID_DEVICE_MESSAGE_INDICATOR Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_DEVICE_MESSAGE_INDICATOR
api_location:
- Poclass.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# GUID_DEVICE_MESSAGE_INDICATOR


The GUID_DEVICE_MESSAGE_INDICATOR [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for Advanced Configuration and Power Interface (ACPI) message indicator devices.

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
<td align="left"><p>GUID_DEVICE_MESSAGE_INDICATOR</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{CD48A365-FA94-4CE2-A232-A1B764E5D8B4}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The system-supplied [ACPI driver](https://msdn.microsoft.com/library/windows/hardware/ff540493) registers an instance of this device interface class to notify the operating system and applications of the presence of ACPI message indicator devices.

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

 

 





