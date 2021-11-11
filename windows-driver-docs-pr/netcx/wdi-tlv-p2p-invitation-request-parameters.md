---
title: WDI_TLV_P2P_INVITATION_REQUEST_PARAMETERS (dot11wificxtypes.hpp)
description: WDI_TLV_P2P_INVITATION_REQUEST_PARAMETERS is a WiFiCx TLV that contains Wi-Fi Direct Invitation Request parameters.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_P2P_INVITATION_REQUEST_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_INVITATION\_REQUEST\_PARAMETERS (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_P2P\_INVITATION\_REQUEST\_PARAMETERS is a TLV that contains Wi-Fi Direct Invitation Request parameters.

## TLV Type


0x7C

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


|Type|Description|
|--- |--- |
|UINT16|The Group Owner Configuration Timeout in milliseconds.|
|UINT16|The Client Configuration Timeout in milliseconds.|
|UINT8|The invitation flags as defined by the Wi-Fi Direct specification.|
|UINT8|A bit that indicates whether or not the outgoing Invitation Request is an invitation to a local Group Owner. Valid values are 0 and 1. This bit is set to 1 if it is an invitation to a local GO.|

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|


 

 




