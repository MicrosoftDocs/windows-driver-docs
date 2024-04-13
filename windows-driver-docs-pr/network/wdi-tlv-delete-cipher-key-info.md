---
title: WDI_TLV_DELETE_CIPHER_KEY_INFO
ms.topic: reference
description: WDI_TLV_DELETE_CIPHER_KEY_INFO is a TLV that contains information to identify a single cipher key to remove with OID_WDI_SET_DELETE_CIPHER_KEYS.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_DELETE_CIPHER_KEY_INFO Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_DELETE\_CIPHER\_KEY\_INFO

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_DELETE\_CIPHER\_KEY\_INFO is a TLV that contains information to identify a single cipher key to remove with [OID\_WDI\_SET\_DELETE\_CIPHER\_KEYS](./oid-wdi-set-delete-cipher-keys.md).

## TLV Type


0x53

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                      | Multiple TLV instances allowed | Optional | Description                                                                                                                |
|---------------------------------------------------------------------------|--------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_PEER\_MAC\_ADDRESS**](wdi-tlv-peer-mac-address.md)          |                                | X        | Specifies the peer MAC address. At least one of WDI\_TLV\_PEER\_MAC\_ADDRESS or WDI\_TLV\_CIPHER\_KEY\_ID must be present. |
| [**WDI\_TLV\_CIPHER\_KEY\_ID**](wdi-tlv-cipher-key-id.md)                |                                | X        | Specifies the cipher key ID. At least one of WDI\_TLV\_PEER\_MAC\_ADDRESS or WDI\_TLV\_CIPHER\_KEY\_ID must be present.    |
| [**WDI\_TLV\_CIPHER\_KEY\_TYPE\_INFO**](wdi-tlv-cipher-key-type-info.md) |                                |          | Specifies the cipher key type information.                                                                                 |

 

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
<td>Wditypes.hpp</td>
</tr>
</tbody>
</table>

 

