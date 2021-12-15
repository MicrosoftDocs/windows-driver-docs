---
title: WDI_TLV_IS_DIRECTED_PROBE_FOR_HIDDEN_PERMITTED (dot11wificxtypes.hpp)
description: WDI_TLV_IS_DIRECTED_PROBE_FOR_HIDDEN_PERMITTED is a WiFiCx TLV that indicates if a directed (non-wildcard) probe request is allowed for an SSID.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_PLDR_SUPPORT Network Drivers Starting with Windows Vista
---

# WDI_TLV_IS_DIRECTED_PROBE_FOR_HIDDEN_PERMITTED (dot11wificxtypes.hpp)


WDI_TLV_IS_DIRECTED_PROBE_FOR_HIDDEN_PERMITTED is a TLV that indicates if a directed (non-wildcard) probe request is allowed for an SSID.  

WDI_TLV_IS_DIRECTED_PROBE_FOR_HIDDEN_PERMITTED is used in [WDI_TLV_SSID_OFFLOAD](wdi-tlv-ssid-offload.md).


## TLV Type


0x131

## Length


The size (in bytes) of a UINT8.

## Values


| Type  | Description                                                                                                                                                                                                                       |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT8 | Specifies if a directed (non-wildcard) probe request is allowed for an SSID. If this value is **false** the firmware **must** use wildcard SSID probe requests for active scans. If **true**, a directed probe request (non-wildcard SSID) is permitted.|

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|



 

