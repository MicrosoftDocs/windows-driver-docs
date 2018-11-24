---
title: Sending an Event with WmiFireEvent
description: Sending an Event with WmiFireEvent
ms.assetid: f9cf8491-0f5a-4d83-849f-3edb77488092
keywords: ["WMI WDK kernel , event tracking", "events WDK WMI", "tracing WDK WMI", "sending WMI events", "event blocks WDK WMI", "notifications WDK WMI", "WmiFireEvent", "dynamic instance names WDK WMI"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Sending an Event with WmiFireEvent





A driver can call [**WmiFireEvent**](https://msdn.microsoft.com/library/windows/hardware/ff565807) to send events that do not use dynamic instance names, and that base static instance names on a single base name string or the device instance ID of a PDO.

The event must be a single instance of a block—that is, a driver cannot call **WmiFireEvent** to send an event that consists of a single item or multiple instances. To send such events, a driver must call [**IoWMIWriteEvent**](https://msdn.microsoft.com/library/windows/hardware/ff550520), as described in [Sending an Event with IoWMIWriteEvent](sending-an-event-with-iowmiwriteevent.md).

A driver should not send events until WMI has enabled the event. After the event has been enabled, when the event's trigger condition occurs, the driver:

1.  Allocates a buffer from the nonpaged pool and writes the event data to the buffer. If the event has no data, the driver can skip this step.

2.  Calls [**WmiFireEvent**](https://msdn.microsoft.com/library/windows/hardware/ff565807) with the following parameters:

    -   A pointer to the driver's device object

    -   A pointer to the GUID that represents the event block

    -   If the event block has multiple instances, the index of the instance

    -   If data is to be sent with the event, the number of bytes of data, or 0 if none

    -   If data is to be sent with the event, a pointer to the driver-allocated buffer that contains the data, or **NULL** if none

    The driver must allocate all parameters passed to **WmiFireEvent**, including the event data buffer, from nonpaged pool. WMI releases the driver-allocated memory without further intervention by the driver.

After **WmiFireEvent** returns, the driver resumes monitoring the event's trigger condition and sends the event each time its trigger condition occurs until WMI disables that event.

 

 




