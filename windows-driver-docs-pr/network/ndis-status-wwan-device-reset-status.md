---
title: NDIS_STATUS_WWAN_DEVICE_RESET_STATUS
ms.topic: reference
description: NDIS_STATUS_WWAN_DEVICE_RESET_STATUS
keywords:
- NDIS_STATUS_WWAN_DEVICE_RESET_STATUS, modem reset status notification, Mobile Broadband modem reset status notification, MB modem reset status notification
ms.date: 03/02/2023
---

# NDIS_STATUS_WWAN_DEVICE_RESET_STATUS

The NDIS_STATUS_WWAN_DEVICE_RESET_STATUS notification is sent by a modem miniport driver to inform the MB host of the reset status of the modem device. This notification is sent as an asynchronous response to an [OID_WWAN_DEVICE_RESET](oid-wwan-device-reset.md) set request.

This notification uses the [NDIS_WWAN_DEVICE_RESET_STATUS](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_device_reset_status) structure.

## Requirements

**Version**: Windows 10, version 1709
**Header**: Ndis.h

## See also

[OID_WWAN_DEVICE_RESET](oid-wwan-device-reset.md)

[NDIS_WWAN_DEVICE_RESET_STATUS](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_device_reset_status)

[MB modem reset operations](mb-modem-reset-operations.md)
