---
title: NDIS_STATUS_WWAN_REGISTER_PARAMS_STATE
description: Miniport drivers use the NDIS_STATUS_WWAN_REGISTER_PARAMS_STATE notification to communicate changes to the MB device's 5G-specific registration parameters to the MB Service.
ms.date: 05/13/2021
keywords: 
 -NDIS_STATUS_WWAN_REGISTER_PARAMS_STATE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS_STATUS_WWAN_REGISTER_PARAMS_STATE

Miniport drivers use the NDIS_STATUS_WWAN_REGISTER_PARAMS_STATE notification to inform the MB Service about the 5G-specific registration parameters used by the MB device.

Drivers send an NDIS_STATUS_WWAN_REGISTER_PARAMS_STATE notification in response to an OID query or set request of [OID_WWAN_REGISTER_PARAMS](/windows-hardware/drivers/network/oid-wwan-register-params).

This notification uses the [**NDIS_WWAN_REGISTER_PARAMS_INFO**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-ndis_wwan_register_params_info) structure which contains a  [**WWAN_REGISTRATION_PARAMS_INFO**](/windows-hardware/drivers/ddi/wwan/ns-wwan-wwan_registration_params_info) structure.

## Remarks

For more information see [OID_WWAN_REGISTER_PARAMS](/windows-hardware/drivers/network/oid-wwan-register-params).

## Requirements

|Requirement|Value|
|-|-|
|Version|Windows Server 2022. NDIS 6.84 and later.|
|Header|Ndis.h|

## See also

[**WWAN_REGISTRATION_PARAMS_INFO**](/windows-hardware/drivers/ddi/wwan/ns-wwan-wwan_registration_params_info)

[**NDIS_WWAN_REGISTER_PARAMS_INFO**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-ndis_wwan_register_params_info)

[OID_WWAN_REGISTER_PARAMS](/windows-hardware/drivers/network/oid-wwan-register-params)

