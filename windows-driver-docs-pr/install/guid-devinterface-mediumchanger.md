---
title: GUID_DEVINTERFACE_MEDIUMCHANGER
description: GUID_DEVINTERFACE_MEDIUMCHANGER
ms.assetid: d7c41c5c-b03b-459e-81b0-b363b4c174b0
keywords: ["GUID_DEVINTERFACE_MEDIUMCHANGER Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_DEVINTERFACE_MEDIUMCHANGER
api_location:
- Ntddstor.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# GUID_DEVINTERFACE_MEDIUMCHANGER


The GUID_DEVINTERFACE_MEDIUMCHANGER [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for medium changer devices.

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
<td align="left"><p>GUID_DEVINTERFACE_MEDIUMCHANGER</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{53F56310-B6BF-11D0-94F2-00A0C91EFB8B}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The system-supplied medium [changer drivers](https://msdn.microsoft.com/library/windows/hardware/ff551455) register an instance of GUID_DEVINTERFACE_MEDIUMCHANGER to notify the operating system and applications of the presence of medium changer devices.

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


[**MediumChangerClassGuid**](mediumchangerclassguid.md)

 

 






