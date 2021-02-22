---
title: GUID_NDIS_GEN_INTERRUPT_MODERATION_PARAMETERS
description: This topic describes the GUID_NDIS_GEN_INTERRUPT_MODERATION_PARAMETERS GUID for the NDIS WMI interface.
keywords:
- GUID_NDIS_GEN_INTERRUPT_MODERATION_PARAMETERS, WDK GUID_NDIS_GEN_INTERRUPT_MODERATION_PARAMETERS network drivers
ms.date: 11/22/2017
ms.localizationpriority: medium
---

# GUID_NDIS_GEN_INTERRUPT_MODERATION_PARAMETERS

WMI clients can use the GUID_NDIS_GEN_PORT_PARAMETERS set GUID to set the interrupt moderation configuration for a miniport adapter. This WMI GUID is supported in NDIS 6.0 and later versions.

NDIS translates this GUID to the [OID_GEN_INTERRUPT_MODERATION](oid-gen-interrupt-moderation.md) OID to set the current configuration. All NDIS miniport drivers must support this OID.

The WMI input buffer contains an [NDIS_WMI_SET_HEADER](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_wmi_set_header) structure that is followed by an [NDIS_INTERRUPT_MODERATION_PARAMETERS](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_interrupt_moderation_parameters) structure.

For more information about port parameters, see [OID_GEN_INTERRUPT_MODERATION](oid-gen-interrupt-moderation.md).
