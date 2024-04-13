---
title: NDIS_STATUS_WWAN_UICC_RESET_INFO
ms.topic: reference
description: NDIS_STATUS_WWAN_UICC_RESET_INFO
keywords:
- NDIS_STATUS_WWAN_UICC_RESET_INFO, UICC reset status notification, Mobile Broadband UICC reset status notification, MB UICC reset status notification
ms.date: 03/02/2023
---

# NDIS_STATUS_WWAN_UICC_RESET_INFO

The NDIS_STATUS_WWAN_UICC_RESET_INFO status notification is sent by a modem miniport adapter to inform the MB host of the current passthrough status to a UICC smart card. This notification is sent in the folloiwng two scenarios:

1. After an [OID_WWAN_UICC_RESET](oid-wwan-uicc-reset.md) query request.
2. After UICC reset is complete following an OID_WWAN_UICC_RESET set request, to inform the MB host of the passthrough status of the UICC card post-reset.

This notification uses the [NDIS_WWAN_UICC_RESET_INFO](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_uicc_reset_info) structure.

## Requirements

**Version**: Windows 10, version 1709
**Header**: Ndis.h

## See also

[OID_WWAN_UICC_RESET](oid-wwan-uicc-reset.md)

[NDIS_WWAN_UICC_RESET_INFO](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_uicc_reset_info)

[MB low level UICC access](mb-low-level-uicc-access.md)
