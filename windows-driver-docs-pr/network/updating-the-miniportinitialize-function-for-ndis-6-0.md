---
title: Updating the MiniportInitialize Function for NDIS 6.0
description: Updating the MiniportInitialize Function for NDIS 6.0
ms.assetid: 8d21f49f-1710-4bd6-bc92-733580765db6
keywords:
- updating MiniportInitialize
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Updating the MiniportInitialize Function for NDIS 6.0





In NDIS 6.0, the [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function replaces the [*MiniportInitialize*](https://msdn.microsoft.com/library/windows/hardware/ff550472) function. *MiniportInitializeEx* initializes an adapter for network I/O operations. NDIS passes *MiniportInitializeEx* an [**NDIS\_MINIPORT\_INIT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff565972) structure. For more information about *MiniportInitializeEx* and this structure, see [Initializing an Adapter](initializing-a-miniport-adapter.md).

The following [standard INF keywords](standardized-inf-keywords-for-network-devices.md) are mandatory for connectionless NDIS 6.0 and later miniport drivers:

-   **\*IfType**

-   **\*MediaType**

-   **\*PhysicalMediaType**

If the mandatory keywords are missing from the driver's INF file, NDIS does not call the miniport driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function.

The *MiniportInitializeEx* function must:

-   Set the miniport attributes. For more information, see [Setting the NDIS 6.0 Miniport Adapter Attributes](setting-the-ndis-6-0-miniport-adapter-attributes.md).

-   Read configuration parameters from the registry. For more information, see [Reading the Registry in NDIS 6.0](reading-the-registry-in-an-ndis-6-0-miniport-driver.md).

-   Allocate memory. For more information, see [Allocating Memory in NDIS 6.0](allocating-memory-in-an-ndis-6-0-miniport-driver.md).

-   Allocate the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) and the [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) pools. For more information, see [Allocating Network Data Pools in NDIS 6.0](allocating-network-data-pools-in-an-ndis-6-0-miniport-driver.md).

-   Register the interrupt services. For more information, see [Porting Interrupt Registration to NDIS 6.0](porting-interrupt-registration-to-ndis-6-0.md).

-   Allocate scatter gather DMA resources. For more information, see [Porting Miniport Driver DMA Operations to NDIS 6.0](porting-miniport-driver-dma-operations-to-ndis-6-0.md).

-   Read and write to the bus-specific configuration space. For more information, see [Updating Bus-Specific Configuration Space Access for NDIS 6.0](updating-bus-specific-configuration-space-access-for-ndis-6-0.md).

 

 





