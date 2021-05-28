---
title: OID_WWAN_REGISTER_PARAMS
description: OID_WWAN_REGISTER_PARAMS sets or returns the parameters that an MB device uses during 5G registration requests.
ms.date: 05/13/2021
keywords: 
 -OID_WWAN_REGISTER_PARAMS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID_WWAN_REGISTER_PARAMS

OID_WWAN_REGISTER_PARAMS sets or returns the parameters that an MB device uses during 5G registration requests.

Before turning on the device radio, the host typically sends an OID_WWAN_REGISTER_PARAMS set request to configure the device with the desired registration parameters. This OID's payload contains an [**NDIS_WWAN_SET_REGISTER_PARAMS**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-ndis_wwan_set_register_params) structure, which in turn contains a [**WWAN_REGISTRATION_PARAMS_INFO**](/windows-hardware/drivers/ddi/wwan/ns-wwan-wwan_registration_params_info) structure that specifies the registration parameters such as a default PDU session hint. If the device accepts these parameters, it will use them during 5G registration requests. 

The host may send an OID_WWAN_REGISTER_PARAMS set request at any time. When the device receives this request, it must compare the new parameters to any parameters it previously used for 5G registration. If there are differences, the device should use the newly received parameters for the next 5G registration. The host can also use the [**WWAN_REGISTRATION_PARAMS_INFO**](/windows-hardware/drivers/ddi/wwan/ns-wwan-wwan_registration_params_info) structure's **ReRegisterIfNeeded** parameter to force immediate 5G re-registration.  

The host may use this OID to query the registration parameters that an MB device is currently using for 5G registration. 

## Remarks

Miniport drivers must process set and query requests asynchronously, initially returning NDIS_STATUS_INDICATION_REQUIRED to the original request before later sending an [NDIS_STATUS_WWAN_REGISTER_PARAMS_STATE](/windows-hardware/drivers/network/ndis-status-wwan-register-params-state) status notification containing an [**NDIS_WWAN_REGISTER_PARAMS_INFO**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-ndis_wwan_register_params_info) structure, which contains a [**WWAN_REGISTRATION_PARAMS_INFO**](/windows-hardware/drivers/ddi/wwan/ns-wwan-wwan_registration_params_info) structure.

For a failured set or query response, the information shall be null and the **InformationBufferLength** shall be zero.

In a successful set response, the **WWAN_REGISTRATION_PARAMS_INFO** structure shall contain the parameters set by the host and accepted by the device.

In a successful query response:

* If the parameters have been set by the host and accepted by the device since the device was rebooted or a different SIM was inserted, the structure shall contain the parameters set by the host and accepted by the device.

* If the parameters have not been set by the host and accepted by the device since the device was rebooted or a different SIM was inserted, the structure shall contain the parameters that the device will most likely use for 5G registration.

For more information about usage of this OID, see MBIM_CID_MS_REGISTRATION_PARAMS in the [MBIMEx 3.0 specification](https://download.microsoft.com/download/8/3/a/83a64106-a1f4-4a03-811f-4dbef2e3bf7a/MBIM%20extensions%20for%205G.docx).


## Requirements

|Requirement|Value|
|-|-|
|Version|Windows Server 2022. NDIS 6.84 and later.|
|Header|Ntddndis.h (include Ndis.h)|

## See also

[**WWAN_REGISTRATION_PARAMS_INFO**](/windows-hardware/drivers/ddi/wwan/ns-wwan-wwan_registration_params_info)

[NDIS_STATUS_WWAN_REGISTER_PARAMS_STATE](/windows-hardware/drivers/network/ndis-status-wwan-register-params-state)