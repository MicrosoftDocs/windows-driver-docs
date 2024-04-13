---
title: NDIS_STATUS_WDI_INDICATION_WAKE_REASON
ms.topic: reference
description: Miniport drivers use NDIS_STATUS_WDI_INDICATION_WAKE_REASON to indicate the reason for a wake when the NIC wakes the host. The wake reason is used for debugging purposes and has no functional effect.
ms.date: 03/02/2023
keywords:
 - NDIS_STATUS_WDI_INDICATION_WAKE_REASON Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WDI\_INDICATION\_WAKE\_REASON


Miniport drivers use NDIS\_STATUS\_WDI\_INDICATION\_WAKE\_REASON to indicate the reason for a wake when the NIC wakes the host. The wake reason is used for debugging purposes and has no functional effect.

| Object |
|--------|
| Port   |

 

When the host goes to low power state, it offloads a few functions to the NIC and arms the NIC for wake. When a wake event occurs, the NIC asserts the wake interrupt line to wake the host. The host then brings the NIC into D0 (running power state). The NIC must indicate the wake reason once it enters D0.

If the wake reason is a wake packet, the NIC should also include the wake packet and the wake pattern ID that matches the packet. The packet is encapsulated as [**WDI\_TLV\_INDICATION\_WAKE\_PACKET**](./wdi-tlv-indication-wake-packet.md). The wake reason should also include [**WDI\_TLV\_INDICATION\_WAKE\_PACKET\_PATTERN\_ID**](./wdi-tlv-indication-wake-packet-pattern-id.md) to specify the pattern ID which matches the packet.

## Payload data


| Type                                                                                                      | Multiple TLV instances allowed | Optional | Description                                                                                                 |
|-----------------------------------------------------------------------------------------------------------|--------------------------------|----------|-------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_INDICATION\_WAKE\_REASON**](./wdi-tlv-indication-wake-reason.md)                         |                                |          | The wake reason.                                                                                            |
| [**WDI\_TLV\_INDICATION\_WAKE\_PACKET**](./wdi-tlv-indication-wake-packet.md)                         |                                | X        | The wake packet.                                                                                            |
| [**WDI\_TLV\_INDICATION\_WAKE\_PACKET\_PATTERN\_ID**](./wdi-tlv-indication-wake-packet-pattern-id.md) |                                | X        | The ID of the pattern that matches the wake packet. The ID is obtained from the Add command of the pattern. |

 

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

 

