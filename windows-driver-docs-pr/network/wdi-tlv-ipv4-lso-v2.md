---
title: WDI_TLV_IPV4_LSO_V2 (0xD3)
description: WDI_TLV_IPV4_LSO_V2 is a TLV that contains Large Send Offload V2 parameters for IPv4.
ms.assetid: 912D5F1B-260F-43B3-93F6-3C38E9D7F1E5
ms.date: 07/18/2017
keywords:
 - WDI_TLV_IPV4_LSO_V2 (0xD3) Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_IPV4\_LSO\_V2 (0xD3)


WDI\_TLV\_IPV4\_LSO\_V2 is a TLV that contains Large Send Offload V2 parameters for IPv4.

## TLV Type


0xD3

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
<td>UINT32</td>
<td>Encapsulation type. Valid values are:
<ul>
<li>WDI_ENCAPSULATION_IEEE_802_11</li>
</ul></td>
</tr>
<tr class="even">
<td>UINT32</td>
<td>The maximum offload size. Specified by the maximum number of bytes of TCP user data per packet.</td>
</tr>
<tr class="odd">
<td>UINT32</td>
<td>The minimum segment count. Specified by the minimum number of segments that should be present after segmentation.</td>
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

 

 




