---
title: GUID_NDIS_STATUS_PORT_STATE
author: windows-driver-content
description: This topic describes the GUID_NDIS_STATUS_PORT_STATE GUID for the NDIS WMI interface.
ms.assetid: c657eef6-eb80-4715-9d60-0d2dde403300
keywords:
- GUID_NDIS_STATUS_PORT_STATE, WDK GUID_NDIS_STATUS_PORT_STATE network drivers
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# GUID_NDIS_STATUS_PORT_STATE

The GUID_NDIS_STATUS_PORT_STATE event GUID indicates a change in the state of an NDIS port. This WMI GUID is supported in NDIS 6.0 and later versions.

Miniport drivers that support NDIS ports use the [NDIS_STATUS_PORT_STATE](ndis-status-port-state.md) status indication to indicate changes in the state of an NDIS port.

When a miniport driver indicates a port state change, NDIS translates the status indication to a WMI GUID_NDIS_STATUS_PORT_STATE event for WMI clients.

The data buffer that NDIS provides with this GUID contains an [NDIS_WMI_EVENT_HEADER](https://msdn.microsoft.com/library/windows/hardware/ff567900) structure that is followed by an [NDIS_PORT_STATE](https://msdn.microsoft.com/library/windows/hardware/ff569624) structure.

For more information about the port state, see [OID_GEN_PORT_STATE](oid-gen-port-state.md).

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")