---
title: Synchronizing with an MSI Interrupt
description: Synchronizing with an MSI Interrupt
ms.assetid: 61745a93-79dc-49ac-9ace-3ecb647b7b9a
keywords:
- MSI-X WDK networking , synchronizing interrupts
- message-signaled interrupts WDK networking , synchronizing interrupts
- MSIs WDK networking , synchronizing interrupts
- interrupts WDK networking , synchronizing
- synchronization WDK MSI-X
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Synchronizing with an MSI Interrupt





If a miniport driver's [*MiniportMessageInterrupt*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_message_interrupt) function shares resources, such as network interface card (NIC) registers or state variables, with another *MiniportXxx* function that runs at a lower IRQL, the other *MiniportXxx* function must call the [**NdisMSynchronizeWithInterruptEx**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsynchronizewithinterruptex) function. This call ensures that the miniport driver's [**MiniportSynchronizeMessageInterrupt**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_synchronize_interrupt) function accesses the shared resources in a synchronized and multiprocessor-safe manner.

 

 





