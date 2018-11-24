---
title: Registering and Deregistering Interrupts
description: Registering and Deregistering Interrupts
ms.assetid: 222782f3-092e-417d-ab1b-1988a593caa4
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





A miniport driver calls [**NdisMRegisterInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff563649) to register an interrupt. The driver allocates and initializes an [**NDIS\_MINIPORT\_INTERRUPT\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff566465) structure to specify the interrupt characteristics and function entry points. The driver passes the structure to **NdisMRegisterInterruptEx**.

Drivers call the [**NdisMDeRegisterInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff563575) function to release resources that were previously allocated with **NdisMRegisterInterruptEx**.

 

 





