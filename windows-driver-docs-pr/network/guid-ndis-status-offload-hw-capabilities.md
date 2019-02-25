---
title: GUID_NDIS_STATUS_OFFLOAD_HW_CAPABILITIES
description: This topic describes the GUID_NDIS_STATUS_OFFLOAD_HW_CAPABILITIES GUID for the NDIS WMI interface.
ms.assetid: 6f5e11c1-4fa0-4a9b-90f3-85a3cb8b8878
keywords:
- GUID_NDIS_STATUS_OFFLOAD_HW_CAPABILITIES, WDK GUID_NDIS_STATUS_OFFLOAD_HW_CAPABILITIES network drivers
ms.date: 11/22/2017
ms.localizationpriority: medium
---

# GUID_NDIS_STATUS_OFFLOAD_HW_CAPABILITIES

The GUID_NDIS_STATUS_OFFLOAD_HW_CAPABILITIES event GUID indicates that there has been a change in the offload characteristics of the hardware that is associated with an NDIS port or miniport adapter. The hardware change typically reflects adding or deleting hardware that is associated with an MUX intermediate driver. This WMI GUID is supported in NDIS 6.0 and later versions.

MUX intermediate drivers use the [NDIS_STATUS_TASK_OFFLOAD_HARDWARE_CAPABILITIES](ndis-status-task-offload-hardware-capabilities.md) status indication to notify NDIS and overlying drivers that there has been a change in task offload capabilities.

When the driver indicates a task offload hardware change, NDIS translates the status indication to a WMI GUID_NDIS_STATUS_OFFLOAD_HW_CAPABILITIES event for WMI clients.

The data buffer that NDIS provides with the GUID contains an [NDIS_WMI_EVENT_HEADER](https://msdn.microsoft.com/library/windows/hardware/ff567900) structure that is followed by an [NDIS_OFFLOAD](https://msdn.microsoft.com/library/windows/hardware/ff566599) structure.

For more information about task offload capabilities, see [NDIS_STATUS_TASK_OFFLOAD_HARDWARE_CAPABILITIES](ndis-status-task-offload-hardware-capabilities.md) and [OID_TCP_OFFLOAD_HARDWARE_CAPABILITIES](oid-tcp-offload-hardware-capabilities.md).

