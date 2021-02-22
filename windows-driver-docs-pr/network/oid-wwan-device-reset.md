---
title: OID_WWAN_DEVICE_RESET
description: OID_WWAN_DEVICE_RESET
keywords:
- MB device reset, Mobile Broadband device reset, Mobile Broadband miniport driver device reset
ms.date: 08/18/2017
ms.localizationpriority: medium
---

# OID_WWAN_DEVICE_RESET

OID_WWAN_DEVICE_RESET is sent by the mobile broadband host to a modem miniport adapter to reset the modem device.

Query requests are not applicable.

For Set requests, OID_WWAN_DEVICE_RESET uses the [NDIS_WWAN_SET_DEVICE_RESET](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_set_device_reset) structure. Modem miniport drivers must respond to set requests asynchronously, initially returning NDIS_STATUS_INDICATION_REQUIRED to the original request before later sending an [NDIS_STATUS_WWAN_DEVICE_RESET_STATUS](ndis-status-wwan-device-reset-status.md) notification containing an [NDIS_WWAN_DEVICE_RESET_STATUS](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_device_reset_status) structure that represents the reset status of the modem device. This response does not contain a payload, but is always a status code from the modem such as *WWAN_STATUS_SUCCESS* or *WWAN_STATUS_BUSY*.

Unsolicited events are not applicable.

## Requirements

**Version**: Windows 10, version 1709
**Header**: Ntddndis.h (include Ndis.h)

## See also

[NDIS_STATUS_WWAN_DEVICE_RESET_STATUS](ndis-status-wwan-device-reset-status.md)

[NDIS_WWAN_DEVICE_RESET_STATUS](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_device_reset_status)

[NDIS_WWAN_SET_DEVICE_RESET](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_set_device_reset)

[MB modem reset operations](mb-modem-reset-operations.md)
