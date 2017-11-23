---
title: GUID_NDIS_GEN_ENUMERATE_PORTS
author: windows-driver-content
description: This topic describes the GUID_NDIS_GEN_ENUMERATE_PORTS GUID for the NDIS WMI interface.
ms.assetid: c7572ff2-c9e1-4605-9768-b14636ce007f
keywords:
- GUID_NDIS_GEN_ENUMERATE_PORTS, WDK GUID_NDIS_GEN_ENUMERATE_PORTS network drivers
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# GUID_NDIS_GEN_ENUMERATE_PORTS

WMI clients can use the GUID_NDIS_GEN_ENUMERATE_PORTS method GUID to obtain list of the ports that are associated with a miniport adapter. This WMI GUID is supported in NDIS 6.0 and later versions.

NDIS handles this request, and miniport drivers do not receive an OID query.

GUID_NDIS_GEN_ENUMERATE_PORTS requires a WMI method request to enumerate the ports. The WMI method identifier should be NDIS_WMI_DEFAULT_METHOD_ID. The WMI input buffer should contain an [NDIS_WMI_METHOD_HEADER](https://msdn.microsoft.com/library/windows/hardware/ff567903) structure that identifies the NDIS network interface name for the miniport adapter in the **NetLuid** member and that specifies zero for the **PortNumber** member. WMI clients can obtain the **NetLuid** value of the adapter with the [GUID_NDIS_ENUMERATE_ADAPTERS_EX](guid-ndis-enumerate-adapters-ex.md) method GUID.

The data buffer that NDIS returns with the GUID contains an [NDIS_PORT_ARRAY](https://msdn.microsoft.com/library/windows/hardware/ff566786) structure. The **NumberOfPorts** member of NDIS_PORT_ARRAY contains the number of active ports that are associated with the miniport adapter. The **Ports** member of NDIS_PORT_ARRAY contains a list of pointers to [NDIS_PORT_CHARACTERISTICS](https://msdn.microsoft.com/library/windows/hardware/ff566791) structures. Each NDIS_PORT_CHARACTERISTICS structure defines the characteristics of a single NDIS port.

For more information about enumerating ports, see [OID_GEN_ENUMERATE_PORTS](oid-gen-enumerate-ports.md).

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")