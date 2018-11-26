---
title: OID_WDI_SET_P2P_START_BACKGROUND_DISCOVERY
description: OID_WDI_SET_P2P_START_BACKGROUND_DISCOVERY instructs the adapter to periodically perform Wi-Fi Direct discovery in the background
ms.assetid: DF58B71D-7D45-4E0D-963F-A70471363DF5
ms.date: 07/18/2017
keywords:
 - OID_WDI_SET_P2P_START_BACKGROUND_DISCOVERY Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WDI\_SET\_P2P\_START\_BACKGROUND\_DISCOVERY


OID\_WDI\_SET\_P2P\_START\_BACKGROUND\_DISCOVERY instructs the adapter to periodically perform Wi-Fi Direct discovery in the background

| Scope | Set serialized with task | Normal execution time (seconds) | Affects data throughput/latency |
|-------|--------------------------|---------------------------------|---------------------------------|
| Port  | No                       | 1                               | Yes                             |

 

The adapter is required to scan the specified channels at regular intervals and be able to find a device that becomes discoverable within the device visibility timeout (typically 5 minutes). The behavior is similar to the regular Wi-Fi Direct Discovery scan (as defined in [OID\_WDI\_TASK\_P2P\_DISCOVER](oid-wdi-task-p2p-discover.md)), but it is not time-bound, and the adapter may schedule the scans at some later point in time. The adapter must perform at least one scan within each device visibility timeout. If the device visibility timeout is 0, the adapter should continue to scan regularly using its own cycle time. If a DISCOVER or SCAN task request is made during this time, the adapter should suspend the background discovery for the duration of the task and continue when the task is finished. Upon completing a background scan, the device should send the [NDIS\_STATUS\_WDI\_INDICATION\_P2P\_DISCOVERY\_COMPLETE](ndis-status-wdi-indication-p2p-discovery-complete.md) indication (with transaction ID equal to 0) to let the operating system know that it has completed a scan. The adapter must send this indication every time it completes a background scan.

If the channel list is provided, the adapter should only scan on the specified channels. Otherwise, it should scan all channels. If the firmware happened to discover a device outside of the specified channels, it should still send the information to the operating system.

When Listen Duration and channels ([**WDI\_TLV\_P2P\_DISCOVERY\_CHANNEL\_SETTINGS**](https://msdn.microsoft.com/library/windows/hardware/dn897877)) are specified, they refer to the listen times for the remote devices. Based on all the values of Listen Duration and channels, the adapter needs to come up with a schedule to scan the requested channels in the most efficient manner. The operating system may also specify multiple instances of Listen Duration and channels. In this case, the adapter should first come up with the scan schedule for those entries which have non-zero values of Listen Duration and Channel list. Then, the adapter should use default values in the following cases:

1.  If the Listen duration is 0, the adapter should use the default scan times for the specified channels.
2.  If the channel list is empty, the adapter should scan all of the channels in that band using the listen and cycle times specified for that band. The scan times would not apply to any channels that have separate listen durations specified by the operating system.

When the NIC is in D0, the adapter indicates the responses to the probe requests for the specific service name(s) as [NDIS\_STATUS\_WDI\_INDICATION\_BSS\_ENTRY\_LIST](ndis-status-wdi-indication-bss-entry-list.md) notifications to the operating system. WDI caches the response information for the OS for the higher layer services, and notifies them as necessary.

When the NIC is in D2, it suspends background discovery until it goes back to D0.

## Set property parameters


| TLV                                                                                                | Multiple TLV instances allowed | Optional | Description                                                                                                                         |
|----------------------------------------------------------------------------------------------------|--------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_P2P\_BACKGROUND\_DISCOVER\_MODE**](https://msdn.microsoft.com/library/windows/hardware/dn897864)     |                                |          | Wi-Fi Direct Background Discover Mode parameters.                                                                                   |
| [**WDI\_TLV\_P2P\_DISCOVERY\_CHANNEL\_SETTINGS**](https://msdn.microsoft.com/library/windows/hardware/dn897877) | X                              | X        | List of recommended channels to scan.                                                                                               |
| [**WDI\_TLV\_P2P\_DEVICE\_FILTER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/dn897873)                 |                                | X        | List of Wi-Fi Direct devices and Group Owners to search for during Wi-Fi Direct device discover.                                    |
| [**WDI\_TLV\_P2P\_SERVICE\_NAME\_HASH**](https://msdn.microsoft.com/library/windows/hardware/dn898009)                   | X                              | X        | List of Service Hash names to be queried. This is required if WDI\_P2P\_SERVICE\_DISCOVERY\_TYPE\_SERVICE\_NAME\_ONLY is specified. |
| [**WDI\_TLV\_VENDOR\_SPECIFIC\_IE**](https://msdn.microsoft.com/library/windows/hardware/dn898076)                          |                                | X        | One or more IEs that must be included in the probe requests sent by the port.                                                       |

 

## Set property results


No additional data. The data in the header is sufficient.
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

 

 




