---
title: GUID_NDIS_TCP_OFFLOAD_HW_CAPABILITIES
description: This topic describes the GUID_NDIS_TCP_OFFLOAD_HW_CAPABILITIES GUID for the NDIS WMI interface.
keywords:
- GUID_NDIS_TCP_OFFLOAD_HW_CAPABILITIES, WDK GUID_NDIS_TCP_OFFLOAD_HW_CAPABILITIES network drivers
ms.date: 03/02/2023
---

# GUID_NDIS_TCP_OFFLOAD_HW_CAPABILITIES

WMI clients can use the GUID_NDIS_TCP_OFFLOAD_HW_CAPABILITIES method GUID to obtain the TCP offload capabilities that are supported by the hardware that is associated with the specified port of a miniport adapter.

This GUID requires a WMI method request to return the hardware capabilities of an NDIS port. The WMI method identifier should be NDIS_WMI_DEFAULT_METHOD_ID, and the WMI input buffer should contain an [NDIS_WMI_METHOD_HEADER](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_wmi_method_header) structure.

NDIS handles this GUID, and miniport drivers do not receive an OID query.

The data buffer that NDIS returns with the GUID contains an [NDIS_OFFLOAD](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_offload) structure.

For more information about the port state, see [OID_TCP_OFFLOAD_HARDWARE_CAPABILITIES](oid-tcp-offload-hardware-capabilities.md).
