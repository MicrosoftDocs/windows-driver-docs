---
title: GUID_NDIS_GEN_INTERRUPT_MODERATION
author: windows-driver-content
description: This topic describes the GUID_NDIS_GEN_INTERRUPT_MODERATION GUID for the NDIS WMI interface.
ms.assetid: 355e5e4d-61b7-4cc0-8cf7-c95a773e805a
keywords:
- GUID_NDIS_GEN_INTERRUPT_MODERATION, WDK GUID_NDIS_GEN_INTERRUPT_MODERATION network drivers
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# GUID_NDIS_GEN_INTERRUPT_MODERATION

WMI clients can use the GUID_NDIS_GEN_INTERRUPT_MODERATION method GUID to obtain the interrupt moderation parameters that are associated with the specified port of a miniport adapter.

This GUID requires a WMI method request to return the interrupt moderation parameters. The WMI method identifier should be NDIS_WMI_DEFAULT_METHOD_ID, and the WMI input buffer should contain an [NDIS_WMI_METHOD_HEADER](https://msdn.microsoft.com/library/windows/hardware/ff567903) structure.

NDIS translates this GUID to an [OID_GEN_INTERRUPT_MODERATION](oid-gen-interrupt-moderation.md) query request for the associated miniport adapter. This OID is mandatory for miniport drivers that support NDIS 6.0 and later versions.

The data buffer that NDIS returns with the GUID contains an [NDIS_INTERRUPT_MODERATION_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff565793) structure.

For more information about the port state, see [OID_GEN_INTERRUPT_MODERATION](oid-gen-interrupt-moderation.md).

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")