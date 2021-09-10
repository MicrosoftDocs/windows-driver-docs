---
title: WDI_TLV_LOCATION_PRIVACY (dot11wificxtypes.hpp)
description: WDI_TLV_LOCATION_PRIVACY is a WiFiCx TLV that contains permissions information for privacy-sensitive location operations. 
ms.date: 08/30/21
keywords:
 - WDI_TLV_LOCATION_PRIVACY Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI_TLV_LOCATION_PRIVACY (dot11wificxtypes.hpp)

**WDI_TLV_LOCATION_PRIVACY** is a TLV that contains permissions information for privacy-sensitive location operations.

This TLV is used in [OID_WDI_SET_LOCATION_PRIVACY](oid-wdi-set-location-privacy.md).

## TLV Type

0x171

## Length

The size (in bytes) of a UINT8.

## Values

| Type | Description |
| --- | --- |
| UINT8 | If **false**, the adapter is not permitted to perform privacy-sensitive location operations, such as sharing the device’s precise location. If **true**, the adapter may perform such operations unless it is restricted by other settings. |

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

