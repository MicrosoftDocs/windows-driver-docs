---
title: NDIS_STATUS_WDI_INDICATION_CIPHER_KEY_UPDATED
ms.topic: reference
description: NDIS_STATUS_WDI_INDICATION_CIPHER_KEY_UPDATED
ms.date: 03/02/2023
keywords:
 - NDIS_STATUS_WDI_INDICATION_CIPHER_KEY_UPDATED Network Drivers Starting with Windows Vista
ms.custom: 19H1
---

# NDIS_STATUS_WDI_INDICATION_CIPHER_KEY_UPDATED

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]

Miniport drivers send this indication to indicate that the cipher key(s) have been updated.

This indication is sent only while the driver has not offload the RSN GTK rekey (via the [WDI_TLV_PM_PROTOCOL_OFFLOAD_80211RSN_REKEY](wdi-tlv-pm-protocol-offload-80211rsn-rekey.md) filed in the [OID_WDI_SET_ADD_PM_PROTOCOL_OFFLOAD](oid-wdi-set-add-pm-protocol-offload.md) command). If the driver is currently in the offload state for the Rsn GTK Rekey, then it should not indicate via this method and should allow the updated key information to be queried via the [OID_WDI_GET_PM_PROTOCOL_OFFLOAD](oid-wdi-get-pm-protocol-offload.md) command when it comes out of the offload state.

For example, the driver would send this notification if it or the firmware receives a new GTK/iGTK in the WNM-Sleep mode response.

## Payload data

| Type | Multiple TLV instances allowed | Optional | Description |
| --- | --- | --- | --- |
| [WDI_TLV_PM_PROTOCOL_RSN_OFFLOAD_KEYS](wdi-tlv-pm-protocol-rsn-offload-keys.md) |   |   | The currently configured Rsn Eapol key information. |

## Requirements

**Minimum supported client**: Windows 10, version 1803

**Minimum supported server**: Windows Server 2016

**Header**: Dot11wdi.h

