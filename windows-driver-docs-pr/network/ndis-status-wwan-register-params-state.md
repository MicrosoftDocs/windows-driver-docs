---
title: NDIS_STATUS_WWAN_REGISTER_PARAMS_STATE
ms.topic: reference
description: Miniport drivers use the NDIS_STATUS_WWAN_REGISTER_PARAMS_STATE notification to communicate changes to the MB device's 5G-specific registration parameters to the MB Service.
ms.date: 03/02/2023
keywords: 
 -NDIS_STATUS_WWAN_REGISTER_PARAMS_STATE Network Drivers Starting with Windows Vista
---

# NDIS_STATUS_WWAN_REGISTER_PARAMS_STATE

Miniport drivers use the NDIS_STATUS_WWAN_REGISTER_PARAMS_STATE notification to inform the MB Service about the 5G-specific registration parameters used by the MB device.

Drivers send an NDIS_STATUS_WWAN_REGISTER_PARAMS_STATE notification in response to an OID query or set request of [OID_WWAN_REGISTER_PARAMS](./oid-wwan-register-params.md).

This notification uses the [**NDIS_WWAN_REGISTER_PARAMS_INFO**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-ndis_wwan_register_params_info) structure which contains a  [**WWAN_REGISTRATION_PARAMS_INFO**](/windows-hardware/drivers/ddi/wwan/ns-wwan-wwan_registration_params_info) structure.

## Remarks

For more information see [OID_WWAN_REGISTER_PARAMS](./oid-wwan-register-params.md).

## Requirements

|Requirement|Value|
|-|-|
|Minimum supported client|Windows 11|
|Version|Windows Server 2022. NDIS 6.84 and later.|
|Header|Ndis.h|

## See also

[**WWAN_REGISTRATION_PARAMS_INFO**](/windows-hardware/drivers/ddi/wwan/ns-wwan-wwan_registration_params_info)

[**NDIS_WWAN_REGISTER_PARAMS_INFO**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-ndis_wwan_register_params_info)

[OID_WWAN_REGISTER_PARAMS](./oid-wwan-register-params.md)
