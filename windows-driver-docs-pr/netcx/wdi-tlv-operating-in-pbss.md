---
title: WDI_TLV_OPERATING_IN_PBSS (dot11wificxtypes.hpp)
description: WDI_TLV_OPERATING_IN_PBSS is a WiFiCx TLV that specifies whether the AP is operating as a PCP in PBSS mode. 
ms.date: 08/30/2021
keywords:
 - WDI_TLV_OPERATING_IN_PBSS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI_TLV_OPERATING_IN_PBSS (dot11wificxtypes.hpp)

**WDI_TLV_OPERATING_IN_PBSS** is a TLV that specifies whether the AP is operating as a PCP in PBSS mode. 

This TLV is used in [WDI_TLV_AP_BAND_INFORMATION](wdi-tlv-ap-band-information.md).

## TLV Type

0x13E

## Length

The size (in bytes) of a UINT8.

## Values

| Type | Description |
| --- | --- |
| UINT8 {0,1} | Specifies whether the AP is operating as a PCP in PBSS mode. |

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

