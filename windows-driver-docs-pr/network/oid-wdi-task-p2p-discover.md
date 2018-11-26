---
title: OID_WDI_TASK_P2P_DISCOVER
description: OID_WDI_TASK_P2P_DISCOVER is issued to the device to perform Wi-Fi Direct discovery.
ms.assetid: 9425a8d1-af68-488c-8a1e-a9b759f102cc
ms.date: 07/18/2017
keywords:
 - OID_WDI_TASK_P2P_DISCOVER Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WDI\_TASK\_P2P\_DISCOVER


OID\_WDI\_TASK\_P2P\_DISCOVER is issued to the device to perform Wi-Fi Direct discovery.

| Object | Abort capable                                           | Default priority (host driver policy) | Normal execution time (seconds) |
|--------|---------------------------------------------------------|---------------------------------------|---------------------------------|
| Port   | Yes. The port must be in a clean state after the abort. | 6                                     | 15                              |

 

The command contains properties which define either a specific set of Wi-Fi Direct devices to search for, or wildcard discovery.

Wi-Fi Direct discovery is mutually exclusive from standard Wi-Fi scanning. While this task is running, broadcast probe requests shall not be sent without a "DIRECT-" SSID, or a specific GO SSID. These probe requests must also include all necessary Wi-Fi Direct IEs.

The host may have search criteria which is not provided as part of the task parameters down to the device. The host may use the task abort mechanism if it has matched the required criteria, therefore it is important that the device can abort Wi-Fi Direct Discovery tasks quickly so as not to degrade scenario performance.

When the task has been completed (either normally or due to an abort), the port should be in a good state such that another discover request can be issued on that port.

## Task parameters


<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>TLV</th>
<th>Multiple TLV instances allowed</th>
<th>Optional</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="https://msdn.microsoft.com/library/windows/hardware/dn897878" data-raw-source="[&lt;strong&gt;WDI_TLV_P2P_DISCOVER_MODE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn897878)"><strong>WDI_TLV_P2P_DISCOVER_MODE</strong></a></td>
<td></td>
<td></td>
<td>Discovery mode information, such as scan type, count, and time between scans.</td>
</tr>
<tr class="even">
<td><a href="https://msdn.microsoft.com/library/windows/hardware/dn898051" data-raw-source="[&lt;strong&gt;WDI_TLV_SCAN_DWELL_TIME&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn898051)"><strong>WDI_TLV_SCAN_DWELL_TIME</strong></a></td>
<td></td>
<td></td>
<td>Scanning dwell time settings.</td>
</tr>
<tr class="odd">
<td><a href="https://msdn.microsoft.com/library/windows/hardware/dn897877" data-raw-source="[&lt;strong&gt;WDI_TLV_P2P_DISCOVERY _CHANNEL_SETTINGS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn897877)"><strong>WDI_TLV_P2P_DISCOVERY _CHANNEL_SETTINGS</strong></a></td>
<td>X</td>
<td>X</td>
<td>Scan duration and list of channels to scan. When specified, the listen settings override those specified in WDI_TLV_SCAN_DWELL_TIME. If this list is empty, the port must scan on all supported channels and use the listen settings from WDI_TLV_SCAN_DWELL_TIME.</td>
</tr>
<tr class="even">
<td><a href="https://msdn.microsoft.com/library/windows/hardware/dn898064" data-raw-source="[&lt;strong&gt;WDI_TLV_SSID&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn898064)"><strong>WDI_TLV_SSID</strong></a></td>
<td>X</td>
<td>X</td>
<td>A list of SSIDs that the port should scan for. There can be multiple SSIDs in this list and one of them can be a wildcard. When doing an active scan on a channel, the port must send a probe request for each SSID in the list. If this list is empty, the port must scan for all SSIDs.</td>
</tr>
<tr class="odd">
<td><a href="https://msdn.microsoft.com/library/windows/hardware/dn898009" data-raw-source="[&lt;strong&gt;WDI_TLV_P2P_SERVICE_NAME_HASH&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn898009)"><strong>WDI_TLV_P2P_SERVICE_NAME_HASH</strong></a></td>
<td>X</td>
<td>X</td>
<td>A list of Service Hash names to be queried. Required if WDI_P2P_SERVICE_DISCOVERY_TYPE_SERVICE_NAME_ONLY or WDI_P2P_SERVICE_DISCOVERY_TYPE_ASP2_SERVICE_NAME_ONLY is specified.</td>
</tr>
<tr class="even">
<td><a href="https://msdn.microsoft.com/library/windows/hardware/dn898076" data-raw-source="[&lt;strong&gt;WDI_TLV_VENDOR_SPECIFIC_IE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn898076)"><strong>WDI_TLV_VENDOR_SPECIFIC_IE</strong></a></td>
<td></td>
<td>X</td>
<td>One or more IEs that must be included in the probe requests sent by the port. These IEs are not used for passive scan.</td>
</tr>
<tr class="odd">
<td><a href="https://msdn.microsoft.com/library/windows/hardware/mt269140" data-raw-source="[&lt;strong&gt;WDI_TLV_P2P_SERVICE_INFORMATION_DISCOVERY_ENTRY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/mt269140)"><strong>WDI_TLV_P2P_SERVICE_INFORMATION_DISCOVERY_ENTRY</strong></a></td>
<td>X</td>
<td>X</td>
<td>An optional list of Service Information Discovery Entries to be queried. This is required if WDI_P2P_SERVICE_DISCOVERY_TYPE_SERVICE_INFORMATION is specified. The driver is expected to perform a P2P service discovery over probe request/response using the service name hash. For each service entry that contains service information, the driver is expected to perform an ANQP query request/response to query the service information.</td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/mt769912" data-raw-source="[&lt;strong&gt;WDI_TLV_P2P_ASP2_SERVICE_INFORMATION_DISCOVERY_ENTRY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/mt769912)"><strong>WDI_TLV_P2P_ASP2_SERVICE_INFORMATION_DISCOVERY_ENTRY</strong></a></p></td>
<td>X</td>
<td><p>X</p></td>
<td><p>Added in Windows 10, version 1607, WDI version 1.0.21.</p>
<p>An optional list of ASP2 Service Information Discovery Entries to be queried. This is required if WDI_P2P_SERVICE_DISCOVERY_TYPE_ASP2_SERVICE_INFORMATION is specified. The driver is expected to perform a P2P service discovery over probe request/response using the service name hash. For each service entry that contains service information, the driver is expected to perform an ANQP query request/response to query the service information.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/mt769913" data-raw-source="[&lt;strong&gt;WDI_TLV_P2P_INCLUDE_LISTEN_CHANNEL&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/mt769913)"><strong>WDI_TLV_P2P_INCLUDE_LISTEN_CHANNEL</strong></a></p></td>
<td></td>
<td><p>X</p></td>
<td><p>Added in Windows 10, version 1607, WDI version 1.0.21.</p>
<p>Specifies whether the probe request should include the Listen Channel attribute during discovery.</p></td>
</tr>
</tbody>
</table>

 

## Task completion indication


[NDIS\_STATUS\_WDI\_INDICATION\_P2P\_DISCOVERY\_COMPLETE](ndis-status-wdi-indication-p2p-discovery-complete.md)
## Unsolicited indication


[NDIS\_STATUS\_WDI\_INDICATION\_BSS\_ENTRY\_LIST](ndis-status-wdi-indication-bss-entry-list.md)
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
<td>Dot11wdi.h</td>
</tr>
</tbody>
</table>

 

 




