---
title: Initializing NDIS Timers
description: Initializing NDIS Timers
keywords:
- timer services WDK NDIS
- NDIS timer services WDK
- initializing NDIS timers
ms.date: 04/20/2017
---

# Initializing NDIS Timers





The [**NDIS\_TIMER\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_timer_characteristics) structure defines characteristics of a one-shot or periodic timer. Any NDIS driver can have more than one timer. Each timer object is associated with a different [**NetTimerCallback**](/windows-hardware/drivers/ddi/ndis/nc-ndis-ndis_timer_function) function that is specified in the **TimerFunction** member. NDIS calls the associated *NetTimerCallback* function when the timer expires.

To allocate and initialize a timer, your driver should call the [**NdisAllocateTimerObject**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisallocatetimerobject) function and provide a driver-allocated NDIS\_TIMER\_CHARACTERISTICS structure. The timer does not start until the driver calls the [**NdisSetTimerObject**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndissettimerobject) function.

To free a timer object, your driver should call the [**NdisFreeTimerObject**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfreetimerobject) function.

 

