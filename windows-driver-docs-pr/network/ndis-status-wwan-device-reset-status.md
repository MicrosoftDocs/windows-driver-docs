---
title: NDIS_STATUS_WWAN_DEVICE_RESET_STATUS
author: windows-driver-content
description: NDIS_STATUS_WWAN_DEVICE_RESET_STATUS
ms.assetid: 3745E3A8-6807-4BAF-8074-90C661EAD15E
keywords:
- NDIS_STATUS_WWAN_DEVICE_RESET_STATUS, modem reset status notification, Mobile Broadband modem reset status notification, MB modem reset status notification
ms.author: windowsdriverdev
ms.date: 08/18/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# NDIS_STATUS_WWAN_DEVICE_RESET_STATUS

The NDIS_STATUS_WWAN_DEVICE_RESET_STATUS notification is sent by a modem miniport driver to inform the MB host of the reset status of the modem device. This notification is sent as an asynchronous response to an [OID_WWAN_DEVICE_RESET](oid-wwan-device-reset.md) set request.

This notification uses the [NDIS_WWAN_DEVICE_RESET_STATUS](TBD) structure.

## Requirements

| | |
| --- | --- |
| Version | Windows 10, version 1709 |
| Header | Ntddndis.h (include Ndis.h) |

## See also

[OID_WWAN_DEVICE_RESET](oid-wwan-device-reset.md)

[NDIS_WWAN_DEVICE_RESET_STATUS](TBD)

[MB modem reset operations](mb-modem-reset-operations.md)

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Slicer%20settings%20%20RELEASE:%20%289/2/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")