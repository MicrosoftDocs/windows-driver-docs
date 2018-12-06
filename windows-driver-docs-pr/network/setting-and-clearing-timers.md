---
title: Setting and Clearing Timers
description: Setting and Clearing Timers
ms.assetid: 75f348f7-173f-4799-88aa-1ca50a6df023
keywords:
- timer services WDK NDIS
- NDIS timer services WDK
- clearing NDIS timers
- allocating NDIS timers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting and Clearing Timers





After allocating and initializing a timer with the [**NdisAllocateTimerObject**](https://msdn.microsoft.com/library/windows/hardware/ff561618) function, an NDIS 6.0 driver calls the [**NdisSetTimerObject**](https://msdn.microsoft.com/library/windows/hardware/ff564563) function to set a timer object to fire after a specified interval or periodically.

The *DueTime* parameter of **NdisSetTimerObject** specifies the interval to elapse before a timer fires and NDIS calls the associated [**NetTimerCallback**](https://msdn.microsoft.com/library/windows/hardware/ff568351) function. The expiration time is expressed in system time units (100-nanosecond intervals).

If the *MillisecondsPeriod* parameter of **NdisSetTimerObject** is not zero, the timer fires periodically and *MillisecondsPeriod* specifies the periodic time interval, in milliseconds, that elapses between each time a periodic timer fires and the next call to the *NetTimerCallback* function.

Your driver can call the [**NdisCancelTimerObject**](https://msdn.microsoft.com/library/windows/hardware/ff561624) function to cancel a timer that is associated with a previous call to the **NdisSetTimerObject** function. NDIS might still call *NetTimerCallback* if the timeout has already expired before the call to **NdisCancelTimerObject**.

 

 





