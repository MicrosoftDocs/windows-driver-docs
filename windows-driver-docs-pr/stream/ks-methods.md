---
title: KS Methods
description: KS Methods
ms.assetid: 1d7bd6f4-0aaf-4d77-8132-f551fd2ecbd2
keywords:
- kernel streaming WDK , methods
- KS WDK , methods
- methods WDK kernel streaming
- method sets WDK kernel streaming
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# KS Methods





Method sets are groups of related actions that kernel streaming clients can invoke on KS objects. For example, an allocator object could provide a method set containing methods that allocate and deallocate memory.

A minidriver supplies a [**KSMETHOD\_SET**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ks/ns-ks-ksmethod_set) structure for each method set it supports. In turn, a KSMETHOD\_SET structure contains an array of [**KSMETHOD\_ITEM**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ks/ns-ks-ksmethod_item) structures that describe single methods. The minidriver supplies pointers to driver-supplied [*KStrMethodHandler*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ks/nc-ks-pfnkshandler) and [*KStrSupportHandler*](https://docs.microsoft.com/previous-versions/ff567206(v=vs.85)) handling routines in the **MethodHandler** and **SupportHandler** members of the KSMETHOD\_ITEM structure.

Clients make synchronous method requests by calling [**KsSynchronousDeviceControl**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ksproxy/nf-ksproxy-kssynchronousdevicecontrol), or asynchronous requests by calling **DeviceIoControl** (described in the Microsoft Windows SDK documentation) with [**IOCTL\_KS\_METHOD**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ks/ni-ks-ioctl_ks_method).

A driver requests a specific method by providing a [**KSMETHOD**](https://docs.microsoft.com/previous-versions/ff563398(v=vs.85)) structure in the *InBuffer* parameter of the above call.

AVStream filters and pins describe methods that they support by supplying a [**KSAUTOMATION\_TABLE**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ks/ns-ks-ksautomation_table_) structure in the **AutomationTable** member of either a [**KSFILTER\_DESCRIPTOR**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ks/ns-ks-_ksfilter_descriptor) structure or a [**KSPIN\_DESCRIPTOR\_EX**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ks/ns-ks-_kspin_descriptor_ex) structure. For more information, see [Defining Automation Tables](defining-automation-tables.md).

 

 




