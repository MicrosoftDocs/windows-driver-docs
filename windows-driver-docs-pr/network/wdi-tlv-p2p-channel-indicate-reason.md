---
title: WDI_TLV_P2P_CHANNEL_INDICATE_REASON
ms.topic: reference
description: WDI_TLV_P2P_CHANNEL_INDICATE_REASON is a TLV that contains a reason for sending an indication.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_P2P_CHANNEL_INDICATE_REASON Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_CHANNEL\_INDICATE\_REASON

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_P2P\_CHANNEL\_INDICATE\_REASON is a TLV that contains a reason for sending an indication.

## TLV Type


0x102

## Length


The size (in bytes) of a UINT32.

## Values


| Type   | Description                                                                                                                                         |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT32 | The reason for sending an indication. See [**WDI\_P2P\_CHANNEL\_INDICATE\_REASON**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_p2p_channel_indicate_reason) for possible reasons. |

 

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

 

