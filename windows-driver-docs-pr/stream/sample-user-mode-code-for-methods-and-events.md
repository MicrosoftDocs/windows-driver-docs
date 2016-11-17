---
title: Sample User-Mode Code for Methods and Events
author: windows-driver-content
description: Sample User-Mode Code for Methods and Events
MS-HAID:
- 'avsover\_5e27cc99-0dca-497c-a539-6f188d46374f.xml'
- 'stream.sample\_user\_mode\_code\_for\_methods\_and\_events'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 0d564eb7-8e81-43bd-b539-f1240b3a21de
keywords: ["events WDK AVStream", "AVStream events WDK", "user-mode KsProxy plug-in sample WDK AVStream", "methods WDK AVStream", "automation tables WDK AVStream", "notifications WDK AVStream", "KsProxy plug-in sample WDK AVStream"]
---

# Sample User-Mode Code for Methods and Events


The code in this section shows how you can use methods and events from a user-mode KsProxy plug-in.

To learn how to support properties, methods, and events in your kernel-mode minidriver, see [Defining Automation Tables](defining-automation-tables.md).

After you have provided a minidriver that supports a given method, you can invoke that method by calling [**IKsControl::KsMethod**](https://msdn.microsoft.com/library/windows/hardware/ff559785) from a user-mode plug-in, as shown in the following code example.

```
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

In the automation tables you provide in kernel mode, you can use the **Flags** member of [**KSMETHOD\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff563420) to specify whether the buffer is read/write and whether it should be mapped or copied.

To register for an event that you support in your minidriver, use the following user-mode code example.

```
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

In the above example, notification continues until the minidriver disables the event. To disable the event. call [**IKsControl::KsEvent**](https://msdn.microsoft.com/library/windows/hardware/ff559772). If you want to be notified only the first time this event happens, set KSEVENT\_TYPE\_ONESHOT in **Event.Flags**.

If you are supporting events with USB Video Class Extension Units, see [Supporting Autoupdate Events with Extension Units](supporting-autoupdate-events-with-extension-units.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Sample%20User-Mode%20Code%20for%20Methods%20and%20Events%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


