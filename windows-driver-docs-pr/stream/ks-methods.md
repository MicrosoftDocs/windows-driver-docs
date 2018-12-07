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

A minidriver supplies a [**KSMETHOD\_SET**](https://msdn.microsoft.com/library/windows/hardware/ff563423) structure for each method set it supports. In turn, a KSMETHOD\_SET structure contains an array of [**KSMETHOD\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff563420) structures that describe single methods. The minidriver supplies pointers to driver-supplied [*KStrMethodHandler*](https://msdn.microsoft.com/library/windows/hardware/ff567191) and [*KStrSupportHandler*](https://msdn.microsoft.com/library/windows/hardware/ff567206) handling routines in the **MethodHandler** and **SupportHandler** members of the KSMETHOD\_ITEM structure.

Clients make synchronous method requests by calling [**KsSynchronousDeviceControl**](https://msdn.microsoft.com/library/windows/hardware/ff567142), or asynchronous requests by calling **DeviceIoControl** (described in the Microsoft Windows SDK documentation) with [**IOCTL\_KS\_METHOD**](https://msdn.microsoft.com/library/windows/hardware/ff560817).

A driver requests a specific method by providing a [**KSMETHOD**](https://msdn.microsoft.com/library/windows/hardware/ff563398) structure in the *InBuffer* parameter of the above call.

AVStream filters and pins describe methods that they support by supplying a [**KSAUTOMATION\_TABLE**](https://msdn.microsoft.com/library/windows/hardware/ff560990) structure in the **AutomationTable** member of either a [**KSFILTER\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff562553) structure or a [**KSPIN\_DESCRIPTOR\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff563534) structure. For more information, see [Defining Automation Tables](defining-automation-tables.md).

 

 




