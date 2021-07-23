---
title: WDI_TLV_ADDITIONAL_PROBE_REQUEST_DEFAULT_IES (dot11wificxtypes.h)
description: WDI_TLV_ADDITIONAL_PROBE_REQUEST_DEFAULT_IES is a WiFiCx TLV that contains additional probe request IEs.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_ADDITIONAL_PROBE_REQUEST_DEFAULT_IES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_ADDITIONAL\_PROBE\_REQUEST\_DEFAULT\_IES (dot11wificxtypes.h)


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

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.h|

 

 




