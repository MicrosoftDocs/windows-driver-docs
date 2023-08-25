---
title: NDIS_STATUS_WDI_INDICATION_SAE_AUTH_PARAMS_NEEDED (dot11wificxintf.h)
ms.topic: reference
description: The WiFiCx adapter sends NDIS_STATUS_WDI_INDICATION_SAE_AUTH_PARAMS_NEEDED to request parameters for SAE authentication.
ms.date: 08/18/2023
keywords:
 - NDIS_STATUS_WDI_INDICATION_SAE_AUTH_PARAMS_NEEDED Network Drivers Starting with Windows Vista
---

# NDIS_STATUS_WDI_INDICATION_SAE_AUTH_PARAMS_NEEDED (dot11wificxintf.h)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]

The Wi-Fi adapter sends this indication to request parameters for Simultaneous Authentication of Equals (SAE) authentication.

When the miniport driver is requested to perform SAE authentication with a target BSSID, it needs to request information at various stages of authentication. Initially, it requests parameters for the Commit request frame, then the Confirm request frame if successful. If the driver encounters an irrecoverable timeout or error, it also indicates that to the OS.

For SAE authentication using Wi-Fi 7 MLO, the driver should set:
  - the **BSSID** ([WDI_TLV_BSSID](wdi-tlv-bssid.md)) to the AP's Link MAC address. 
  - the **LocalMloLinkBssId** ([WDI_TLV_MLO_LINK_BSSID](wdi-tlv-mlo-link-bssid.md)) to the local Link MAC address.

This indication is sent during the SAE authentication process. For more information, see [WPA3-SAE authentication](wificx-wpa3-sae-authentication.md).

## Payload data

| TLV | Type | Multiple TLV instances allowed | Optional | Description |
| --- | --- | --- | --- | --- |
| [WDI_TLV_BSSID](wdi-tlv-bssid.md) | [**WDI_MAC_ADDRESS**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_mac_address) |   |   | The BSSID of the AP. |
| [WDI_TLV_SAE_INDICATION_TYPE](wdi-tlv-sae-indication-type.md) | [**WDI_SAE_INDICATION_TYPE**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_sae_indication_type) |   |   | The type of information needed to continue SAE authentication with the BSSID, or notification that authentication cannot continue. |
| [WDI_TLV_SAE_COMMIT_FRAME](wdi-tlv-sae-commit-frame.md) | TLV\<LIST\<UINT8>> |   | X | The SAE Commit Response frame. |
| [WDI_TLV_SAE_CONFIRM_FRAME](wdi-tlv-sae-confirm-frame.md) | TLV\<LIST\<UINT8>> |   | X | The SAE Confirm Response frame. |
| [WDI_TLV_SAE_STATUS](wdi-tlv-sae-status.md) | [**WDI_SAE_STATUS**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_sae_status) |   | X | The SAE authentication failure error status. |
| [WDI_TLV_MLO_LINK_BSSID](wdi-tlv-mlo-link-bssid.md) | [**WDI_MAC_ADDRESS**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_mac_address) |   | X | The local Link MAC address. |

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|
