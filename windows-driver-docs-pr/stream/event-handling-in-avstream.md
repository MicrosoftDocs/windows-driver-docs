---
title: Event Handling in AVStream
description: Event Handling in AVStream
ms.assetid: 7add2055-8d3f-432d-8aa1-44459ac197dd
keywords:
- events WDK AVStream
- AVStream events WDK
- automation tables WDK AVStream
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Event Handling in AVStream





AVStream filters and pins describe properties, events, and methods that they support by supplying a [**KSAUTOMATION\_TABLE**](https://msdn.microsoft.com/library/windows/hardware/ff560990) structure in the **AutomationTable** member of either a [**KSFILTER\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff562553) structure or a [**KSPIN\_DESCRIPTOR\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff563534) structure. For more information, see [AVStream Descriptors](avstream-descriptors.md).

To support events, an AVStream minidriver provides an array of [**KSEVENT\_SET**](https://msdn.microsoft.com/library/windows/hardware/ff561867) structures in an automation table. Each KSEVENT\_SET structure contains an array of [**KSEVENT\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff561862) structures. Each KSEVENT\_ITEM structure describes how the minidriver supports a specific event.

The minidriver can customize event behavior by supplying [*AVStrMiniAddEvent*](https://msdn.microsoft.com/library/windows/hardware/ff554260) and [*AVStrMiniRemoveEvent*](https://msdn.microsoft.com/library/windows/hardware/ff556361) handlers in the KSEVENT\_ITEM structures.

When AVStream receives an event enable request, it generates a KSEVENT\_ENTRY structure. If the minidriver has provided an *AVStrAddEvent* handler, AVStream passes a pointer to the KSEVENT\_ENTRY structure in the call to *AVStrAddEvent*.

If you do not provide an *AVStrAddEvent* handler, then by default AVStream adds the event to the object list. Your minidriver does not receive a [**KSEVENT\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/ff561853) pointer. Your minidriver can trigger the event by calling [**KsFilterGenerateEvents**](https://msdn.microsoft.com/library/windows/hardware/ff562541) or [**KsPinGenerateEvents**](https://msdn.microsoft.com/library/windows/hardware/ff563500).

 

 




