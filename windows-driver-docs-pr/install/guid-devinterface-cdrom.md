---
title: GUID_DEVINTERFACE_CDROM
description: GUID_DEVINTERFACE_CDROM
keywords: ["GUID_DEVINTERFACE_CDROM Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_DEVINTERFACE_CDROM
api_location:
- Ntddstor.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# GUID_DEVINTERFACE_CDROM


The GUID_DEVINTERFACE_CDROM [device interface class](./overview-of-device-interface-classes.md) is defined for CD-ROM [storage devices](../storage/index.md).

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
<td align="left"><p>GUID_DEVINTERFACE_CDROM</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{53F56308-B6BF-11D0-94F2-00A0C91EFB8B}</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The system-supplied class driver for CD-ROM storage devices registers instances of this device interface class to notify the operating system and applications of the presence of a CD-ROM device.

The storage [samples](https://go.microsoft.com/fwlink/p/?LinkId=618052) in the WDK include the [CDROM class driver](/samples/browse/) sample and the [Addfilter Storage Filter Tool](/samples/browse/). The CD-ROM class driver sample uses the obsolete identifier [**CdRomClassGuid**](cdromclassguid.md) to register instances of the GUID_DEVINTERFACE_CDROM device interface class. The sample Addfilter application uses CdRomClassGuid to enumerate instances of the GUID_DEVINTERFACE_CDROM device interface class.

For information about the device interface class for CD-ROM changer devices, see [**GUID_DEVINTERFACE_CDCHANGER**](guid-devinterface-cdchanger.md).

For information about storage devices, see [Storage Drivers](../storage/storage-drivers.md).

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


[**CdRomClassGuid**](cdromclassguid.md)

[**GUID_DEVINTERFACE_CDCHANGER**](guid-devinterface-cdchanger.md)

