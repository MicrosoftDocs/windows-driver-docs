---
title: Stream Pointer Timers
description: Stream Pointer Timers
keywords:
- stream pointers WDK AVStream , timers
- timers WDK AVStream
- time-outs WDK AVStream
ms.date: 04/20/2017
---

# Stream Pointer Timers





To set a timer on a stream pointer, call [**KsStreamPointerScheduleTimeout**](/windows-hardware/drivers/ddi/ks/nf-ks-ksstreampointerscheduletimeout). If the specified stream pointer has not been deleted by the time *Interval* expires, AVStream calls the vendor-supplied timer callback routine. Specify *Interval* in 100-nanosecond units.

To cancel a timeout, call [**KsStreamPointerCancelTimeout**](/windows-hardware/drivers/ddi/ks/nf-ks-ksstreampointercanceltimeout).

 

