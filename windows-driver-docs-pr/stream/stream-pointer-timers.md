---
title: Stream Pointer Timers
description: Stream Pointer Timers
ms.assetid: 98413fc6-2b62-4c52-9ac4-bd2a3a60db60
keywords:
- stream pointers WDK AVStream , timers
- timers WDK AVStream
- time-outs WDK AVStream
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Stream Pointer Timers





To set a timer on a stream pointer, call [**KsStreamPointerScheduleTimeout**](https://msdn.microsoft.com/library/windows/hardware/ff567135). If the specified stream pointer has not been deleted by the time *Interval* expires, AVStream calls the vendor-supplied timer callback routine. Specify *Interval* in 100-nanosecond units.

To cancel a timeout, call [**KsStreamPointerCancelTimeout**](https://msdn.microsoft.com/library/windows/hardware/ff567128).

 

 




