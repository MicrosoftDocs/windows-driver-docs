---
title: WDI_TLV_HESSID_INFO (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_HESSID_INFO is a WiFiCx TLV that contains HESSID information - a list of HESSIDs, the Access Network Type, and Hotspot Indication Element.
ms.date: 08/30/2021
keywords:
 - WDI_TLV_HESSID_INFO Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_HESSID\_INFO (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_HESSID\_INFO is a TLV that contains HESSID information, which includes a list of HESSIDs, the Access Network Type, and Hotspot Indication Element.

## TLV Type


0xFF

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                                 | Multiple TLV instances allowed | Optional | Description                                                                              |
|--------------------------------------------------------------------------------------|--------------------------------|----------|------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_ACCESS\_NETWORK\_TYPE**](wdi-tlv-access-network-type.md)               |                                |          | The Access Network Type to be used in probe requests for the network being connected to. |
| [**WDI\_TLV\_HESSID**](wdi-tlv-hessid.md)                                           |                                |          | The list of HESSIDs that the port is allowed to connect to.                              |
| [**WDI\_TLV\_HOTSPOT\_INDICATION\_ELEMENT**](wdi-tlv-hotspot-indication-element.md) |                                |          | The Hotspot Indication Element to be used in the Association Request.                    |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 




