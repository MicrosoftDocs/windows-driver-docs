---
title: WPP Software Tracing
description: WPP Software Tracing
ms.assetid: dab776b3-bac9-4157-a530-6e48868ba900
keywords: ["Windows software trace preprocessor WDK", "WPP software tracing WDK", "software tracing WDK , WPP", "kernel-mode WPP WDK software tracing", "Windows software trace preprocessor WDK , about WPP", "WPP software tracing WDK , about WPP", "default WPP software tracing", "tracing WDK , WPP"]
---

# WPP Software Tracing


## <span id="ddk_wpp_software_tracing_tools"></span><span id="DDK_WPP_SOFTWARE_TRACING_TOOLS"></span>


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
<li>For kernel-mode drivers, use the [Event Tracing for Windows (ETW)](event-tracing-for-windows--etw-.md) API.</li>
<li>For user-mode drivers or applications, use the [Event Tracing](https://msdn.microsoft.com/library/windows/desktop/bb968803) (Windows Desktop) API.</li>
</ul>
For more information, see [When should I use WPP Software Tracing or the Event Tracing for Windows (ETW) API?](tools-for-software-tracing.md#when_to_use_event_tracing)</td>
</tr>
</tbody>
</table>

 

Logging messages with WPP software tracing is similar to using Windows event logging services. The driver logs a message ID and unformatted binary data in a log file. Subsequently, a postprocessor converts the information in the log file to a human-readable form. However, WPP software tracing supports message formats that are more capable and flexible than that supported by the event logging services. For example, WPP software tracing has built-in support for IP addresses, GUIDs, system IDs, time stamps, and other useful data types. In addition, users can add custom data types relevant to their application.

WPP software tracing is supported on Microsoft Windows 2000 and later versions of Windows.

### <span id="ddk_using_wpp_software_tracing_in_a_driver_tools"></span><span id="DDK_USING_WPP_SOFTWARE_TRACING_IN_A_DRIVER_TOOLS"></span>An overview of the WPP software tracing process

The basic process for adding WPP software tracing to a driver or application, includes the following steps. If you use one of the Visual Studio templates provided in the WDK for creating a WDF driver, much of the work is done for you.

-   Define a control GUID that uniquely identifies the driver or application as a [trace provider](trace-provider.md). The provider specifies this GUID in its definition of the [WPP\_CONTROL\_GUIDS](https://msdn.microsoft.com/library/windows/hardware/ff556186) macro and in a related control file used by [Tracelog](tracelog.md) or another [Trace Controller](trace-controller.md).

-   Add the required WPP-related C preprocessor directives and WPP macro calls to the provider's source files, as described in [Adding WPP Software Tracing to a Windows Driver](adding-wpp-software-tracing-to-a-windows-driver.md) and in [WPP Software Tracing Reference](https://msdn.microsoft.com/library/windows/hardware/ff556205).

-   Modify the Visual Studio project to run the WPP preprocessor and build the driver, as described in [Step 6](adding-wpp-software-tracing-to-a-windows-driver.md#step_run_wpp) of Adding WPP Software Tracing to a Windows Driver. You can refer to the [WPP Preprocessor](wpp-preprocessor.md) for more build time options.

-   Install the driver or component. Start a trace session and record the trace messages. Use the tools for software tracing, such as [TraceView](traceview.md), [Tracelog](tracelog.md), [Tracefmt](tracefmt.md), and [Tracepdb](tracepdb.md) to configure, start, and stop tracing sessions and to display and filter trace messages. These tools are included in the Windows Driver Kit (WDK).

## <span id="in_this_section"></span>In this section


-   [Adding WPP Software Tracing to a Windows Driver](adding-wpp-software-tracing-to-a-windows-driver.md)
-   [Inflight Trace Recorder for logging traces](using-wpp-recorder.md)
-   [Using WPP Software Tracing in a Trace Provider](using-wpp-software-tracing-in-a-trace-provider.md)
-   [Adding WPP Macros to a Trace Provider](adding-wpp-macros-to-a-trace-provider.md)
-   [WPP Preprocessor](wpp-preprocessor.md)
-   [Tracing and Diagnosability for WDF Drivers](tracing-and-diagnosability-for-wdf-drivers.md)

**Note**   Event Tracing for Windows (ETW) and WPP support most types of kernel-mode and user-mode drivers. However, ETW and WPP use types that are not available for certain types of drivers, such as miniport drivers. To determine whether a particular driver type is supported, add basic WPP macros to the driver, such as [WPP\_INIT\_TRACING](https://msdn.microsoft.com/library/windows/hardware/ff556191) and [WPP\_CLEANUP](https://msdn.microsoft.com/library/windows/hardware/ff556179). If the code does not compile because the types that are used are not defined, ETW and WPP cannot support the driver type.
For more information about ETW, see [Event Tracing](http://go.microsoft.com/fwlink/p/?linkid=179202) in the Windows SDK documentation.

 

For information about the [WMI library support routines](https://msdn.microsoft.com/library/windows/hardware/ff566359) that support WPP software tracing, see:

[**WmiQueryTraceInformation**](https://msdn.microsoft.com/library/windows/hardware/ff565820)

[**WmiTraceMessage**](https://msdn.microsoft.com/library/windows/hardware/ff565836)

[**WmiTraceMessageVa**](https://msdn.microsoft.com/library/windows/hardware/ff566340)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20WPP%20Software%20Tracing%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




