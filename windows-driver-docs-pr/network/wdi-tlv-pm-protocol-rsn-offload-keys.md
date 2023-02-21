---
title: WDI_TLV_PM_PROTOCOL_RSN_OFFLOAD_KEYS
ms.topic: reference
description: WDI_TLV_PM_PROTOCOL_RSN_OFFLOAD_KEYS is a TLV that contains currently configured Rsn Eapol key information.
ms.date: 04/02/2018
keywords:
 - WDI_TLV_PM_PROTOCOL_RSN_OFFLOAD_KEYS Network Drivers Starting with Windows Vista
---

# WDI_TLV_PM_PROTOCOL_RSN_OFFLOAD_KEYS

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]

WDI_TLV_PM_PROTOCOL_RSN_OFFLOAD_KEYS is a TLV that contains currently configured Rsn Eapol key information. This TLV is used in the [NDIS_STATUS_WDI_INDICATION_CIPHER_KEY_UPDATED](ndis-status-wdi-indication-cipher-key-updated.md) status indication.

## TLV Type

0x149

## Values

| Type | Description |
| --- | --- |
| WDI_RSN_OFFLOAD_KEYS_CONTAINER | The currently configured Rsn Eapol key information. |

## Requirements

**Minimum supported client**: Windows 10, version 1803

**Minimum supported server**: Windows Server 2016

**Header**: Wditypes.hpp

