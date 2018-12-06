---
title: GUID_DEVINTERFACE_TAPE
description: GUID_DEVINTERFACE_TAPE
ms.assetid: af19bdf6-5205-4fc1-842f-081e34ea2337
keywords: ["GUID_DEVINTERFACE_TAPE Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_DEVINTERFACE_TAPE
api_location:
- Ntddstor.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# GUID_DEVINTERFACE_TAPE


The GUID_DEVINTERFACE_TAPE [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for tape [storage devices](https://msdn.microsoft.com/library/windows/hardware/ff566969).

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
<td align="left"><p>GUID_DEVINTERFACE_TAPE</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{53F5630B-B6BF-11D0-94F2-00A0C91EFB8B}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The system-supplied [tape class driver](https://msdn.microsoft.com/library/windows/hardware/ff567961) registers an instance of GUID_DEVINTERFACE_TAPE to notify the operating system and applications of the presence of tape storage devices.

For more information about storage drivers, see [Storage Drivers](https://msdn.microsoft.com/library/windows/hardware/ff566976).

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
<td align="left">Ntddstor.h (include Ntddstor.h)</td>
</tr>
</tbody>
</table>

## See also


[**TapeClassGuid**](tapeclassguid.md)

 

 






