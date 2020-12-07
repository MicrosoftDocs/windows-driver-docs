---
title: AVStream Dispatch Tables
description: AVStream Dispatch Tables
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





The AVStream dispatch table, [**KSDEVICE\_DISPATCH**](/windows-hardware/drivers/ddi/ks/ns-ks-_ksdevice_dispatch), is a set of function pointers to dispatch functions. A minidriver can extend the behavior provided by AVStream by providing callback routines that perform driver-specific tasks.

These minidriver-provided routines receive notifications of certain events and may extend or modify the default event handling provided by AVStream.

Both [**KSFILTER\_DISPATCH**](/windows-hardware/drivers/ddi/ks/ns-ks-_ksfilter_dispatch) and [**KSPIN\_DISPATCH**](/windows-hardware/drivers/ddi/ks/ns-ks-_kspin_dispatch) structures provide a dispatch called *Process*. Use this dispatch to differentiate a [filter-centric](filter-centric-processing.md) filter from a [pin-centric](pin-centric-processing.md) filter.To specify a filter-centric filter, supply a pointer to a process dispatch callback routine in the filter dispatch table. A pin-centric filter provides a process dispatch in each of the pin descriptor tables.

You can register filters to be notified about creations, deletions, the need to process data, and resets. You can register pins to be notified of events such as creations, closure, the need to process data, resets, setting of data formats, and state changes. To register objects for notification, supply a pointer to a vendor-supplied dispatch routine in the relevant dispatch structure.

For more information about dispatch functions, see [**KSFILTER\_DISPATCH**](/windows-hardware/drivers/ddi/ks/ns-ks-_ksfilter_dispatch), [**KSPIN\_DISPATCH**](/windows-hardware/drivers/ddi/ks/ns-ks-_kspin_dispatch), and [**KSALLOCATOR\_DISPATCH**](/windows-hardware/drivers/ddi/ks/ns-ks-_ksallocator_dispatch).

 

