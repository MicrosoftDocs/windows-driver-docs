---
title: OID_WDI_TASK_SCAN
description: OID_WDI_TASK_SCAN requests a survey of BSS networks. The port performs a scan according to the requirements of the IEEE 802.11 specification.
ms.assetid: c4131010-20f2-45a4-8fb9-5a1e3e9735e5
ms.date: 07/18/2017
keywords:
 - OID_WDI_TASK_SCAN Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WDI\_TASK\_SCAN


OID\_WDI\_TASK\_SCAN requests a survey of BSS networks. The port performs a scan according to the requirements of the IEEE 802.11 specification.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Object</th>
<th>Abort capable</th>
<th>Default priority (host driver policy)</th>
<th>Normal execution time (seconds)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Port</td>
<td>Yes. The port must be in a clean state after the abort.</td>
<td><p>6 (background scan)</p>
<p>5 (user-initiated scan)</p></td>
<td>4</td>
</tr>
</tbody>
</table>

 

A task started message containing a [**WDI\_TLV\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/dn898068) is indicated once the port has started the scan and is ready to receive other commands.

Once a scan is started when enabled by LiveUpdatesNeeded, the port must provide incremental updates (using unsolicited indications of [NDIS\_STATUS\_WDI\_INDICATION\_BSS\_ENTRY\_LIST](ndis-status-wdi-indication-bss-entry-list.md)) about discovered BSS entries. BSS entries that had previously been discovered but were not found by the port in the current scan should not be reported by the port. For power and performance reasons, the port should throttle indications and send updates to the host only when it has discovered 3 or more, or when it has discovered less than 3 entries but has not reported them to the host for more than 500 milliseconds. After the scan is completed, if the adapter does not manage BSS entries, it does not need to remember the BSS entries that it has discovered. Once the scan operation has finished, the port must send the task complete notification to the operating system and stop reporting BSS entries to the host. The scan command is used for finding legacy (non-Wi-Fi Direct networks) and the port should not include the Wi-Fi Direct IEs in the probe requests.

If the adapter does not manage BSS entries, the host remembers the BSS entries reported by the port from a scan for a finite period of time. It times out its cached entries and flushes them. If the adapter manages the BSS entries, it caches and times them out. The host may send the [OID\_WDI\_SET\_FLUSH\_BSS\_ENTRY](oid-wdi-set-flush-bss-entry.md) command to explicitly flush the entries.

The host tracks BSS entries using their BSSID. If the port reports two BSS entries for the same BSSID, the host overwrites one with another.

While the scan is ongoing, the port must maintain the existing connections (for example, Infrastructure or Wi-Fi Direct). If connections already exist, the port should scan a subset of channels at a time and in between subsets, provide the other connections access to the medium. During the scan, the host can submit packet send requests to any port on the adapter.

In the indicated BSS entries, the port can include device specific context information. This context information is passed back to the device if the port is asked to connect to that BSS entry. However, this context may be cleared by the host automatically if the BSS entry is flushed.

The scan command can be aborted. On receiving the abort command, the port should stop trying to find new BSS networks and complete the scan task as soon as possible. When the task has been completed (either normally or due to an abort), the port should be in a good state such that another scan can be issued on that port.

The adapter must not violate regulatory restrictions when performing a scan.

## Task parameters


| TLV                                                                       | Multiple TLV instances allowed | Optional | Description                                                                                                                                                                                                                                                                                   |
|---------------------------------------------------------------------------|--------------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_BSSID**](https://msdn.microsoft.com/library/windows/hardware/dn926153)                             |                                |          | BSSID of the network to scan for. If this is the broadcast MAC address, the station scans for all BSSIDs.                                                                                                                                                                                     |
| [**WDI\_TLV\_SSID**](https://msdn.microsoft.com/library/windows/hardware/dn898064)                               | X                              |          | A list of SSID list that the port should scan for. There can be multiple SSIDs in this list and one of them can be a wildcard. When doing an active scan on a channel, the port must send a probe request for each SSID in the list. If this list is empty, the port must scan for all SSIDs. |
| [**WDI\_TLV\_VENDOR\_SPECIFIC\_IE**](https://msdn.microsoft.com/library/windows/hardware/dn898076) |                                | X        | One or more IEs that must be included in the probe requests sent by the port. These IEs are not used for passive scan.                                                                                                                                                                        |
| [**WDI\_TLV\_SCAN\_MODE**](https://msdn.microsoft.com/library/windows/hardware/dn898052)                    |                                |          | Scan mode parameters.                                                                                                                                                                                                                                                                         |
| [**WDI\_TLV\_SCAN\_DWELL\_TIME**](https://msdn.microsoft.com/library/windows/hardware/dn898051)       |                                |          | Dwell time parameters.                                                                                                                                                                                                                                                                        |
| [**WDI\_TLV\_BAND\_CHANNEL**](https://msdn.microsoft.com/library/windows/hardware/dn926144)              | X                              | X        | A list of recommended channels to scan. The adapter can perform a scan on a subset or superset of the channel list as long as it meets the Maximum Scan Time requirements. If this list is empty, the port must scan on all supported channels.                                               |

 

## Task completion indication


[NDIS\_STATUS\_WDI\_INDICATION\_SCAN\_COMPLETE](ndis-status-wdi-indication-scan-complete.md)
## Unsolicited indication


[NDIS\_STATUS\_WDI\_INDICATION\_BSS\_ENTRY\_LIST](ndis-status-wdi-indication-bss-entry-list.md)
This notification is used by the device to tell the host about updates to the BSS entries. It can be sent at any time.

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

 

 




