---
title: KS Events
description: KS Events
keywords:
- kernel streaming WDK , events
- KS WDK , events
- events WDK kernel streaming
- event sets WDK kernel streaming
ms.date: 04/20/2017
---

# KS Events





If you are writing an AVStream minidriver, see [Event Handling in AVStream](event-handling-in-avstream.md).

Event sets are groups of related events for which a listener can request notification. For example, a listener could register to be notified of device state changes, or changes in stream position. When an event occurs, kernel streaming notifies any clients that have registered for this event.

Minidrivers describe how they support an event by providing a [**KSEVENT\_ITEM**](/windows-hardware/drivers/ddi/ks/ns-ks-ksevent_item) structure that contains pointers to handling routines.

Listeners register for notification by calling the kernel streaming proxy routine [**KsSynchronousDeviceControl**](/windows-hardware/drivers/ddi/ksproxy/nf-ksproxy-kssynchronousdevicecontrol) with the IOCTL\_KS\_ENABLE\_EVENT control code and pointers to [**KSEVENT**](./ksevent-structure.md) and [**KSEVENTDATA**](/windows-hardware/drivers/ddi/ks/ns-ks-kseventdata).structures.

The IOCTL\_KS\_DISABLE\_EVENT request disables a specified event. The same pointer that was used to enable the event must be used to disable it. This pointer uniquely identifies the event. Optionally, the client may specify a **NULL** pointer and length of zero to disable all active events for the client.

All event sets must support the KSEVENT\_TYPE\_BASICSUPPORT flag. Refer to [**KSEVENT**](./ksevent-structure.md) for a list of available event flags.

Some event types require additional parameters to register for event notification. For example, the [**KSEVENT\_CLOCK\_POSITION\_MARK**](./ksevent-clock-position-mark.md) event on a clock is triggered when the clock reaches a certain time stamp. Consequently, clients that register to be notified of this event must specify the time stamp at which to trigger the event.

In such a case, a minidriver passes additional data parameters in the data buffer after the [**KSEVENTDATA**](/windows-hardware/drivers/ddi/ks/ns-ks-kseventdata) structure. Minidrivers that support such an event type use an extended data structure, of which the first member is of type KSEVENTDATA, to hold the notification data.

