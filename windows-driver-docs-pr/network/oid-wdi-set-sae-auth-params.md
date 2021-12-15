---
title: OID_WDI_SET_SAE_AUTH_PARAMS
description: OID_WDI_SET_SAE_AUTH_PARAMS is sent by WDI in response to an NDIS_STATUS_WDI_INDICATION_SAE_AUTH_PARAMS_NEEDED indication from the driver. It contains the parameters required to send the Simultaneous Authentication of Equals (SAE) Commit or Confirm request, or an error message indicating a failure to perform SAE with the BSSID.
ms.date: 02/15/2019
keywords:
 - OID_WDI_SET_SAE_AUTH_PARAMS Network Drivers Starting with Windows Vista
ms.custom: 19H1
---

# OID_WDI_SET_SAE_AUTH_PARAMS

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]

**OID_WDI_SET_SAE_AUTH_PARAMS** is sent by WDI in response to an [NDIS_STATUS_WDI_INDICATION_SAE_AUTH_PARAMS_NEEDED](ndis-status-wdi-indication-sae-auth-params-needed.md) indication from the driver. It contains the parameters required to send the Simultaneous Authentication of Equals (SAE) Commit or Confirm request, or an error message indicating a failure to perform SAE with the BSSID. 

This command is sent as a Direct OID request to the driver.

For more information about SAE authentication, see [WPA3 SAE authentication](wpa3-sae-authentication.md).

## Command parameters

| TLV | Type | Multiple TLV instances allowed | Optional | Description |
| --- | --- | --- | --- | --- |
| [WDI_TLV_BSSID](wdi-tlv-bssid.md) | [**WDI_MAC_ADDRESS**](/windows-hardware/drivers/ddi/dot11wdi/ns-dot11wdi-_wdi_mac_address) |  |  | The BSSID of the AP. |
| [WDI_TLV_SAE_REQUEST_TYPE](wdi-tlv-sae-request-type.md) | [**WDI_SAE_REQUEST_TYPE**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_sae_request_type) |   |   | The type of SAE request frame to send to the BSSID. |
| [WDI_TLV_SAE_COMMIT_REQUEST](wdi-tlv-sae-commit-request.md) | WDI_SAE_COMMIT_REQUEST |  | X | The SAE Commit request parameters. |
| [WDI_TLV_SAE_CONFIRM_REQUEST](wdi-tlv-sae-confirm-request.md) | WDI_SAE_CONFIRM_REQUEST |  | X | The SAE Confirm request parameters. |
| [WDI_TLV_SAE_STATUS](wdi-tlv-sae-status.md) | [**WDI_SAE_STATUS**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_sae_status) |   | X | SAE authentication failure error status. |

## Requirements

**Minimum supported client**: Windows 10, version 1903

**Minimum supported server**: Windows Server 2016

**Header**: Dot11wdi.h
