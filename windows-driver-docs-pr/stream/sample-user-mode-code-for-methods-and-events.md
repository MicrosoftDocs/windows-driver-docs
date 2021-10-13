---
title: Sample User-Mode Code for Methods and Events
description: Sample User-Mode Code for Methods and Events
keywords:
- events WDK AVStream
- AVStream events WDK
- user-mode KsProxy plug-in sample WDK AVStream
- methods WDK AVStream
- automation tables WDK AVStream
- notifications WDK AVStream
- KsProxy plug-in sample WDK AVStream
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Sample User-Mode Code for Methods and Events


The code in this section shows how you can use methods and events from a user-mode KsProxy plug-in.

To learn how to support properties, methods, and events in your kernel-mode minidriver, see [Defining Automation Tables](defining-automation-tables.md).

After you have provided a minidriver that supports a given method, you can invoke that method by calling [**IKsControl::KsMethod**](/windows-hardware/drivers/ddi/ksproxy/nf-ksproxy-ikscontrol-ksmethod) from a user-mode plug-in, as shown in the following code example.

```cpp
PVOID MethodBuffer; // Your method arguments buffer
ULONG MethodBufferSize; // Your method buffer size

KSMETHOD Method;
ULONG BytesReturned;

Method.Set = KSMETHODSETID_MyMethodSet;
Method.Id = KSMETHOD_MyMethodId;
Method.Flags = KSMETHOD_TYPE_SEND;

HRESULT hr = 
pIKsControl -> KsMethod (
    &Method,
        sizeof (Method),
    MethodBuffer,
    &MethodBufferSize,
    &BytesReturned);
```

In the automation tables you provide in kernel mode, you can use the **Flags** member of [**KSMETHOD\_ITEM**](/windows-hardware/drivers/ddi/ks/ns-ks-ksmethod_item) to specify whether the buffer is read/write and whether it should be mapped or copied.

To register for an event that you support in your minidriver, use the following user-mode code example.

```cpp
HANDLE EventHandle; // Your event handle.

KSEVENT Event;
KSEVENTDATA EventData;

Event.Set = KSEVENTSETID_MyEventSet;
Event.Id = KSEVENT_MyEventId;
Event.Flags = KSEVENT_TYPE_ENABLE;

EventData.NotificationType = KSEVENTF_EVENT_HANDLE;
EventData.EventHandle.Event = EventHandle;
EventData.EventHandle.Reserved [0] = 0;
EventData.EventHandle.Reserved [1] = 0;

ULONG BytesReturned;

HRESULT hr =
pIKsControl -> KsEvent (
    &Event,
        sizeof (Event),
    &EventData,
        sizeof (EventData),
    &BytesReturned);
```

In the above example, notification continues until the minidriver disables the event. To disable the event. call [**IKsControl::KsEvent**](/windows-hardware/drivers/ddi/ksproxy/nf-ksproxy-ikscontrol-ksevent). If you want to be notified only the first time this event happens, set KSEVENT\_TYPE\_ONESHOT in **Event.Flags**.

If you are supporting events with USB Video Class Extension Units, see [Supporting Autoupdate Events with Extension Units](supporting-autoupdate-events-with-extension-units.md).

 

