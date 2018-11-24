---
title: Writing a NetDMA Provider Driver
description: Writing a NetDMA Provider Driver
ms.assetid: a4fcecdf-284d-4cae-b930-4a02492e4eec
keywords:
- memory-to-memory data transfers WDK NetDMA , writing provider drivers
- data transfers WDK NetDMA , writing provider drivers
- transferring data WDK NetDMA , writing provider drivers
- NetDMA WDK networking , writing provider drivers
- DMA transfers WDK N
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Writing a NetDMA Provider Driver


**Note**  The NetDMA interface is not supported in Windows 8 and later.

 




The NetDMA interface provides a standard interface for NetDMA provider drivers. NetDMA provider drivers enable higher-level applications to use direct memory access (DMA) to move blocks of memory. By using a DMA engine to move memory, you free the CPU to perform other tasks.

NetDMA provider drivers are kernel-mode drivers that support the NetDMA interface and manage DMA engines. This section provides details about writing NetDMA provider drivers. For more general information about writing kernel-mode drivers, see [Kernel-Mode Driver Components](https://msdn.microsoft.com/library/windows/hardware/ff553213).

This section includes:

[Initializing a NetDMA Provider Driver](initializing-a-netdma-provider-driver.md)

[Unloading a NetDMA Provider Driver](unloading-a-netdma-provider-driver.md)

[Registering a NetDMA Provider](registering-a-netdma-provider.md)

[Deregistering a NetDMA Provider](deregistering-a-netdma-provider.md)

[Starting a NetDMA Provider](starting-a-netdma-provider.md)

[Stopping a NetDMA Provider](stopping-a-netdma-provider.md)

[NetDMA Provider Services](netdma-provider-services.md)

[Managing NetDMA Interrupts](managing-netdma-interrupts.md)

 

 





