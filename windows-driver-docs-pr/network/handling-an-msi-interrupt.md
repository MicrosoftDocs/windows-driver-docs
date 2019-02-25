---
title: Handling an MSI Interrupt
description: Handling an MSI Interrupt
ms.assetid: c8e2a5a4-17f5-48a3-a2d0-6eca2a0b7f45
keywords:
- MSI-X WDK networking , handling interrupts
- message-signaled interrupts WDK networking , handling interrupts
- MSIs WDK networking , handling interrupts
- interrupts WDK networking , handling
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling an MSI Interrupt





NDIS calls the [*MiniportMessageInterrupt*](https://msdn.microsoft.com/library/windows/hardware/ff559407) function when a network interface card (NIC) generates an interrupt. The *MessageId* parameter in this function identifies the MSI-X message.

*MiniportMessageInterrupt* should always return **TRUE** after processing the interrupt because message interrupts are not shared.

A miniport driver should do as little work as possible in its *MiniportMessageInterrupt* function. The driver should defer I/O operations to the [*MiniportMessageInterruptDpc*](https://msdn.microsoft.com/library/windows/hardware/ff559411) function, which NDIS calls to complete the deferred processing of an interrupt.

To queue additional deferred procedure calls (DPCs) after [*MiniportMessageInterrupt*](https://msdn.microsoft.com/library/windows/hardware/ff559407) returns, the miniport driver sets the bits of the *TargetProcessors* parameter of the *MiniportMessageInterrupt* function. To request additional DPCs from *MiniportMessageInterrupt* or *MiniportMessageInterruptDPC*, the miniport driver can call the [**NdisMQueueDpc**](https://msdn.microsoft.com/library/windows/hardware/ff563637) function.

The miniport driver can call **NdisMQueueDpc** to request additional DPCs for other processors.

NDIS 6.1 and later versions guarantees that DPCs for different messages that are scheduled for the same CPU are queued separately. For example, if a miniport driver schedules two DPCs at the same time on CPU 1 (one DPC for message 0 and the other DPC for message 1), two DPCs are queued for CPU 1 (one DPC with message 0 and the other DPC with message 1).

NDIS also guarantees that DPCs for the same message that are scheduled on different CPUs are queued separately. For example, if a miniport driver schedules two DPCs (one DPC on CPU 0 for message 0 and one DPC on CPU 1 for message 0), two separate DPCs are queued on CPU 0 and CPU 1, both for message 0.

 

 





