---
title: Sending an Event with IoWMIWriteEvent
description: Sending an Event with IoWMIWriteEvent
ms.assetid: 77c1041a-340c-4c59-a30a-e946adf60a95
keywords: ["WMI WDK kernel , event tracking", "events WDK WMI", "tracing WDK WMI", "sending WMI events", "event blocks WDK WMI", "notifications WDK WMI", "IoWMIWriteEvent", "dynamic instance names WDK WMI"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Sending an Event with IoWMIWriteEvent





A driver can call [**IoWMIWriteEvent**](https://msdn.microsoft.com/library/windows/hardware/ff550520) to send any event. The event can consist of a single item, a single instance, or all instances of a data block, and it can use dynamic instance names.

Unlike **WNODE\_*XXX*** structures passed with query or change requests, which are allocated and partially initialized by WMI, the driver must allocate and initialize all members of the **WNODE\_*XXX*** structure that contains an event.

A driver must send an event only after WMI has sent an [**IRP\_MN\_ENABLE\_EVENTS**](https://msdn.microsoft.com/library/windows/hardware/ff550859) request to enable the event. Then, when the event's trigger condition occurs, the driver:

1. Allocates a buffer from nonpaged pool to contain the **WNODE\_*XXX*** structure needed for the event, including space for variable data, if any.

   Depending on the event, the driver might allocate a [**WNODE\_SINGLE\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff566378), a [**WNODE\_SINGLE\_INSTANCE**](https://msdn.microsoft.com/library/windows/hardware/ff566377), or a [**WNODE\_ALL\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff566372) for the event. The size of the **WNODE\_*XXX*** plus variable data must not exceed the registry-defined limit of 1K.

2. Initializes all members of the **WNODE\_*XXX*** structure, including **WnodeHeader.Flags**:

   - The driver sets the **WNODE\_FLAG\_EVENT\_ITEM** flag to indicate that the structure is an event.

   - The driver sets one of the following flags to indicate the type of **WNODE\_*XXX*** structure:

     **WNODE\_FLAG\_ALL\_DATA**

     **WNODE\_FLAG\_SINGLE\_INSTANCE**

     **WNODE\_FLAG\_SINGLE\_ITEM**

   - The driver sets or clears the following flags to indicate whether the block uses static or dynamic instance names:

     **WNODE\_FLAG\_STATIC\_INSTANCE\_NAMES**

     **WNODE\_FLAG\_PDO\_INSTANCE\_NAMES**

   - The driver might set additional flags depending on the event.

3. Casts a pointer to the **WNODE\_*XXX*** to a PWNODE\_EVENT\_ITEM.

4. Calls **IoWMIWriteEvent** with the pointer.

   If **IoWMIWriteEvent** completes successfully, WMI releases the driver-allocated memory for the event.

After [**IoWMIWriteEvent**](https://msdn.microsoft.com/library/windows/hardware/ff550520) returns, the driver resumes monitoring the event's trigger condition and sending the event each time its trigger condition occurs, until WMI sends an [**IRP\_MN\_DISABLE\_EVENTS**](https://msdn.microsoft.com/library/windows/hardware/ff550851) request to disable that event.

If the size of an event exceeds the registry-defined maximum of 1K (not recommended) the driver should call **IoWmiWriteEvent** with an initialized [**WNODE\_EVENT\_REFERENCE**](https://msdn.microsoft.com/library/windows/hardware/ff566374) that specifies the event's GUID, its size, and its instance index (for static instance names) or name (for dynamic instance names). WMI will use the information in the **WNODE\_EVENT\_REFERENCE** to query for the event.

A driver can send an events that does not use dynamic instance names and that consists of a single instance by calling the WMI library routine [**WmiFireEvent**](https://msdn.microsoft.com/library/windows/hardware/ff565807). The driver does not need to allocate and initialize a **WNODE\_*XXX*** structure for a **WmiFireEvent** call. WMI packages the driver's event data in a [**WNODE\_SINGLE\_INSTANCE**](https://msdn.microsoft.com/library/windows/hardware/ff566377) and delivers it to data consumers. For more information about sending events with **WmiFireEvent**, see [Sending an Event with WmiFireEvent](sending-an-event-with-wmifireevent.md).

 

 




