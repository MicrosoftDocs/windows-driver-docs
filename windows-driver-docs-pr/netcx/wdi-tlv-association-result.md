---
title: WDI_TLV_ASSOCIATION_RESULT (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_ASSOCIATION_RESULT is a WiFiCx TLV that contains the results of an association.
ms.date: 04/06/2022
keywords:
 - WDI_TLV_ASSOCIATION_RESULT Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_ASSOCIATION\_RESULT (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_ASSOCIATION\_RESULT is a TLV that contains the results of an association.

## TLV Type


0x35

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                                       | Multiple TLV instances allowed | Optional | Description                                                                                                                                                                                                 |
|--------------------------------------------------------------------------------------------|--------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_BSSID**](wdi-tlv-bssid.md)                                                   |                                |          | The BSSID of the BSS.                                                                                                                                                                                       |
| [**WDI\_TLV\_ASSOCIATION\_RESULT\_PARAMETERS**](wdi-tlv-association-result-parameters.md) |                                |          | The association result parameters.                                                                                                                                                                          |
| [**WDI\_TLV\_ASSOCIATION\_REQUEST\_FRAME**](wdi-tlv-association-request-frame.md)         |                                | X        | The association request that was used for association. This does not include the 802.11 MAC header.                                                                                                         |
| [**WDI\_TLV\_ASSOCIATION\_RESPONSE\_FRAME**](wdi-tlv-association-response-frame.md)       |                                | X        | The association response that was received. This does not include the 802.11 MAC header.                                                                                                                    |
| [**WDI\_TLV\_AUTHENTICATION\_RESPONSE\_FRAME**](wdi-tlv-authentication-response-frame.md) |                                | X        | The authentication response that was received with a failure code. This does not include the 802.11 MAC header. It should only be included if the connection attempt failed during authentication exchange. |
| [**WDI\_TLV\_BEACON\_PROBE\_RESPONSE**](wdi-tlv-beacon-probe-response.md)                 |                                | X        | The latest beacon or probe response frame received by the port. This does not include the 802.11 MAC header. In the case of DMG phy (802.11ad), only ProbeResponse frames should be included.                                                                                               |
| [**WDI\_TLV\_ETHERTYPE\_ENCAP\_TABLE**](wdi-tlv-ethertype-encap-table.md)                 |                                | X        | The Ethertype encapsulations for the association.                                                                                                                                                           |
| [**WDI\_TLV\_PHY\_TYPE\_LIST**](wdi-tlv-phy-type-list.md)                                 |                                |          | The list of PHY identifiers that the 802.11 station uses to send or receive packets on the BSS network connection.                                                                                          |
| [**WDI_TLV_MLO_LINK_BSSID**](wdi-tlv-mlo-link-bssid.md) |   | X | The local Link MAC address. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 




