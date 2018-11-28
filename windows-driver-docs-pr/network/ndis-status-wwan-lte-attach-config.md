---
title: NDIS_STATUS_WWAN_LTE_ATTACH_CONFIG
description: Miniport drivers use the NDIS_STATUS_WWAN_LTE_ATTACH_CONFIG notification to inform the mobile broadband (MB) service about the completion of a previous OID_WWAN_LTE_ATTACH_CONFIG Query or Set request.
ms.assetid: 866BCD4F-85A1-46C8-9FE2-8C5A8ADCD3CA
ms.date: 08/22/2018
keywords: 
 -NDIS_STATUS_WWAN_LTE_ATTACH_CONFIG Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS_STATUS_WWAN_LTE_ATTACH_CONFIG

Miniport drivers use the NDIS_STATUS_WWAN_LTE_ATTACH_CONFIG notification to inform the mobile broadband (MB) service about the completion of a previous [OID_WWAN_LTE_ATTACH_CONFIG](oid-wwan-lte-attach-config.md) Query or Set request.

Unsolicited events are sent if the default LTE attach context is updated by the network either over the air (OTA) or by short message service (SMS). In this case, the miniport driver must update the default LTE attach contexts and send this notification to the host OS with the updated list.

This status notification uses the [**NDIS_WWAN_LTE_ATTACH_CONTEXTS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndiswwan/ns-ndiswwan-_ndis_wwan_lte_attach_contexts) structure.

## Requirements

|   |   |
| --- | --- |
| Version | Windows 10, version 1703 |
| Header | Ntddndis.h (include Ndis.h) |

## See also

[MB LTE Attach Operations](mb-lte-attach-operations.md)

[OID_WWAN_LTE_ATTACH_CONFIG](oid-wwan-lte-attach-config.md)

[**NDIS_WWAN_LTE_ATTACH_CONTEXTS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndiswwan/ns-ndiswwan-_ndis_wwan_lte_attach_contexts)
