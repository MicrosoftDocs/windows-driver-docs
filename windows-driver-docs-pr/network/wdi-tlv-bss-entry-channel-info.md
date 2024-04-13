---
title: WDI_TLV_BSS_ENTRY_CHANNEL_INFO
ms.topic: reference
description: WDI_TLV_BSS_ENTRY_CHANNEL_INFO is a TLV that contains BSS entry channel information.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_BSS_ENTRY_CHANNEL_INFO Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_BSS\_ENTRY\_CHANNEL\_INFO

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_BSS\_ENTRY\_CHANNEL\_INFO is a TLV that contains BSS entry channel information.

## TLV Type


0x3A

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                          | Description                                                  |
|-------------------------------|--------------------------------------------------------------|
| WDI\_CHANNEL\_NUMBER (UINT32) | The logical channel number on which the peer was discovered. |
| UINT32                        | The band ID for the BSS entry.                               |

 

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

 

 




