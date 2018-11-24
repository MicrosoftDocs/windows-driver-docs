---
title: GUID_NDIS_STATUS_PORT_STATE
description: This topic describes the GUID_NDIS_STATUS_PORT_STATE GUID for the NDIS WMI interface.
ms.assetid: c657eef6-eb80-4715-9d60-0d2dde403300
keywords:
- GUID_NDIS_STATUS_PORT_STATE, WDK GUID_NDIS_STATUS_PORT_STATE network drivers
ms.date: 11/22/2017
ms.localizationpriority: medium
---

# GUID_NDIS_STATUS_PORT_STATE

The GUID_NDIS_STATUS_PORT_STATE event GUID indicates a change in the state of an NDIS port. This WMI GUID is supported in NDIS 6.0 and later versions.

Miniport drivers that support NDIS ports use the [NDIS_STATUS_PORT_STATE](ndis-status-port-state.md) status indication to indicate changes in the state of an NDIS port.

When a miniport driver indicates a port state change, NDIS translates the status indication to a WMI GUID_NDIS_STATUS_PORT_STATE event for WMI clients.

The data buffer that NDIS provides with this GUID contains an [NDIS_WMI_EVENT_HEADER](https://msdn.microsoft.com/library/windows/hardware/ff567900) structure that is followed by an [NDIS_PORT_STATE](https://msdn.microsoft.com/library/windows/hardware/ff569624) structure.

For more information about the port state, see [OID_GEN_PORT_STATE](oid-gen-port-state.md).

