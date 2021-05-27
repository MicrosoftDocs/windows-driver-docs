---
title: Storport Event Log Extensions
description: Storport Event Log Extensions
ms.date: 06/13/2019
ms.localizationpriority: medium
---

# Storport Event Log Extensions

Like many other types of drivers, Storport miniport drivers must create entries in the system event log to keep administrators informed of the condition of attached storage devices. These event log entries are often created in response to device-related failures. Events can also be logged for telemetry, debugging, and optimization.

Although the Windows kernel itself provides a flexible interface for creating event log entries, the Storport miniport model does not allow miniport drivers to access that interface directly. Instead, Storport provides a wrapper around the kernel's system event log facility, and miniport drivers use the wrapper to create event log entries.

Specifically, Storport provides the following event log routines:

* [**StorPortLogTelemetryEx**](/windows-hardware/drivers/ddi/storport/nf-storport-storportlogtelemetryex) allows a miniport to log a tracelogging measures or telemetry event with miniport-customized data (Windows 10 version 1903 and newer).
* [**StorPortEtwChannelEvent2**](/windows-hardware/drivers/ddi/storport/nf-storport-storportetwevent2), [**StorPortEtwChannelEvent4**](/windows-hardware/drivers/ddi/storport/nf-storport-storportetwevent4), and [**StorPortEtwChannelEvent8**](/windows-hardware/drivers/ddi/storport/nf-storport-storportetwevent8) allow miniports to publish ETW events to a storage trace channel (Windows 10 version 1809 and newer).
* [**StorPortLogSystemEvent**](/windows-hardware/drivers/ddi/storport/nf-storport-storportlogsystemevent) allows miniports to create an event log entry (Windows 7 and newer).

Storport logs events under the "**Microsoft-Windows-Storage-Storport**" provider name. Errors are logged in the **Operational** channel, and debug/analytics are logged in **Diagnose** (**Analytic** and **Debug**). When using the *Event Viewer* application, you must first enable the **Diagnose** channel to view it (to enable, click on *View->Show Analytic and Debug Logs*).

 The above functions are implemented as Storport extended functions and are available to miniport drivers using the existing extended function interface. Use of the extended function interface avoids a direct dynamic link reference to the new function. By avoiding that direct reference, miniport drivers that use the new function load properly on operating systems that do not support the function, with the function returning STOR_STATUS_NOT_IMPLEMENTED when not supported. In this way, vendors can create a single miniport driver that runs on multiple OS releases, taking advantage of the new event logging function where it is supported.

**Note:** In versions of Storport prior to Windows 7, Storport's system event log interface, [**StorPortLogError**](/windows-hardware/drivers/ddi/storport/nf-storport-storportlogerror), gave miniport drivers access to a small fraction of the capabilities of the kernel's system event log facility, which impacts the usefulness of miniport event log entries.

For general information about Windows events, see [Windows Events](/windows/desktop/Events/windows-events).
