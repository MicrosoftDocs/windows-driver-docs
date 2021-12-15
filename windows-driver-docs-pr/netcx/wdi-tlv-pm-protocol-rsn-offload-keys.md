---
title: WDI_TLV_PM_PROTOCOL_RSN_OFFLOAD_KEYS (dot11wificxtypes.hpp)
description: WDI_TLV_PM_PROTOCOL_RSN_OFFLOAD_KEYS is a WiFiCx TLV that contains currently configured Rsn Eapol key information.
ms.date: 08/31/2021
keywords:
 - WDI_TLV_PM_PROTOCOL_RSN_OFFLOAD_KEYS Network Drivers Starting with Windows Vista
---

# WDI_TLV_PM_PROTOCOL_RSN_OFFLOAD_KEYS (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]

WDI_TLV_PM_PROTOCOL_RSN_OFFLOAD_KEYS is a TLV that contains currently configured Rsn Eapol key information. This TLV is used in the [NDIS_STATUS_WDI_INDICATION_CIPHER_KEY_UPDATED](ndis-status-wdi-indication-cipher-key-updated.md) status indication.

## TLV Type

0x149

## Values

| Type | Description |
| --- | --- |
| WDI_RSN_OFFLOAD_KEYS_CONTAINER | The currently configured Rsn Eapol key information. |

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

