---
title: WDI_TLV_RSNA_AKM_CIPHER_SUITE (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_RSNA_AKM_CIPHER_SUITE is a WiFiCx TLV that contains the RSNA AKM and cipher pairs that the driver supports.
ms.date: 02/06/2024
---

# WDI_TLV_RSNA_AKM_CIPHER_SUITE (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]

WDI_TLV_RSNA_AKM_CIPHER_SUITE is a WiFiCx TLV that contains the Robust Security Network Association (RSNA) authentication and key management (AKM) and cipher pairs that the driver supports.

## TLV Type

0x209

## Length

The size (in bytes) of the array of [**RSNA_AKM_CIPHER_PAIR**](/windows-hardware/drivers/ddi/windot11/ns-windot11-rsna_akm_cipher_pair) structures. 

## Values

| Type | Description |
|-----------------|-----------------|
| [**RSNA_AKM_CIPHER_PAIR**](/windows-hardware/drivers/ddi/windot11/ns-windot11-rsna_akm_cipher_pair)[] | An array of RSNA AKM and cipher pairs. |

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|WIN11_NEXT|
|Header|dot11wificxtypes.hpp|
