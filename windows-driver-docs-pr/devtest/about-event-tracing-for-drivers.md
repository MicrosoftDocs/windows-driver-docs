---
title: About Event Tracing for Drivers
description: About Event Tracing for Drivers
ms.assetid: 1b5c85b1-5b7a-48bc-bdd4-356316d4467f
keywords: ["Event Tracing for Windows WDK , about Event Tracing for Windows", "ETW WDK , about Event Tracing for Windows", "Event Tracing for Windows WDK , kernel-mode", "ETW WDK , kernel-mode", "kernel-mode ETW WDK software tracing"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20About%20Event%20Tracing%20for%20Drivers%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




