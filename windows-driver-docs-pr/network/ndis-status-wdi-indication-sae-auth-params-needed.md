---
title: NDIS_STATUS_WDI_INDICATION_SAE_AUTH_PARAMS_NEEDED
ms.topic: reference
description: NDIS_STATUS_WDI_INDICATION_SAE_AUTH_PARAMS_NEEDED
ms.date: 03/02/2023
keywords:
 - NDIS_STATUS_WDI_INDICATION_SAE_AUTH_PARAMS_NEEDED Network Drivers Starting with Windows Vista
ms.custom: 19H1
---

# NDIS_STATUS_WDI_INDICATION_SAE_AUTH_PARAMS_NEEDED

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]

The Wi-Fi adapter sends this indication to request parameters for Simultaneous Authentication of Equals (SAE) authentication.

When the miniport driver is requested to perform SAE authentication with a target BSSID, it needs to request information at various stages of authentication. Initially, it requests parameters for the Commit request frame, then the Confirm request frame if successful. If the driver encounters an irrecoverable timeout or error, it also indicates that to the OS.

This indication is sent during the SAE authentication process. For more information, see [WPA3-SAE authentication](wpa3-sae-authentication.md).

## Payload data

| TLV | Type | Multiple TLV instances allowed | Optional | Description |
| --- | --- | --- | --- | --- |
| [WDI_TLV_BSSID](wdi-tlv-bssid.md) | [**WDI_MAC_ADDRESS**](/windows-hardware/drivers/ddi/dot11wdi/ns-dot11wdi-_wdi_mac_address) |   |   | The BSS ID of the AP. |
| [WDI_TLV_SAE_INDICATION_TYPE](wdi-tlv-sae-indication-type.md) | [**WDI_SAE_INDICATION_TYPE**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_sae_indication_type) |   |   | The type of information needed to continue SAE authentication with the BSSID, or notification that authentication cannot continue. |
| [WDI_TLV_SAE_COMMIT_RESPONSE](wdi-tlv-sae-commit-response.md) | TLV\<LIST\<UINT8>> |   | X | The SAE Commit Response frame. |
| [WDI_TLV_SAE_CONFIRM_RESPONSE](wdi-tlv-sae-confirm-response.md) | TLV\<LIST\<UINT8>> |   | X | The SAE Confirm Response frame. |
| [WDI_TLV_SAE_STATUS](wdi-tlv-sae-status.md) | [**WDI_SAE_STATUS**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_sae_status) |   | X | The SAE authentication failure error status. |

## Requirements

**Minimum supported client**: Windows 10, version 1903

**Minimum supported server**: Windows Server 2016

**Header**: Dot11wdi.h
