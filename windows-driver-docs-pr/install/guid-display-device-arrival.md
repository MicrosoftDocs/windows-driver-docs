---
title: GUID_DISPLAY_DEVICE_ARRIVAL
description: GUID_DISPLAY_DEVICE_ARRIVAL
ms.assetid: 4915c6b0-b9a7-4602-ae43-032e20353719
keywords: ["GUID_DISPLAY_DEVICE_ARRIVAL Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_DISPLAY_DEVICE_ARRIVAL
api_location:
- Ntddvdeo.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# GUID_DISPLAY_DEVICE_ARRIVAL


The GUID_DISPLAY_DEVICE_ARRIVAL [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for [display adapters](https://msdn.microsoft.com/library/windows/hardware/ff554044).

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
<td align="left"><p>GUID_DISPLAY_DEVICE_ARRIVAL</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{1CA05180-A699-450A-9A0C-DE4FBE3DDD89}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The system-supplied components of the [Windows Vista Display Driver Model](https://msdn.microsoft.com/library/windows/hardware/ff570593) register instances of this device interface class to notify the operating system and applications of the presence of display adapters.

For information about the device interface class for display views that are supported by display adapters, see [**GUID_DEVINTERFACE_DISPLAY_ADAPTER**](guid-devinterface-display-adapter.md).

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Available in Windows Vista and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ntddvdeo.h (include Ntddvdeo.h)</td>
</tr>
</tbody>
</table>

## See also


[**GUID_DEVINTERFACE_DISPLAY_ADAPTER**](guid-devinterface-display-adapter.md)

 

 






