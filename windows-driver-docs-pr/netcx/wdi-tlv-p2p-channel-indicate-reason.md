---
title: WDI_TLV_P2P_CHANNEL_INDICATE_REASON (dot11wificxtypes.hpp)
description: WDI_TLV_P2P_CHANNEL_INDICATE_REASON is a WiFiCx TLV that contains a reason for sending an indication.
ms.date: 08/30/2021
keywords:
 - WDI_TLV_P2P_CHANNEL_INDICATE_REASON Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_CHANNEL\_INDICATE\_REASON (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_P2P\_CHANNEL\_INDICATE\_REASON is a TLV that contains a reason for sending an indication.

## TLV Type


0x102

## Length


The size (in bytes) of a UINT32.

## Values


| Type   | Description                                                                                                                                         |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT32 | The reason for sending an indication. See [**WDI\_P2P\_CHANNEL\_INDICATE\_REASON**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_p2p_channel_indicate_reason) for possible reasons. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

