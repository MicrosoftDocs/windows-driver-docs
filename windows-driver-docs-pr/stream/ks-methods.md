---
title: KS Methods
author: windows-driver-content
description: KS Methods
ms.assetid: 1d7bd6f4-0aaf-4d77-8132-f551fd2ecbd2
keywords: ["kernel streaming WDK , methods", "KS WDK , methods", "methods WDK kernel streaming", "method sets WDK kernel streaming"]
---

# KS Methods


## <a href="" id="ddk-ks-methods-ksg"></a>


Method sets are groups of related actions that kernel streaming clients can invoke on KS objects. For example, an allocator object could provide a method set containing methods that allocate and deallocate memory.

A minidriver supplies a [**KSMETHOD\_SET**](https://msdn.microsoft.com/library/windows/hardware/ff563423) structure for each method set it supports. In turn, a KSMETHOD\_SET structure contains an array of [**KSMETHOD\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff563420) structures that describe single methods. The minidriver supplies pointers to driver-supplied [*KStrMethodHandler*](https://msdn.microsoft.com/library/windows/hardware/ff567191) and [*KStrSupportHandler*](https://msdn.microsoft.com/library/windows/hardware/ff567206) handling routines in the **MethodHandler** and **SupportHandler** members of the KSMETHOD\_ITEM structure.

Clients make synchronous method requests by calling [**KsSynchronousDeviceControl**](https://msdn.microsoft.com/library/windows/hardware/ff567142), or asynchronous requests by calling **DeviceIoControl** (described in the Microsoft Windows SDK documentation) with [**IOCTL\_KS\_METHOD**](https://msdn.microsoft.com/library/windows/hardware/ff560817).

A driver requests a specific method by providing a [**KSMETHOD**](https://msdn.microsoft.com/library/windows/hardware/ff563398) structure in the *InBuffer* parameter of the above call.

AVStream filters and pins describe methods that they support by supplying a [**KSAUTOMATION\_TABLE**](https://msdn.microsoft.com/library/windows/hardware/ff560990) structure in the **AutomationTable** member of either a [**KSFILTER\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff562553) structure or a [**KSPIN\_DESCRIPTOR\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff563534) structure. For more information, see [Defining Automation Tables](defining-automation-tables.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KS%20Methods%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


