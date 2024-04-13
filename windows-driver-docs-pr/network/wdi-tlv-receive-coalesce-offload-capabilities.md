---
title: WDI_TLV_RECEIVE_COALESCE_OFFLOAD_CAPABILITIES
ms.topic: reference
description: WDI_TLV_RECEIVE_COALESCE_OFFLOAD_CAPABILITIES is a TLV that contains Rx coalesce offload capabilities.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_RECEIVE_COALESCE_OFFLOAD_CAPABILITIES Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_RECEIVE\_COALESCE\_OFFLOAD\_CAPABILITIES


WDI\_TLV\_RECEIVE\_COALESCE\_OFFLOAD\_CAPABILITIES is a TLV that contains Rx coalesce offload capabilities.

## TLV Type


0xCE

## Length


The size (in bytes) of the below values.

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
<td>Specifies whether or not Rx coalesce is enabled for IPv4.
<p>Valid values are 0 (not enabled) and 1 (enabled).</p></td>
</tr>
<tr class="even">
<td>UINT8</td>
<td>Specifies whether or not Rx coalesce is enabled for IPv6.
<p>Valid values are 0 (not enabled) and 1 (enabled).</p></td>
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

 

 




