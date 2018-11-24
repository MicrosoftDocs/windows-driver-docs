---
title: GUID_NDIS_GEN_STATISTICS
description: This topic describes the GUID_NDIS_GEN_STATISTICS GUID for the NDIS WMI interface.
ms.assetid: 3751d4e7-7991-4329-9eb2-6a44ca1190d4
keywords:
- GUID_NDIS_GEN_STATISTICS, WDK GUID_NDIS_GEN_STATISTICS network drivers
ms.date: 11/22/2017
ms.localizationpriority: medium
---

# GUID_NDIS_GEN_STATISTICS

WMI clients can use the GUID_NDIS_GEN_STATISTICS method GUID to obtain miniport adapter statistics. This WMI GUID is supported in NDIS 6.0 and later versions.

When a WMI client issues a GUID_NDIS_GEN_STATISTICS WMI method request, NDIS returns the current statistics for the miniport adapter or NDIS port. The WMI method identifier should be NDIS_WMI_DEFAULT_METHOD_ID, and the WMI input buffer should contain an [NDIS_WMI_METHOD_HEADER](https://msdn.microsoft.com/library/windows/hardware/ff567903) structure.

NDIS uses the [OID_GEN_STATISTICS](oid-gen-statistics.md) OID to obtain the statistics for a miniport adapter. This OID is mandatory for miniport drivers that support NDIS 6.0 and later versions. The statistics counters are unsigned 64-bit values. The miniport driver returns the statistics in an NDIS_STATISTICS_INFO structure.

The data buffer that NDIS returns with the GUID contains an NDIS_STATISTICS_INFO structure.

