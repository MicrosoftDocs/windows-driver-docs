---
title: WDI_TLV_ASSOCIATION_RESPONSE_RESULT_PARAMETERS
ms.topic: reference
description: WDI_TLV_ASSOCIATION_RESPONSE_RESULT_PARAMETERS is a TLV that contains association response result parameters.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_ASSOCIATION_RESPONSE_RESULT_PARAMETERS Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_ASSOCIATION\_RESPONSE\_RESULT\_PARAMETERS

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_ASSOCIATION\_RESPONSE\_RESULT\_PARAMETERS is a TLV that contains association response result parameters.

## TLV Type


0x76

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
<td><a href="/windows-hardware/drivers/ddi/dot11wdi/ns-dot11wdi-_wdi_mac_address" data-raw-source="[&lt;strong&gt;WDI_MAC_ADDRESS&lt;/strong&gt;](/windows-hardware/drivers/ddi/dot11wdi/ns-dot11wdi-_wdi_mac_address)"><strong>WDI_MAC_ADDRESS</strong></a></td>
<td>The MAC address of the peer adapter.</td>
</tr>
<tr class="even">
<td>UINT8</td>
<td>A bit value that indicates whether the request from the peer station is a reassociation request.
<p>Valid values are 0 and 1. A value of 1 indicates that it is a reassociation request.</p></td>
</tr>
<tr class="odd">
<td>UINT8</td>
<td>A bit value that indicates whether the response from the peer station is a reassociation response.
<p>Valid values are 0 and 1. A value of 1 indicates that it is a reassociation response.</p></td>
</tr>
<tr class="even">
<td><a href="/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_auth_algorithm" data-raw-source="[&lt;strong&gt;WDI_AUTH_ALGORITHM&lt;/strong&gt;](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_auth_algorithm)"><strong>WDI_AUTH_ALGORITHM</strong></a></td>
<td>The authentication algorithm for the association.</td>
</tr>
<tr class="odd">
<td><a href="/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_cipher_algorithm" data-raw-source="[&lt;strong&gt;WDI_CIPHER_ALGORITHM&lt;/strong&gt;](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_cipher_algorithm)"><strong>WDI_CIPHER_ALGORITHM</strong></a></td>
<td>The unicast cipher algorithm for the association.</td>
</tr>
<tr class="even">
<td><a href="/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_cipher_algorithm" data-raw-source="[&lt;strong&gt;WDI_CIPHER_ALGORITHM&lt;/strong&gt;](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_cipher_algorithm)"><strong>WDI_CIPHER_ALGORITHM</strong></a></td>
<td>The multicast cipher algorithm for the association.</td>
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

