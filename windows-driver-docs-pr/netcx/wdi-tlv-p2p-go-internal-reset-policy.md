---
title: WDI_TLV_P2P_GO_INTERNAL_RESET_POLICY (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_P2P_GO_INTERNAL_RESET_POLICY is a WiFiCx TLV that contains the policy used by the firmware for operating channel selection after a Wi-Fi Direct GO Reset is stopped/restarted.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_P2P_GO_INTERNAL_RESET_POLICY Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_GO\_INTERNAL\_RESET\_POLICY (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_P2P\_GO\_INTERNAL\_RESET\_POLICY is a TLV that contains the policy used by the firmware for operating channel selection after a Wi-Fi Direct GO Reset is stopped/restarted.

## TLV Type


0xB2

## Length


The size (in bytes) of a UINT32.

## Values


| Type                                                                                            | Description                                                                                                                                                                                                                                                        |
|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_P2P\_GO\_INTERNAL\_RESET\_POLICY**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_p2p_go_internal_reset_policy) (UINT32) | If an Wi-Fi Direct GO Reset is stopped/restarted by the IHV component on its own (for example, for Bluetooth co-ex spatial stream downgrade), this configuration defines the policy to be adopted by the firmware for operating channel selection after the reset. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

