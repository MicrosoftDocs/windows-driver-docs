---
title: WDI_TLV_P2P_GO_NEGOTIATION_CONFIRMATION_PARAMETERS (dot11wificxtypes.hpp)
description: WDI_TLV_P2P_GO_NEGOTIATION_CONFIRMATION_PARAMETERS is a WiFiCx TLV that contains incoming GO Negotiation Confirmation parameters.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_P2P_GO_NEGOTIATION_CONFIRMATION_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_GO\_NEGOTIATION\_CONFIRMATION\_PARAMETERS (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_P2P\_GO\_NEGOTIATION\_CONFIRMATION\_PARAMETERS is a TLV that contains incoming GO Negotiation Confirmation parameters.

## TLV Type


0xAA

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type  | Description                                                                                                                                                          |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT8 | The Wi-Fi Direct Status Code, as defined by the Wi-Fi Direct specification.                                                                                          |
| UINT8 | Wi-Fi Direct Group capability bitmask. The bitmask matches those defined in Table 13-Group Capability Bitmap definition of the Wi-Fi Direct technical specification. |
| UINT8 | The bits in the Group capability bitmap above that are set by the operating system.                                                                                  |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 




