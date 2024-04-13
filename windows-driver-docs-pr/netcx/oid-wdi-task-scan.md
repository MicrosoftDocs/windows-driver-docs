---
title: OID_WDI_TASK_SCAN (dot11wificxintf.h)
ms.topic: reference
description: OID_WDI_TASK_SCAN requests a survey of BSS networks. The port performs a scan according to the IEEE 802.11 specification requirements.
ms.date: 06/30/2021
keywords:
 - OID_WDI_TASK_SCAN Network Drivers Starting with Windows Vista
---

# OID_WDI_TASK_SCAN (dot11wificxintf.h)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


OID_WDI_TASK_SCAN requests a survey of BSS networks. The port performs a scan according to the requirements of the IEEE 802.11 specification.

|Object|Abort capable|Default priority (host driver policy)|Normal execution time (seconds)|
|--- |--- |--- |--- |
|Port|Yes. The port must be in a clean state after the abort.|6 (background scan) <br/>5 (user-initiated scan)|4|


A task started message containing a [**WDI_TLV_STATUS**](wdi-tlv-status.md) is indicated once the port has started the scan and is ready to receive other commands.

Once a scan is started when enabled by LiveUpdatesNeeded, the port must provide incremental updates (using unsolicited indications of [NDIS_STATUS_WDI_INDICATION_BSS_ENTRY_LIST](ndis-status-wdi-indication-bss-entry-list.md)) about discovered BSS entries. BSS entries that had previously been discovered but were not found by the port in the current scan should not be reported by the port. For power and performance reasons, the port should throttle indications and send updates to the host only when it has discovered 3 or more, or when it has discovered less than 3 entries but has not reported them to the host for more than 500 milliseconds. After the scan is completed, if the adapter does not manage BSS entries, it does not need to remember the BSS entries that it has discovered. Once the scan operation has finished, the port must send the task complete notification to the operating system and stop reporting BSS entries to the host. The scan command is used for finding legacy (non-Wi-Fi Direct networks) and the port should not include the Wi-Fi Direct IEs in the probe requests.

If the adapter does not manage BSS entries, the host remembers the BSS entries reported by the port from a scan for a finite period of time. It times out its cached entries and flushes them. If the adapter manages the BSS entries, it caches and times them out. The host may send the [OID_WDI_SET_FLUSH_BSS_ENTRY](oid-wdi-set-flush-bss-entry.md) command to explicitly flush the entries.

The host tracks BSS entries using their BSSID. If the port reports two BSS entries for the same BSSID, the host overwrites one with another.

While the scan is ongoing, the port must maintain the existing connections (for example, Infrastructure or Wi-Fi Direct). If connections already exist, the port should scan a subset of channels at a time and in between subsets, provide the other connections access to the medium. During the scan, the host can submit packet send requests to any port on the adapter.

In the indicated BSS entries, the port can include device specific context information. This context information is passed back to the device if the port is asked to connect to that BSS entry. However, this context may be cleared by the host automatically if the BSS entry is flushed.

The scan command can be aborted. On receiving the abort command, the port should stop trying to find new BSS networks and complete the scan task as soon as possible. When the task has been completed (either normally or due to an abort), the port should be in a good state such that another scan can be issued on that port.

The adapter must not violate regulatory restrictions when performing a scan.

## Task parameters


| TLV                                                                       | Multiple TLV instances allowed | Optional | Description                                                                                                                                                                                                                                                                                   |
|---------------------------------------------------------------------------|--------------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_BSSID**](./wdi-tlv-bssid.md)                             |                                |    X      | BSSID of the network to scan for. If this is the broadcast MAC address, the station scans for all BSSIDs.                                                                                                                                                                                     |
| [**WDI\_TLV\_SSID**](./wdi-tlv-ssid.md)                               | X                              |     X     | A list of SSID list that the port should scan for. There can be multiple SSIDs in this list and one of them can be a wildcard. When doing an active scan on a channel, the port must send a probe request for each SSID in the list. If this list is empty, the port must scan for all SSIDs. |
| [**WDI\_TLV\_BAND\_CHANNEL**](./wdi-tlv-band-channel.md)              | X                              | X        | A list of recommended channels to scan. The adapter can perform a scan on a subset or superset of the channel list as long as it meets the Maximum Scan Time requirements. If this list is empty, the port must scan on all supported channels.                                               |
| [**WDI\_TLV\_VENDOR\_SPECIFIC\_IE**](./wdi-tlv-vendor-specific-ie.md) |                                | X        | One or more IEs that must be included in the probe requests sent by the port. These IEs are not used for passive scan.                                                                                                                                                                        |
| [**WDI\_TLV\_SCAN\_MODE**](./wdi-tlv-scan-mode.md)                    |                                |          | Scan mode parameters.                                                                                                                                                                                                                                                                         |
| [**WDI\_TLV\_SCAN\_DWELL\_TIME**](./wdi-tlv-scan-dwell-time.md)       |                                |          | Dwell time parameters.                                                                                                                                                                                                                                                                        |
| [**WDI_TLV_6_GHZ_BAND_CHANNEL**](./wdi-tlv-6-ghz-band-channel.md)       |                                |     X     | List of channels recommended to scan in the 6 GHz band. When specified, the adapter can perform a scan on a subset or superset of the channel list as long as it meets the Maximum Scan Time requirements.                                                                                                                                                                                                                                                                 |

 

## Task completion indication


[NDIS_STATUS_WDI_INDICATION_SCAN_COMPLETE](ndis-status-wdi-indication-scan-complete.md)

## Unsolicited indication

[NDIS_STATUS_WDI_INDICATION_BSS_ENTRY_LIST](ndis-status-wdi-indication-bss-entry-list.md)

This notification is used by the device to tell the host about updates to the BSS entries. It can be sent at any time.

## Requirements


|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|

 

