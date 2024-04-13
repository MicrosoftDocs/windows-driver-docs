---
title: GUID_NDIS_GEN_LINK_STATE
description: This topic describes the GUID_NDIS_GEN_LINK_STATE GUID for the NDIS WMI interface.
keywords:
- GUID_NDIS_GEN_LINK_STATE, WDK GUID_NDIS_GEN_LINK_STATE network drivers
ms.date: 03/02/2023
---

# GUID_NDIS_GEN_LINK_STATE

WMI clients can use the GUID_NDIS_GEN_LINK_STATE method GUID to determine the current link state. This WMI GUID is supported in NDIS 6.0 and later versions.

NDIS handles this GUID and miniport drivers do not receive an OID query.

When a WMI client issues a GUID_NDIS_GEN_LINK_STATE WMI method request, NDIS returns the current link state for the miniport adapter or NDIS port.

The WMI method identifier should be NDIS_WMI_DEFAULT_METHOD_ID, and the WMI input buffer should contain an [NDIS_WMI_METHOD_HEADER](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_wmi_method_header) structure.

The data buffer that NDIS returns with this GUID contains an [NDIS_LINK_STATE](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_link_state) structure.

Miniport drivers supply the link state during initialization and provide updates with status indications. WMI clients can use the GUID_NDIS_GEN_LINK_STATE GUID to receive updates when the link state changes.

For more information about link status, see [OID_GEN_LINK_STATE](oid-gen-link-state.md) and [NDIS_STATUS_LINK_STATE](ndis-status-link-state.md).
