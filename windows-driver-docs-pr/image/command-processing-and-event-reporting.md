---
title: Command Processing and Event Reporting
description: Command Processing and Event Reporting
ms.assetid: f51c082d-1be5-4f34-b7a6-82235e8c14f4
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Command Processing and Event Reporting





WIA minidrivers can support command requests originating from a WIA application, or directly from the WIA service. Further, some still image devices have the ability to send notifications to the driver as a result of a user action. For example, a scanner with one or more front panel buttons can notify the driver when the user presses one of those buttons. This ability enables the driver to take some action. When the driver notifies the WIA service that a particular button has been pressed, the WIA service can launch a previously registered application to handle the event.

This section contains the following topics:

[Command Handling](command-handling.md)

[Event Reporting](event-reporting.md)

 

 




