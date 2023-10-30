---
title: Command processing and event reporting
description: Command processing and event reporting
ms.date: 03/29/2023
---

# Command processing and event reporting

WIA minidrivers can support command requests originating from a WIA application, or directly from the WIA service. Further, some still image devices have the ability to send notifications to the driver as a result of a user action. For example, a scanner with one or more front panel buttons can notify the driver when the user presses one of those buttons. This ability enables the driver to take some action. When the driver notifies the WIA service that a particular button has been pressed, the WIA service can launch a previously registered application to handle the event.

This section contains the following topics:

[Command handling](command-handling.md)

[Event reporting](event-reporting.md)
