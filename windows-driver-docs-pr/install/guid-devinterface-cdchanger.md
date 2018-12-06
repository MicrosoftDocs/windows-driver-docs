---
title: GUID_DEVINTERFACE_CDCHANGER
description: GUID_DEVINTERFACE_CDCHANGER
ms.assetid: 9bcbe3d5-2057-44cb-a495-6edee14a9cbb
keywords: ["GUID_DEVINTERFACE_CDCHANGER Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_DEVINTERFACE_CDCHANGER
api_location:
- Ntddstor.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# GUID_DEVINTERFACE_CDCHANGER


The GUID_DEVINTERFACE_CDCHANGER [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for CD-ROM changer devices.

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
<td align="left"><p>GUID_DEVINTERFACE_CDCHANGER</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{53F56312-B6BF-11D0-94F2-00A0C91EFB8B}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The system-supplied CD-ROM [changer driver](https://msdn.microsoft.com/library/windows/hardware/ff551455) registers instances of GUID_DEVINTERFACE_CDCHANGER to notify the operating system and applications of the presence of CD-ROM changer devices.

For information about the device interface class for CD-ROM devices, see [**GUID_DEVINTERFACE_CDROM**](guid-devinterface-cdrom.md).

For information about storage devices, see [Storage Drivers](https://msdn.microsoft.com/library/windows/hardware/ff566976).

[**CdChangerClassGuid**](cdchangerclassguid.md) is an obsolete identifier for the GUID_DEVINTERFACE_CDCHANGER device interface class; for new instances of this class, use GUID_DEVINTERFACE_CDCHANGER instead.

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


[**CdChangerClassGuid**](cdchangerclassguid.md)

[**GUID_DEVINTERFACE_CDROM**](guid-devinterface-cdrom.md)

 

 






