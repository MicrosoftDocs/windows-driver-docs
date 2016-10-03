---
title: AVStream Clocks
author: windows-driver-content
description: AVStream Clocks
MS-HAID:
- 'avsover\_466db2a8-840f-494b-a360-9169e9ea2a1b.xml'
- 'stream.avstream\_clocks'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: fc1d5bca-72e3-48e2-b46f-09a13bba83b4
keywords: ["clocks WDK AVStream", "AVStream clocks WDK", "pin clocks WDK AVStream", "timers WDK AVStream", "time WDK AVStream"]
---

# AVStream Clocks


## <a href="" id="ddk-avstream-clocks-ksg"></a>


AVStream filters support clocks on pins.

To indicate that an AVStream pin exposes a clock, set KSPIN\_FLAG\_IMPLEMENT\_CLOCK in the **Flags** member of the first [**KSPIN\_DESCRIPTOR\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff563534) in the **PinDescriptors** member of [**KSFILTER\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff562553).

Also provide a pointer to a [**KSCLOCK\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/ff561017) structure in [**KSPIN\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/ff563535).

To make clock requests, use the methods defined on the [IKsReferenceClock](https://msdn.microsoft.com/library/windows/hardware/ff560725) interface. You can acquire an *IKsReferenceClock* interface by calling [**KsPinGetReferenceClockInterface**](https://msdn.microsoft.com/library/windows/hardware/ff563517). The AVStream minidriver is responsible for releasing the interface when finished.

To obtain timer values to place in the **PresentationTime** field of [**KSSTREAM\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff567138), call [**IKsReferenceClock::GetCorrelatedTime**](https://msdn.microsoft.com/library/windows/hardware/ff560728).

Note that the clock never appears in GraphEdit, even if the clock has been selected.

To verify that the clock has been selected, verify that calls to [IKsReferenceClock](https://msdn.microsoft.com/library/windows/hardware/ff560725) methods generate calls to dispatch routines specified in KSCLOCK\_DISPATCH.

The filter graph manager selects a clock when a graph transitions into the pause state. Any filter that is a push source, for instance a capture filter, is given preference as a clock provider.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20AVStream%20Clocks%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


