---
title: DiskClassGuid
description: DiskClassGuid
ms.assetid: eeefc86c-caff-4d1c-b2c1-aefde3bd21ed
keywords: ["DiskClassGuid Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DiskClassGuid
api_location:
- Ntddstor.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DiskClassGuid


DiskClassGuid is an obsolete identifier for the device interface class for hard disk [storage devices](https://msdn.microsoft.com/library/windows/hardware/ff566969). Starting with Microsoft Windows 2000, use the [**GUID_DEVINTERFACE_DISK**](guid-devinterface-disk.md) class identifier for new instances of this class.

Remarks
-------

The storage [samples](http://go.microsoft.com/fwlink/p/?LinkId=618052) in the WDK include the [disk class driver](http://go.microsoft.com/fwlink/p/?linkid=256103) sample and the [Addfilter Storage Filter Tool](http://go.microsoft.com/fwlink/p/?linkid=256076). The disk class driver sample uses DiskClassGuid to register instances of the GUID_DEVINTERFACE_DISK device interface class. The sample Addfilter application uses DiskClassGuid to enumerate instances of the GUID_DEVINTERFACE_DISK device interface class.

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
<td align="left"><p>Obsolete. Starting with Windows 2000, use GUID_DEVINTERFACE_DISK instead.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ntddstor.h (include Ntddstor.h)</td>
</tr>
</tbody>
</table>

## See also


[**GUID_DEVINTERFACE_DISK**](guid-devinterface-disk.md)

 

 






