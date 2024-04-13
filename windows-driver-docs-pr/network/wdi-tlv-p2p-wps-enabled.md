---
title: WDI_TLV_P2P_WPS_ENABLED
ms.topic: reference
description: WDI_TLV_P2P_WPS_ENABLED is a TLV that specifies if Wi-Fi Protected Setup is enabled.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_P2P_WPS_ENABLED Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_WPS\_ENABLED

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_P2P\_WPS\_ENABLED is a TLV that specifies if Wi-Fi Protected Setup is enabled.

## TLV Type


0xF7

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
<td>Specifies if Wi-Fi Protected Setup is enabled.
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

## See also


[OID\_WDI\_SET\_P2P\_WPS\_ENABLED](./oid-wdi-set-p2p-wps-enabled.md)

 

