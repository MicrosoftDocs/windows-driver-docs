---
title: WDI_TLV_RADIO_STATE
ms.topic: reference
description: WDI_TLV_RADIO_STATE is a TLV that contains the state of the radio in hardware and software.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_RADIO_STATE Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_RADIO\_STATE

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_RADIO\_STATE is a TLV that contains the state of the radio in hardware and software.

## TLV Type


0xA1

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>UINT8</td>
<td>The current state of the radio in hardware.
<p>Valid values are 0 and 1.</p></td>
</tr>
<tr class="even">
<td>UINT8</td>
<td>The current state of the radio in software.
<p>Valid values are 0 and 1.</p></td>
</tr>
</tbody>
</table>

 

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

 

 




