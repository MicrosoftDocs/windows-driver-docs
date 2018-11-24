---
title: Introduction to WHEA-Aware User-Mode Applications
description: Introduction to WHEA-Aware User-Mode Applications
ms.assetid: cf2de8fa-191b-4dae-aaac-5d6d74f94ca7
keywords:
- Windows Hardware Error Architecture WDK , user-mode applications
- WHEA WDK , user-mode applications
- hardware errors WDK WHEA , user-mode applications
- errors WDK WHEA , user-mode applications
- user-mode applications WDK WHEA
- events WDK WHEA
- events WDK WHEA , categories
- Windows Hardware Error Architecture WDK , events
- WHEA WDK , events
- hardware errors WDK WHEA , events
- errors WDK WHEA , events
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




