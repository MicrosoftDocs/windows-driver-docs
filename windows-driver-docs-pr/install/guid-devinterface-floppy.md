---
title: GUID_DEVINTERFACE_FLOPPY
description: GUID_DEVINTERFACE_FLOPPY
keywords: ["GUID_DEVINTERFACE_FLOPPY Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_DEVINTERFACE_FLOPPY
api_location:
- Ntddstor.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# GUID_DEVINTERFACE_FLOPPY


The GUID_DEVINTERFACE_FLOPPY [device interface class](./overview-of-device-interface-classes.md) is defined for floppy disk [storage devices](../storage/index.md).

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
<td align="left"><p>GUID_DEVINTERFACE_FLOPPY</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{53F56311-B6BF-11D0-94F2-00A0C91EFB8B}</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The system-supplied storage class driver for floppy disk storage devices registers an instance of GUID_DEVINTERFACE_FLOPPY for a floppy disk storage device.

The storage [samples](https://go.microsoft.com/fwlink/p/?LinkId=618052) in the WDK include a [floppy driver](/samples/browse/) sample that uses the obsolete identifier [**FloppyClassGuid**](floppyclassguid.md) to register an instance of the GUID_DEVINTERFACE_FLOPPY device interface class.

For information about storage drivers, see [Storage Drivers](../storage/storage-drivers.md).

## Requirements

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


[**FloppyClassGuid**](floppyclassguid.md)

