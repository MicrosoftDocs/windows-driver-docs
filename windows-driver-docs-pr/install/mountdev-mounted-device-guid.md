---
title: MOUNTDEV_MOUNTED_DEVICE_GUID
description: MOUNTDEV_MOUNTED_DEVICE_GUID
keywords: ["MOUNTDEV_MOUNTED_DEVICE_GUID Device and Driver Installation"]
topic_type:
- apiref
api_name:
- MOUNTDEV_MOUNTED_DEVICE_GUID
api_location:
- Mountmgr.h
api_type:
- HeaderDef
ms.date: 10/17/2018
ms.topic: reference
---

# MOUNTDEV_MOUNTED_DEVICE_GUID


The MOUNTDEV_MOUNTED_DEVICE_GUID [device interface class](./overview-of-device-interface-classes.md) is defined for volume devices.

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
<td align="left"><p>MOUNTDEV_MOUNTED_DEVICE_GUID</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{53F5630D-B6BF-11D0-94F2-00A0C91EFB8B}</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The MOUNTDEV_MOUNTED_DEVICE_GUID identifier for this device interface class is an alias for the [**GUID_DEVINTERFACE_VOLUME**](guid-devinterface-volume.md) device interface class.

The storage [samples](https://go.microsoft.com/fwlink/p/?LinkId=618052) in the WDK includes the [ClassPnP Storage Class Driver Library](/samples/browse/) that uses MOUNTDEV_MOUNTED_DEVICE_GUID to register instances of the GUID_DEVINTERFACE_VOLUME device interface class.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Mountmgr.h (include Mountmgr.h)</td>
</tr>
</tbody>
</table>

## See also


[**GUID_DEVINTERFACE_VOLUME**](guid-devinterface-volume.md)

