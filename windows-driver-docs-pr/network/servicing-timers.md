---
title: Servicing Timers
description: Servicing Timers
ms.assetid: 6a80a55b-4c7e-4a48-8903-0a1fb28af153
keywords:
- timer services WDK NDIS
- NDIS timer services WDK
- canceling NDIS timers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Servicing Timers





NDIS calls the [**NetTimerCallback**](https://msdn.microsoft.com/library/windows/hardware/ff568351) function when an NDIS 6.0 timer fires. The *FunctionContext* parameter of this function contains a pointer to a driver-supplied context area. The default value for *FunctionContext* is specified in an [**NDIS\_TIMER\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff567886) structure. The driver passed the structure to the [**NdisAllocateTimerObject**](https://msdn.microsoft.com/library/windows/hardware/ff561618) function to allocate and initialize the associated timer object.

If the driver specified a non-NULL value in the *FunctionContext* parameter that is passed to the [**NdisSetTimerObject**](https://msdn.microsoft.com/library/windows/hardware/ff564563) function, NDIS passes that value to the *FunctionContext* parameter of the *NetTimerCallback* function. Otherwise, NDIS passes the default value that is specified in the NDIS\_TIMER\_CHARACTERISTICS structure.

Any NDIS driver can have more than one *NetTimerCallback* function. Each such *NetTimerCallback* function must be associated with a different driver-allocated and initialized timer object.

A call to the [**NdisSetTimerObject**](https://msdn.microsoft.com/library/windows/hardware/ff564563) function causes the *NetTimerCallback* function that is associated with the timer object to be run after a specified interval or periodically.

To stop calls to a *NetTimerCallback* function, call the [**NdisCancelTimerObject**](https://msdn.microsoft.com/library/windows/hardware/ff561624) function. NDIS might still call *NetTimerCallback* if the timeout has already expired before the call to **NdisCancelTimerObject**.

If a *NetTimerCallback* function shares resources with other driver functions, the driver should synchronize access to those resources with a spin lock.

 

 





