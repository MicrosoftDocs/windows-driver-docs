---
title: WDI_TLV_CIPHER_KEY_RECEIVE_SEQUENCE_COUNT
description: WDI_TLV_CIPHER_KEY_RECEIVE_SEQUENCE_COUNT is a TLV that contains the receive sequence count.
ms.assetid: 29AA9D90-834F-4043-B12A-87705EDC1DF0
ms.date: 07/18/2017
keywords:
 - WDI_TLV_CIPHER_KEY_RECEIVE_SEQUENCE_COUNT Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_CIPHER\_KEY\_RECEIVE\_SEQUENCE\_COUNT


WDI\_TLV\_CIPHER\_KEY\_RECEIVE\_SEQUENCE\_COUNT is a TLV that contains the receive sequence count.

## TLV Type


0x4F

## Length


The size (in bytes) of the array of UINT8 elements.

## Values


| Type       | Description                                                                                    |
|------------|------------------------------------------------------------------------------------------------|
| UINT8\[6\] | Specifies the initial 48-bit value of Packet Number (PN), which is used for replay protection. |

 

Requirements
------------

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

 

 




