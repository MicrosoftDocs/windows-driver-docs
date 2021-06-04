---
title: GUID_DEVINTERFACE_PARALLEL
description: GUID_DEVINTERFACE_PARALLEL
keywords: ["GUID_DEVINTERFACE_PARALLEL Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_DEVINTERFACE_PARALLEL
api_location:
- Ntddpar.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# GUID_DEVINTERFACE_PARALLEL


The GUID_DEVINTERFACE_PARALLEL [device interface class](./overview-of-device-interface-classes.md) is defined for [parallel ports](/previous-versions/ff544263(v=vs.85)) that support an IEEE 1284-compatible hardware interface.

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
<td align="left"><p>GUID_DEVINTERFACE_PARALLEL</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{97F76EF0-F883-11D0-AF1F-0000F800845C}</p></td>
</tr>
</tbody>
</table>

 

## Remarks

Drivers for parallel ports register instances of GUID_DEVINTERFACE_PARALLEL to notify the operating system and applications of the presence of parallel ports.

The system-supplied function driver for parallel ports registers an instance of this device class for a parallel port.

For information about parallel devices and drivers, see [Introduction to Parallel Ports and Devices](/previous-versions/ff543964(v=vs.85)).

For information about the device interface class for devices that are attached to a parallel port, see [**GUID_DEVINTERFACE_PARCLASS**](guid-devinterface-parclass.md).

[**GUID_PARALLEL_DEVICE**](guid-parallel-device.md) is an obsolete identifier for this device interface class; for new instances of this class, use GUID_DEVINTERFACE_PARALLEL instead.

## Requirements

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


[**GUID_DEVINTERFACE_PARCLASS**](guid-devinterface-parclass.md)

[**GUID_PARALLEL_DEVICE**](guid-parallel-device.md)

 

