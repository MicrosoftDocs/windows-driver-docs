---
title: Initializing NDIS Timers
description: Initializing NDIS Timers
ms.assetid: 2f304f5c-fa70-441e-853e-a48ad70d61a0
keywords:
- timer services WDK NDIS
- NDIS timer services WDK
- initializing NDIS timers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Initializing NDIS Timers





The [**NDIS\_TIMER\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff567886) structure defines characteristics of a one-shot or periodic timer. Any NDIS driver can have more than one timer. Each timer object is associated with a different [**NetTimerCallback**](https://msdn.microsoft.com/library/windows/hardware/ff568351) function that is specified in the **TimerFunction** member. NDIS calls the associated *NetTimerCallback* function when the timer expires.

To allocate and initialize a timer, your driver should call the [**NdisAllocateTimerObject**](https://msdn.microsoft.com/library/windows/hardware/ff561618) function and provide a driver-allocated NDIS\_TIMER\_CHARACTERISTICS structure. The timer does not start until the driver calls the [**NdisSetTimerObject**](https://msdn.microsoft.com/library/windows/hardware/ff564563) function.

To free a timer object, your driver should call the [**NdisFreeTimerObject**](https://msdn.microsoft.com/library/windows/hardware/ff562605) function.

 

 





