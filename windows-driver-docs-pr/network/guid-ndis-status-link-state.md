---
title: GUID_NDIS_STATUS_LINK_STATE
description: This topic describes the GUID_NDIS_STATUS_LINK_STATE GUID for the NDIS WMI interface.
keywords:
- GUID_NDIS_STATUS_LINK_STATE, WDK GUID_NDIS_STATUS_LINK_STATE network drivers
ms.date: 03/02/2023
---

# GUID_NDIS_STATUS_LINK_STATE

The GUID_NDIS_STATUS_LINK_STATE event GUID indicates that there has been a change in the link state of a miniport adapter. This WMI GUID is supported in NDIS 6.0 and later versions.

Miniport drivers use the [NDIS_STATUS_LINK_STATE](ndis-status-link-state.md) status indication to notify NDIS and overlying drivers that there has been a change in link state.

When a miniport driver indicates a link state change, NDIS translates the status indication to a WMI GUID_NDIS_STATUS_LINK_STATE event for WMI clients.

The data buffer that NDIS provides with the GUID contains an [NDIS_WMI_EVENT_HEADER](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_wmi_event_header) structure that is followed by an [NDIS_LINK_STATE](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_link_state) structure. The **NDIS_LINK_STATE** structure specifies the physical state of the medium.

For more information about link status, see [OID_GEN_LINK_STATE](oid-gen-link-state.md) and [NDIS_STATUS_LINK_STATE](ndis-status-link-state.md).
