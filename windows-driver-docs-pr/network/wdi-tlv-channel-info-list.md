---
title: WDI_TLV_CHANNEL_INFO_LIST
description: WDI_TLV_CHANNEL_INFO_LIST is a TLV that contains a list of channels.
ms.assetid: D1B82F4F-6722-4D54-B6FF-B7F1309F8C0E
ms.date: 07/18/2017
keywords:
 - WDI_TLV_CHANNEL_INFO_LIST Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_CHANNEL\_INFO\_LIST


WDI\_TLV\_CHANNEL\_INFO\_LIST is a TLV that contains a list of channels.

## TLV Type


0x41

## Length


The size (in bytes) of the array of WDI\_CHANNEL\_NUMBER (UINT32) structures. The array must contain 1 or more elements.

## Values


| Type       | Description                 |
|------------|-----------------------------|
| UINT32\[\] | An array of Wi-Fi channels. |

 

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

 

 




