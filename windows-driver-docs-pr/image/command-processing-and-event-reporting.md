---
title: Command Processing and Event Reporting
author: windows-driver-content
description: Command Processing and Event Reporting
ms.assetid: f51c082d-1be5-4f34-b7a6-82235e8c14f4
---

# Command Processing and Event Reporting


## <a href="" id="ddk-command-processing-and-event-reporting-si"></a>


WIA minidrivers can support command requests originating from a WIA application, or directly from the WIA service. Further, some still image devices have the ability to send notifications to the driver as a result of a user action. For example, a scanner with one or more front panel buttons can notify the driver when the user presses one of those buttons. This ability enables the driver to take some action. When the driver notifies the WIA service that a particular button has been pressed, the WIA service can launch a previously registered application to handle the event.

This section contains the following topics:

[Command Handling](command-handling.md)

[Event Reporting](event-reporting.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Command%20Processing%20and%20Event%20Reporting%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


