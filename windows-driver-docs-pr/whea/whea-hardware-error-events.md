---
title: WHEA Hardware Error Events
description: WHEA Hardware Error Events
ms.assetid: c9f88e3b-3915-4a77-8d60-f0f3da514abc
keywords:
- events WDK WHEA , about events
- Windows Hardware Error Architecture WDK , events
- WHEA WDK , events
- hardware errors WDK WHEA , events
- errors WDK WHEA , events
- hardware error events WDK WHEA
- events WDK WHEA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WHEA Hardware Error Events


The Windows Hardware Error Architecture (WHEA) raises an Event Tracing for Windows (ETW) event whenever a hardware error occurs. These hardware error events are recorded in the system event log. For descriptions of the various hardware error events that can be raised by WHEA, see [Hardware Error Events](https://msdn.microsoft.com/library/windows/hardware/ff559387).

An application can retrieve hardware error events from the system event log by querying for any events that were logged by WHEA. For examples of how to retrieve WHEA hardware error events from the system event log, see [Querying the System Event Log for Hardware Error Events](querying-the-system-event-log-for-hardware-error-events.md).

An application can also register to be notified whenever new hardware error events are raised by WHEA. For examples of how to register for the notification of new hardware error events, see [Registering for Notification of Hardware Error Events](registering-for-notification-of-hardware-error-events.md).

Regardless of whether a particular hardware error event was obtained by querying the system event log or by receiving an event notification, the process of retrieving the hardware error data from the event is the same.

Each hardware error event contains an [error record](error-records.md) that describes the error condition that occurred. The error record can be retrieved from each event for further analysis.

 

 




