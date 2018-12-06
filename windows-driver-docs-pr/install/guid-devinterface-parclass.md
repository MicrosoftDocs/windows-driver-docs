---
title: GUID_DEVINTERFACE_PARCLASS
description: GUID_DEVINTERFACE_PARCLASS
ms.assetid: d55195d4-f4f5-464f-a1ca-5fe0eafccb2a
keywords: ["GUID_DEVINTERFACE_PARCLASS Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_DEVINTERFACE_PARCLASS
api_location:
- Ntddpar.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# GUID_DEVINTERFACE_PARCLASS


The GUID_DEVINTERFACE_PARCLASS [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for devices that are attached to a [parallel port](https://msdn.microsoft.com/library/windows/hardware/ff544263).

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
<td align="left"><p>GUID_DEVINTERFACE_PARCLASS</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{811FC6A5-F728-11D0-A537-0000F8753ED1}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Drivers for parallel devices that are attached to parallel ports register instances of GUID_DEVINTERFACE_PARCLASS to notify the operating system and applications of the presence of parallel devices.

The system-supplied bus driver for parallel ports creates an instance of this device interface class for each hardware device that is attached to a parallel port.

For information about parallel devices and drivers, see [Parallel Devices Design Guide](https://msdn.microsoft.com/library/windows/hardware/ff544263).

For information about the device interface class for parallel ports, see [**GUID_DEVINTERFACE_PARALLEL**](guid-devinterface-parallel.md).

[**GUID_PARCLASS_DEVICE**](guid-parclass-device.md) is an obsolete identifier for this device interface class; for new instances of this class, use GUID_DEVINTERFACE_PARCLASS instead.

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
<td align="left"><p>Available in Microsoft Windows 2000 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ntddpar.h (include Ntddpar.h)</td>
</tr>
</tbody>
</table>

## See also


[**GUID_DEVINTERFACE_PARALLEL**](guid-devinterface-parallel.md)

[**GUID_PARCLASS_DEVICE**](guid-parclass-device.md)

 

 






