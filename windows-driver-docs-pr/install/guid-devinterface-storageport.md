---
title: GUID_DEVINTERFACE_STORAGEPORT
description: GUID_DEVINTERFACE_STORAGEPORT
keywords: ["GUID_DEVINTERFACE_STORAGEPORT Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_DEVINTERFACE_STORAGEPORT
api_location:
- Ntddstor.h
api_type:
- HeaderDef
ms.date: 10/17/2018
ms.topic: reference
---

# GUID_DEVINTERFACE_STORAGEPORT


The GUID_DEVINTERFACE_STORAGEPORT [device interface class](./overview-of-device-interface-classes.md) is defined for [storage port devices](../storage/storage-port-drivers.md).

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
<td align="left"><p>GUID_DEVINTERFACE_STORAGEPORT</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{2ACCFE60-C130-11D2-B082-00A0C91EFB8B}</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The system-supplied drivers for storage port devices register instances of GUID_DEVINTERFACE_STORAGEPORT to notify the operating system and applications of the presence of storage device adapters.

For more information about storage drivers, see [Storage Drivers](../storage/storage-drivers.md).

[**StoragePortClassGuid**](storageportclassguid.md) is an obsolete identifier for the GUID_DEVINTERFACE_STORAGEPORT device interface class. For new instances of this class, use GUID_DEVINTERFACE_STORAGEPORT instead.

## Requirements

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


[**StoragePortClassGuid**](storageportclassguid.md)

 

