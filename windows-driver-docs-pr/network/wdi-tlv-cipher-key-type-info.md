---
title: WDI_TLV_CIPHER_KEY_TYPE_INFO
description: WDI_TLV_CIPHER_KEY_TYPE_INFO is a TLV that contains cipher key type information for OID_WDI_SET_ADD_CIPHER_KEYS and OID_WDI_SET_DELETE_CIPHER_KEYS.
ms.date: 07/18/2017
keywords:
 - WDI_TLV_CIPHER_KEY_TYPE_INFO Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_CIPHER\_KEY\_TYPE\_INFO


WDI\_TLV\_CIPHER\_KEY\_TYPE\_INFO is a TLV that contains cipher key type information for [OID\_WDI\_SET\_ADD\_CIPHER\_KEYS](./oid-wdi-set-add-cipher-keys.md) and [OID\_WDI\_SET\_DELETE\_CIPHER\_KEYS](./oid-wdi-set-delete-cipher-keys.md).

## TLV Type


0x4E

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                                                 | Description                                                                                                                                                                                                                                                                                     |
|----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_CIPHER\_ALGORITHM**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_cipher_algorithm)          | Specifies the cipher algorithm that uses the key.                                                                                                                                                                                                                                               |
| [**WDI\_CIPHER\_KEY\_DIRECTION**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_cipher_key_direction) | Specifies whether the key should be used for transmit only, receive only, or both.                                                                                                                                                                                                              |
| UINT8                                                                | Specifies whether the port should delete the key on a roam. If this value is set to 0, the key must be deleted when the port disconnects from the BSS network or connects to the BSS network. If this value is set to 1, the key should be deleted on an explicit delete or on a reset request. |
| [**WDI\_CIPHER\_KEY\_TYPE**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_cipher_key_type)           | Specifies the type of key being published.                                                                                                                                                                                                                                                      |

 

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

 

