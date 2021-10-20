---
title: WDI_TLV_P2P_INVITATION_RESPONSE_PARAMETERS (dot11wificxtypes.hpp)
description: WDI_TLV_P2P_INVITATION_RESPONSE_PARAMETERS is a WiFiCx TLV that contains Wi-Fi Direct Invitation Response parameters.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_P2P_INVITATION_RESPONSE_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_INVITATION\_RESPONSE\_PARAMETERS (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_P2P\_INVITATION\_RESPONSE\_PARAMETERS is a TLV that contains Wi-Fi Direct Invitation Response parameters.

## TLV Type


0x80

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type   | Description                                                                    |
|--------|--------------------------------------------------------------------------------|
| UINT8  | The Wi-Fi Direct Status Code, as specified by the Wi-Fi Direct specification.. |
| UINT16 | The GO Configuration Timeout, in milliseconds.                                 |
| UINT16 | The Client Configuration Timeout, in milliseconds.                             |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|


 

 




