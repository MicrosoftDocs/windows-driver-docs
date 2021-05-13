---
title: FloppyClassGuid
description: FloppyClassGuid
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


FloppyClassGuid is an obsolete identifier for the [device interface class](./overview-of-device-interface-classes.md) for floppy disk [storage devices](../storage/index.md). Starting Microsoft Windows 2000, use the [**GUID_DEVINTERFACE_FLOPPY**](guid-devinterface-floppy.md) class identifier for new instances of this class.

## Remarks

The storage [samples](https://go.microsoft.com/fwlink/p/?LinkId=618052) in the WDK include a [floppy driver](/samples/browse/) sample that uses FloppyClassGuid to register instances of this device interface class.

## Requirements

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

