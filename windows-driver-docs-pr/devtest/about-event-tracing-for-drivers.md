---
title: About Event Tracing for Drivers
description: About Event Tracing for Drivers
ms.assetid: 1b5c85b1-5b7a-48bc-bdd4-356316d4467f
keywords:
- Event Tracing for Windows WDK , about Event Tracing for Windows
- ETW WDK , about Event Tracing for Windows
- Event Tracing for Windows WDK , kernel-mode
- ETW WDK , kernel-mode
- kernel-mode ETW WDK software tracing
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# About Event Tracing for Drivers


### <span id="what_is_event_tracing_"></span><span id="WHAT_IS_EVENT_TRACING_"></span>What is Event Tracing?

Event Tracing for Windows (ETW) is an efficient and effective mechanism for tracing and logging events that are raised by user-mode applications and kernel-mode drivers. ETW consists of three components:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Term</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><span id="Providers"></span><span id="providers"></span><span id="PROVIDERS"></span>Providers</p></td>
<td align="left"><p>Applications or components that raise event tracing instrumentation.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Controllers"></span><span id="controllers"></span><span id="CONTROLLERS"></span>Controllers</p></td>
<td align="left"><p>Applications that start, stop, and configure event tracing sessions.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Consumers"></span><span id="consumers"></span><span id="CONSUMERS"></span>Consumers</p></td>
<td align="left"><p>Applications that receive event tracing sessions (in real time) or from a file.</p></td>
</tr>
</tbody>
</table>

 

### <span id="the_etw_kernel_mode_api"></span><span id="THE_ETW_KERNEL_MODE_API"></span>The ETW Kernel-Mode API

The ETW application programming interface (API) provides a set of functions that are available to kernel-mode components and drivers. Support for Event Tracing was first introduced in Windows 2000. [WMI Event Tracing](https://msdn.microsoft.com/library/windows/hardware/ff566350) and [WPP Software Tracing](wpp-software-tracing.md) both use ETW. To unify and simplify the event and logging model, a new API was introduced in Windows Vista. Driver developers can use these functions to register the driver as an ETW provider. ETW providers can raise events and can publish them to the Windows Event Log or can write their events to an ETW session, which gets written to a trace file or delivered to real-time consumer. Events are entities that describe interesting occurrences within the system and are defined by a set of attributes that are determined by the ETW providers.

ETW is implemented in the Windows operating system and provides developers a fast, reliable, and versatile set of event tracing features with very little impact on performance. You can dynamically enable or disable tracing without rebooting your computer, or reloading your application or driver. Unlike debugging statements that you add to your code during development, you can use ETW in your production code.

### <span id="when_to_use_event_tracing"></span><span id="WHEN_TO_USE_EVENT_TRACING"></span>When to Use Event Tracing

The ETW kernel-mode API was introduced with Windows Vista and is not supported in earlier operating systems. Use the ETW kernel-mode API if you want to publish events that can be consumed by applications interested in administrative, operational and analytical events, in addition to the detailed tracing you might require during development. Use WPP Software Tracing if you are interested in primarily collecting trace data for development and debugging purposes and your driver needs to support this capability in Windows 2000 and later.

 

 





