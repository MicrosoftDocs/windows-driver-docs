---
title: GUID_NDIS_TCP_OFFLOAD_HW_CAPABILITIES
description: This topic describes the GUID_NDIS_TCP_OFFLOAD_HW_CAPABILITIES GUID for the NDIS WMI interface.
ms.assetid: 5918fcb0-ebcf-4021-99a5-9ecfd2fdb987
keywords:
- GUID_NDIS_TCP_OFFLOAD_HW_CAPABILITIES, WDK GUID_NDIS_TCP_OFFLOAD_HW_CAPABILITIES network drivers
ms.date: 11/22/2017
ms.localizationpriority: medium
---

# GUID_NDIS_TCP_OFFLOAD_HW_CAPABILITIES

WMI clients can use the GUID_NDIS_TCP_OFFLOAD_HW_CAPABILITIES method GUID to obtain the TCP offload capabilities that are supported by the hardware that is associated with the specified port of a miniport adapter.

This GUID requires a WMI method request to return the hardware capabilities of an NDIS port. The WMI method identifier should be NDIS_WMI_DEFAULT_METHOD_ID, and the WMI input buffer should contain an [NDIS_WMI_METHOD_HEADER](https://msdn.microsoft.com/library/windows/hardware/ff567903) structure.

NDIS handles this GUID, and miniport drivers do not receive an OID query.

The data buffer that NDIS returns with the GUID contains an [NDIS_OFFLOAD](https://msdn.microsoft.com/library/windows/hardware/ff566599) structure.

For more information about the port state, see [OID_TCP_OFFLOAD_HARDWARE_CAPABILITIES](oid-tcp-offload-hardware-capabilities.md).

