---
title: WDI_TLV_DEFAULT_TX_KEY_ID_PARAMETERS
ms.topic: reference
description: WDI_TLV_DEFAULT_TX_KEY_ID_PARAMETERS is a TLV that contains the default key ID for packet transmission on a port for OID_WDI_SET_DEFAULT_KEY_ID.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_DEFAULT_TX_KEY_ID_PARAMETERS Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_DEFAULT\_TX\_KEY\_ID\_PARAMETERS

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_DEFAULT\_TX\_KEY\_ID\_PARAMETERS is a TLV that contains the default key ID for packet transmission on a port for [OID\_WDI\_SET\_DEFAULT\_KEY\_ID](./oid-wdi-set-default-key-id.md).

## TLV Type


0x54

## Length


The size (in bytes) of a UINT32.

## Values


| Type   | Description                                                     |
|--------|-----------------------------------------------------------------|
| UINT32 | Specifies the default key ID for packet transmission on a port. |

 

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

 

