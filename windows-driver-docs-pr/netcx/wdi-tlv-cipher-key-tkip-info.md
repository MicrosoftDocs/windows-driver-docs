---
title: WDI_TLV_CIPHER_KEY_TKIP_INFO (dot11wificxtypes.hpp)
description: WDI_TLV_CIPHER_KEY_TKIP_INFO is a WiFiCx TLV that contains TKIP information.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_CIPHER_KEY_TKIP_INFO Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_CIPHER\_KEY\_TKIP\_INFO (dot11wificxtypes.hpp)

[!INCLUDE[WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_CIPHER\_KEY\_TKIP\_INFO is a TLV that contains TKIP information.

## TLV Type


0x4B

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                    | Multiple TLV instances allowed | Optional | Description                      |
|-------------------------------------------------------------------------|--------------------------------|----------|----------------------------------|
| [**WDI\_TLV\_CIPHER\_KEY\_TKIP\_KEY**](wdi-tlv-cipher-key-tkip-key.md) |                                |          | Specifies the TKIP key material. |
| [**WDI\_TLV\_CIPHER\_KEY\_TKIP\_MIC**](wdi-tlv-cipher-key-tkip-mic.md) |                                |          | Specifies the TKIP MIC material. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 




