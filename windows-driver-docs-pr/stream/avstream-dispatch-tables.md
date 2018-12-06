---
title: AVStream Dispatch Tables
description: AVStream Dispatch Tables
ms.assetid: 974ea9ee-bb59-4973-83ef-c61f0240a555
keywords:
- dispatch tables WDK AVStream
- AVStream dispatch tables WDK
- KSDEVICE_DISPATCH
- dispatching functions WDK AVStream
- dispatch functions WDK AVStream
- Process dispatch WDK AVStream
- filter-centric filters WDK AVStream
- pin-centric filters WDK AVStream
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# AVStream Dispatch Tables





The AVStream dispatch table, [**KSDEVICE\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/ff561693), is a set of function pointers to dispatch functions. A minidriver can extend the behavior provided by AVStream by providing callback routines that perform driver-specific tasks.

These minidriver-provided routines receive notifications of certain events and may extend or modify the default event handling provided by AVStream.

Both [**KSFILTER\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/ff562554) and [**KSPIN\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/ff563535) structures provide a dispatch called *Process*. Use this dispatch to differentiate a [filter-centric](filter-centric-processing.md) filter from a [pin-centric](pin-centric-processing.md) filter.To specify a filter-centric filter, supply a pointer to a process dispatch callback routine in the filter dispatch table. A pin-centric filter provides a process dispatch in each of the pin descriptor tables.

You can register filters to be notified about creations, deletions, the need to process data, and resets. You can register pins to be notified of events such as creations, closure, the need to process data, resets, setting of data formats, and state changes. To register objects for notification, supply a pointer to a vendor-supplied dispatch routine in the relevant dispatch structure.

For more information about dispatch functions, see [**KSFILTER\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/ff562554), [**KSPIN\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/ff563535), and [**KSALLOCATOR\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/ff560976).

 

 




