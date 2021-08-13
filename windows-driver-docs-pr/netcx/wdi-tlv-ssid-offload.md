---
title: WDI_TLV_SSID_OFFLOAD (dot11wificxtypes.h)
description: WDI_TLV_SSID_OFFLOAD is a WiFiCx TLV that contains an SSID and hints about the SSID.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_SSID_OFFLOAD Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_SSID\_OFFLOAD (dot11wificxtypes.h)


WDI\_TLV\_SSID\_OFFLOAD is a TLV that contains an SSID and hints about the SSID.

## TLV Type


0x9E

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                         | Multiple TLV instances allowed | Optional | Description                 |
|------------------------------------------------------------------------------|--------------------------------|----------|-----------------------------|
| [**WDI\_TLV\_SSID**](wdi-tlv-ssid.md)                                       |                                |          | The SSID.                   |
| [**WDI\_TLV\_UNICAST\_ALGORITHM\_LIST**](wdi-tlv-unicast-algorithm-list.md) |                                |          | The unicast algorithm list. |
| [**WDI\_TLV\_BAND\_CHANNEL\_LIST**](wdi-tlv-band-channel-list.md)                      |                                |          | The channel list.           |
| [**WDI_TLV_IS_DIRECTED_PROBE_FOR_HIDDEN_PERMITTED**](wdi-tlv-is-directed-probe-for-hidden-permitted.md)                      |                                |     X     | When present, This TLV indicates if a directed (non-wildcard) probe request is allowed for this SSID.  If this TLV is present and **false** then the firmware **must** not use this SSID in any probe request for privacy reasons. If this TLV is not present then the firmware may use whatever behavior was previously used (WDI version 1.0.21 behavior or earlier). |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.h|

 

 




