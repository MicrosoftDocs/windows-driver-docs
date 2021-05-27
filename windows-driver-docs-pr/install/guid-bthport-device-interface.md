---
title: GUID_BTHPORT_DEVICE_INTERFACE
description: GUID_BTHPORT_DEVICE_INTERFACE
keywords: ["GUID_BTHPORT_DEVICE_INTERFACE Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_BTHPORT_DEVICE_INTERFACE
api_location:
- Bthdef.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# GUID_BTHPORT_DEVICE_INTERFACE


The GUID_BTHPORT_DEVICE_INTERFACE [device interface class](./overview-of-device-interface-classes.md) is defined for [Bluetooth radios](/previous-versions/windows/hardware/drivers/ff536596(v=vs.85)).

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
<td align="left"><p>GUID_BTHPORT_DEVICE_INTERFACE</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{0850302A-B344-4fda-9BE9-90576B8D46F0}</p></td>
</tr>
</tbody>
</table>

 

## Remarks

Drivers for [Bluetooth radios](/previous-versions/windows/hardware/drivers/ff536596(v=vs.85)) register instances of this device interface class to notify the operating system and applications of the presence of Bluetooth radios.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Available in Windows Vista, Windows XP SP2, and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Bthdef.h (include Bthdef.h)</td>
</tr>
</tbody>
</table>

 

