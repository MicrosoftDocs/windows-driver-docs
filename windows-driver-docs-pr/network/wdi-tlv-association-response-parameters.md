---
title: WDI_TLV_ASSOCIATION_RESPONSE_PARAMETERS
ms.topic: reference
description: WDI_TLV_ASSOCIATION_RESPONSE_PARAMETERS is a TLV that contains association response parameters for OID_WDI_TASK_SEND_AP_ASSOCIATION_RESPONSE.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_ASSOCIATION_RESPONSE_PARAMETERS Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_ASSOCIATION\_RESPONSE\_PARAMETERS

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_ASSOCIATION\_RESPONSE\_PARAMETERS is a TLV that contains association response parameters for [OID\_WDI\_TASK\_SEND\_AP\_ASSOCIATION\_RESPONSE](./oid-wdi-task-send-ap-association-response.md).

## TLV Type


0x97

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
<td>Specifies whether or not to accept the association request.
<p>Valid values are 0 (do not accept) and 1 (accept).</p></td>
</tr>
<tr class="even">
<td>UINT16</td>
<td>Specifies the reason code. If accept request is set to 0, this field provides a reason code to send back to the peer adapter.</td>
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

 

