---
title: Porting Interrupt Handling to NDIS 6.0
description: Porting Interrupt Handling to NDIS 6.0
ms.assetid: 528fa358-c174-49a8-b067-6f1351fff30c
keywords:
- DPCs WDK networking
- deferred procedure calls WDK networking
- receive-side scaling WDK networking , porting interrupt handling
- RSS WDK networking , porting interrupt handling
- interrupts WDK networking , receive-side scaling
- message-signaled inter
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting Interrupt Handling to NDIS 6.0





In NDIS 6.0, when a NIC asserts an interrupt line, NDIS calls the miniport driver's [*MiniportInterrupt*](https://msdn.microsoft.com/library/windows/hardware/ff559395) function (formerly [**MiniportISR**](https://msdn.microsoft.com/library/windows/hardware/ff550478)). *MiniportInterrupt* dismisses the interrupt, saves necessary interrupt state information, and defers as much of the I/O processing as possible to the [*MiniportInterruptDpc*](https://msdn.microsoft.com/library/windows/hardware/ff559398) function (formerly [**MiniportHandleInterrupt**](https://msdn.microsoft.com/library/windows/hardware/ff549458)).

Unlike an NDIS 5.*x* miniport driver, an NDIS 6.0 miniport driver can request deferred procedure calls (DPCs) to distribute the processing of receive queues across additional processors. This functionality is called receive side scaling (RSS). To queue additional DPCs after *MiniportInterrupt* returns, the miniport driver sets the bits of the *TargetProcessors* parameter of the *MiniportInterrupt* function. To request additional DPCs from *MiniportInterrupt* or *MiniportInterruptDPC*, the miniport driver calls the [**NdisMQueueDpc**](https://msdn.microsoft.com/library/windows/hardware/ff563637) function.

For more information about handling interrupts, see [Handling Interrupts](handling-interrupts.md).

 

 





