---
title: Porting Miniport Driver Interrupt Operations to NDIS 6.0
description: Porting Miniport Driver Interrupt Operations to NDIS 6.0
ms.assetid: bfd62833-8c7e-4b59-a6e4-4e91a4bb6c53
keywords:
- interrupts WDK networking , porting operations
- miniport drivers WDK networking , interrupts
- NDIS miniport drivers WDK , interrupts
- message-signaled interrupts WDK networking , porting
- MSIs WDK networking , porting operations
- porting miniport driv
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting Miniport Driver Interrupt Operations to NDIS 6.0





In NDIS 6.0, the interrupt function entry points are moved from the driver characteristics into the [**NDIS\_MINIPORT\_INTERRUPT\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff566465) structure.

Also, the names of the interrupt function entry points are changed. For example, replace the [**MiniportISR**](https://msdn.microsoft.com/library/windows/hardware/ff550478) function with the [*MiniportInterrupt*](https://msdn.microsoft.com/library/windows/hardware/ff559395) function.

Optional entry points for message signaled interrupts (MSI) are provided. For example, a [*MiniportMessageInterrupt*](https://msdn.microsoft.com/library/windows/hardware/ff559407) function is defined.

Additional information about porting interrupt operations is included in the following topics:

[Porting Interrupt Registration to NDIS 6.0](porting-interrupt-registration-to-ndis-6-0.md)

[Porting Interrupt Handling to NDIS 6.0](porting-interrupt-handling-to-ndis-6-0.md)

[Supporting Message Signaled Interrupts in NDIS 6.0](supporting-message-signaled-interrupts-in-ndis-6-0.md)

 

 





