---
title: OID_WWAN_DEVICE_RESET
description: OID_WWAN_DEVICE_RESET
ms.assetid: CF15A1FD-9E48-458C-80DF-F63636F73962
keywords:
- MB device reset, Mobile Broadband device reset, Mobile Broadband miniport driver device reset
ms.author: windowsdriverdev
ms.date: 08/18/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Slicer%20settings%20%20RELEASE:%20%289/2/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")