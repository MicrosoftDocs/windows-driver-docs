---
title: WDI_TLV_P2P_ADVERTISED_SERVICES
description: WDI_TLV_P2P_ADVERTISED_SERVICES is a TLV that contains a list of advertised services.
ms.assetid: C210DDF3-0349-4108-82EC-1823F562E5D7
ms.date: 07/18/2017
keywords:
 - WDI_TLV_P2P_ADVERTISED_SERVICES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_ADVERTISED\_SERVICES


WDI\_TLV\_P2P\_ADVERTISED\_SERVICES is a TLV that contains a list of advertised services.

## TLV Type


0xEF

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Type</th>
<th>Multiple TLV instances allowed</th>
<th>Optional</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="wdi-tlv-p2p-advertised-service-entry.md" data-raw-source="[&lt;strong&gt;WDI_TLV_P2P_ADVERTISED_SERVICE_ENTRY&lt;/strong&gt;](wdi-tlv-p2p-advertised-service-entry.md)"><strong>WDI_TLV_P2P_ADVERTISED_SERVICE_ENTRY</strong></a></p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td>A list of advertised services.</td>
</tr>
<tr class="even">
<td><p><a href="wdi-tlv-p2p-advertised-prefix-entry.md" data-raw-source="[&lt;strong&gt;WDI_TLV_P2P_ADVERTISED_PREFIX_ENTRY&lt;/strong&gt;](wdi-tlv-p2p-advertised-prefix-entry.md)"><strong>WDI_TLV_P2P_ADVERTISED_PREFIX_ENTRY</strong></a></p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>A list of advertised prefixes that are derived from the list of advertised services.</p></td>
</tr>
<tr class="odd">
<td><p><a href="wdi-tlv-p2p-asp2-advertised-service-entry.md" data-raw-source="[&lt;strong&gt;WDI_TLV_P2P_ASP2_ADVERTISED_SERVICE_ENTRY&lt;/strong&gt;](wdi-tlv-p2p-asp2-advertised-service-entry.md)"><strong>WDI_TLV_P2P_ASP2_ADVERTISED_SERVICE_ENTRY</strong></a></p></td>
<td><p>X</p></td>
<td><p>X</p></td>
<td><p>Added in Windows 10, version 1607, WDI version 1.0.21.</p>
<p>A list of advertised ASP2 services.</p></td>
</tr>
<tr class="even">
<td><p><a href="wdi-tlv-p2p-service-update-indicator.md" data-raw-source="[&lt;strong&gt;WDI_TLV_P2P_SERVICE_UPDATE_INDICATOR&lt;/strong&gt;](wdi-tlv-p2p-service-update-indicator.md)"><strong>WDI_TLV_P2P_SERVICE_UPDATE_INDICATOR</strong></a></p></td>
<td></td>
<td></td>
<td><p>The service update indicator to include in ANQP responses if the driver supports responding to service information discovery ANQP requests.</p></td>
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

 

 




