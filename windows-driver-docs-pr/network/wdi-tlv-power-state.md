---
title: WDI_TLV_POWER_STATE
description: WDI_TLV_POWER_STATE is a TLV that contains a power state.
ms.assetid: EC65FE08-ABF0-488A-A6FA-21B1794418B3
ms.date: 07/18/2017
keywords:
 - WDI_TLV_POWER_STATE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_POWER\_STATE


WDI\_TLV\_POWER\_STATE is a TLV that contains a power state.

## TLV Type


0x44

## Length


The size (in bytes) of a UINT32.

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
<td>UINT32</td>
<td>Specifies a power state.
<p>Valid values are:</p>
<ul>
<li>0x0001: Exit low power (D0)</li>
<li>0x0003: Enter low power (D2)</li>
<li>0x0004: Enter power off (D3, may not actually be powered off on some platforms)</li>
</ul></td>
</tr>
</tbody>
</table>

 

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

 

 




