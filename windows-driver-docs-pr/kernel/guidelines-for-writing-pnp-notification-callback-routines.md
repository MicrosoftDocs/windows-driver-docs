---
title: Guidelines for Writing PnP Notification Callback Routines
description: Guidelines for Writing PnP Notification Callback Routines
ms.assetid: 2153b4c2-f60f-4ac9-8eee-66c5f3a9f414
keywords: ["notifications WDK PnP , callback routines", "callback routines WDK PnP"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Guidelines for Writing PnP Notification Callback Routines





The PnP manager calls notification callback routines at IRQL = PASSIVE\_LEVEL.

To ensure smooth operation of the PnP subsystem, a PnP notification callback routine must follow these guidelines:

1.  A notification callback routine must not block.

2.  A notification callback routine must not call, or cause a call to, synchronous routines that generate PnP events or any routine that blocks waiting for device installation or removal.

    Calling such routines during a notification callback can cause a system deadlock.

    For example, a driver must not call [**IoReportTargetDeviceChange**](https://msdn.microsoft.com/library/windows/hardware/ff549625) in a notification callback routine. Call [**IoReportTargetDeviceChangeAsynchronous**](https://msdn.microsoft.com/library/windows/hardware/ff549634) instead.

3.  A notification callback routine should return success for any events it does not explicitly fail.

    When a driver registers for notification on an event category, the PnP manager notifies the driver of all events in that category, present and future. If a driver returns an error status for events it does not handle, the driver risks failing a new query event by mistake.

    A driver correctly returns an error status when, for example, the driver fails a query notification to veto the event being proposed.

4.  A notification callback routine should be paged code.

 

 




