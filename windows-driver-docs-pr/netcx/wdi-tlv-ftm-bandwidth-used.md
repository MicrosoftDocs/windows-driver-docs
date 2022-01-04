---
title: WDI_TLV_FTM_BANDWIDTH_USED (dot11wificxtypes.hpp)
description: WDI_TLV_FTM_BANDWIDTH_USED is a WiFiCx TLV that contains the negotiated bandwidth in MHz between two STAs to exercise the FTM.
ms.date: 07/30/2021
keywords:
 - WDI_TLV_FTM_BANDWIDTH_USED Network Drivers Starting with Windows Vista
---

# WDI_TLV_FTM_BANDWIDTH_USED (dot11wificxtypes.hpp)


WDI_TLV_FTM_BANDWIDTH_USED is a TLV that contains the negotiated bandwidth in MHz between two STAs to exercise the Fine Timing Measurement (FTM). 

This TLV is used in [WDI_TLV_FTM_RESPONSE](wdi-tlv-ftm-response.md).

## TLV Type


0x16B

## Length


The size (in bytes) of a UINT32.

## Values


| Type                                              | Description                                 |
|---------------------------------------------------|---------------------------------------------|
| [**WDI_FTM_BANDWIDTH**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_ftm_bandwidth) | The  FTM bandwidth. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

