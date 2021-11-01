---
title: WDI_TLV_INDICATION_CAN_SUSTAIN_AP (dot11wificxtypes.hpp)
description: WDI_TLV_INDICATION_CAN_SUSTAIN_AP is a WiFiCx TLV that contains the reason for a Can Sustain AP indication.
ms.date: 08/31/2021
keywords:
 - WDI_TLV_INDICATION_CAN_SUSTAIN_AP Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_INDICATION\_CAN\_SUSTAIN\_AP (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_INDICATION\_CAN\_SUSTAIN\_AP is a TLV that contains the reason for a Can Sustain AP indication.

## TLV Type


0xE7

## Length


The size (in bytes) of a UINT32.

## Values


| Type   | Description                                                                                                                        |
|--------|------------------------------------------------------------------------------------------------------------------------------------|
| UINT32 | The Can Sustain AP reason. See [**WDI\_CAN\_SUSTAIN\_AP\_REASON**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_can_sustain_ap_reason) for possible reason values. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

## See also


[NDIS\_STATUS\_WDI\_INDICATION\_CAN\_SUSTAIN\_AP](./ndis-status-wdi-indication-can-sustain-ap.md)

 

