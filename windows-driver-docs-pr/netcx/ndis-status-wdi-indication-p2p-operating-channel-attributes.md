---
title: NDIS_STATUS_WDI_INDICATION_P2P_OPERATING_CHANNEL_ATTRIBUTES (dot11wificxintf.h)
ms.topic: reference
description: WiFiCx drivers use NDIS_STATUS_WDI_INDICATION_P2P_OPERATING_CHANNEL_ATTRIBUTES to indicate supported channels. 
ms.date: 08/30/2021
keywords:
 - NDIS_STATUS_WDI_INDICATION_P2P_OPERATING_CHANNEL_ATTRIBUTES Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WDI\_INDICATION\_P2P\_OPERATING\_CHANNEL\_ATTRIBUTES (dot11wificxintf.h)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WiFiCx drivers use NDIS\_STATUS\_WDI\_INDICATION\_P2P\_OPERATING\_CHANNEL\_ATTRIBUTES to indicate the preferred operating channel to start a GO, the preferred listen channel if asked to enter listen state, and the full set of supported channels at any point of time. The indication is sent once when adapter initializes, and then sent each time one of these parameters changes due to events such as roaming or connecting or disconnecting from an access point.

| Object |
|--------|
| Port   |

 

The operating channel and channel list values are local settings and do not account for the actual channel negotiation during GO negotiation/invitation. The driver is still expected to negotiate the channel when GO negotiation/invitation is performed.

It is expected that the listen channel reported by the driver is honored if listen state is turned on. It is expected that this indication is fired if the host configured a listen channel that is different from the preferred listen channel reported earlier via this indication.

## Payload data


| Type                                                                                       | Multiple TLV instances allowed | Optional | Description                                              |
|--------------------------------------------------------------------------------------------|--------------------------------|----------|----------------------------------------------------------|
| [**WDI\_TLV\_P2P\_CHANNEL\_NUMBER**](./wdi-tlv-p2p-channel-number.md)                  |                                |          | The Wi-Fi Direct Operating channel attribute.            |
| [**WDI\_TLV\_P2P\_CHANNEL\_LIST\_ATTRIBUTE**](./wdi-tlv-p2p-channel-list-attribute.md) |                                |          | The full set of channels supported by the local adapter. |
| [**WDI\_TLV\_P2P\_LISTEN\_CHANNEL**](./wdi-tlv-p2p-listen-channel.md)                  |                                |          | The Wi-Fi Direct Listen channel attribute.               |

 

## Requirements


|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|

 

