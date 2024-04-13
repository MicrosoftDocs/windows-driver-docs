---
title: WDI_TLV_NEXT_DIALOG_TOKEN
ms.topic: reference
description: WDI_TLV_NEXT_DIALOG_TOKEN is a TLV that contains the dialog token to be used in the next Action frame.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_NEXT_DIALOG_TOKEN Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_NEXT\_DIALOG\_TOKEN

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_NEXT\_DIALOG\_TOKEN is a TLV that contains the dialog token to be used in the next Action frame.

## TLV Type


0xE1

## Length


The size (in bytes) of a UINT8.

## Values


| Type  | Description                                           |
|-------|-------------------------------------------------------|
| UINT8 | The dialog token to be used in the next Action frame. |

 

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

## See also


[OID\_WDI\_GET\_NEXT\_ACTION\_FRAME\_DIALOG\_TOKEN](./oid-wdi-get-next-action-frame-dialog-token.md)

 

