---
title: Handling an MSI Interrupt
description: Handling an MSI Interrupt
keywords:
- MSI-X WDK networking , handling interrupts
- message-signaled interrupts WDK networking , handling interrupts
- MSIs WDK networking , handling interrupts
- interrupts WDK networking , handling
ms.date: 04/20/2017
---

# Handling an MSI Interrupt





NDIS calls the [*MiniportMessageInterrupt*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_message_interrupt) function when a network interface card (NIC) generates an interrupt. The *MessageId* parameter in this function identifies the MSI-X message.

*MiniportMessageInterrupt* should always return **TRUE** after processing the interrupt because message interrupts are not shared.

A miniport driver should do as little work as possible in its *MiniportMessageInterrupt* function. The driver should defer I/O operations to the [*MiniportMessageInterruptDpc*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_message_interrupt_dpc) function, which NDIS calls to complete the deferred processing of an interrupt.

To queue additional deferred procedure calls (DPCs) after [*MiniportMessageInterrupt*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_message_interrupt) returns, the miniport driver sets the bits of the *TargetProcessors* parameter of the *MiniportMessageInterrupt* function. To request additional DPCs from *MiniportMessageInterrupt* or *MiniportMessageInterruptDPC*, the miniport driver can call the [**NdisMQueueDpc**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismqueuedpc) function.

The miniport driver can call **NdisMQueueDpc** to request additional DPCs for other processors.

NDIS 6.1 and later versions guarantees that DPCs for different messages that are scheduled for the same CPU are queued separately. For example, if a miniport driver schedules two DPCs at the same time on CPU 1 (one DPC for message 0 and the other DPC for message 1), two DPCs are queued for CPU 1 (one DPC with message 0 and the other DPC with message 1).

NDIS also guarantees that DPCs for the same message that are scheduled on different CPUs are queued separately. For example, if a miniport driver schedules two DPCs (one DPC on CPU 0 for message 0 and one DPC on CPU 1 for message 0), two separate DPCs are queued on CPU 0 and CPU 1, both for message 0.

 

