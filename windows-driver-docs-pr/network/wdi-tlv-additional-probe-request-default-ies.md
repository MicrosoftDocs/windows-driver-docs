---
title: WDI_TLV_ADDITIONAL_PROBE_REQUEST_DEFAULT_IES
description: WDI_TLV_ADDITIONAL_PROBE_REQUEST_DEFAULT_IES is a TLV that contains additional probe request IEs.
ms.assetid: E364B1BC-5A78-42C8-B04D-31BD21141477
ms.date: 07/18/2017
keywords:
 - WDI_TLV_ADDITIONAL_PROBE_REQUEST_DEFAULT_IES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_ADDITIONAL\_PROBE\_REQUEST\_DEFAULT\_IES


WDI\_TLV\_ADDITIONAL\_PROBE\_REQUEST\_DEFAULT\_IES is a TLV that contains additional probe request IEs.

## TLV Type


0x70

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

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
<td>UINT8[]</td>
<td>An array of probe request IEs. The Wi-Fi Direct port must add these additional IEs to transmitted probe request packets.
<div class="alert">
<strong>Note</strong>  A Wi-Fi Direct Discover Request may override the default probe request IEs.
</div>
<div>
 
</div></td>
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

 

 




