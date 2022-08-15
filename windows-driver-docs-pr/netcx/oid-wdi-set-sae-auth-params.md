---
title: OID_WDI_SET_SAE_AUTH_PARAMS (dot11wificxintf.h)
description: The OID_WDI_SET_SAE_AUTH_PARAMS command contains parameters required to send the SAE Commit or Confirm request, or an error message.
ms.date: 07/31/2021
keywords:
 - OID_WDI_SET_SAE_AUTH_PARAMS Network Drivers Starting with Windows Vista
---

# OID_WDI_SET_SAE_AUTH_PARAMS (dot11wificxintf.h)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]

**OID_WDI_SET_SAE_AUTH_PARAMS** is sent by WDI in response to an [NDIS_STATUS_WDI_INDICATION_SAE_AUTH_PARAMS_NEEDED](ndis-status-wdi-indication-sae-auth-params-needed.md) indication from the driver. It contains the parameters required to send the Simultaneous Authentication of Equals (SAE) Commit or Confirm request, or an error message indicating a failure to perform SAE with the BSSID. 

This command is sent as a Direct OID request to the driver.

For more information about SAE authentication, see [WiFiCx WPA3 SAE authentication](wificx-wpa3-sae-authentication.md).

## Command parameters

| TLV | Type | Multiple TLV instances allowed | Optional | Description |
| --- | --- | --- | --- | --- |
| [WDI_TLV_BSSID](wdi-tlv-bssid.md) | [**WDI_MAC_ADDRESS**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_mac_address) |  |  | The BSSID of the AP. |
| [WDI_TLV_SAE_REQUEST_TYPE](wdi-tlv-sae-request-type.md) | [**WDI_SAE_REQUEST_TYPE**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_sae_request_type) |   |   | The type of SAE request frame to send to the BSSID. |
| [WDI_TLV_SAE_COMMIT_REQUEST](wdi-tlv-sae-commit-request.md) | WDI_SAE_COMMIT_REQUEST |  | X | The SAE Commit request parameters. |
| [WDI_TLV_SAE_CONFIRM_REQUEST](wdi-tlv-sae-confirm-request.md) | WDI_SAE_CONFIRM_REQUEST |  | X | The SAE Confirm request parameters. |
| [WDI_TLV_SAE_STATUS](wdi-tlv-sae-status.md) | [**WDI_SAE_STATUS**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_sae_status) |   | X | SAE authentication failure error status. |

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|
