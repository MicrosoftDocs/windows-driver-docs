---
title: GUID_DEVINTERFACE_DISK
description: GUID_DEVINTERFACE_DISK
ms.assetid: 47782789-4504-4705-8c32-4d2bc508a7e2
keywords: ["GUID_DEVINTERFACE_DISK Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_DEVINTERFACE_DISK
api_location:
- Ntddstor.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# GUID_DEVINTERFACE_DISK


The GUID_DEVINTERFACE_DISK [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for hard disk [storage devices](https://msdn.microsoft.com/library/windows/hardware/ff566969).

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
<td align="left"><p>GUID_DEVINTERFACE_DISK</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{53F56307-B6BF-11D0-94F2-00A0C91EFB8B}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The system-supplied storage class drivers register an instance of GUID_DEVINTERFACE_DISK for a hard disk storage device.

The storage [samples](http://go.microsoft.com/fwlink/p/?LinkId=618052) in the WDK include the [disk class driver](http://go.microsoft.com/fwlink/p/?linkid=256103) sample and the [Addfilter Storage Filter Tool](http://go.microsoft.com/fwlink/p/?linkid=256076). The disk class driver sample uses the obsolete identifier [**DiskClassGuid**](diskclassguid.md) to register instances of the GUID_DEVINTERFACE_DISK device interface class. The sample Addfilter application uses DiskClassGuid to enumerate instances of GUID_DEVINTERFACE_DISK device interface class.

For information about storage drivers, see [Storage Drivers](https://msdn.microsoft.com/library/windows/hardware/ff566976).

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


[**DiskClassGuid**](diskclassguid.md)

 

 






