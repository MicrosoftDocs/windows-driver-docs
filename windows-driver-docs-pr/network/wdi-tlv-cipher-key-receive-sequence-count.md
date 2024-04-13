---
title: WDI_TLV_CIPHER_KEY_RECEIVE_SEQUENCE_COUNT
ms.topic: reference
description: WDI_TLV_CIPHER_KEY_RECEIVE_SEQUENCE_COUNT is a TLV that contains the receive sequence count.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_CIPHER_KEY_RECEIVE_SEQUENCE_COUNT Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_CIPHER\_KEY\_RECEIVE\_SEQUENCE\_COUNT

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_CIPHER\_KEY\_RECEIVE\_SEQUENCE\_COUNT is a TLV that contains the receive sequence count.

## TLV Type


0x4F

## Length


The size (in bytes) of the array of UINT8 elements.

## Values


| Type       | Description                                                                                    |
|------------|------------------------------------------------------------------------------------------------|
| UINT8\[6\] | Specifies the initial 48-bit value of Packet Number (PN), which is used for replay protection. |

 

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

 

 




