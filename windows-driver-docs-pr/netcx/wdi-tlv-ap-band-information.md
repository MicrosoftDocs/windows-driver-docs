---
title: WDI_TLV_AP_BAND_INFORMATION (dot11wificxtypes.hpp)
description: WDI_TLV_AP_BAND_INFORMATION is a WiFiCx TLV that contains AP band ID information. 
ms.date: 08/30/2021
keywords:
 - WDI_TLV_AP_BAND_INFORMATION Network Drivers Starting with Windows Vista
---

# WDI_TLV_AP_BAND_INFORMATION (dot11wificxtypes.hpp)

**WDI_TLV_AP_BAND_INFORMATION** is a TLV that contains the AP band information.

This TLV is used in the payload data for [NDIS_STATUS_WDI_INDICATION_P2P_GROUP_OPERATING_CHANNEL](ndis-status-wdi-indication-p2p-group-operating-channel.md).

## TLV Type

0x13D

## Length

The sum (in bytes) of the sizes of all contained TLVs.

## Values

| Type                                                                                      | Multiple TLV instances allowed | Optional                                                                            | Description                                                                                                                                                                                                                                                       |
|-------------------------------------------------------------------------------------------|--------------------------------|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI_TLV_BANDID**](wdi-tlv-bandid.md)                                                  |                                |                                                                                     | The identifier for this band.                                                                                                                                                                                                                                          |
| [**WDI_TLV_OPERATING_IN_PBSS**](wdi-tlv-operating-in-pbss.md)                  |                                |                                                                                    | Specifies whether the AP is operating as a PCP in PBSS mode.                                                                                                                                                                           |

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

