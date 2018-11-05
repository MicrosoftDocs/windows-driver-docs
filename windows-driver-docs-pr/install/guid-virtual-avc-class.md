---
title: GUID_VIRTUAL_AVC_CLASS
description: GUID_VIRTUAL_AVC_CLASS
ms.assetid: bd577fd7-f50c-4477-9619-8dd9e849367a
keywords: ["GUID_VIRTUAL_AVC_CLASS Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_VIRTUAL_AVC_CLASS
api_location:
- Avc.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# GUID_VIRTUAL_AVC_CLASS


The GUID_VIRTUAL_AVC_CLASS [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for virtual audio video control (AV/C) devices that are supported by the [AVStream](https://msdn.microsoft.com/library/windows/hardware/ff554240) architecture.

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
<td align="left"><p>GUID_VIRTUAL_AVC_CLASS</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{616EF4D0-23CE-446D-A568-C31EB01913D0}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The system-supplied [AV/C client driver](https://msdn.microsoft.com/library/windows/hardware/ff556367) [Avc.sys](https://msdn.microsoft.com/library/windows/hardware/ff568667) registers an instance of GUID_VIRTUAL_AVC_CLASS to represent a virtual AV/C device.

For information about the device interface class for AV/C units on a 1394 bus, see [**GUID_AVC_CLASS**](guid-avc-class.md).

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
<td align="left"><p>Available in Windows Vista, Microsoft Windows Server 2003, Windows XP and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Avc.h (include Avc.h)</td>
</tr>
</tbody>
</table>

## See also


[**GUID_AVC_CLASS**](guid-avc-class.md)

 

 






