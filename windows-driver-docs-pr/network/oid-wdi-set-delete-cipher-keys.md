---
title: OID_WDI_SET_DELETE_CIPHER_KEYS
ms.topic: reference
description: OID_WDI_SET_DELETE_CIPHER_KEYS deletes cipher keys from the device's cipher key table.
ms.date: 03/02/2023
keywords:
 - OID_WDI_SET_DELETE_CIPHER_KEYS Network Drivers Starting with Windows Vista
ms.custom: 19H1
---

# OID\_WDI\_SET\_DELETE\_CIPHER\_KEYS

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


OID\_WDI\_SET\_DELETE\_CIPHER\_KEYS deletes cipher keys from the device's cipher key table.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | Yes                      | 1                               |

 

## Set property parameters


| TLV                                                                                | Multiple TLV instances allowed | Optional | Description                                                |
|------------------------------------------------------------------------------------|--------------------------------|----------|------------------------------------------------------------|
| [**WDI\_TLV\_DELETE\_CIPHER\_KEY\_INFO**](./wdi-tlv-delete-cipher-key-info.md) | X                              |          | The cipher keys to be deleted from the device's key table. |

 

## Set property results


No additional data. The data in the header is sufficient.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Minimum supported client</p></td>
<td><p>Windows 10</p></td>
</tr>
<tr class="even">
<td><p>Minimum supported server</p></td>
<td><p>Windows Server 2016</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Dot11wdi.h</td>
</tr>
</tbody>
</table>

## See also


[OID\_WDI\_SET\_ADD\_CIPHER\_KEYS](oid-wdi-set-add-cipher-keys.md)

 

