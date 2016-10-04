---
title: Stream Pointer Timers
author: windows-driver-content
description: Stream Pointer Timers
MS-HAID:
- 'avsover\_3039cb42-9c7f-4638-87fe-4b2b6c02427f.xml'
- 'stream.stream\_pointer\_timers'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 98413fc6-2b62-4c52-9ac4-bd2a3a60db60
keywords: ["stream pointers WDK AVStream , timers", "timers WDK AVStream", "time-outs WDK AVStream"]
---

# Stream Pointer Timers


## <a href="" id="ddk-stream-pointer-timers-ksg"></a>


To set a timer on a stream pointer, call [**KsStreamPointerScheduleTimeout**](https://msdn.microsoft.com/library/windows/hardware/ff567135). If the specified stream pointer has not been deleted by the time *Interval* expires, AVStream calls the vendor-supplied timer callback routine. Specify *Interval* in 100-nanosecond units.

To cancel a timeout, call [**KsStreamPointerCancelTimeout**](https://msdn.microsoft.com/library/windows/hardware/ff567128).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Stream%20Pointer%20Timers%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


