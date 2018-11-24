---
title: Updating ProtocolBindAdapter for an NDIS 6.0 protocol driver
description: Updating the ProtocolBindAdapter Function for an NDIS 6.0 Protocol Driver
ms.assetid: 7e11e468-72a1-4c77-a240-76e0679ed880
keywords:
- ProtocolBindAdapter
- ProtocolBindAdapterEx
- updating ProtocolBindAdapter
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Updating the ProtocolBindAdapter Function for an NDIS 6.0 Protocol Driver





In NDIS 6.0, the [*ProtocolBindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570220) function replaces the [*ProtocolBindAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff562465) function. NDIS calls *ProtocolBindAdapterEx* to perform binding operations whenever an underlying miniport adapter, to which the protocol driver can bind, becomes available.

*ProtocolBindAdapterEx* initializes a binding for network I/O operations. NDIS passes *ProtocolBindAdapterEx* an [**NDIS\_BIND\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff564832) structure. For more information about *ProtocolBindAdapterEx* and this structure, see [Binding to an Adapter](binding-to-an-adapter.md).

The *ProtocolBindAdapterEx* function must:

-   Allocate sufficient memory to maintain the binding context information. For more information, see [Allocating Memory in an NDIS 6.0 Protocol Driver](allocating-memory-in-an-ndis-6-0-protocol-driver.md).

-   Save the required binding information from the NDIS\_BIND\_PARAMETERS structure. Protocol drivers should not issue OID queries to obtain information that is already provided in the NDIS\_BIND\_PARAMETERS structure.

-   Allocate the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) and the [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) pools. For more information, see [Allocating Network Data Pools in NDIS 6.0 Protocol Drivers](allocating-network-data-pools-in-an-ndis-6-0-protocol-driver.md).

-   Open the underlying miniport adapter. For more information, see [Opening an Adapter in an NDIS 6.0 Protocol Driver](opening-an-adapter-in-an-ndis-6-0-protocol-driver.md).

-   Optionally, read configuration parameters from the registry. For more information, see [Reading the Registry in NDIS 6.0 Protocol Drivers](reading-the-registry-in-an-ndis-6-0-protocol-driver.md).

 

 





