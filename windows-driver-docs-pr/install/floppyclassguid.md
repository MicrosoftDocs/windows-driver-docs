---
title: FloppyClassGuid
description: FloppyClassGuid
ms.assetid: 60811704-0a59-48b4-b9c6-baf6c0f8c1c2
keywords: ["FloppyClassGuid Device and Driver Installation"]
topic_type:
- apiref
api_name:
- FloppyClassGuid
api_location:
- Ntddstor.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# FloppyClassGuid


FloppyClassGuid is an obsolete identifier for the [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) for floppy disk [storage devices](https://msdn.microsoft.com/library/windows/hardware/ff566969). Starting Microsoft Windows 2000, use the [**GUID_DEVINTERFACE_FLOPPY**](guid-devinterface-floppy.md) class identifier for new instances of this class.

Remarks
-------

The storage [samples](http://go.microsoft.com/fwlink/p/?LinkId=618052) in the WDK include a [floppy driver](http://go.microsoft.com/fwlink/p/?linkid=256192) sample that uses FloppyClassGuid to register instances of this device interface class.

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
<td align="left"><p>Obsolete. Starting with Windows 2000, use GUID_DEVINTERFACE_FLOPPY instead.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ntddstor.h (include Ntddstor.h)</td>
</tr>
</tbody>
</table>

## See also


[**GUID_DEVINTERFACE_FLOPPY**](guid-devinterface-floppy.md)

 

 






