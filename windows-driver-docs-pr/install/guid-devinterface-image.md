---
title: GUID_DEVINTERFACE_IMAGE
description: GUID_DEVINTERFACE_IMAGE
keywords: ["GUID_DEVINTERFACE_IMAGE Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_DEVINTERFACE_IMAGE
api_location:
- Wiaintfc.h
api_type:
- HeaderDef
ms.date: 10/17/2018
ms.topic: reference
---

# GUID_DEVINTERFACE_IMAGE


The GUID_DEVINTERFACE_IMAGE [device interface class](./overview-of-device-interface-classes.md) is defined for [WIA devices and Still Image (STI) devices](../image/index.md), including digital cameras and scanners.

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
<td align="left"><p>GUID_DEVINTERFACE_IMAGE</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{6BDD1FC6-810F-11D0-BEC7-08002BE2092F}</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The system-supplied kernel-mode drivers for WIA devices register an instance of this device interface class to notify the operating system and applications of the presence of WIA devices.

For information about WIA drivers and STI drivers, see [Windows Image Acquisition Drivers](../image/windows-image-acquisition-drivers.md).

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
<td align="left">Wiaintfc.h (include Wiaintfc.h)</td>
</tr>
</tbody>
</table>

 

