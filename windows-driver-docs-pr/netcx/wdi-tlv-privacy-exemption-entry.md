---
title: WDI_TLV_PRIVACY_EXEMPTION_ENTRY (dot11wificxtypes.hpp)
description: WDI_TLV_PRIVACY_EXEMPTION_ENTRY is a WiFiCx TLV that contains a privacy exemption entry.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_PRIVACY_EXEMPTION_ENTRY Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_PRIVACY\_EXEMPTION\_ENTRY (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_PRIVACY\_EXEMPTION\_ENTRY is a TLV that contains a privacy exemption entry.

## TLV Type


0x48

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                                                   | Description                                                 |
|------------------------------------------------------------------------|-------------------------------------------------------------|
| UINT16                                                                 | Specifies the IEEE EtherType in big-endian byte order.      |
| [**WDI\_EXEMPTION\_ACTION\_TYPE**](/windows-hardware/drivers/ddi/dot11wificxintf/ne-dot11wificxintf-wdi_exemption_action_type) | Specifies the action type of the exemption.                 |
| [**WDI\_EXEMPTION\_PACKET\_TYPE**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_exemption_packet_type) | Specifies the type of packet that the exemption applies to. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

