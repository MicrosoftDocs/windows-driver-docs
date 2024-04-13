---
title: GUID_NDIS_STATUS_NETWORK_CHANGE
description: This topic describes the GUID_NDIS_STATUS_NETWORK_CHANGE GUID for the NDIS WMI interface.
keywords:
- GUID_NDIS_STATUS_NETWORK_CHANGE, WDK GUID_NDIS_STATUS_NETWORK_CHANGE network drivers
ms.date: 03/02/2023
---

# GUID_NDIS_STATUS_NETWORK_CHANGE

The GUID_NDIS_STATUS_NETWORK_CHANGE event GUID indicates that the layer-three addresses must be renegotiated. This WMI GUID is supported in NDIS 6.0 and later versions.

NDIS or a miniport driver can generate an [NDIS_STATUS_NETWORK_CHANGE](ndis-status-network-change.md) status indication to report a change in network status.

When miniport drivers or NDIS indicate a change in the network status, NDIS translates the status indication to a WMI GUID_NDIS_STATUS_NETWORK_CHANGE event for WMI clients.

The data buffer that NDIS provides with this GUID contains an [NDIS_WMI_EVENT_HEADER](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_wmi_event_header) structure that is followed by an NDIS_NETWORK_CHANGE_TYPE-typed value. For a list of the possible values, see [NDIS_STATUS_NETWORK_CHANGE](ndis-status-network-change.md).
