---
title: WDI_TLV_CIPHER_KEY_RECEIVE_SEQUENCE_COUNT (dot11wificxtypes.hpp)
description: WDI_TLV_CIPHER_KEY_RECEIVE_SEQUENCE_COUNT is a WiFix TLV that contains the receive sequence count.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_CIPHER_KEY_RECEIVE_SEQUENCE_COUNT Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_CIPHER\_KEY\_RECEIVE\_SEQUENCE\_COUNT (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_CIPHER\_KEY\_RECEIVE\_SEQUENCE\_COUNT is a TLV that contains the receive sequence count.

## TLV Type


0x4F

## Length


The size (in bytes) of the array of UINT8 elements.

## Values


| Type       | Description                                                                                    |
|------------|------------------------------------------------------------------------------------------------|
| UINT8\[6\] | Specifies the initial 48-bit value of Packet Number (PN), which is used for replay protection. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 




