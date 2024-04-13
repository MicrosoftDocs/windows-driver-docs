---
title: GUID_NDIS_STATUS_OFFLOAD_CAPABILITIES_CHANGE
description: This topic describes the GUID_NDIS_STATUS_OFFLOAD_CAPABILITIES_CHANGE GUID for the NDIS WMI interface.
keywords:
- GUID_NDIS_STATUS_OFFLOAD_CAPABILITIES_CHANGE, WDK GUID_NDIS_STATUS_OFFLOAD_CAPABILITIES_CHANGE network drivers
ms.date: 03/02/2023
---

# GUID_NDIS_STATUS_OFFLOAD_CAPABILITIES_CHANGE

The GUID_NDIS_STATUS_OFFLOAD_CAPABILITIES_CHANGE event GUID indicates that there has been a change in the offload characteristics of an NDIS port or miniport adapter. This WMI GUID is supported in NDIS 6.0 and later versions.

Miniport drivers use the [NDIS_STATUS_TASK_OFFLOAD_CURRENT_CONFIG](ndis-status-task-offload-current-config.md) status indication to notify NDIS and overlying drivers that there has been a change in task offload capabilities.

When a miniport driver indicates a task offload change, NDIS translates the status indication to a WMI GUID_NDIS_STATUS_OFFLOAD_CAPABILITIES_CHANGE event for WMI clients.

The data buffer that NDIS provides with the GUID contains an [NDIS_WMI_EVENT_HEADER](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_wmi_event_header) structure that is followed by an [NDIS_OFFLOAD](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_offload) structure.

For more information about task offload capabilities, see [NDIS_STATUS_TASK_OFFLOAD_CURRENT_CONFIG](ndis-status-task-offload-current-config.md) and [OID_TCP_OFFLOAD_CURRENT_CONFIG](oid-tcp-offload-current-config.md).
