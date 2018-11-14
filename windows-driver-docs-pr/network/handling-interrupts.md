---
title: Handling interrupts for NDIS miniport drivers
description: Discusses the calls that an NDIS miniport driver uses when a NIC or another device generates an interrupt
ms.assetid: 75dc3676-f88f-4d86-8c77-02f48083de71
keywords:
- interrupts WDK networking , handling
- MiniportInterrupt
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling interrupts for NDIS miniport drivers





NDIS calls the [*MiniportInterrupt*](https://msdn.microsoft.com/library/windows/hardware/ff559395) function when a NIC, or another device that shares the interrupt with the NIC, generates an interrupt.

*MiniportInterrupt* should return **FALSE** immediately if the underlying NIC did not generate the interrupt. Otherwise, it returns **TRUE** after processing the interrupt.

A miniport driver should do as little work as possible in its *MiniportInterrupt* function. It should defer I/O operations to the [*MiniportInterruptDPC*](https://msdn.microsoft.com/library/windows/hardware/ff559398) function. NDIS calls *MiniportInterruptDPC* to complete the deferred processing of an interrupt.

To queue additional DPCs after *MiniportInterrupt* returns, the miniport driver sets the bits of the [**TargetProcessors**](https://msdn.microsoft.com/library/windows/hardware/ff563637) parameter of the *MiniportInterrupt* function. To request additional DPCs from *MiniportInterrupt* or *MiniportInterruptDPC*, the miniport driver calls the **NdisMQueueDpc** function.

The miniport driver can call **NdisMQueueDpc** to request additional DPC calls for other processors.

 

 





