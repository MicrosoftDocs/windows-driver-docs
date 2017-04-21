---
title: AVStream Dispatch Tables
author: windows-driver-content
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
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# AVStream Dispatch Tables


## <a href="" id="ddk-avstream-dispatch-tables-ksg"></a>


The AVStream dispatch table, [**KSDEVICE\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/ff561693), is a set of function pointers to dispatch functions. A minidriver can extend the behavior provided by AVStream by providing callback routines that perform driver-specific tasks.

These minidriver-provided routines receive notifications of certain events and may extend or modify the default event handling provided by AVStream.

Both [**KSFILTER\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/ff562554) and [**KSPIN\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/ff563535) structures provide a dispatch called *Process*. Use this dispatch to differentiate a [filter-centric](filter-centric-processing.md) filter from a [pin-centric](pin-centric-processing.md) filter.To specify a filter-centric filter, supply a pointer to a process dispatch callback routine in the filter dispatch table. A pin-centric filter provides a process dispatch in each of the pin descriptor tables.

You can register filters to be notified about creations, deletions, the need to process data, and resets. You can register pins to be notified of events such as creations, closure, the need to process data, resets, setting of data formats, and state changes. To register objects for notification, supply a pointer to a vendor-supplied dispatch routine in the relevant dispatch structure.

For more information about dispatch functions, see [**KSFILTER\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/ff562554), [**KSPIN\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/ff563535), and [**KSALLOCATOR\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/ff560976).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20AVStream%20Dispatch%20Tables%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


