---
title: OID_WWAN_PCO
author: windows-driver-content
description: OID_WWAN_PCO reports the status and the payload of a PCO value that the modem has received from the operator network. 
ms.assetid: BE664B41-3FE7-4E93-8739-12BD2F0AE5B8
keywords:
- OID_WWAN_PCO, PCO OID
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# OID_WWAN_PCO

OID_WWAN_PCO reports the status and the payload of a PCO value that the modem has received from the operator network. The PCO value that is returned from the modem corresponds to the PDN that the port number specifies in the OID request structure.

For query requests, the modem first responds with NDIS_STATUS_INDICATION_REQUIRED when it receives this OID. An [NDIS_STATUS_WWAN_PCO_STATUS](ndis-status-wwan-pco-status.md) notification will be returned containing an [NDIS_WWAN_PCO_STATUS](TBD) structure when the query request is completed. **NDIS_WWAN_PCO_STATUS**, in turn, contains the PCO status and a [WWAN_PCO_VALUE](TBD) structure that contains the PCO value.

Set requests are not applicable.

## Remarks

For modems that choose to use the Microsoft inbox miniport class driver, to receive query requests from the host, the modem must advertise that it supports the new **MBIM_CID_PCO** CID (index = 9) in the **MBB_UUID_BASIC_CONNECT_EXT_CONSTANT** service when responding to an **MBIM_CID_DEVICE_SERVICES** query. For more info about *MBIM_CID_PCO**, see [MB Protocol Configuration Option (PCO) Operations](mb-protocol-configuration-option-pco-operations.md).

For modems that choose not use Microsoft inbox miniport class driver, to receive query requests from WWANSVC, the modem’s miniport driver must advertise that it supports the *WWAN_OPTIONAL_SERVICE_CAPS_PCO* option when responding to [OID OID_WWAN_DEVICE_CAPS_EX](oid-wwan-device-caps-ex.md) query requests.

## Requirements

| | |
| --- | --- |
| Version | Windows 10, version 1709 |
| Header | Ntddndis.h (include Ndis.h) |

## See also

[**NDIS_STATUS_WWAN_PCO_STATUS**](https://msdn.microsoft.com/library/windows/hardware/mt782396)

[**NDIS_WWAN_PCO_STATUS**](TBD)

[**WWAN_PCO_VALUE**](TBD)

[MB Protocol Configuration Option (PCO) Operations](mb-protocol-configuration-option-pco-operations.md)

[OID OID_WWAN_DEVICE_CAPS_EX](oid-wwan-device-caps-ex.md)

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_DEVICE_CAPS_EX%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")