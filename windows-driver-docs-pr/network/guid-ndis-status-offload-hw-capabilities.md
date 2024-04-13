---
title: GUID_NDIS_STATUS_OFFLOAD_HW_CAPABILITIES
description: This topic describes the GUID_NDIS_STATUS_OFFLOAD_HW_CAPABILITIES GUID for the NDIS WMI interface.
keywords:
- GUID_NDIS_STATUS_OFFLOAD_HW_CAPABILITIES, WDK GUID_NDIS_STATUS_OFFLOAD_HW_CAPABILITIES network drivers
ms.date: 03/02/2023
---

# GUID_NDIS_STATUS_OFFLOAD_HW_CAPABILITIES

The GUID_NDIS_STATUS_OFFLOAD_HW_CAPABILITIES event GUID indicates that there has been a change in the offload characteristics of the hardware that is associated with an NDIS port or miniport adapter. The hardware change typically reflects adding or deleting hardware that is associated with an MUX intermediate driver. This WMI GUID is supported in NDIS 6.0 and later versions.

MUX intermediate drivers use the [NDIS_STATUS_TASK_OFFLOAD_HARDWARE_CAPABILITIES](ndis-status-task-offload-hardware-capabilities.md) status indication to notify NDIS and overlying drivers that there has been a change in task offload capabilities.

When the driver indicates a task offload hardware change, NDIS translates the status indication to a WMI GUID_NDIS_STATUS_OFFLOAD_HW_CAPABILITIES event for WMI clients.

The data buffer that NDIS provides with the GUID contains an [NDIS_WMI_EVENT_HEADER](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_wmi_event_header) structure that is followed by an [NDIS_OFFLOAD](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_offload) structure.

For more information about task offload capabilities, see [NDIS_STATUS_TASK_OFFLOAD_HARDWARE_CAPABILITIES](ndis-status-task-offload-hardware-capabilities.md) and [OID_TCP_OFFLOAD_HARDWARE_CAPABILITIES](oid-tcp-offload-hardware-capabilities.md).
