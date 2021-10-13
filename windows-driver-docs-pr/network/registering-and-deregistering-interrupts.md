---
title: Registering and Deregistering Interrupts
description: Registering and Deregistering Interrupts
keywords:
- interrupts WDK networking , registering
- interrupts WDK networking , deregistering
- NdisMRegisterInterruptEx
- NdisMDeregisterInterruptEx
- registering interrupts
- deregistering interrupts
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registering and Deregistering Interrupts





A miniport driver calls [**NdisMRegisterInterruptEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismregisterinterruptex) to register an interrupt. The driver allocates and initializes an [**NDIS\_MINIPORT\_INTERRUPT\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_interrupt_characteristics) structure to specify the interrupt characteristics and function entry points. The driver passes the structure to **NdisMRegisterInterruptEx**.

Drivers call the [**NdisMDeRegisterInterruptEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismderegisterinterruptex) function to release resources that were previously allocated with **NdisMRegisterInterruptEx**.

 

