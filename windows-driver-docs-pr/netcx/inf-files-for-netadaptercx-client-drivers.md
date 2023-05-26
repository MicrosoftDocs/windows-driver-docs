---
title: INF files for NetAdapterCx client drivers
description: INF files for NetAdapterCx client drivers
keywords:
- INF files for NetAdapterCx client drivers, NetCx INF files, NetAdapterCx INF
ms.date: 08/13/2018
---

# INF files for NetAdapterCx client drivers

INF files for NetAdapterCx client drivers build on top of standard network INF files, with some additional keywords specific to NetAdapterCx. 

For more information about standard network INF files, see [Creating Network INF Files](../network/creating-network-inf-files.md). For more information about base INF files, see [Overview of INF files](../install/overview-of-inf-files.md).

**Note**: Starting in Windows 10, version 2004, Selective Suspend keywords are deprecated and must not be used by NetAdapterCx client drivers.

The following table describes the new INF keywords in NetAdapterCx.

| New network keyword | INF file section | Optional or required | Description |
| --- | --- | --- | --- |
| **\*IfConnectorPresent** | Device.NT | Required | <p>A boolean value that indicates if a connector is present. Set this keyword to **1**, or **TRUE**, if there is a physical adapter.</p> <p>**Note** Replaces the **IfConnectorPresent** field from the [**NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_general_attributes) structure.</p> |
| **\*ConnectionType** | Device.NT | Required | A [**NET_IF_CONNECTION_TYPE**](/windows/win32/api/ifdef/ne-ifdef-net_if_connection_type) value that specifies the [NDIS network interface](../network/ndis-network-interfaces2.md) connection type. |
| **\*DirectionType** | Device.NT | Required | A [**NET_IF_DIRECTION_TYPE**](/windows/win32/api/ifdef/ne-ifdef-net_if_direction_type) value that specifies the [NDIS network interface](../network/ndis-network-interfaces2.md) direction type. |
| **\*AccessType** | Device.NT | Required | A [**NET_IF_ACCESS_TYPE**](/windows/win32/api/ifdef/ne-ifdef-net_if_access_type) value that specifies the [NDIS network interface](../network/ndis-network-interfaces2.md) access type. |
| **\*HardwareLoopback** | Device.NT | Required | <p>A boolean value that indicates if the network interface card (NIC) has hardware loopback support.</p> <p>**Note** Setting this keyword to **1**, or **TRUE**, is the equivalent of **not** setting the **NDIS_MAC_OPTION_NO_LOOPBACK** flag in the **MacOptions** field of the [**NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_general_attributes) structure.</p> |
| **NumberOfNetworkInterfaces** | Device.NT | Optional | Specifies how many network interfaces the NIC supports. Required only if the NIC supports more than one network interface per device. |

For example:

```INF
[Device.NT]
CopyFiles=Drivers_Dir

; Existing network keywords
*IfType       = 6
*MediaType     = 0
*PhysicalMediaType = 14

; New network keywords
*IfConnectorPresent = 1     ; BOOLEAN
*ConnectionType   = 1       ; NET_IF_CONNECTION_TYPE
*DirectionType   = 0        ; NET_IF_DIRECTION_TYPE
*AccessType     = 2         ; NET_IF_ACCESS_TYPE
*HardwareLoopback  = 0      ; BOOLEAN
NumberOfNetworkInterfaces = 11
```
