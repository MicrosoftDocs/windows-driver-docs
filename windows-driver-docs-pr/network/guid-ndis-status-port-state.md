---
title: GUID_NDIS_STATUS_PORT_STATE
description: This topic describes the GUID_NDIS_STATUS_PORT_STATE GUID for the NDIS WMI interface.
keywords:
- GUID_NDIS_STATUS_PORT_STATE, WDK GUID_NDIS_STATUS_PORT_STATE network drivers
ms.date: 11/22/2017
---

# GUID_NDIS_STATUS_PORT_STATE

The GUID_NDIS_STATUS_PORT_STATE event GUID indicates a change in the state of an NDIS port. This WMI GUID is supported in NDIS 6.0 and later versions.

Miniport drivers that support NDIS ports use the [NDIS_STATUS_PORT_STATE](ndis-status-port-state.md) status indication to indicate changes in the state of an NDIS port.

When a miniport driver indicates a port state change, NDIS translates the status indication to a WMI GUID_NDIS_STATUS_PORT_STATE event for WMI clients.

The data buffer that NDIS provides with this GUID contains an [NDIS_WMI_EVENT_HEADER](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_wmi_event_header) structure that is followed by an [NDIS_PORT_STATE](./oid-gen-port-state.md) structure.

For more information about the port state, see [OID_GEN_PORT_STATE](oid-gen-port-state.md).
