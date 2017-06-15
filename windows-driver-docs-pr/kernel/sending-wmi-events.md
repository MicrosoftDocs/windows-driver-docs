---
title: Sending WMI Events
author: windows-driver-content
description: Sending WMI Events
MS-HAID:
- 'WMI\_ed60eb46-222f-4be1-8093-17886b03f16d.xml'
- 'kernel.sending\_wmi\_events'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 0d5e62f1-b84e-42b7-be40-8665f0b58ba8
keywords: ["WMI WDK kernel , event tracking", "events WDK WMI", "tracing WDK WMI", "sending WMI events", "event blocks WDK WMI", "notifications WDK WMI", "dynamic instance names WDK WMI"]
---

# Sending WMI Events


## <a href="" id="ddk-sending-wmi-events-kg"></a>


A driver can use WMI events to notify user-mode applications of events without requiring the applications to poll or send IRPs. A driver should use WMI events to notify WMI clients of exceptional conditions, not as an alternative to error logging. A driver should support any standard event blocks defined for its device type in Wmicore.mof, and might define and register additional custom event blocks to support device-specific notifications.

An event block is simply a data block that derives from the abstract base class **WMIEvent**. An event block can contain any of the same data as a data block, or it can be empty—that is, an event block need not contain any driver-defined data items. If an event block does contain data, the total size of the **WNODE\_*XXX*** plus the data should not exceed the registry-defined limit of 1 kilobyte. In general, smaller events result in better system performance and more timely notification. For information about defining blocks, see [MOF Syntax for WMI Data and Event Blocks](mof-syntax-for-wmi-data-and-event-blocks.md) and [Designing WMI Data and Event Blocks](designing-wmi-data-and-event-blocks.md).

A driver indicates support for an event by registering the corresponding event block with WMIREG\_FLAG\_EVENT\_ONLY\_GUID set in the block's [**WMIREGGUID**](https://msdn.microsoft.com/library/windows/hardware/ff565827) structure. For information about registering blocks, see [Registering as a WMI Data Provider](registering-as-a-wmi-data-provider.md).

When a WMI client user requests notification of an event, WMI sends an [**IRP\_MN\_ENABLE\_EVENTS**](https://msdn.microsoft.com/library/windows/hardware/ff550859) request to the driver, which alerts the driver to begin monitoring the event's driver-determined trigger condition. Then, when the trigger condition occurs, the driver sends the event to WMI, which delivers it to all data consumers that have registered for the event.

A driver sends an event to WMI in one of the following ways:

-   Call the kernel-mode WMI library routine [**WmiFireEvent**](https://msdn.microsoft.com/library/windows/hardware/ff565807). A driver can call **WmiFireEvent** to send only events that do not use dynamic instance names, and that base static instance names on a single base name string or the device instance ID of a PDO. Furthermore, the event must be a single instance—that is, a driver cannot call **WmiFireEvent** to send an event that consists of a single item or multiple instances. For more information, see [Sending an Event with WmiFireEvent](sending-an-event-with-wmifireevent.md).

-   Call the kernel-mode routine [**IoWMIWriteEvent**](https://msdn.microsoft.com/library/windows/hardware/ff550520) with a pointer to a driver-allocated and initialized **WNODE\_*XXX*** structure that contains the event's data. For more information, see [Sending an Event with IoWMIWriteEvent](sending-an-event-with-iowmiwriteevent.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Sending%20WMI%20Events%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


