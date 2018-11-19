---
title: WDI_TLV_RADIO_STATE_PARAMETERS
description: WDI_TLV_RADIO_STATE_PARAMETERS is a TLV that contains radio state parameters for OID_WDI_TASK_SET_RADIO_STATE.
ms.assetid: D977DF8A-146C-4921-AE7C-5FBEC7FBA4C8
ms.date: 07/18/2017
keywords:
 - WDI_TLV_RADIO_STATE_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_RADIO\_STATE\_PARAMETERS


WDI\_TLV\_RADIO\_STATE\_PARAMETERS is a TLV that contains radio state parameters for [OID\_WDI\_TASK\_SET\_RADIO\_STATE](https://msdn.microsoft.com/library/windows/hardware/dn925963).

## TLV Type


0xA0

## Length


The size (in bytes) of a UINT8.

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
<td>The desired radio state.
<p>Valid values are 0 (the radio is turned off) and 1 (the radio is enabled).</p></td>
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

 

 




