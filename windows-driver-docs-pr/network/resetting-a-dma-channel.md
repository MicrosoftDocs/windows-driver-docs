---
title: Resetting a DMA Channel
description: Resetting a DMA Channel
ms.assetid: 40dfbe7c-fda6-4c6b-a3aa-265937538100
keywords:
- memory-to-memory data transfers WDK NetDMA , resetting channels
- data transfers WDK NetDMA , resetting channels
- transferring data WDK NetDMA , resetting channels
- DMA transfers WDK NetDMA , resetting channels
- NetDMA WDK networking , resetting channe
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Resetting a DMA Channel


**Note**  The NetDMA interface is not supported in Windows 8 and later.

 




The NetDMA interface calls the NetDMA provider driver's [**ProviderResetChannel**](https://msdn.microsoft.com/library/windows/hardware/ff570400) function, if any, to reset a dynamic memory access (DMA) channel.

In *ProviderResetChannel*, the NetDMA provider should terminate any active transfer immediately without completing the transfer of the data that is associated with the current DMA descriptor. If completion status reporting is enabled, the DMA engine writes the **NetDmaTransferStatusHalted** status in the address that is specified in the **CompletionVirtualAddress** and **CompletionPhysicalAddress** members in the [**NET\_DMA\_CHANNEL\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff568732) structure.

Before the reset operation is complete, the NetDMA provider must set the DMA channel to the initial state that existed after the channel was allocated. After the NetDMA interface calls *ProviderResetChannel*, the NetDMA provider cannot access any of the previously submitted DMA descriptors. The DMA channel must be ready for the NetDMA interface to call the [**ProviderStartDma**](https://msdn.microsoft.com/library/windows/hardware/ff570404) function.

 

 





