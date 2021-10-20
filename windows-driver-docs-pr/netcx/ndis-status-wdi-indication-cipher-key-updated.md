---
title: NDIS_STATUS_WDI_INDICATION_CIPHER_KEY_UPDATED (dot11wificxintf.h)
description: WiFiCx drivers send this indication to indicate that the cipher key(s) have been updated.
ms.date: 08/30/2021
keywords:
 - NDIS_STATUS_WDI_INDICATION_CIPHER_KEY_UPDATED Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS_STATUS_WDI_INDICATION_CIPHER_KEY_UPDATED (dot11wificxintf.h)

[!INCLUDE[WiFiCx topic note](../includes/wificx-version-warning.md)]

WiFiCx drivers send this indication to indicate that the cipher key(s) have been updated.

This indication is sent only while the driver has not offloaded the RSN GTK rekey (via the WDI_TLV_PM_PROTOCOL_OFFLOAD_80211RSN_REKEY filed in the OID_WDI_SET_ADD_PM_PROTOCOL_OFFLOAD command). If the driver is currently in the offload state for the Rsn GTK Rekey, then it should not indicate via this method and should allow the updated key information to be queried via the OID_WDI_GET_PM_PROTOCOL_OFFLOAD command when it comes out of the offload state.

For example, the driver would send this notification if it or the firmware receives a new GTK/iGTK in the WNM-Sleep mode response.

## Payload data

| Type | Multiple TLV instances allowed | Optional | Description |
| --- | --- | --- | --- |
| [WDI_TLV_PM_PROTOCOL_RSN_OFFLOAD_KEYS](wdi-tlv-pm-protocol-rsn-offload-keys.md) |   |   | The currently configured Rsn Eapol key information. |

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|

