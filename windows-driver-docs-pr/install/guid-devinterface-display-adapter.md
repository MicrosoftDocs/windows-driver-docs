---
title: GUID_DEVINTERFACE_DISPLAY_ADAPTER
description: GUID_DEVINTERFACE_DISPLAY_ADAPTER
ms.assetid: 22f705b0-bc79-43e8-8445-adf611ae1429
keywords: ["GUID_DEVINTERFACE_DISPLAY_ADAPTER Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_DEVINTERFACE_DISPLAY_ADAPTER
api_location:
- Ntddvdeo.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# GUID_DEVINTERFACE_DISPLAY_ADAPTER


The GUID_DEVINTERFACE_DISPLAY_ADAPTER [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for display views that are supported by display adapters.

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
<td align="left"><p>GUID_DEVINTERFACE_DISPLAY_ADAPTER</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{5B45201D-F2F2-4F3B-85BB-30FF1F953599}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The system-supplied display drivers register an instance of this device interface class to notify the operating system and applications of the presence of a display view.

For information about display devices, see [Windows Vista Display Driver Model](https://msdn.microsoft.com/library/windows/hardware/ff570593) and [Windows 2000 Display Driver Model](https://msdn.microsoft.com/library/windows/hardware/ff570584).

For information about the device interface class for display adapters, see [**GUID_DISPLAY_DEVICE_ARRIVAL**](guid-display-device-arrival.md).

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
<td align="left">Ntddvdeo.h (include Ntddvdeo.h)</td>
</tr>
</tbody>
</table>

## See also


[**GUID_DISPLAY_DEVICE_ARRIVAL**](guid-display-device-arrival.md)

 

 






