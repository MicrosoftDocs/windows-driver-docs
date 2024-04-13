---
title: WDI_TLV_ASSOCIATION_RESPONSE_RESULT_PARAMETERS (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_ASSOCIATION_RESPONSE_RESULT_PARAMETERS is a WiFiCx TLV that contains association response result parameters.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_ASSOCIATION_RESPONSE_RESULT_PARAMETERS Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_ASSOCIATION\_RESPONSE\_RESULT\_PARAMETERS (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_ASSOCIATION\_RESPONSE\_RESULT\_PARAMETERS is a TLV that contains association response result parameters.

## TLV Type


0x76

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


|Type|Description|
|--- |--- |
|[**WDI_MAC_ADDRESS**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_mac_address)|The MAC address of the peer adapter.|
|UINT8|A bit value that indicates whether the request from the peer station is a reassociation request. Valid values are 0 and 1\. A value of 1 indicates that it is a reassociation request.|
|UINT8|A bit value that indicates whether the response from the peer station is a reassociation response. Valid values are 0 and 1\. A value of 1 indicates that it is a reassociation response.|
|[**WDI_AUTH_ALGORITHM**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_auth_algorithm)|The authentication algorithm for the association.|
|[**WDI_CIPHER_ALGORITHM**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_cipher_algorithm)|The unicast cipher algorithm for the association.|
|[**WDI_CIPHER_ALGORITHM**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_cipher_algorithm)|The multicast cipher algorithm for the association.|

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

