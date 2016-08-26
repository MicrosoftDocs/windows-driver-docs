---
title: Event Handling in AVStream
author: windows-driver-content
description: Event Handling in AVStream
MS-HAID:
- 'avsover\_379c97a2-ccdd-4e5b-acbf-1df52dd0b75c.xml'
- 'stream.event\_handling\_in\_avstream'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 7add2055-8d3f-432d-8aa1-44459ac197dd
keywords: ["events WDK AVStream", "AVStream events WDK", "automation tables WDK AVStream"]
---

# Event Handling in AVStream


## <a href="" id="ddk-event-handling-in-avstream-ksg"></a>


AVStream filters and pins describe properties, events, and methods that they support by supplying a [**KSAUTOMATION\_TABLE**](https://msdn.microsoft.com/library/windows/hardware/ff560990) structure in the **AutomationTable** member of either a [**KSFILTER\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff562553) structure or a [**KSPIN\_DESCRIPTOR\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff563534) structure. For more information, see [AVStream Descriptors](avstream-descriptors.md).

To support events, an AVStream minidriver provides an array of [**KSEVENT\_SET**](https://msdn.microsoft.com/library/windows/hardware/ff561867) structures in an automation table. Each KSEVENT\_SET structure contains an array of [**KSEVENT\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff561862) structures. Each KSEVENT\_ITEM structure describes how the minidriver supports a specific event.

The minidriver can customize event behavior by supplying [*AVStrMiniAddEvent*](https://msdn.microsoft.com/library/windows/hardware/ff554260) and [*AVStrMiniRemoveEvent*](https://msdn.microsoft.com/library/windows/hardware/ff556361) handlers in the KSEVENT\_ITEM structures.

When AVStream receives an event enable request, it generates a KSEVENT\_ENTRY structure. If the minidriver has provided an *AVStrAddEvent* handler, AVStream passes a pointer to the KSEVENT\_ENTRY structure in the call to *AVStrAddEvent*.

If you do not provide an *AVStrAddEvent* handler, then by default AVStream adds the event to the object list. Your minidriver does not receive a [**KSEVENT\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/ff561853) pointer. Your minidriver can trigger the event by calling [**KsFilterGenerateEvents**](https://msdn.microsoft.com/library/windows/hardware/ff562541) or [**KsPinGenerateEvents**](https://msdn.microsoft.com/library/windows/hardware/ff563500).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Event%20Handling%20in%20AVStream%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


