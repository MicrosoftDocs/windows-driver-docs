---
title: WDI_TLV_AP_CAPABILITIES
description: WDI_TLV_AP_CAPABILITIES is a TLV that contains the capabilities of an access point.
ms.assetid: 2DE866C8-9414-46D8-A156-3A35F1E325EF
ms.date: 07/18/2017
keywords:
 - WDI_TLV_AP_CAPABILITIES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_AP\_CAPABILITIES


WDI\_TLV\_AP\_CAPABILITIES is a TLV that contains the capabilities of an access point.

## TLV Type


0x16

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
<td>The scan SSID list size.</td>
</tr>
<tr class="even">
<td>UINT32</td>
<td>The desired SSID list size.</td>
</tr>
<tr class="odd">
<td>UINT32</td>
<td>The privacy exemption list size.</td>
</tr>
<tr class="even">
<td>UINT32</td>
<td>The association table size.</td>
</tr>
<tr class="odd">
<td>UINT32</td>
<td>The key mapping table size.</td>
</tr>
<tr class="even">
<td>UINT32</td>
<td>The default key table size.</td>
</tr>
<tr class="odd">
<td>UINT32</td>
<td>The maximum length of the WEP key value.</td>
</tr>
<tr class="even">
<td>UINT8</td>
<td>Specifies whether the AP supports radar detection.
<p>Valid values are 0 (not supported) and 1 (supported).</p></td>
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

 

 




