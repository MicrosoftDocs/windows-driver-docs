---
title: Sending an Event with IoWMIWriteEvent
author: windows-driver-content
description: Sending an Event with IoWMIWriteEvent
MS-HAID:
- 'WMI\_1ec9f117-31d5-43d8-812b-aacc5bca9180.xml'
- 'kernel.sending\_an\_event\_with\_iowmiwriteevent'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 77c1041a-340c-4c59-a30a-e946adf60a95
keywords: ["WMI WDK kernel , event tracking", "events WDK WMI", "tracing WDK WMI", "sending WMI events", "event blocks WDK WMI", "notifications WDK WMI", "IoWMIWriteEvent", "dynamic instance names WDK WMI"]
---

# Sending an Event with IoWMIWriteEvent


## <a href="" id="ddk-sending-an-event-with-iowmiwriteevent-kg"></a>


A driver can call [**IoWMIWriteEvent**](https://msdn.microsoft.com/library/windows/hardware/ff550520) to send any event. The event can consist of a single item, a single instance, or all instances of a data block, and it can use dynamic instance names.

Unlike **WNODE\_*XXX*** structures passed with query or change requests, which are allocated and partially initialized by WMI, the driver must allocate and initialize all members of the **WNODE\_*XXX*** structure that contains an event.

A driver must send an event only after WMI has sent an [**IRP\_MN\_ENABLE\_EVENTS**](https://msdn.microsoft.com/library/windows/hardware/ff550859) request to enable the event. Then, when the event's trigger condition occurs, the driver:

1.  Allocates a buffer from nonpaged pool to contain the **WNODE\_*XXX*** structure needed for the event, including space for variable data, if any.

    Depending on the event, the driver might allocate a [**WNODE\_SINGLE\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff566378), a [**WNODE\_SINGLE\_INSTANCE**](https://msdn.microsoft.com/library/windows/hardware/ff566377), or a [**WNODE\_ALL\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff566372) for the event. The size of the **WNODE\_*XXX*** plus variable data must not exceed the registry-defined limit of 1K.

2.  Initializes all members of the **WNODE\_*XXX*** structure, including **WnodeHeader.Flags**:

    -   The driver sets the **WNODE\_FLAG\_EVENT\_ITEM** flag to indicate that the structure is an event.

    -   The driver sets one of the following flags to indicate the type of **WNODE\_*XXX*** structure:

        **WNODE\_FLAG\_ALL\_DATA**

        **WNODE\_FLAG\_SINGLE\_INSTANCE**

        **WNODE\_FLAG\_SINGLE\_ITEM**

    -   The driver sets or clears the following flags to indicate whether the block uses static or dynamic instance names:

        **WNODE\_FLAG\_STATIC\_INSTANCE\_NAMES**

        **WNODE\_FLAG\_PDO\_INSTANCE\_NAMES**

    -   The driver might set additional flags depending on the event.

3.  Casts a pointer to the **WNODE\_*XXX*** to a PWNODE\_EVENT\_ITEM.

4.  Calls **IoWMIWriteEvent** with the pointer.

    If **IoWMIWriteEvent** completes successfully, WMI releases the driver-allocated memory for the event.

After [**IoWMIWriteEvent**](https://msdn.microsoft.com/library/windows/hardware/ff550520) returns, the driver resumes monitoring the event's trigger condition and sending the event each time its trigger condition occurs, until WMI sends an [**IRP\_MN\_DISABLE\_EVENTS**](https://msdn.microsoft.com/library/windows/hardware/ff550851) request to disable that event.

If the size of an event exceeds the registry-defined maximum of 1K (not recommended) the driver should call **IoWmiWriteEvent** with an initialized [**WNODE\_EVENT\_REFERENCE**](https://msdn.microsoft.com/library/windows/hardware/ff566374) that specifies the event's GUID, its size, and its instance index (for static instance names) or name (for dynamic instance names). WMI will use the information in the **WNODE\_EVENT\_REFERENCE** to query for the event.

A driver can send an events that does not use dynamic instance names and that consists of a single instance by calling the WMI library routine [**WmiFireEvent**](https://msdn.microsoft.com/library/windows/hardware/ff565807). The driver does not need to allocate and initialize a **WNODE\_*XXX*** structure for a **WmiFireEvent** call. WMI packages the driver's event data in a [**WNODE\_SINGLE\_INSTANCE**](https://msdn.microsoft.com/library/windows/hardware/ff566377) and delivers it to data consumers. For more information about sending events with **WmiFireEvent**, see [Sending an Event with WmiFireEvent](sending-an-event-with-wmifireevent.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Sending%20an%20Event%20with%20IoWMIWriteEvent%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


