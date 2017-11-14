---
title: OID_GEN_CO_SUPPORTED_LIST
author: windows-driver-content
description: This topic describes the OID_GEN_CO_SUPPORTED_LIST object identifier (OID).
ms.assetid: 51c2b7f5-8429-4609-b048-542a3509f645
keywords:
- OID_GEN_CO_SUPPORTED_LIST
ms.author: windowsdriverdev
ms.date: 11/02/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# OID_GEN_CO_SUPPORTED_LIST

The OID_GEN_CO_SUPPORTED_LIST OID specifies an array of OIDs for objects that the underlying driver or its NIC supports. Objects include general, media-specific, and implementation-specific objects.

The underlying driver should order the OID list it returns in increasing numeric order. NDIS forwards a subset of the returned list to protocols that make this query. That is, NDIS filters any supported statistics OIDs out of the list since protocols never make statistics queries subsequently.

## Requirements

| | |
| --- | --- |
| Version | Windows Vista and later |
| Header | Ntddndis.h (include Ndis.h) |

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_DEVICE_CAPS_EX%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")