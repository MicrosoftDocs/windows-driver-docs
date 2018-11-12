---
title: Starting a NetDMA Provider
description: Starting a NetDMA Provider
ms.assetid: c6f91535-25d6-4e3c-9daf-53f07d4c7c67
keywords:
- starting NetDMA provider drivers
- NetDMA provider drivers WDK networking , starting
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Starting a NetDMA Provider


**Note**  The NetDMA interface is not supported in Windows 8 and later.

 




A NetDMA provider driver initializes a dynamic memory access (DMA) engine and starts the NetDMA provider while handling the [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749) IRP. After the driver successfully initializes all of the DMA channels, the NetDMA provider driver calls the [**NetDmaProviderStart**](https://msdn.microsoft.com/library/windows/hardware/ff568334) function to notify the NetDMA interface that the NetDMA provider is started and ready for use.

The NetDMA provider driver supplies a [**NET\_DMA\_PROVIDER\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff568737) structure in the *ProviderAttributes* parameter of **NetDmaProviderStart**. This attributes structure contains:

-   The major and minor hardware version numbers.

-   A vendor identifier (ID) that uniquely identifies the vendor that created the DMA engine. This ID is the vendor ID that is specified in the device's PCI configuration space. For more information about the ID, see [Identifiers for PCI Devices](https://msdn.microsoft.com/library/windows/hardware/ff546262).

-   The actual number of DMA channels that the DMA engine supports.

-   The maximum transfer size that the DMA engine supports.

-   The maximum address space that the DMA engine supports.

Before a NetDMA provider driver calls [**NetDmaProviderStart**](https://msdn.microsoft.com/library/windows/hardware/ff568334), it must be ready to handle all NetDMA interface requests, such as allocating DMA channels and performing DMA transfers.

DMA provider drivers call the [**NetDmaProviderStop**](https://msdn.microsoft.com/library/windows/hardware/ff568335) function to notify the NetDMA interface that a previously started NetDMA provider is no longer available. For more information about stopping a NetDMA provider, see [Stopping a NetDMA Provider](stopping-a-netdma-provider.md).

 

 





