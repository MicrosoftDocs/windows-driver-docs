---
title: Timer Objects
description: Any driver can use a timer object within a nonarbitrary thread context to time-out operations in the driver's other routines, or to schedule operations to be performed periodically.
ms.assetid: A4844F19-3BEC-48C0-A5BF-E17CCEEC1601
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Timer Objects


Any driver can use a timer object within a nonarbitrary thread context to time-out operations in the driver's other routines, or to schedule operations to be performed periodically. Starting with Windows 2000, timer objects based on the [**KTIMER**](https://docs.microsoft.com/windows-hardware/drivers/kernel/eprocess) structure are available to use with [**KeSetTimer**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-kesettimer) and the other **Ke*Xxx*Timer** routines. Starting with Windows 8.1, timer objects based on the [**EX\_TIMER**](https://docs.microsoft.com/windows-hardware/drivers/kernel/eprocess) structure are available to use with [**ExSetTimer**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-exsettimer) and the other **Ex*Xxx*Timer** routines. Timer objects based on the **KTIMER** and **EX\_TIMER** structures are [kernel dispatcher objects](kernel-dispatcher-objects.md) that are signaled when a timer expires. Timer expiration can be periodic or one-shot (nonperiodic).

This section contains the following topics:

-   [KeXxxTimer Routines, KTIMER Objects, and DPCs](timer-objects-and-dpcs.md)

-   [ExXxxTimer Routines and EX\_TIMER Objects](exxxxtimer-routines-and-ex-timer-objects.md)

 

 




