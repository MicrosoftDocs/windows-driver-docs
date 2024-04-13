---
title: NDIS_STATUS_WDI_INDICATION_P2P_GROUP_OPERATING_CHANNEL (dot11wificxintf.h)
ms.topic: reference
description: WiFiCx drivers use NDIS_STATUS_WDI_INDICATION_P2P_GROUP_OPERATING_CHANNEL to indicate which operating channel a given Wi-Fi Direct port is operating on.
ms.date: 08/30/2021
keywords:
 - NDIS_STATUS_WDI_INDICATION_P2P_GROUP_OPERATING_CHANNEL Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WDI\_INDICATION\_P2P\_GROUP\_OPERATING\_CHANNEL (dot11wificxintf.h)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WiFiCx drivers use NDIS\_STATUS\_WDI\_INDICATION\_P2P\_GROUP\_OPERATING\_CHANNEL to indicate which operating channel a given Wi-Fi Direct port is operating on.

For a Wi-Fi Direct Client port, this must be indicated during the connect (before the connect completion).

For a Wi-Fi Direct GO port, this must be indicated during [OID\_WDI\_TASK\_START\_AP](oid-wdi-task-start-ap.md) (before the OID completion).

## Payload data


| Type                                                                                         | Multiple TLV instances allowed | Optional | Description                                                        |
|----------------------------------------------------------------------------------------------|--------------------------------|----------|--------------------------------------------------------------------|
| [**WDI\_TLV\_P2P\_CHANNEL\_NUMBER**](./wdi-tlv-p2p-channel-number.md)                    |                                |          | The operating channel the given Wi-Fi Direct port is operating on. |
| [**WDI\_TLV\_P2P\_CHANNEL\_INDICATE\_REASON**](./wdi-tlv-p2p-channel-indicate-reason.md) |                                |          | The reason for sending the indication.                             |
| [**WDI_TLV_AP_BAND_INFORMATION**](./wdi-tlv-ap-band-information.md) |                                |          | The Band ID and whether the BSS type is PBSS.                           |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|

 

