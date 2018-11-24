---
title: WDI_TLV_BSS_ENTRY_CHANNEL_INFO
description: WDI_TLV_BSS_ENTRY_CHANNEL_INFO is a TLV that contains BSS entry channel information.
ms.assetid: 01DA2EDA-2BE2-4E4F-AE5D-8E07EEF691FE
ms.date: 07/18/2017
keywords:
 - WDI_TLV_BSS_ENTRY_CHANNEL_INFO Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_BSS\_ENTRY\_CHANNEL\_INFO


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

 

 




