---
title: OID_WDI_TASK_P2P_DISCOVER (dot11wificxintf.h)
description: The OID_WDI_TASK_P2P_DISCOVER task command is issued to the device to perform Wi-Fi Direct discovery.
ms.date: 06/30/2021
keywords:
 - OID_WDI_TASK_P2P_DISCOVER Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WDI\_TASK\_P2P\_DISCOVER (dot11wificxintf.h)


OID\_WDI\_TASK\_P2P\_DISCOVER is issued to the device to perform Wi-Fi Direct discovery.

| Object | Abort capable                                           | Default priority (host driver policy) | Normal execution time (seconds) |
|--------|---------------------------------------------------------|---------------------------------------|---------------------------------|
| Port   | Yes. The port must be in a clean state after the abort. | 6                                     | 15                              |

 

The command contains properties which define either a specific set of Wi-Fi Direct devices to search for, or wildcard discovery.

Wi-Fi Direct discovery is mutually exclusive from standard Wi-Fi scanning. While this task is running, broadcast probe requests shall not be sent without a "DIRECT-" SSID, or a specific GO SSID. These probe requests must also include all necessary Wi-Fi Direct IEs.

The host may have search criteria which is not provided as part of the task parameters down to the device. The host may use the task abort mechanism if it has matched the required criteria, therefore it is important that the device can abort Wi-Fi Direct Discovery tasks quickly so as not to degrade scenario performance.

When the task has been completed (either normally or due to an abort), the port should be in a good state such that another discover request can be issued on that port.

## Task parameters

|TLV|Multiple TLV instances allowed|Optional|Description|
|--- |--- |--- |--- |
|[**WDI_TLV_P2P_DISCOVER_MODE**](wdi-tlv-p2p-discover-mode.md)|||Discovery mode information, such as scan type, count, and time between scans.|
|[**WDI_TLV_SCAN_DWELL_TIME**](wdi-tlv-scan-dwell-time.md)|||Scanning dwell time settings.|
|[**WDI_TLV_P2P_DISCOVERY _CHANNEL_SETTINGS**](wdi-tlv-p2p-discovery-channel-settings.md)|X|X|Scan duration and list of channels to scan. When specified, the listen settings override those specified in WDI_TLV_SCAN_DWELL_TIME. If this list is empty, the port must scan on all supported channels and use the listen settings from WDI_TLV_SCAN_DWELL_TIME.|
|[**WDI_TLV_SSID**](wdi-tlv-ssid.md)|X|X|A list of SSIDs that the port should scan for. There can be multiple SSIDs in this list and one of them can be a wildcard. When doing an active scan on a channel, the port must send a probe request for each SSID in the list. If this list is empty, the port must scan for all SSIDs.|
|[**WDI_TLV_P2P_SERVICE_NAME_HASH**](wdi-tlv-p2p-service-name-hash.md)|X|X|A list of Service Hash names to be queried. Required if WDI_P2P_SERVICE_DISCOVERY_TYPE_SERVICE_NAME_ONLY or WDI_P2P_SERVICE_DISCOVERY_TYPE_ASP2_SERVICE_NAME_ONLY is specified.|
|[**WDI_TLV_VENDOR_SPECIFIC_IE**](wdi-tlv-vendor-specific-ie.md)|X||One or more IEs that must be included in the probe requests sent by the port. These IEs are not used for passive scan.|
|[**WDI_TLV_P2P_SERVICE_INFORMATION_DISCOVERY_ENTRY**](wdi-tlv-p2p-service-information-discovery-entry.md)|X|X|An optional list of Service Information Discovery Entries to be queried. This is required if WDI_P2P_SERVICE_DISCOVERY_TYPE_SERVICE_INFORMATION is specified. The driver is expected to perform a P2P service discovery over probe request/response using the service name hash. For each service entry that contains service information, the driver is expected to perform an ANQP query request/response to query the service information.|
|[**WDI_TLV_P2P_ASP2_SERVICE_INFORMATION_DISCOVERY_ENTRY**](wdi-tlv-p2p-asp2-service-information-discovery-entry.md)|X|X|An optional list of ASP2 Service Information Discovery Entries to be queried. This is required if WDI_P2P_SERVICE_DISCOVERY_TYPE_ASP2_SERVICE_INFORMATION is specified. The driver is expected to perform a P2P service discovery over probe request/response using the service name hash. For each service entry that contains service information, the driver is expected to perform an ANQP query request/response to query the service information.|
|[**WDI_TLV_P2P_INCLUDE_LISTEN_CHANNEL**](wdi-tlv-p2p-include-listen-channel.md)||X|Specifies whether the probe request should include the Listen Channel attribute during discovery.|

## Task completion indication


[NDIS\_STATUS\_WDI\_INDICATION\_P2P\_DISCOVERY\_COMPLETE](ndis-status-wdi-indication-p2p-discovery-complete.md)
## Unsolicited indication


[NDIS\_STATUS\_WDI\_INDICATION\_BSS\_ENTRY\_LIST](ndis-status-wdi-indication-bss-entry-list.md)

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|

