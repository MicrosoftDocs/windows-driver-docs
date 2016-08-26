---
title: KS Events
author: windows-driver-content
description: KS Events
MS-HAID:
- 'ks-overview\_381d42e5-9858-4c03-a424-2e560e51fa49.xml'
- 'stream.ks\_events'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 3eaa1d65-8417-4a07-b358-823394baec9b
keywords: ["kernel streaming WDK , events", "KS WDK , events", "events WDK kernel streaming", "event sets WDK kernel streaming"]
---

# KS Events


## <a href="" id="ddk-ks-events-ksg"></a>


If you are writing an AVStream minidriver, see [Event Handling in AVStream](event-handling-in-avstream.md).

Event sets are groups of related events for which a listener can request notification. For example, a listener could register to be notified of device state changes, or changes in stream position. When an event occurs, kernel streaming notifies any clients that have registered for this event.

Minidrivers describe how they support an event by providing a [**KSEVENT\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff561862) structure that contains pointers to handling routines.

Listeners register for notification by calling the kernel streaming proxy routine [**KsSynchronousDeviceControl**](https://msdn.microsoft.com/library/windows/hardware/ff567142) with the IOCTL\_KS\_ENABLE\_EVENT control code and pointers to [**KSEVENT**](https://msdn.microsoft.com/library/windows/hardware/ff561744) and [**KSEVENTDATA**](https://msdn.microsoft.com/library/windows/hardware/ff561750).structures.

The IOCTL\_KS\_DISABLE\_EVENT request disables a specified event. The same pointer that was used to enable the event must be used to disable it. This pointer uniquely identifies the event. Optionally, the client may specify a **NULL** pointer and length of zero to disable all active events for the client.

All event sets must support the KSEVENT\_TYPE\_BASICSUPPORT flag. Refer to [**KSEVENT**](https://msdn.microsoft.com/library/windows/hardware/ff561744) for a list of available event flags.

Some event types require additional parameters to register for event notification. For example, the [**KSEVENT\_CLOCK\_POSITION\_MARK**](https://msdn.microsoft.com/library/windows/hardware/ff561811) event on a clock is triggered when the clock reaches a certain time stamp. Consequently, clients that register to be notified of this event must specify the time stamp at which to trigger the event.

In such a case, a minidriver passes additional data parameters in the data buffer after the [**KSEVENTDATA**](https://msdn.microsoft.com/library/windows/hardware/ff561750) structure. Minidrivers that support such an event type use an extended data structure, of which the first member is of type KSEVENTDATA, to hold the notification data.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KS%20Events%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


