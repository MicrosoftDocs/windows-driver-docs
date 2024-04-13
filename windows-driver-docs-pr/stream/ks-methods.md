---
title: KS Methods
description: KS Methods
keywords:
- kernel streaming WDK , methods
- KS WDK , methods
- methods WDK kernel streaming
- method sets WDK kernel streaming
ms.date: 04/20/2017
---

# KS Methods





Method sets are groups of related actions that kernel streaming clients can invoke on KS objects. For example, an allocator object could provide a method set containing methods that allocate and deallocate memory.

A minidriver supplies a [**KSMETHOD\_SET**](/windows-hardware/drivers/ddi/ks/ns-ks-ksmethod_set) structure for each method set it supports. In turn, a KSMETHOD\_SET structure contains an array of [**KSMETHOD\_ITEM**](/windows-hardware/drivers/ddi/ks/ns-ks-ksmethod_item) structures that describe single methods. The minidriver supplies pointers to driver-supplied [*KStrMethodHandler*](/windows-hardware/drivers/ddi/ks/nc-ks-pfnkshandler) and [*KStrSupportHandler*](/previous-versions/ff567206(v=vs.85)) handling routines in the **MethodHandler** and **SupportHandler** members of the KSMETHOD\_ITEM structure.

Clients make synchronous method requests by calling [**KsSynchronousDeviceControl**](/windows-hardware/drivers/ddi/ksproxy/nf-ksproxy-kssynchronousdevicecontrol), or asynchronous requests by calling **DeviceIoControl** (described in the Microsoft Windows SDK documentation) with [**IOCTL\_KS\_METHOD**](/windows-hardware/drivers/ddi/ks/ni-ks-ioctl_ks_method).

A driver requests a specific method by providing a [**KSMETHOD**](./ksmethod-structure.md) structure in the *InBuffer* parameter of the above call.

AVStream filters and pins describe methods that they support by supplying a [**KSAUTOMATION\_TABLE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksautomation_table_) structure in the **AutomationTable** member of either a [**KSFILTER\_DESCRIPTOR**](/windows-hardware/drivers/ddi/ks/ns-ks-_ksfilter_descriptor) structure or a [**KSPIN\_DESCRIPTOR\_EX**](/windows-hardware/drivers/ddi/ks/ns-ks-_kspin_descriptor_ex) structure. For more information, see [Defining Automation Tables](defining-automation-tables.md).

