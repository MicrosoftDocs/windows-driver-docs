---
title: GUID_NDIS_TCP_OFFLOAD_CAPABILITIES
author: windows-driver-content
description: This topic describes the GUID_NDIS_TCP_OFFLOAD_CAPABILITIES GUID for the NDIS WMI interface.
ms.assetid: 93b8af60-3c15-4eea-a0ea-ce1c71f0b60c
keywords:
- GUID_NDIS_TCP_OFFLOAD_CAPABILITIES, WDK GUID_NDIS_TCP_OFFLOAD_CAPABILITIES network drivers
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# GUID_NDIS_TCP_OFFLOAD_CAPABILITIES

WMI clients can use the GUID_NDIS_TCP_OFFLOAD_CAPABILITIES method GUID to obtain the task offload capabilities that are associated with the specified port of a miniport adapter.

This GUID requires a WMI method request to return the offload capabilities of an NDIS port. The WMI method identifier should be NDIS_WMI_DEFAULT_METHOD_ID, and the WMI input buffer should contain an [NDIS_WMI_METHOD_HEADER](https://msdn.microsoft.com/library/windows/hardware/ff567903) structure.

NDIS handles this GUID, and miniport drivers do not receive an OID query.

The data buffer that NDIS returns with the GUID contains an [NDIS_OFFLOAD](https://msdn.microsoft.com/library/windows/hardware/ff566599) structure.

For more information about the port state, see [OID_TCP_OFFLOAD_CURRENT_CONFIG](oid-tcp-offload-current-config.md).

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")