---
title: OID_WWAN_LTE_ATTACH_STATUS
ms.topic: reference
description: OID_WWAN_LTE_ATTACH_STATUS is used to inform the OS of the last used LTE attach context.
ms.date: 08/23/2018
keywords: 
 -OID_WWAN_LTE_ATTACH_STATUS Network Drivers Starting with Windows Vista
---

# OID_WWAN_LTE_ATTACH_STATUS

OID_WWAN_LTE_ATTACH_STATUS is used to inform the OS of the last used default LTE attach context.

Miniport drivers must process Query requests asynchronously, initially returning NDIS_STATUS_INDICATION_REQUIRED to the original request before later sending an [NDIS_STATUS_WWAN_LTE_ATTACH_STATUS](ndis-status-wwan-lte-attach-status.md) notification containing an [**NDIS_WWAN_LTE_ATTACH_STATUS**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_lte_attach_status) structure that describes the last used default LTE attach context.

Set requests are not applicable.

## Remarks

For more information about using this OID, see [MBIM_CID_MS_LTE_ATTACH_STATUS](mb-lte-attach-operations.md).

## Requirements

**Version**: Windows 10, version 1703
**Header**: Ntddndis.h (include Ndis.h)

## See also

[MB LTE Attach Operations](mb-lte-attach-operations.md)

[NDIS_STATUS_WWAN_LTE_ATTACH_STATUS](ndis-status-wwan-lte-attach-status.md)

[**NDIS_WWAN_LTE_ATTACH_STATUS**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_lte_attach_status)
