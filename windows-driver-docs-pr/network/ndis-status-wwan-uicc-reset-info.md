---
title: NDIS_STATUS_WWAN_UICC_RESET_INFO
author: windows-driver-content
description: NDIS_STATUS_WWAN_UICC_RESET_INFO
ms.assetid: ADA3ADC9-82AD-423A-ABA4-902EAF5F5C74
keywords:
- NDIS_STATUS_WWAN_UICC_RESET_INFO, UICC reset status notification, Mobile Broadband UICC reset status notification, MB UICC reset status notification
ms.author: windowsdriverdev
ms.date: 08/18/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# NDIS_STATUS_WWAN_UICC_RESET_INFO

The NDIS_STATUS_WWAN_UICC_RESET_INFO status notification is sent by a modem miniport adapter to inform the MB host of the current passthrough status to a UICC smart card. This notification is sent in the folloiwng two scenarios:

1. After an [OID_WWAN_UICC_RESET](oid-wwan-uicc-reset.md) query request.
2. After UICC reset is complete following an OID_WWAN_UICC_RESET set request, to inform the MB host of the passthrough status of the UICC card post-reset.

This notification uses the [NDIS_WWAN_UICC_RESET_INFO](TBD) structure.

## Requirements

| | |
| --- | --- |
| Version | Windows 10, version 1709 |
| Header | Ntddndis.h (include Ndis.h) |

## See also

[OID_WWAN_UICC_REST](oid-wwan-uicc-reset.md)

[NDIS_WWAN_UICC_RESET_INFO](TBD)

[MB UICC reset operations](mb-uicc-reset-operations.md)

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Slicer%20settings%20%20RELEASE:%20%289/2/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")