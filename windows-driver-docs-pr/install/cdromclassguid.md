---
title: CdRomClassGuid
description: CdRomClassGuid
ms.assetid: 406c28c9-8ef3-4ccc-bb70-a13b8d1ad64e
keywords: ["CdRomClassGuid Device and Driver Installation"]
topic_type:
- apiref
api_name:
- CdRomClassGuid
api_location:
- Ntddstor.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# CdRomClassGuid


CdRomClassGuid is an obsolete identifier for the [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) for CD-ROM [storage devices](https://msdn.microsoft.com/library/windows/hardware/ff566969). Starting with Microsoft Windows 2000, use the [**GUID_DEVINTERFACE_CDROM**](guid-devinterface-cdrom.md) class identifier for new instances of this class.

Remarks
-------

The storage [samples](http://go.microsoft.com/fwlink/p/?LinkId=618052) in the WDK include the [CDROM class driver](http://go.microsoft.com/fwlink/p/?linkid=256093) sample and the [Addfilter Storage Filter Tool](http://go.microsoft.com/fwlink/p/?linkid=256076). The CDROM class driver sample uses CdRomClassGuid to register instances of the GUID_DEVINTERFACE_CDROM device interface class. The sample Addfilter application uses CdRomClassGuid to enumerate instances of the GUID_DEVINTERFACE_CDROM device interface class.

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
<td align="left"><p>Obsolete. Starting with Windows 2000, use GUID_DEVINTERFACE_CDROM instead.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ntddstor.h (include Ntddstor.h)</td>
</tr>
</tbody>
</table>

## See also


[**GUID_DEVINTERFACE_CDROM**](guid-devinterface-cdrom.md)

 

 






