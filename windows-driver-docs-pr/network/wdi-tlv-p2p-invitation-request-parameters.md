---
title: WDI_TLV_P2P_INVITATION_REQUEST_PARAMETERS
description: WDI_TLV_P2P_INVITATION_REQUEST_PARAMETERS is a TLV that contains Wi-Fi Direct Invitation Request parameters.
ms.assetid: CC9B0454-4522-4589-8E21-4986BAEBC6D0
ms.date: 07/18/2017
keywords:
 - WDI_TLV_P2P_INVITATION_REQUEST_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_INVITATION\_REQUEST\_PARAMETERS


WDI\_TLV\_P2P\_INVITATION\_REQUEST\_PARAMETERS is a TLV that contains Wi-Fi Direct Invitation Request parameters.

## TLV Type


0x7C

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
<td>UINT16</td>
<td>The Group Owner Configuration Timeout in milliseconds.</td>
</tr>
<tr class="even">
<td>UINT16</td>
<td>The Client Configuration Timeout in milliseconds.</td>
</tr>
<tr class="odd">
<td>UINT8</td>
<td>The invitation flags as defined by the Wi-Fi Direct specification.</td>
</tr>
<tr class="even">
<td>UINT8</td>
<td>A bit that indicates whether or not the outgoing Invitation Request is an invitation to a local Group Owner.
<p>Valid values are 0 and 1. This bit is set to 1 if it is an invitation to a local GO.</p></td>
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

 

 




