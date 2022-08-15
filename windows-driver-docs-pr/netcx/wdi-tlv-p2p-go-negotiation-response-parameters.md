---
title: WDI_TLV_P2P_GO_NEGOTIATION_RESPONSE_PARAMETERS (dot11wificxtypes.hpp)
description: WDI_TLV_P2P_GO_NEGOTIATION_RESPONSE_PARAMETERS is a WiFiCx TLV that contains incoming GO Negotiation Response parameters.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_P2P_GO_NEGOTIATION_RESPONSE_PARAMETERS Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_GO\_NEGOTIATION\_RESPONSE\_PARAMETERS (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_P2P\_GO\_NEGOTIATION\_RESPONSE\_PARAMETERS is a TLV that contains incoming GO Negotiation Response parameters.

## TLV Type


0x71

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                              | Description                                                                                                                                                                     |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT8                                             | Specifies the Wi-Fi Direct Status Code, as defined by the Wi-Fi Direct specification.                                                                                           |
| UINT8                                             | Specifies the local Wi-Fi Direct GO Intent. This is a value between 0 and 15.                                                                                                   |
| UINT8                                             | Specifies the tie-breaker field of the GO Intent.                                                                                                                               |
| UINT16                                            | Specifies the GO Configuration Timeout in milliseconds.                                                                                                                         |
| UINT16                                            | Specifies the Client Configuration Timeout in milliseconds.                                                                                                                     |
| [**WDI\_MAC\_ADDRESS**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_mac_address) | Intended interface address. Specifies the local MAC Address for future Wi-Fi Direct connection.                                                                                 |
| UINT8                                             | Specifies the Wi-Fi Direct Group capability bitmask. The bitmask matches those defined in Table 13-Group Capability Bitmap definition of the Wi-Fi P2P technical specification. |
| UINT8                                             | Specifies the bits set by the operating system in the Group capability bitmap above.                                                                                            |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

