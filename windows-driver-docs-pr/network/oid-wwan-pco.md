---
title: OID_WWAN_PCO
ms.topic: reference
description: OID_WWAN_PCO reports the status and the payload of a PCO value that the modem has received from the operator network. 
keywords:
- OID_WWAN_PCO, PCO OID
ms.date: 08/08/2017
---

# OID_WWAN_PCO

OID_WWAN_PCO reports the status and the payload of a Protocol Configuration Optiont (PCO) value that the modem has received from a mobile operator network. The PCO value that is returned from the modem corresponds to the PDN that the port number specifies in the OID request structure.

For query requests, the modem first responds with NDIS_STATUS_INDICATION_REQUIRED when it receives this OID. An [NDIS_STATUS_WWAN_PCO_STATUS](ndis-status-wwan-pco-status.md) notification will be returned containing an [NDIS_WWAN_PCO_STATUS](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_pco_status) structure when the query request is completed. **NDIS_WWAN_PCO_STATUS**, in turn, contains the PCO status and a [WWAN_PCO_VALUE](/windows-hardware/drivers/ddi/wwan/ns-wwan-_wwan_pco_value) structure that represents the PCO value.

Set requests are not applicable.

## Remarks

For modems that choose to use the Microsoft inbox miniport class driver, to receive query requests from the host, the modem must advertise that it supports the new **MBIM_CID_PCO** CID (index = 9) in the **MBB_UUID_BASIC_CONNECT_EXT_CONSTANT** service when responding to an **MBIM_CID_DEVICE_SERVICES** query. For more info about *MBIM_CID_PCO*, see [MB Protocol Configuration Options (PCO) operations](mb-protocol-configuration-options-pco-operations.md).

For modems that choose not use Microsoft inbox miniport class driver, to receive query requests from WWANSVC, the modem’s miniport driver must advertise that it supports the *WWAN_OPTIONAL_SERVICE_CAPS_PCO* option when responding to [OID OID_WWAN_DEVICE_CAPS_EX](oid-wwan-device-caps-ex.md) query requests.

## Requirements

**Version**: Windows 10, version 1709
**Header**: Ntddndis.h (include Ndis.h)

## See also

[**NDIS_STATUS_WWAN_PCO_STATUS**](ndis-status-wwan-pco-status.md)

[**NDIS_WWAN_PCO_STATUS**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_pco_status)

[**WWAN_PCO_VALUE**](/windows-hardware/drivers/ddi/wwan/ns-wwan-_wwan_pco_value) 

[**OID OID_WWAN_DEVICE_CAPS_EX**](oid-wwan-device-caps-ex.md)

[MB Protocol Configuration Options (PCO) operations](mb-protocol-configuration-options-pco-operations.md)
