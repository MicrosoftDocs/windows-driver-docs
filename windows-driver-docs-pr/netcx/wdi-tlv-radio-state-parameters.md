---
title: WDI_TLV_RADIO_STATE_PARAMETERS (dot11wificxtypes.hpp)
description: WDI_TLV_RADIO_STATE_PARAMETERS is a WiFiCx TLV that contains radio state parameters for OID_WDI_TASK_SET_RADIO_STATE.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_RADIO_STATE_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_RADIO\_STATE\_PARAMETERS (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_RADIO\_STATE\_PARAMETERS is a TLV that contains radio state parameters for [OID\_WDI\_TASK\_SET\_RADIO\_STATE](./oid-wdi-task-set-radio-state.md).

## TLV Type


0xA0

## Length


The size (in bytes) of a UINT8.

## Values


|Type|Description|
|--- |--- |
|UINT8|The desired radio state. Valid values are 0 (the radio is turned off) and 1 (the radio is enabled).|

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

