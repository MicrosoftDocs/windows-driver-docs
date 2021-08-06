---
title: NDIS_STATUS_WDI_INDICATION_TKIP_MIC_FAILURE (dot11wificxintf.h)
description: WiFiCx drivers use NDIS_STATUS_WDI_INDICATION_TKIP_MIC_FAILURE to indicate when a received packet that was successfully decrypted by the TKIP cipher algorithm fails the message integrity code (MIC) verification.
ms.date: 08/30/21
keywords:
 - NDIS_STATUS_WDI_INDICATION_TKIP_MIC_FAILURE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WDI\_INDICATION\_TKIP\_MIC\_FAILURE (dot11wificxintf.h)


WiFiCx drivers use NDIS\_STATUS\_WDI\_INDICATION\_TKIP\_MIC\_FAILURE to indicate when a received packet that was successfully decrypted by the TKIP cipher algorithm fails the message integrity code (MIC) verification.

| Object |
|--------|
| Port   |

 

## Payload data


| Type                                                                             | Multiple TLV instances allowed | Optional | Description                       |
|----------------------------------------------------------------------------------|--------------------------------|----------|-----------------------------------|
| [**WDI\_TLV\_TKIP\_MIC\_FAILURE\_INFO**](./wdi-tlv-tkip-mic-failure-info.md) |                                |          | The TKIP MIC failure information. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|

 

