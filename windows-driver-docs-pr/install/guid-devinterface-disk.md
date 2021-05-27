---
title: GUID_DEVINTERFACE_DISK
description: GUID_DEVINTERFACE_DISK
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


The GUID_DEVINTERFACE_DISK [device interface class](./overview-of-device-interface-classes.md) is defined for hard disk [storage devices](../storage/index.md).

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

 

## Remarks

The system-supplied storage class drivers register an instance of GUID_DEVINTERFACE_DISK for a hard disk storage device.

The storage [samples](https://go.microsoft.com/fwlink/p/?LinkId=618052) in the WDK include the [disk class driver](/samples/browse/) sample and the [Addfilter Storage Filter Tool](/samples/browse/). The disk class driver sample uses the obsolete identifier [**DiskClassGuid**](diskclassguid.md) to register instances of the GUID_DEVINTERFACE_DISK device interface class. The sample Addfilter application uses DiskClassGuid to enumerate instances of GUID_DEVINTERFACE_DISK device interface class.

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


[**DiskClassGuid**](diskclassguid.md)

