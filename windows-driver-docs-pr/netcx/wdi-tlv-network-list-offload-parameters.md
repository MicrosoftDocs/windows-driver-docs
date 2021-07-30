---
title: WDI_TLV_NETWORK_LIST_OFFLOAD_PARAMETERS (dot11wificxtypes.h)
description: WDI_TLV_NETWORK_LIST_OFFLOAD_PARAMETERS is a WiFiCx TLV that contains Network List Offload (NLO) parameters for OID_WDI_SET_NETWORK_LIST_OFFLOAD.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_NETWORK_LIST_OFFLOAD_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_NETWORK\_LIST\_OFFLOAD\_PARAMETERS (dot11wificxtypes.h)


WDI\_TLV\_NETWORK\_LIST\_OFFLOAD\_PARAMETERS is a TLV that contains Network List Offload (NLO) parameters for [OID\_WDI\_SET\_NETWORK\_LIST\_OFFLOAD](./oid-wdi-set-network-list-offload.md).

## TLV Type


0x59

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                                    | Multiple TLV instances allowed | Optional | Description                                                                                  |
|-----------------------------------------------------------------------------------------|--------------------------------|----------|----------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_NETWORK\_LIST\_OFFLOAD\_CONFIG**](wdi-tlv-network-list-offload-config.md) |                                |          | Specifies NLO configuration.                                                                 |
| [**WDI\_TLV\_SSID\_OFFLOAD**](wdi-tlv-ssid-offload.md)                                 | X                              | X        | Specifies offload SSIDs. When this element is absent, the firmware should stop NLO scanning. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.h|

 

