---
title: OID_WWAN_DEVICE_RESET
description: OID_WWAN_DEVICE_RESET
ms.assetid: CF15A1FD-9E48-458C-80DF-F63636F73962
keywords:
- MB device reset, Mobile Broadband device reset, Mobile Broadband miniport driver device reset
ms.date: 08/18/2017
ms.localizationpriority: medium
---

# OID_WWAN_DEVICE_RESET

OID_WWAN_DEVICE_RESET is sent by the mobile broadband host to a modem miniport adapter to reset the modem device.

Query requests are not applicable.

For Set requests, OID_WWAN_DEVICE_RESET uses the [NDIS_WWAN_SET_DEVICE_RESET](https://msdn.microsoft.com/library/windows/hardware/73894308-CFE0-49EF-BB09-E104CEE9C746) structure. Modem miniport drivers must respond to set requests asynchronously, initially returning NDIS_STATUS_INDICATION_REQUIRED to the original request before later sending an [NDIS_STATUS_WWAN_DEVICE_RESET_STATUS](ndis-status-wwan-device-reset-status.md) notification containing an [NDIS_WWAN_DEVICE_RESET_STATUS](https://msdn.microsoft.com/library/windows/hardware/D18E8633-BEAD-49A5-A730-10564AFF8A3E) structure that represents the reset status of the modem device. This response does not contain a payload, but is always a status code from the modem such as *WWAN_STATUS_SUCCESS* or *WWAN_STATUS_BUSY*.

Unsolicited events are not applicable.

## Requirements

| | |
| --- | --- |
| Version | Windows 10, version 1709 |
| Header | Ntddndis.h (include Ndis.h) |

## See also

[NDIS_STATUS_WWAN_DEVICE_RESET_STATUS](ndis-status-wwan-device-reset-status.md)

[NDIS_WWAN_DEVICE_RESET_STATUS](https://msdn.microsoft.com/library/windows/hardware/D18E8633-BEAD-49A5-A730-10564AFF8A3E)

[NDIS_WWAN_SET_DEVICE_RESET](https://msdn.microsoft.com/library/windows/hardware/73894308-CFE0-49EF-BB09-E104CEE9C746)

[MB modem reset operations](mb-modem-reset-operations.md)

