---
title: NDIS_STATUS_WWAN_LTE_ATTACH_STATUS
ms.topic: reference
description: Miniport drivers use the NDIS_STATUS_WWAN_LTE_ATTACH_STATUS notification to inform the mobile broadband (MB) service about the completion of a previous OID_WWAN_LTE_ATTACH_STATUS Query request.
ms.date: 03/02/2023
keywords: 
 -NDIS_STATUS_WWAN_LTE_ATTACH_STATUS Network Drivers Starting with Windows Vista
---

# NDIS_STATUS_WWAN_LTE_ATTACH_STATUS

Miniport drivers use the NDIS_STATUS_WWAN_LTE_ATTACH_STATUS notification to inform the mobile broadband (MB) service about the completion of a previous [OID_WWAN_LTE_ATTACH_STATUS](oid-wwan-lte-attach-status.md) Query request.

Unsolicited events are sent if a context for LTE attach is activated, which could be when a SIM is inserted for example. In this case, the miniport driver should send this notification to the host OS.

This status notification uses the [**NDIS_WWAN_LTE_ATTACH_STATUS**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_lte_attach_status) structure.

## Requirements

**Version**: Windows 10, version 1703
**Header**: Ntddndis.h (include Ndis.h)

## See also

[MB LTE Attach Operations](mb-lte-attach-operations.md)

[OID_WWAN_LTE_ATTACH_STATUS](oid-wwan-lte-attach-status.md)

[**NDIS_WWAN_LTE_ATTACH_STATUS**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_lte_attach_status)
