---
title: GUID_NDIS_STATUS_OFFLOAD_CAPABILITIES_CHANGE
description: This topic describes the GUID_NDIS_STATUS_OFFLOAD_CAPABILITIES_CHANGE GUID for the NDIS WMI interface.
ms.assetid: f1daadff-a564-4308-82cd-525a1dae866a
keywords:
- GUID_NDIS_STATUS_OFFLOAD_CAPABILITIES_CHANGE, WDK GUID_NDIS_STATUS_OFFLOAD_CAPABILITIES_CHANGE network drivers
ms.date: 11/22/2017
ms.localizationpriority: medium
---

# GUID_NDIS_STATUS_OFFLOAD_CAPABILITIES_CHANGE

The GUID_NDIS_STATUS_OFFLOAD_CAPABILITIES_CHANGE event GUID indicates that there has been a change in the offload characteristics of an NDIS port or miniport adapter. This WMI GUID is supported in NDIS 6.0 and later versions.

Miniport drivers use the [NDIS_STATUS_TASK_OFFLOAD_CURRENT_CONFIG](ndis-status-task-offload-current-config.md) status indication to notify NDIS and overlying drivers that there has been a change in task offload capabilities.

When a miniport driver indicates a task offload change, NDIS translates the status indication to a WMI GUID_NDIS_STATUS_OFFLOAD_CAPABILITIES_CHANGE event for WMI clients.

The data buffer that NDIS provides with the GUID contains an [NDIS_WMI_EVENT_HEADER](https://msdn.microsoft.com/library/windows/hardware/ff567900) structure that is followed by an [NDIS_OFFLOAD](https://msdn.microsoft.com/library/windows/hardware/ff566599) structure.

For more information about task offload capabilities, see [NDIS_STATUS_TASK_OFFLOAD_CURRENT_CONFIG](ndis-status-task-offload-current-config.md) and [OID_TCP_OFFLOAD_CURRENT_CONFIG](oid-tcp-offload-current-config.md).

