---
title: NDIS_STATUS_WWAN_DEVICE_RESET_STATUS
description: NDIS_STATUS_WWAN_DEVICE_RESET_STATUS
ms.assetid: 3745E3A8-6807-4BAF-8074-90C661EAD15E
keywords:
- NDIS_STATUS_WWAN_DEVICE_RESET_STATUS, modem reset status notification, Mobile Broadband modem reset status notification, MB modem reset status notification
ms.date: 08/18/2017
ms.localizationpriority: medium
---

# NDIS_STATUS_WWAN_DEVICE_RESET_STATUS

The NDIS_STATUS_WWAN_DEVICE_RESET_STATUS notification is sent by a modem miniport driver to inform the MB host of the reset status of the modem device. This notification is sent as an asynchronous response to an [OID_WWAN_DEVICE_RESET](oid-wwan-device-reset.md) set request.

This notification uses the [NDIS_WWAN_DEVICE_RESET_STATUS](https://msdn.microsoft.com/library/windows/hardware/D18E8633-BEAD-49A5-A730-10564AFF8A3E) structure.

## Requirements

| | |
| --- | --- |
| Version | Windows 10, version 1709 |
| Header | Ndis.h |

## See also

[OID_WWAN_DEVICE_RESET](oid-wwan-device-reset.md)

[NDIS_WWAN_DEVICE_RESET_STATUS](https://msdn.microsoft.com/library/windows/hardware/D18E8633-BEAD-49A5-A730-10564AFF8A3E)

[MB modem reset operations](mb-modem-reset-operations.md)

