---
title: Servicing Timers
description: Servicing Timers
keywords:
- timer services WDK NDIS
- NDIS timer services WDK
- canceling NDIS timers
ms.date: 04/20/2017
---

# Servicing Timers





NDIS calls the [**NetTimerCallback**](/windows-hardware/drivers/ddi/ndis/nc-ndis-ndis_timer_function) function when an NDIS 6.0 timer fires. The *FunctionContext* parameter of this function contains a pointer to a driver-supplied context area. The default value for *FunctionContext* is specified in an [**NDIS\_TIMER\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_timer_characteristics) structure. The driver passed the structure to the [**NdisAllocateTimerObject**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisallocatetimerobject) function to allocate and initialize the associated timer object.

If the driver specified a non-NULL value in the *FunctionContext* parameter that is passed to the [**NdisSetTimerObject**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndissettimerobject) function, NDIS passes that value to the *FunctionContext* parameter of the *NetTimerCallback* function. Otherwise, NDIS passes the default value that is specified in the NDIS\_TIMER\_CHARACTERISTICS structure.

Any NDIS driver can have more than one *NetTimerCallback* function. Each such *NetTimerCallback* function must be associated with a different driver-allocated and initialized timer object.

A call to the [**NdisSetTimerObject**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndissettimerobject) function causes the *NetTimerCallback* function that is associated with the timer object to be run after a specified interval or periodically.

To stop calls to a *NetTimerCallback* function, call the [**NdisCancelTimerObject**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiscanceltimerobject) function. NDIS might still call *NetTimerCallback* if the timeout has already expired before the call to **NdisCancelTimerObject**.

If a *NetTimerCallback* function shares resources with other driver functions, the driver should synchronize access to those resources with a spin lock.

 

