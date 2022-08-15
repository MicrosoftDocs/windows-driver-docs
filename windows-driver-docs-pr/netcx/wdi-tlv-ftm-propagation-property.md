---
title: WDI_TLV_FTM_PROPAGATION_PROPERTY (dot11wificxtypes.hpp)
description: WDI_TLV_FTM_PROPAGATION_PROPERTY is a WiFiCx TLV that contains the negotiated bandwidth in MHz between two STAs to exercise the FTM.
ms.date: 07/30/2021
keywords:
 - WDI_TLV_FTM_PROPAGATION_PROPERTY Network Drivers Starting with Windows Vista
---

# WDI_TLV_FTM_PROPAGATION_PROPERTY (dot11wificxtypes.hpp)


WDI_TLV_FTM_PROPAGATION_PROPERTY is a TLV that contains the propagation properties of a signal that are estimated by the LE's logic.

This TLV is used in [WDI_TLV_FTM_RESPONSE](wdi-tlv-ftm-response.md).

## TLV Type


0x16C

## Length


The size (in bytes) of a UINT32.

## Values


| Type                                              | Description                                 |
|---------------------------------------------------|---------------------------------------------|
| [**WDI_FTM_PROPAGATION**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_ftm_propagation) | The  estimated propagation properties of a signal. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

