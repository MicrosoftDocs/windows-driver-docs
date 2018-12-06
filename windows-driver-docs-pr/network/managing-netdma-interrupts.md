---
title: Managing NetDMA Interrupts
description: Managing NetDMA Interrupts
ms.assetid: cd518cc2-dc0d-47fd-ac52-aa9c64b7d882
keywords:
- memory-to-memory data transfers WDK NetDMA , interrupts
- data transfers WDK NetDMA , interrupts
- transferring data WDK NetDMA , interrupts
- DMA transfers WDK NetDMA , interrupts
- NetDMA WDK networking , interrupts
- interrupts WDK NetDMA
- interrupts
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Managing NetDMA Interrupts


**Note**  The NetDMA interface is not supported in Windows 8 and later.

 




With the NetDMA interface, you can complete dynamic memory access (DMA) operations with an interrupt service routine (ISR). For general information about servicing interrupts in Microsoft Windows drivers, see [Servicing Interrupts](https://msdn.microsoft.com/library/windows/hardware/ff563737).

DMA providers can use line-based interrupts if the computer does not support message-based interrupts (MSI). NetDMA providers must use extended message-based interrupts (MSI-X) on computers that support MSI-X. If the computer supports MSI-X and the NetDMA interface calls the [**ProviderSetDmaChannelCpuAffinity**](https://msdn.microsoft.com/library/windows/hardware/ff570402) function, the NetDMA provider driver must set the CPU affinities for the interrupts that are associated with each DMA channel.

This section includes:

[Setting the NetDMA Interrupt CPU Affinities](setting-the-netdma-interrupt-cpu-affinities.md)

[Handling a NetDMA Interrupt](handling-a-netdma-interrupt.md)

[Handling a NetDMA Interrupt DPC](handling-a-netdma-interrupt-dpc.md)

 

 





