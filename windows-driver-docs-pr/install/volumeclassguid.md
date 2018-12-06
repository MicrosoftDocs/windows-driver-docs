---
title: VolumeClassGuid
description: VolumeClassGuid
ms.assetid: 30d0db03-fbea-4245-b8d7-ca3a06a54861
keywords: ["VolumeClassGuid Device and Driver Installation"]
topic_type:
- apiref
api_name:
- VolumeClassGuid
api_location:
- Ntddstor.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# VolumeClassGuid


VolumeClassGuid is an obsolete identifier for the [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) for volume devices. Starting with Microsoft Windows 2000, use the [**GUID_DEVINTERFACE_VOLUME**](guid-devinterface-volume.md) class identifier for new instances of this class.

Remarks
-------

The storage [samples](http://go.microsoft.com/fwlink/p/?LinkId=618052) in the WDK include an [Addfilter Storage Filter Tool](http://go.microsoft.com/fwlink/p/?linkid=256076) that uses VolumeClassGuid to enumerate instances of the [**GUID_DEVINTERFACE_VOLUME**](guid-devinterface-volume.md) device interface class.

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
<td align="left"><p>Obsolete. Starting with Windows 2000, use GUID_DEVINTERFACE_VOLUME instead.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ntddstor.h (include Ntddstor.h)</td>
</tr>
</tbody>
</table>

## See also


[**GUID_DEVINTERFACE_VOLUME**](guid-devinterface-volume.md)

 

 






