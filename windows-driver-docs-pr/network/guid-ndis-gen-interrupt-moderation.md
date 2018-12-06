---
title: GUID_NDIS_GEN_INTERRUPT_MODERATION
description: This topic describes the GUID_NDIS_GEN_INTERRUPT_MODERATION GUID for the NDIS WMI interface.
ms.assetid: 355e5e4d-61b7-4cc0-8cf7-c95a773e805a
keywords:
- GUID_NDIS_GEN_INTERRUPT_MODERATION, WDK GUID_NDIS_GEN_INTERRUPT_MODERATION network drivers
ms.date: 11/22/2017
ms.localizationpriority: medium
---

# GUID_NDIS_GEN_INTERRUPT_MODERATION

WMI clients can use the GUID_NDIS_GEN_INTERRUPT_MODERATION method GUID to obtain the interrupt moderation parameters that are associated with the specified port of a miniport adapter.

This GUID requires a WMI method request to return the interrupt moderation parameters. The WMI method identifier should be NDIS_WMI_DEFAULT_METHOD_ID, and the WMI input buffer should contain an [NDIS_WMI_METHOD_HEADER](https://msdn.microsoft.com/library/windows/hardware/ff567903) structure.

NDIS translates this GUID to an [OID_GEN_INTERRUPT_MODERATION](oid-gen-interrupt-moderation.md) query request for the associated miniport adapter. This OID is mandatory for miniport drivers that support NDIS 6.0 and later versions.

The data buffer that NDIS returns with the GUID contains an [NDIS_INTERRUPT_MODERATION_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff565793) structure.

For more information about the port state, see [OID_GEN_INTERRUPT_MODERATION](oid-gen-interrupt-moderation.md).

