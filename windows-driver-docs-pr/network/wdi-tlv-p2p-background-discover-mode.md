---
title: WDI_TLV_P2P_BACKGROUND_DISCOVER_MODE
description: WDI_TLV_P2P_BACKGROUND_DISCOVER_MODE is a TLV that contains Wi-Fi Direct Background Discover Mode parameters.
ms.date: 07/18/2017
keywords:
 - WDI_TLV_P2P_BACKGROUND_DISCOVER_MODE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_BACKGROUND\_DISCOVER\_MODE


WDI\_TLV\_P2P\_BACKGROUND\_DISCOVER\_MODE is a TLV that contains Wi-Fi Direct Background Discover Mode parameters.

## TLV Type


0xCE

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
<td><a href="/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_p2p_discover_type" data-raw-source="[&lt;strong&gt;WDI_P2P_DISCOVER_TYPE&lt;/strong&gt;](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_p2p_discover_type)"><strong>WDI_P2P_DISCOVER_TYPE</strong></a></td>
<td>The type of discovery to be performed by the port.</td>
</tr>
<tr class="even">
<td><a href="/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_p2p_service_discovery_type" data-raw-source="[&lt;strong&gt;WDI_P2P_SERVICE_DISCOVERY_TYPE&lt;/strong&gt;](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_p2p_service_discovery_type)"><strong>WDI_P2P_SERVICE_DISCOVERY_TYPE</strong></a></td>
<td>The type of Service Discovery to be performed by the port.
<p>The only valid values are WDI_P2P_SERVICE_DISCOVERY_TYPE_NO_SERVICE_DISCOVERY and WDI_P2P_SERVICE_DISCOVERY_TYPE_SERVICE_NAME_ONLY.</p></td>
</tr>
<tr class="odd">
<td>UINT32</td>
<td>The device visibility timeout. Specifies the maximum timeout (in milliseconds) for reporting a device entry. This is required for background scan only.</td>
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

