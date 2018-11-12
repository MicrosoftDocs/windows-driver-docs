---
title: TraceLogging API
description: TraceLogging API
ms.assetid: AE93DD45-05D7-4E7A-B086-B40A6FA0904B
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# TraceLogging API


New for Windows 10, TraceLogging is the tracing and telemetry framework for user-mode applications and kernel-mode drivers. The TraceLogging API is based upon [Event Tracing for Windows (ETW)](event-tracing-for-windows--etw-.md) and offers a simplified way of instrumenting code to create a native C/C++ ETW provider. The TraceLogging instrumentation can be structured when needed, but does not require the overhead of defining events and event data in a separate instrumentation manifest (XML file). In addition, the instrumentation you add with the [TraceLogging](https://msdn.microsoft.com/library/windows/desktop/dn904636) API can easily be extended to provide telemetry data for performance measurements and diagnostics.

The [TraceLogging](https://msdn.microsoft.com/library/windows/desktop/dn904636) API offers the advantages of [WPP Software Tracing](wpp-software-tracing.md) or debug print statements, in that it is easy to code, and it also provides the benefits of manifest-based ETW, in that it is easy to analyze and correlate the events from the collected trace data.

TraceLogging is built on ETW and is compatible with existing tools. Providers that use manifest-based ETW will continue to be supported. There is no need to convert manifest based ETW providers to TraceLogging providers, except in those cases where you need events for telemetry data.

[WPP Software Tracing](wpp-software-tracing.md) is supported. However, TraceLogging offers many advantages in terms of maintenance and extensibility, and is even easier to use in your code.

## <span id="in_this_section"></span>In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Topic</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="tracelogging-for-kernel-mode-drivers-and-components.md" data-raw-source="[TraceLogging for kernel-mode drivers and components](tracelogging-for-kernel-mode-drivers-and-components.md)">TraceLogging for kernel-mode drivers and components</a></p></td>
<td align="left"><p>This topic describes how to use the <a href="https://msdn.microsoft.com/library/windows/desktop/dn904636" data-raw-source="[TraceLogging](https://msdn.microsoft.com/library/windows/desktop/dn904636)">TraceLogging</a> API from within kernel-mode drivers and components.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="tracelogging-examples.md" data-raw-source="[TraceLogging Examples](tracelogging-examples.md)">TraceLogging Examples</a></p></td>
<td align="left"><p>The source code in this topic demonstrates how to use TraceLogging.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="how-to-fix-tracelogging-build-errors.md" data-raw-source="[How to fix TraceLogging build errors](how-to-fix-tracelogging-build-errors.md)">How to fix TraceLogging build errors</a></p></td>
<td align="left"><p>This topic describes some common build errors and how to resolve them.</p></td>
</tr>
</tbody>
</table>

 

 

 





