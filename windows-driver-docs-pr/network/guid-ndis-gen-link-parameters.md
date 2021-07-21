---
title: GUID_NDIS_GEN_LINK_PARAMETERS
description: This topic describes the GUID_NDIS_GEN_LINK_PARAMETERS GUID for the NDIS WMI interface.
keywords:
- GUID_NDIS_GEN_LINK_PARAMETERS, WDK GUID_NDIS_GEN_LINK_PARAMETERS network drivers
ms.date: 11/22/2017
ms.localizationpriority: medium
---

# GUID_NDIS_GEN_LINK_PARAMETERS

WMI clients can use the GUID_NDIS_GEN_LINK_PARAMETERS set GUID to set the link parameters for a miniport adapter. This WMI GUID is supported in NDIS 6.0 and later versions.

NDIS translates this GUID to the [OID_GEN_LINK_PARAMETERS](oid-gen-link-parameters.md) OID to set the current link parameters of a miniport adapter. This OID is mandatory for miniport drivers that support NDIS 6.0 and later versions.

The WMI input buffer specifies the data that NDIS should set. The input buffer contains an [NDIS_WMI_SET_HEADER](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_wmi_set_header) structure that is followed by an [NDIS_LINK_PARAMETERS](./oid-gen-link-parameters.md) structure.
