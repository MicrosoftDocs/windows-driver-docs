---
title: NDIS_STATUS_WDI_INDICATION_ACTION_FRAME_RECEIVED (dot11wificxintf.h)
description: WiFiCx drivers use NDIS_STATUS_WDI_INDICATION_ACTION_FRAME_RECEIVED to indicate that an Action Frame has been received.
ms.date: 07/30/2021
keywords:
 - NDIS_STATUS_WDI_INDICATION_ACTION_FRAME_RECEIVED Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WDI\_INDICATION\_ACTION\_FRAME\_RECEIVED (dot11wificxintf.h)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WiFiCx drivers use NDIS\_STATUS\_WDI\_INDICATION\_ACTION\_FRAME\_RECEIVED to indicate that an Action Frame has been received.

| Object |
|--------|
| Port   |

 

## Payload data


| Type                                                                               | Multiple TLV instances allowed | Optional | Description                                               |
|------------------------------------------------------------------------------------|--------------------------------|----------|-----------------------------------------------------------|
| [**WDI\_TLV\_BSSID**](./wdi-tlv-bssid.md)                                      |                                |          | The BSSID of the source.                                  |
| [**WDI\_TLV\_BSS\_ENTRY\_CHANNEL\_INFO**](./wdi-tlv-bss-entry-channel-info.md) |                                |          | The logical channel number and band ID for the BSS entry. |
| [**WDI\_TLV\_ACTION\_FRAME\_BODY**](./wdi-tlv-action-frame-body.md)            |                                |          | The incoming Action Frame body.                           |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|

## See also


[OID\_WDI\_SET\_ADVERTISEMENT\_INFORMATION](oid-wdi-set-advertisement-information.md)

 

