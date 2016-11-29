---
title: TraceLogging API
description: TraceLogging API
ms.assetid: AE93DD45-05D7-4E7A-B086-B40A6FA0904B
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
<td align="left"><p>[TraceLogging for kernel-mode drivers and components](tracelogging-for-kernel-mode-drivers-and-components.md)</p></td>
<td align="left"><p>This topic describes how to use the [TraceLogging](https://msdn.microsoft.com/library/windows/desktop/dn904636) API from within kernel-mode drivers and components.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[TraceLogging Examples](tracelogging-examples.md)</p></td>
<td align="left"><p>The source code in this topic demonstrates how to use TraceLogging.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[How to fix TraceLogging build errors](how-to-fix-tracelogging-build-errors.md)</p></td>
<td align="left"><p>This topic describes some common build errors and how to resolve them.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20TraceLogging%20API%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




