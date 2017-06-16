---
title: Sending an Event with WmiFireEvent
author: windows-driver-content
description: Sending an Event with WmiFireEvent
ms.assetid: f9cf8491-0f5a-4d83-849f-3edb77488092
keywords: ["WMI WDK kernel , event tracking", "events WDK WMI", "tracing WDK WMI", "sending WMI events", "event blocks WDK WMI", "notifications WDK WMI", "WmiFireEvent", "dynamic instance names WDK WMI"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Sending an Event with WmiFireEvent


## <a href="" id="ddk-sending-an-event-with-wmifireevent-kg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Sending%20an%20Event%20with%20WmiFireEvent%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


