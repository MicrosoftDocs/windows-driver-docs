---
title: WHEA Hardware Error Events
author: windows-driver-content
description: WHEA Hardware Error Events
MS-HAID:
- 'whea\_ef5bac2d-30d1-4434-b99e-abc4e9f39b02.xml'
- 'whea.whea\_hardware\_error\_events'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: c9f88e3b-3915-4a77-8d60-f0f3da514abc
keywords: ["events WDK WHEA , about events", "Windows Hardware Error Architecture WDK , events", "WHEA WDK , events", "hardware errors WDK WHEA , events", "errors WDK WHEA , events", "hardware error events WDK WHEA", "events WDK WHEA"]
---

# WHEA Hardware Error Events


The Windows Hardware Error Architecture (WHEA) raises an Event Tracing for Windows (ETW) event whenever a hardware error occurs. These hardware error events are recorded in the system event log. For descriptions of the various hardware error events that can be raised by WHEA, see [Hardware Error Events](https://msdn.microsoft.com/library/windows/hardware/ff559387).

An application can retrieve hardware error events from the system event log by querying for any events that were logged by WHEA. For examples of how to retrieve WHEA hardware error events from the system event log, see [Querying the System Event Log for Hardware Error Events](querying-the-system-event-log-for-hardware-error-events.md).

An application can also register to be notified whenever new hardware error events are raised by WHEA. For examples of how to register for the notification of new hardware error events, see [Registering for Notification of Hardware Error Events](registering-for-notification-of-hardware-error-events.md).

Regardless of whether a particular hardware error event was obtained by querying the system event log or by receiving an event notification, the process of retrieving the hardware error data from the event is the same.

Each hardware error event contains an [error record](error-records.md) that describes the error condition that occurred. The error record can be retrieved from each event for further analysis.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwhea\whea%5D:%20WHEA%20Hardware%20Error%20Events%20%20RELEASE:%20%289/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


