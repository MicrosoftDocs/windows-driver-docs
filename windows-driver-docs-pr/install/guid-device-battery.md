---
title: GUID_DEVICE_BATTERY
description: GUID_DEVICE_BATTERY
ms.assetid: 8391b167-0d17-46bf-9320-4fceed54aead
keywords: ["GUID_DEVICE_BATTERY Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_DEVICE_BATTERY
api_location:
- Batclass.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# GUID_DEVICE_BATTERY


The GUID_DEVICE_BATTERY [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for [battery devices](https://msdn.microsoft.com/library/windows/hardware/ff536281).

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
<td align="left"><p>GUID_DEVICE_BATTERY</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{72631E54-78A4-11D0-BCF7-00AA00B7B32A}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The system-supplied [battery class driver](https://msdn.microsoft.com/library/windows/hardware/ff536278) registers an instance of this device interface class for a battery device on behalf of a battery miniclass driver.

For information about battery devices and drivers, see [Overview of System Battery Management](https://msdn.microsoft.com/library/windows/hardware/ff536300).

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
<td align="left">Batclass.h (include Batclass.h)</td>
</tr>
</tbody>
</table>

 

 





