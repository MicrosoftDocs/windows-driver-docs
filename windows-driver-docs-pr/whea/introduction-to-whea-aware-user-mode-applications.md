---
title: Introduction to WHEA-Aware User-Mode Applications
author: windows-driver-content
description: Introduction to WHEA-Aware User-Mode Applications
ms.assetid: cf2de8fa-191b-4dae-aaac-5d6d74f94ca7
keywords: ["Windows Hardware Error Architecture WDK , user-mode applications", "WHEA WDK , user-mode applications", "hardware errors WDK WHEA , user-mode applications", "errors WDK WHEA , user-mode applications", "user-mode applications WDK WHEA", "events WDK WHEA", "events WDK WHEA , categories", "Windows Hardware Error Architecture WDK , events", "WHEA WDK , events", "hardware errors WDK WHEA , events", "errors WDK WHEA , events"]
---

# Introduction to WHEA-Aware User-Mode Applications


The Windows Hardware Error Architecture (WHEA) provides mechanisms for user-mode applications to process WHEA hardware error events and to perform WHEA management operations.

The processing of WHEA hardware error events falls into two categories:

<a href="" id="event-log-processing"></a>*Event log processing*  
Querying the system event log to retrieve and process past WHEA hardware error events.

<a href="" id="event-notification"></a>*Event notification*  
Registering for notification of WHEA hardware error events to process new events as they occur.

WHEA management operations include actions such as enabling or disabling an error source and injecting hardware errors for testing purposes.

A single user-mode application can use any combination of the event processing and management mechanisms.

WHEA hardware error event processing applications are supported starting with Windows Vista. For more information about how to implement a user-mode application that processes WHEA hardware error events, see [WHEA Hardware Error Event Processing Applications](whea-hardware-error-event-processing-applications.md).

WHEA management applications are supported in Windows Server 2008, Windows Vista SP1 and later versions of Windows For more information about how to implement a user-mode application that performs WHEA management operations, see [WHEA Management Applications](whea-management-applications.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwhea\whea%5D:%20Introduction%20to%20WHEA-Aware%20User-Mode%20Applications%20%20RELEASE:%20%289/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


