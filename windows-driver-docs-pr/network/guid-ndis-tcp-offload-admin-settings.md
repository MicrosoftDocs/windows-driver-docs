---
title: GUID_NDIS_TCP_OFFLOAD_ADMIN_SETTINGS
description: This topic describes the GUID_NDIS_TCP_OFFLOAD_ADMIN_SETTINGS GUID for the NDIS WMI interface.
ms.assetid: 8648c75a-dcb3-4723-a2d0-d406d3a073d6
keywords:
- GUID_NDIS_TCP_OFFLOAD_ADMIN_SETTINGS, WDK GUID_NDIS_TCP_OFFLOAD_ADMIN_SETTINGS network drivers
ms.date: 11/22/2017
ms.localizationpriority: medium
---

# GUID_NDIS_TCP_OFFLOAD_ADMIN_SETTINGS

WMI clients can use the GUID_NDIS_TCP_OFFLOAD_ADMIN_SETTINGS set GUID to set the offload configuration parameters for an NDIS port. This WMI GUID is supported in NDIS 6.0 and later versions.

NDIS translates this GUID to the [OID_TCP_OFFLOAD_PARAMETERS](oid-tcp-offload-parameters.md) OID to set the current configuration of an NDIS port. NDIS miniport drivers that provide any kind of support for task offload must support this OID.

The WMI input buffer contains an [NDIS_WMI_SET_HEADER](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddndis/ns-ntddndis-_ndis_wmi_set_header) structure that is followed by an [NDIS_OFFLOAD_PARAMETERS](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddndis/ns-ntddndis-_ndis_offload_parameters) structure.

For more information about port parameters, see [OID_TCP_OFFLOAD_PARAMETERS](oid-tcp-offload-parameters.md).

