---
title: Default Clocks
description: Default Clocks
keywords:
- default clocks WDK kernel streaming
ms.date: 04/20/2017
---

# Default Clocks





Kernel streaming minidrivers can call [**KsAllocateDefaultClockEx**](/windows-hardware/drivers/ddi/ks/nf-ks-ksallocatedefaultclockex) to allocate and initialize a default clock structure. Alternatively, they can call [**KsAllocateDefaultClock**](/windows-hardware/drivers/ddi/ks/nf-ks-ksallocatedefaultclock), which is a wrapper for **KsAllocateDefaultClockEx** with default parameters for the nonclock members. Call [**KsCreateDefaultClock**](/windows-hardware/drivers/ddi/ks/nf-ks-kscreatedefaultclock) after using **KsAllocateDefaultClockEx** to initialize the default clock.

The default clock supports [KSPROPSETID\_Clock](./kspropsetid-clock.md), and may be accessed just as any other clock presented by a filter pin. The underlying data structure, however, is created by the filter pin, and shared by that pin and any instances of the clock that are created. The clock relies on the pin to update the current state and other elements in the shared structure. The default clock handles notification requests and clock queries.

When a pin on the filter that provides this clock is assigned a master clock, the pin owns this clock. The pin should reference the clock file object, just as if it was assigned some other clock implementation. The default clock does not reference the pin's file object when an instance is created. Instead, it keeps an internal reference count based on the initial allocation of the common clock structure, and on each file object opened on the clock. Even if the clock's owner frees the clock structure, it remains in place until all file objects are closed. The pin can directly access the default clock object, rather than go through the standard clock interface.

Minidrivers can support the [**KSPROPERTY\_CLOCK\_FUNCTIONTABLE**](./ksproperty-clock-functiontable.md) property to provide user-mode clients with a mechanism to check reference clock time. This property fills in a structure with function pointers that enable this, thereby supporting precise rate matching.

In addition, minidrivers support the [**KSPROPERTY\_STREAM\_RATE**](./ksproperty-stream-rate.md) property if a specified pin allows rate changes.

Applications that use the kernel streaming proxy interface call methods in the [IKsClockPropertySet](/windows-hardware/drivers/ddi/ksproxy/nn-ksproxy-iksclockpropertyset) interface to get and set time on physical clocks that may be used elsewhere for rate matching.

See [Quality Management](quality-management.md) for related information.

 

