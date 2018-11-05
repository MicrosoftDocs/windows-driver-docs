---
title: Supporting Message Signaled Interrupts in NDIS 6.0
description: Supporting Message Signaled Interrupts in NDIS 6.0
ms.assetid: f8beae05-7376-4de7-ba90-90e8aa7da802
keywords:
- interrupts WDK networking , adding entry points
- message-signaled interrupts WDK networking , adding entry points
- MSIs WDK networking , adding entry points
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting Message Signaled Interrupts in NDIS 6.0





To support message signaled interrupts (MSI), add optional entry points to the [**NDIS\_MINIPORT\_INTERRUPT\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff566465) structure during interrupt registration. For example, define a [*MiniportMessageInterrupt*](https://msdn.microsoft.com/library/windows/hardware/ff559407) function. For more information about registering interrupt entry points, see [Porting Interrupt Registration to NDIS 6.0](porting-interrupt-registration-to-ndis-6-0.md).

The driver should provide entry points for the normal interrupt functions, even if the driver supports the MSI entry points. If NDIS does not grant an MSI interrupt, it can grant a normal interrupt as a fallback condition. If the driver does not support MSI, set the MSI entry points to **NULL**.

MSI support can provide significant performance benefits. This is particularly true for NICs that support receive side scaling. For more information about receive side scaling, see [Receive Side Scaling](ndis-receive-side-scaling2.md).

 

 





