---
title: GUID_NDIS_STATUS_PACKET_FILTER
description: This topic describes the GUID_NDIS_STATUS_PACKET_FILTER GUID for the NDIS WMI interface.
keywords:
- GUID_NDIS_STATUS_PACKET_FILTER, WDK GUID_NDIS_STATUS_PACKET_FILTER network drivers
ms.date: 03/02/2023
---

# GUID_NDIS_STATUS_PACKET_FILTER

The GUID_NDIS_STATUS_PACKET_FILTER event GUID indicates that there has been a change in the packet filter for miniport adapter. This WMI GUID is supported in NDIS 6.0 and later versions.

NDIS generates the NDIS_STATUS_PACKET_FILTER status indication to notify overlying drivers that there might be a change in the packet filter configuration.

NDIS translates the status indication to a WMI GUID_NDIS_STATUS_PACKET_FILTER event for WMI clients.

The data buffer that NDIS provides with the GUID contains an [NDIS_WMI_EVENT_HEADER](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_wmi_event_header) structure that is followed by a ULONG value. For more information about packet filter status and the possible values, see [OID_GEN_CURRENT_PACKET_FILTER](oid-gen-current-packet-filter.md).
