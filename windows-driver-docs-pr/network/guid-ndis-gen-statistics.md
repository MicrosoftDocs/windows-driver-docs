---
title: GUID_NDIS_GEN_STATISTICS
description: This topic describes the GUID_NDIS_GEN_STATISTICS GUID for the NDIS WMI interface.
keywords:
- GUID_NDIS_GEN_STATISTICS, WDK GUID_NDIS_GEN_STATISTICS network drivers
ms.date: 03/02/2023
---

# GUID_NDIS_GEN_STATISTICS

WMI clients can use the GUID_NDIS_GEN_STATISTICS method GUID to obtain miniport adapter statistics. This WMI GUID is supported in NDIS 6.0 and later versions.

When a WMI client issues a GUID_NDIS_GEN_STATISTICS WMI method request, NDIS returns the current statistics for the miniport adapter or NDIS port. The WMI method identifier should be NDIS_WMI_DEFAULT_METHOD_ID, and the WMI input buffer should contain an [NDIS_WMI_METHOD_HEADER](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_wmi_method_header) structure.

NDIS uses the [OID_GEN_STATISTICS](oid-gen-statistics.md) OID to obtain the statistics for a miniport adapter. This OID is mandatory for miniport drivers that support NDIS 6.0 and later versions. The statistics counters are unsigned 64-bit values. The miniport driver returns the statistics in an NDIS_STATISTICS_INFO structure.

The data buffer that NDIS returns with the GUID contains an NDIS_STATISTICS_INFO structure.
