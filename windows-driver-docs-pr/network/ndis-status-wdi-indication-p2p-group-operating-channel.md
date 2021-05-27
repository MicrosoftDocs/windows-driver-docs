---
title: NDIS_STATUS_WDI_INDICATION_P2P_GROUP_OPERATING_CHANNEL
description: Miniport drivers use NDIS_STATUS_WDI_INDICATION_P2P_GROUP_OPERATING_CHANNEL to indicate which operating channel a given Wi-Fi Direct port is operating on.
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_WDI_INDICATION_P2P_GROUP_OPERATING_CHANNEL Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WDI\_INDICATION\_P2P\_GROUP\_OPERATING\_CHANNEL


Miniport drivers use NDIS\_STATUS\_WDI\_INDICATION\_P2P\_GROUP\_OPERATING\_CHANNEL to indicate which operating channel a given Wi-Fi Direct port is operating on.

For a Wi-Fi Direct Client port, this must be indicated during the connect (before the connect completion).

For a Wi-Fi Direct GO port, this must be indicated during [OID\_WDI\_TASK\_START\_AP](oid-wdi-task-start-ap.md) (before the OID completion).

## Payload data


| Type                                                                                         | Multiple TLV instances allowed | Optional | Description                                                        |
|----------------------------------------------------------------------------------------------|--------------------------------|----------|--------------------------------------------------------------------|
| [**WDI\_TLV\_P2P\_CHANNEL\_NUMBER**](./wdi-tlv-p2p-channel-number.md)                    |                                |          | The operating channel the given Wi-Fi Direct port is operating on. |
| [**WDI\_TLV\_P2P\_CHANNEL\_INDICATE\_REASON**](./wdi-tlv-p2p-channel-indicate-reason.md) |                                |          | The reason for sending the indication.                             |

 

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
<td>Dot11wdi.h</td>
</tr>
</tbody>
</table>

 

