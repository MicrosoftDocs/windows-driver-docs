---
title: WDI_TLV_P2P_ADVERTISED_SERVICES (dot11wificxtypes.h)
description: WDI_TLV_P2P_ADVERTISED_SERVICES is a WiFiCx TLV that contains a list of advertised services.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_P2P_ADVERTISED_SERVICES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_ADVERTISED\_SERVICES (dot11wificxtypes.h)


WDI\_TLV\_P2P\_ADVERTISED\_SERVICES is a TLV that contains a list of advertised services.

## TLV Type


0xEF

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values

| Type                                                                                                       | Multiple TLV instances allowed | Optional | Description                                                                                                                                                                                                                                                                                                          |
|------------------------------------------------------------------------------------------------------------|--------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI_TLV_P2P_ADVERTISED_SERVICE_ENTRY**](wdi-tlv-p2p-advertised-service-entry.md)                                 |                                | X        | A list of advertised services.                                                                                          |
|     UINT16                              |                              |         | Service update indicator to include in ANQP response if the driver supports responding to service information discovery ANQP requests.                                                                                           |



 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.h|

 

 




