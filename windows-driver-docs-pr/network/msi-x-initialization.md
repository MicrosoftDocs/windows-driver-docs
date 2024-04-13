---
title: MSI-X Initialization
description: MSI-X Initialization
keywords:
- MSI-X WDK networking , initializing
- message-signaled interrupts WDK networking , initializing
- MSIs WDK networking , initializing
- initializing MSI-X
ms.date: 04/20/2017
---

# MSI-X Initialization





To support MSI-X, MSI initialization requires a pre-registration phase in which the miniport driver establishes a function that filters resource-requirements. This function can change the interrupt affinity for each MSI-X message or remove message interrupt resources if the driver will register for line-based interrupts in the [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function.

The pre-registration phase occurs before NDIS calls the [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function. As with line-based interrupts, miniport drivers also register MSI interrupts while initializing miniport adapters in *MiniportInitializeEx*.

This section includes:

[MSI-X Pre-Registration](msi-x-pre-registration.md)

[MSI-X Resource Filtering](msi-x-resource-filtering.md)

[Registering and Deregistering an MSI Interrupt](registering-and-deregistering-an-msi-interrupt.md)

 

