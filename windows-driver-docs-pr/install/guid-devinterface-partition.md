---
title: GUID_DEVINTERFACE_PARTITION
description: GUID_DEVINTERFACE_PARTITION
ms.assetid: c489b62a-167d-47a9-bfeb-fdd40cc8dece
keywords: ["GUID_DEVINTERFACE_PARTITION Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_DEVINTERFACE_PARTITION
api_location:
- Ntddstor.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# GUID_DEVINTERFACE_PARTITION


The GUID_DEVINTERFACE_PARTITION [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for partition devices.

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
<td align="left"><p>GUID_DEVINTERFACE_PARTITION</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{53F5630A-B6BF-11D0-94F2-00A0C91EFB8B}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The system-supplied [storage drivers](https://msdn.microsoft.com/library/windows/hardware/ff566976) register an instance of GUID_DEVINTERFACE_PARTITION for a partition that is a child device of a [storage device](https://msdn.microsoft.com/library/windows/hardware/ff566969).

[**PartitionClassGuid**](partitionclassguid.md) is an obsolete identifier for the GUID_DEVINTERFACE_PARTITION device interface class. For new instances of this class, use GUID_DEVINTERFACE_PARTITION instead.

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
<td align="left">Ntddstor.h (include Ntddstor.h)</td>
</tr>
</tbody>
</table>

## See also


[**PartitionClassGuid**](partitionclassguid.md)

 

 






