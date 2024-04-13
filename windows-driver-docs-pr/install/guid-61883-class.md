---
title: GUID_61883_CLASS
description: GUID_61883_CLASS
keywords: ["GUID_61883_CLASS Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_61883_CLASS
api_location:
- 61883.h
api_type:
- HeaderDef
ms.date: 10/17/2018
ms.topic: reference
---

# GUID_61883_CLASS


The GUID_61883_CLASS [device interface class](./overview-of-device-interface-classes.md) is defined for devices in the 61883 [device setup class](./overview-of-device-setup-classes.md).

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
<td align="left"><p>GUID_61883_CLASS</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{7EBEFBC0-3200-11d2-B4C2-00A0C9697D07}</p></td>
</tr>
</tbody>
</table>

 

## Remarks

Drivers for devices in the 61883 device setup class register instances of this device interface class to notify the operating system and applications of the presence of 61883 devices. The 61883 device interface class includes IEEE 1394 devices that support the IEC-61883 protocol. For information about 61883 devices and drivers, see [IEC-61883 Client Drivers](../ieee/iec-61883-client-drivers.md).

For information about the device setup class for 1394 bus devices, see [**BUS1394_CLASS_GUID**](bus1394-class-guid.md).

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Available in Windows XP and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">61883.h (include 61883.h)</td>
</tr>
</tbody>
</table>

## See also


[**BUS1394_CLASS_GUID**](bus1394-class-guid.md)

 

