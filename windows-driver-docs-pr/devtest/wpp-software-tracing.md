---
title: WPP Software Tracing
description: This section describes how to use the Windows software trace preprocessor (WPP) to trace the operation of a software component trace provider.
ms.assetid: dab776b3-bac9-4157-a530-6e48868ba900
keywords:
- Windows software trace preprocessor WDK
- WPP software tracing WDK
- software tracing WDK , WPP
- kernel-mode WPP WDK software tracing
- Windows software trace preprocessor WDK , about WPP
- WPP software tracing WDK , about WPP
- default WPP software tracing
- tracing WDK , WPP
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WPP Software Tracing


This section describes how to use the *Windows software trace preprocessor* (WPP) to trace the operation of a software component ([trace provider](trace-provider.md)). A trace provider can be one of the following:

-   A kernel-mode driver.

-   A user-mode driver, application, or dynamic-link library (DLL).

WPP software tracing supplements and enhances [WMI event tracing](https://msdn.microsoft.com/library/windows/hardware/ff566350) by adding ways to simplify tracing the operation of the trace provider. It is an efficient mechanism for the trace provider to log real-time binary messages. The logged messages can subsequently be converted to a human-readable trace of the operation of the trace provider.

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">When should you use WPP software tracing?</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>WPP software tracing is primarily intended for debugging code during development. If you want to publish events that can be consumed by applications interested in structured ETW events, in addition to tracing during development, use the following:</p>
<ul>
<li>For kernel-mode drivers, use the <a href="event-tracing-for-windows--etw-.md" data-raw-source="[Event Tracing for Windows (ETW)](event-tracing-for-windows--etw-.md)">Event Tracing for Windows (ETW)</a> API.</li>
<li>For user-mode drivers or applications, use the <a href="https://msdn.microsoft.com/library/windows/desktop/bb968803" data-raw-source="[Event Tracing](https://msdn.microsoft.com/library/windows/desktop/bb968803)">Event Tracing</a> (Windows Desktop) API.</li>
</ul>
For more information, see <a href="tools-for-software-tracing.md" data-raw-source="[When should I use WPP Software Tracing or the Event Tracing for Windows (ETW) API?](tools-for-software-tracing.md)">When should I use WPP Software Tracing or the Event Tracing for Windows (ETW) API?</a></td>
</tr>
</tbody>
</table>

 

Logging messages with WPP software tracing is similar to using Windows event logging services. The driver logs a message ID and unformatted binary data in a log file. Subsequently, a postprocessor converts the information in the log file to a human-readable form. However, WPP software tracing supports message formats that are more capable and flexible than that supported by the event logging services. For example, WPP software tracing has built-in support for IP addresses, GUIDs, system IDs, time stamps, and other useful data types. In addition, users can add custom data types relevant to their application.

WPP software tracing is supported on Microsoft Windows 2000 and later versions of Windows.

### An overview of the WPP software tracing process

The basic process for adding WPP software tracing to a driver or application, includes the following steps. If you use one of the Visual Studio templates provided in the WDK for creating a WDF driver, much of the work is done for you.

-   Define a control GUID that uniquely identifies the driver or application as a [trace provider](trace-provider.md). The provider specifies this GUID in its definition of the [WPP\_CONTROL\_GUIDS](https://msdn.microsoft.com/library/windows/hardware/ff556186) macro and in a related control file used by [Tracelog](tracelog.md) or another [Trace Controller](trace-controller.md).

-   Add the required WPP-related C preprocessor directives and WPP macro calls to the provider's source files, as described in [Adding WPP Software Tracing to a Windows Driver](adding-wpp-software-tracing-to-a-windows-driver.md) and in [WPP Software Tracing Reference](https://msdn.microsoft.com/library/windows/hardware/ff556205).

-   Modify the Visual Studio project to run the WPP preprocessor and build the driver, as described in [Step 6](adding-wpp-software-tracing-to-a-windows-driver.md#step-6-modify-the-visual-studio-project-to-run-the-wpp-preprocessor-and-build-the-solution) of Adding WPP Software Tracing to a Windows Driver. You can refer to the [WPP Preprocessor](wpp-preprocessor.md) for more build time options.

-   Install the driver or component. Start a trace session and record the trace messages. Use the tools for software tracing, such as [TraceView](traceview.md), [Tracelog](tracelog.md), [Tracefmt](tracefmt.md), and [Tracepdb](tracepdb.md) to configure, start, and stop tracing sessions and to display and filter trace messages. These tools are included in the Windows Driver Kit (WDK).

## In this section


-   [Adding WPP Software Tracing to a Windows Driver](adding-wpp-software-tracing-to-a-windows-driver.md)
-   [Inflight Trace Recorder for logging traces](using-wpp-recorder.md)
-   [Using WPP Software Tracing in a Trace Provider](using-wpp-software-tracing-in-a-trace-provider.md)
-   [Adding WPP Macros to a Trace Provider](adding-wpp-macros-to-a-trace-provider.md)
-   [WPP Preprocessor](wpp-preprocessor.md)
-   [Tracing and Diagnosability for WDF Drivers](tracing-and-diagnosability-for-wdf-drivers.md)

**Note**   Event Tracing for Windows (ETW) and WPP support most types of kernel-mode and user-mode drivers. However, ETW and WPP use types that are not available for certain types of drivers, such as miniport drivers. To determine whether a particular driver type is supported, add basic WPP macros to the driver, such as [WPP\_INIT\_TRACING](https://msdn.microsoft.com/library/windows/hardware/ff556191) and [WPP\_CLEANUP](https://msdn.microsoft.com/library/windows/hardware/ff556179). If the code does not compile because the types that are used are not defined, ETW and WPP cannot support the driver type.
For more information about ETW, see [Event Tracing](http://go.microsoft.com/fwlink/p/?linkid=179202) in the Windows SDK documentation.

**Note** WPP trace providers can only be enabled by one trace session at a time. See [WPP Providers](https://msdn.microsoft.com/library/windows/desktop/aa363668#providers) for more information.

For information about the [WMI library support routines](https://msdn.microsoft.com/library/windows/hardware/ff566359) that support WPP software tracing, see:

[**WmiQueryTraceInformation**](https://msdn.microsoft.com/library/windows/hardware/ff565820)

[**WmiTraceMessage**](https://msdn.microsoft.com/library/windows/hardware/ff565836)

[**WmiTraceMessageVa**](https://msdn.microsoft.com/library/windows/hardware/ff566340)

 

 





