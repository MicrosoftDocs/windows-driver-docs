---
title: GUID_NDIS_GEN_ENUMERATE_PORTS
description: This topic describes the GUID_NDIS_GEN_ENUMERATE_PORTS GUID for the NDIS WMI interface.
ms.assetid: c7572ff2-c9e1-4605-9768-b14636ce007f
keywords:
- GUID_NDIS_GEN_ENUMERATE_PORTS, WDK GUID_NDIS_GEN_ENUMERATE_PORTS network drivers
ms.date: 11/22/2017
ms.localizationpriority: medium
---

# GUID_NDIS_GEN_ENUMERATE_PORTS

WMI clients can use the GUID_NDIS_GEN_ENUMERATE_PORTS method GUID to obtain list of the ports that are associated with a miniport adapter. This WMI GUID is supported in NDIS 6.0 and later versions.

NDIS handles this request, and miniport drivers do not receive an OID query.

GUID_NDIS_GEN_ENUMERATE_PORTS requires a WMI method request to enumerate the ports. The WMI method identifier should be NDIS_WMI_DEFAULT_METHOD_ID. The WMI input buffer should contain an [NDIS_WMI_METHOD_HEADER](https://msdn.microsoft.com/library/windows/hardware/ff567903) structure that identifies the NDIS network interface name for the miniport adapter in the **NetLuid** member and that specifies zero for the **PortNumber** member. WMI clients can obtain the **NetLuid** value of the adapter with the [GUID_NDIS_ENUMERATE_ADAPTERS_EX](guid-ndis-enumerate-adapters-ex.md) method GUID.

The data buffer that NDIS returns with the GUID contains an [NDIS_PORT_ARRAY](https://msdn.microsoft.com/library/windows/hardware/ff566786) structure. The **NumberOfPorts** member of NDIS_PORT_ARRAY contains the number of active ports that are associated with the miniport adapter. The **Ports** member of NDIS_PORT_ARRAY contains a list of pointers to [NDIS_PORT_CHARACTERISTICS](https://msdn.microsoft.com/library/windows/hardware/ff566791) structures. Each NDIS_PORT_CHARACTERISTICS structure defines the characteristics of a single NDIS port.

For more information about enumerating ports, see [OID_GEN_ENUMERATE_PORTS](oid-gen-enumerate-ports.md).

