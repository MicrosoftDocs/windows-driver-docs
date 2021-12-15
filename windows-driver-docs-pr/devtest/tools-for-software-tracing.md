---
title: Tools for Software Tracing
description: The WDK includes tools that are designed to support Event Tracing for Windows (ETW) and to supplement the tracing tools that are included in Windows.
keywords:
- tools WDK , software tracing
- driver development tools WDK , software tracing
- software tracing WDK
- tracing WDK
- tracing WDK , about software tracing
- event tracing WDK
- trace tools WDK
ms.date: 04/20/2017
---

# Tools for Software Tracing


The Microsoft Windows Driver Kit (WDK) includes a set of applications and command-line tools for software tracing. These tools are designed to support Event Tracing for Windows (ETW) and to supplement the tracing tools that are included in Windows.

- [What are the tracing tools?](#what-are-the-tracing-tools)
- [When should I use WPP Software Tracing or the Event Tracing for Windows (ETW) API?](#when-should-i-use-wpp-software-tracing-or-the-event-tracing-for-windows-etw-api)
- [What's in this section](#whats-in-this-section)

## What are the tracing tools?

The tools include [trace controllers](trace-controller.md) that configure, start, update, and stop trace sessions, and [trace consumers](trace-consumer.md) that receive trace messages generated during the sessions and convert the binary data into human-readable format for files or display.

The tools support a variety of [trace providers](trace-provider.md), including user-mode applications and kernel-mode drivers, which are instrumented for software tracing by using [WPP software tracing](wpp-software-tracing.md) or ([Event Tracing for Windows (ETW)](event-tracing-for-windows--etw-.md). For a comparison of the two approaches to instrumenting your code, see [When to Use WPP Software Tracing and Event Tracing for Windows (ETW)](#when-should-i-use-wpp-software-tracing-or-the-event-tracing-for-windows-etw-api).

The tools also can access reserved [trace sessions](trace-session.md) that are built into Windows, such as the [Global Logger trace session](global-logger-trace-session.md) / [NT Kernel Logger trace session](nt-kernel-logger-trace-session.md).

Some of these tools are located in the tools\\&lt;*Platform*&gt; subdirectory of the Windows Driver Kit (WDK), where &lt;*Platform*&gt; is either x86 or x64. Other tools are either included with Windows or are located in the bin\\&lt;*Platform*&gt; subdirectory of the WDK.

## When should I use WPP Software Tracing or the Event Tracing for Windows (ETW) API?

Use [WPP Software Tracing](wpp-software-tracing.md) if you are interested in primarily collecting trace data for development and debugging purposes. Use [Event Tracing for Windows (ETW)](event-tracing-for-windows--etw-.md) for other types of tracing.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">WPP software tracing</th>
<th align="left">Manifested/TraceLogging ETW</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">Supported on Windows 2000 and later.</td>
<td align="left">Supported on Windows Vista and later.</td>
</tr>
<tr class="even">
<td align="left">Tracing events for development and debugging. Mostly internal developer focused.</td>
<td align="left">Tracing events for administrative, operational, analytical and debugging purposes.</td>
</tr>
<tr class="even">
<td align="left">Needs TMF files to decode the events, which are extracted from the logging binary's PDB.</td>
<td align="left">The metadata to decode the events is contained in a local binary or in the event payload.</td>
</tr>
<tr class="odd">
<td align="left">Can be only one active session per trace provider.</td>
<td align="left">Events can be multiplexed to multiple consumers.</td>
</tr>
<tr class="even">
<td align="left">Message strings cannot be localized.</td>
<td align="left">Strings can be localized.</td>
</tr>
<tr class="odd">
<td align="left">Provider security is limited to not sharing the control GUID or TMF files required to enable and decode the events, respectively.</td>
<td align="left">Provider can have ACLs applied to restrict which users can collect events from it.</td>
</tr>
</tbody>
</table> 

For information about using Windows software trace preprocessor (WPP) macros to add software tracing to a driver or application, see [WPP Software Tracing](wpp-software-tracing.md).

For information about the using the kernel-mode ETW API for drivers, see [Event Tracing for Windows (ETW)](event-tracing-for-windows--etw-.md).

For information about using the Windows Management Instrumentation (WMI) extensions to the Windows Driver Model (WDM) to add software tracing to any driver, see [WMI Event Tracing](../kernel/wmi-event-tracing.md).

**Note**   ETW and WPP support most types of kernel-mode drivers and user-mode applications. However, ETW and WPP use types that are not available for certain types of drivers, such as miniport drivers. To determine whether a particular driver type is supported, add basic WPP macros to the driver, such as [WPP\_INIT\_TRACING](/previous-versions/windows/hardware/previsioning-framework/ff556191(v=vs.85)) and [WPP\_CLEANUP](/previous-versions/windows/hardware/previsioning-framework/ff556179(v=vs.85)). If the code does not compile because the types that are used are not defined, then ETW and WPP cannot support the driver type. 

## What's in this section

This section begins with a survey of software tracing tools, discusses the concepts underlying the tools, and then includes documentation of the software tracing tools in the WDK.

This section includes:

[Survey of Software Tracing Tools](survey-of-software-tracing-tools.md)

[Tracing Tool Concepts](tracing-tool-concepts.md)

[TraceView](traceview.md)

[Tracelog](tracelog.md)

[Tracepdb](tracepdb.md)

[Tracefmt](tracefmt.md)

[Tracing During Boot](tracing-during-boot.md)

[WPP Software Tracing](wpp-software-tracing.md)

[Software Tracing FAQ](software-tracing-faq.md)

[Event Tracing for Windows (ETW)](event-tracing-for-windows--etw-.md)

[Kernel Mode Performance Monitoring](kernel-mode-performance-monitoring.md)

For conceptual information [About Event Tracing](/windows/desktop/ETW/about-event-tracing), see the Microsoft Windows SDK documentation. 
