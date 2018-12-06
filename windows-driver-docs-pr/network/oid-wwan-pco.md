---
title: OID_WWAN_PCO
description: OID_WWAN_PCO reports the status and the payload of a PCO value that the modem has received from the operator network. 
ms.assetid: BE664B41-3FE7-4E93-8739-12BD2F0AE5B8
keywords:
- OID_WWAN_PCO, PCO OID
ms.date: 08/08/2017
ms.localizationpriority: medium
---

# OID_WWAN_PCO

OID_WWAN_PCO reports the status and the payload of a Protocol Configuration Optiont (PCO) value that the modem has received from a mobile operator network. The PCO value that is returned from the modem corresponds to the PDN that the port number specifies in the OID request structure.

For query requests, the modem first responds with NDIS_STATUS_INDICATION_REQUIRED when it receives this OID. An [NDIS_STATUS_WWAN_PCO_STATUS](ndis-status-wwan-pco-status.md) notification will be returned containing an [NDIS_WWAN_PCO_STATUS](https://msdn.microsoft.com/library/windows/hardware/C71187C5-74B6-450A-8461-BB9FDF60DB8D) structure when the query request is completed. **NDIS_WWAN_PCO_STATUS**, in turn, contains the PCO status and a [WWAN_PCO_VALUE](https://msdn.microsoft.com/library/windows/hardware/45A499CE-2C9A-4070-BEF8-880E7673FA8E) structure that represents the PCO value.

Set requests are not applicable.

## Remarks

For modems that choose to use the Microsoft inbox miniport class driver, to receive query requests from the host, the modem must advertise that it supports the new **MBIM_CID_PCO** CID (index = 9) in the **MBB_UUID_BASIC_CONNECT_EXT_CONSTANT** service when responding to an **MBIM_CID_DEVICE_SERVICES** query. For more info about *MBIM_CID_PCO*, see [MB Protocol Configuration Options (PCO) operations](mb-protocol-configuration-options-pco-operations.md).

For modems that choose not use Microsoft inbox miniport class driver, to receive query requests from WWANSVC, the modem’s miniport driver must advertise that it supports the *WWAN_OPTIONAL_SERVICE_CAPS_PCO* option when responding to [OID OID_WWAN_DEVICE_CAPS_EX](oid-wwan-device-caps-ex.md) query requests.

## Requirements

| | |
| --- | --- |
| Version | Windows 10, version 1709 |
| Header | Ntddndis.h (include Ndis.h) |

## See also

[**NDIS_STATUS_WWAN_PCO_STATUS**](ndis-status-wwan-pco-status.md)

[**NDIS_WWAN_PCO_STATUS**](https://msdn.microsoft.com/library/windows/hardware/C71187C5-74B6-450A-8461-BB9FDF60DB8D)

[**WWAN_PCO_VALUE**](https://msdn.microsoft.com/library/windows/hardware/45A499CE-2C9A-4070-BEF8-880E7673FA8E) 

[**OID OID_WWAN_DEVICE_CAPS_EX**](oid-wwan-device-caps-ex.md)

[MB Protocol Configuration Options (PCO) operations](mb-protocol-configuration-options-pco-operations.md)
