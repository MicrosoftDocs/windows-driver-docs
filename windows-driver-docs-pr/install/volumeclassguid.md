---
title: VolumeClassGuid
description: VolumeClassGuid
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


VolumeClassGuid is an obsolete identifier for the [device interface class](./overview-of-device-interface-classes.md) for volume devices. Starting with Microsoft Windows 2000, use the [**GUID_DEVINTERFACE_VOLUME**](guid-devinterface-volume.md) class identifier for new instances of this class.

## Remarks

The storage [samples](https://go.microsoft.com/fwlink/p/?LinkId=618052) in the WDK include an [Addfilter Storage Filter Tool](/samples/browse/) that uses VolumeClassGuid to enumerate instances of the [**GUID_DEVINTERFACE_VOLUME**](guid-devinterface-volume.md) device interface class.

## Requirements

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

