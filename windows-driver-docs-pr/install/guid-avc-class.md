---
title: GUID_AVC_CLASS
description: GUID_AVC_CLASS
keywords: ["GUID_AVC_CLASS Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_AVC_CLASS
api_location:
- Avc.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# GUID_AVC_CLASS


The GUID_AVC_CLASS [device interface class](./overview-of-device-interface-classes.md) is defined for audio video control (AV/C) devices that are supported by the [AVStream](../stream/avstream-overview.md) architecture.

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
<td align="left"><p>GUID_AVC_CLASS</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{095780C3-48A1-4570-BD95-46707F78C2DC}</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The system-supplied [AV/C client driver](../stream/av-c-client-drivers2.md) [Avc.sys](../stream/using-avc-sys.md) registers an instance of GUID_AVC_CLASS to represent an external AV/C unit on a 1394 bus.

For information about the device interface class for virtual AV/C devices, see [**GUID_VIRTUAL_AVC_CLASS**](guid-virtual-avc-class.md).

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Available in Windows Vista, Windows Server 2003, Windows XP and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Avc.h (include Avc.h)</td>
</tr>
</tbody>
</table>

## See also


[**GUID_VIRTUAL_AVC_CLASS**](guid-virtual-avc-class.md)

 

