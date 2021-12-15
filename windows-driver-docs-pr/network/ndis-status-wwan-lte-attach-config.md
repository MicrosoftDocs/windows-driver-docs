---
title: NDIS_STATUS_WWAN_LTE_ATTACH_CONFIG
description: Miniport drivers use the NDIS_STATUS_WWAN_LTE_ATTACH_CONFIG notification to inform the mobile broadband (MB) service about the completion of a previous OID_WWAN_LTE_ATTACH_CONFIG Query or Set request.
ms.date: 08/22/2018
keywords: 
 -NDIS_STATUS_WWAN_LTE_ATTACH_CONFIG Network Drivers Starting with Windows Vista
---

# NDIS_STATUS_WWAN_LTE_ATTACH_CONFIG

Miniport drivers use the NDIS_STATUS_WWAN_LTE_ATTACH_CONFIG notification to inform the mobile broadband (MB) service about the completion of a previous [OID_WWAN_LTE_ATTACH_CONFIG](oid-wwan-lte-attach-config.md) Query or Set request.

Unsolicited events are sent if the default LTE attach context is updated by the network either over the air (OTA) or by short message service (SMS). In this case, the miniport driver must update the default LTE attach contexts and send this notification to the host OS with the updated list.

This status notification uses the [**NDIS_WWAN_LTE_ATTACH_CONTEXTS**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_lte_attach_contexts) structure.

## Requirements

**Version**: Windows 10, version 1703
**Header**: Ntddndis.h (include Ndis.h)

## See also

[MB LTE Attach Operations](mb-lte-attach-operations.md)

[OID_WWAN_LTE_ATTACH_CONFIG](oid-wwan-lte-attach-config.md)

[**NDIS_WWAN_LTE_ATTACH_CONTEXTS**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_lte_attach_contexts)
