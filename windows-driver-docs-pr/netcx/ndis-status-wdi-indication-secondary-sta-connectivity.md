---
title: NDIS_STATUS_WDI_INDICATION_SECONDARY_STA_CONNECTIVITY (dot11wificxintf.h)
description: WiFiCx drivers use NDIS_STATUS_WDI_INDICATION_SECONDARY_STA_CONNECTIVITY to notify the OS when a secondary STA connection will no longer be usable.
ms.date: 08/30/2021
keywords:
 - NDIS_STATUS_WDI_INDICATION_SECONDARY_STA_CONNECTIVITY  Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS_STATUS_WDI_INDICATION_SECONDARY_STA_CONNECTIVITY  (dot11wificxintf.h)


WiFiCx drivers use NDIS_STATUS_WDI_INDICATION_SECONDARY_STA_CONNECTIVITY to notify the OS when a secondary STA connection will no longer be usable and when it will be usable again.

When secondary STA connectivity is supported, the driver is required to prioritize Wi-Fi Direct (WFD) connections over secondary STA connections at all times. Therefore if the driver is unable to sustain both connections at the same time, it must send the WDI_INDICATION_SECONDARY_STA_CONNECTIVITY indication with [**WDI_TLV_LIMITED_CONNECTIVITY**](wdi-tlv-limited-connectivity.md) set to **TRUE**. When the secondary STA can be connected again without compromising WFD connectivity, the driver must send the WDI_INDICATION_SECONDARY_STA_CONNECTIVITY indication with [**WDI_TLV_LIMITED_CONNECTIVITY**](wdi-tlv-limited-connectivity.md) set to **FALSE**.

> [!NOTE]
> If the driver indicates WDI_INDICATION_SECONDARY_STA_CONNECTIVITY with [**WDI_TLV_LIMITED_CONNECTIVITY**](wdi-tlv-limited-connectivity.md) set to **TRUE**, it may also include an optional list of Band/Channels in [**WDI_TLV_SECONDARY_STA_BAND_CHANNEL**](wdi-tlv-secondary-sta-band-channel.md) to indicate which band/channels (if any) the OS can use for secondary STA connections.


| Object |
|--------|
| Adapter   |

 

## Payload data


| Type                                                                  | Multiple TLV instances allowed | Optional | Description                                              |
|-----------------------------------------------------------------------|--------------------------------|----------|----------------------------------------------------------|
| [**WDI_TLV_LIMITED_CONNECTIVITY**](wdi-tlv-limited-connectivity.md) |                                |          | Specifies whether the driver can maintain a secondary STA connection. If this value is **1**, the driver cannot maintain a secondary STA connection. Otherwise this value is **0**.  |
| [**WDI_TLV_SECONDARY_STA_BAND_CHANNEL**](wdi-tlv-secondary-sta-band-channel.md)|     X                           |    X      | When **WDI_TLV_LIMITED_CONNECTIVITY** is **1**, the driver can include a list of band IDs and optional channel numbers that are available for secondary STA connection. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|


## See also


[Dual STA connectivity](dual-sta-connectivity.md)

[WDI_TLV_LIMITED_CONNECTIVITY](wdi-tlv-limited-connectivity.md)

[WDI_TLV_SECONDARY_STA_BAND_CHANNEL](wdi-tlv-secondary-sta-band-channel.md)

