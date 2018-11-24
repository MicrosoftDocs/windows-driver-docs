---
title: NDIS_STATUS_WDI_INDICATION_P2P_OPERATING_CHANNEL_ATTRIBUTES
description: Miniport drivers use NDIS_STATUS_WDI_INDICATION_P2P_OPERATING_CHANNEL_ATTRIBUTES to indicate the preferred operating channel to start a GO, the preferred listen channel if asked to enter listen state, and the full set of supported channels at any point of time. The indication is sent once when adapter initializes, and then sent each time one of these parameters changes due to events such as roaming or connecting or disconnecting from an access point.
ms.assetid: F7D27328-99B3-4EB5-9F48-864338EF8D8A
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_WDI_INDICATION_P2P_OPERATING_CHANNEL_ATTRIBUTES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WDI\_INDICATION\_P2P\_OPERATING\_CHANNEL\_ATTRIBUTES


Miniport drivers use NDIS\_STATUS\_WDI\_INDICATION\_P2P\_OPERATING\_CHANNEL\_ATTRIBUTES to indicate the preferred operating channel to start a GO, the preferred listen channel if asked to enter listen state, and the full set of supported channels at any point of time. The indication is sent once when adapter initializes, and then sent each time one of these parameters changes due to events such as roaming or connecting or disconnecting from an access point.

| Object |
|--------|
| Port   |

 

The operating channel and channel list values are local settings and do not account for the actual channel negotiation during GO negotiation/invitation. The driver is still expected to negotiate the channel when GO negotiation/invitation is performed.

It is expected that the listen channel reported by the driver is honored if listen state is turned on. It is expected that this indication is fired if the host configured a listen channel that is different from the preferred listen channel reported earlier via this indication.

## Payload data


| Type                                                                                       | Multiple TLV instances allowed | Optional | Description                                              |
|--------------------------------------------------------------------------------------------|--------------------------------|----------|----------------------------------------------------------|
| [**WDI\_TLV\_P2P\_CHANNEL\_NUMBER**](https://msdn.microsoft.com/library/windows/hardware/dn897869)                  |                                |          | The Wi-Fi Direct Operating channel attribute.            |
| [**WDI\_TLV\_P2P\_CHANNEL\_LIST\_ATTRIBUTE**](https://msdn.microsoft.com/library/windows/hardware/dn897868) |                                |          | The full set of channels supported by the local adapter. |
| [**WDI\_TLV\_P2P\_LISTEN\_CHANNEL**](https://msdn.microsoft.com/library/windows/hardware/mt269138)                  |                                |          | The Wi-Fi Direct Listen channel attribute.               |

 

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

 

 




