---
title: NDIS_STATUS_WWAN_NETWORK_PARAMS_STATE
description: Miniport drivers use the NDIS_STATUS_WWAN_NETWORK_PARAMS_STATE notification to communicate changes to network configuration to the MB Service.
ms.date: 05/13/2021
keywords: 
 -NDIS_STATUS_WWAN_NETWORK_PARAMS_STATE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS_STATUS_WWAN_NETWORK_PARAMS_STATE

Miniport drivers use the NDIS_STATUS_WWAN_NETWORK_PARAMS_STATE notification to inform the MB Service about changes to network configuration data and/or policy information.

Drivers send an NDIS_STATUS_WWAN_NETWORK_PARAMS_STATE notification in response to an OID query request of [OID_WWAN_NETWORK_PARAMS](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-ndis_wwan_network_params_info).

This notification uses the [**NDIS_WWAN_NETWORK_PARAMS_INFO**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-ndis_wwan_register_params_info) structure which contains a [**WWAN_NETWORK_PARAMS_INFO**](/windows-hardware/drivers/ddi/wwan/ns-wwan-wwan_network_params_info) structure.

## Remarks

For more information see [OID_WWAN_NETWORK_PARAMS](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-ndis_wwan_network_params_info).

## Requirements

|Requirement|Value|
|-|-|
|Version|Windows Server 2022. NDIS 6.84 and later.|
|Header|Ndis.h|

## See also

[OID_WWAN_NETWORK_PARAMS](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-ndis_wwan_network_params_info)

[**NDIS_WWAN_NETWORK_PARAMS_INFO**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-ndis_wwan_register_params_info)

[**WWAN_NETWORK_PARAMS_INFO**](/windows-hardware/drivers/ddi/wwan/ns-wwan-wwan_network_params_info)