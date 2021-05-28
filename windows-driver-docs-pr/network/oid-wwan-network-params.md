---
title: OID_WWAN_NETWORK_PARAMS
description: OID_WWAN_NETWORK_PARAMS retrieves the network parameters from an MB device.
ms.date: 06/15/2021
keywords: 
 -OID_WWAN_NETWORK_PARAMS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID_WWAN_NETWORK_PARAMS

The host may send an OID_WWAN_NETWORK_PARAMS query request to retrieve network configuration data and/or policy information from an MB device.

Set requests are not valid. 

Miniport drivers must process query requests asynchronously, initially returning NDIS_STATUS_INDICATION_REQUIRED to the original request, and later sending an [NDIS_STATUS_WWAN_NETWORK_PARAMS_STATE](ndis-status-wwan-network-params-state.md) status notification.

## Remarks

For more information about usage of this OID, see MBIM_CID_MS_NETWORK_PARAMS in the [MBIMEx 3.0 specification](https://download.microsoft.com/download/8/3/a/83a64106-a1f4-4a03-811f-4dbef2e3bf7a/MBIM%20extensions%20for%205G.docx).

## Requirements

|Requirement|Value|
|-|-|
|Version|Windows Server 2022. NDIS 6.84 and later.|
|Header|Ntddndis.h (include Ndis.h)|

## See also

[NDIS_STATUS_WWAN_NETWORK_PARAMS_STATE](ndis-status-wwan-network-params-state.md)