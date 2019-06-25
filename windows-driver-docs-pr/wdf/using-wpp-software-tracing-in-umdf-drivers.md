---
title: Using WPP Software Tracing in UMDF Drivers
description: Using WPP Software Tracing in UMDF Drivers
ms.assetid: d8469d29-dfc3-41b9-a72d-9dafb3e70123
keywords:
- software tracing WDK , framework-based drivers
- debugging drivers WDK UMDF , software tracing
- tracing WDK , framework-based drivers
- WPP software tracing WDK , framework-based driver
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using WPP Software Tracing in UMDF Drivers


[WPP software tracing](https://docs.microsoft.com/windows-hardware/drivers/devtest/wpp-software-tracing) enables you to add tracing messages that help you debug your driver. Additionally, the framework's [event logger](using-the-framework-s-event-logger.md) provides hundreds of tracing messages that you can view.

You can view tracing messages by using [TraceView](https://docs.microsoft.com/windows-hardware/drivers/devtest/traceview) or [Tracelog](https://docs.microsoft.com/windows-hardware/drivers/devtest/tracelog). You can also [send trace messages to a kernel debugger](https://docs.microsoft.com/windows-hardware/drivers/devtest/how-do-i-send-trace-messages-to-a-kernel-debugger-).

### Adding Tracing Messages to Your Driver

To add tracing messages to your framework-based driver, you must:

-   Add an **\#include** directive to each of your driver's source files that contains any of the WPP macros. This directive must identify a [trace message header (TMH) file](https://docs.microsoft.com/windows-hardware/drivers/devtest/trace-message-header-file). The file name must have a format of &lt;*driver-source-file-name*&gt;.tmh.

    For example, if your driver consists of two source files, called *MyDriver1.c* and *MyDriver2.c*, then *MyDriver1.c* must contain:

    `#include "MyDriver1.tmh"`

    and *MyDriver2.c* must contain:

    `#include "MyDriver2.tmh"`

    When you build your driver in Microsoft Visual Studio, the WPP preprocessor generates the .tmh files.

-   Define a [WPP\_CONTROL\_GUIDS](https://docs.microsoft.com/previous-versions/windows/hardware/previsioning-framework/ff556186(v=vs.85)) macro in a header file. This macro defines a GUID and [trace flags](https://docs.microsoft.com/windows-hardware/drivers/devtest/trace-flags) for your driver's tracing messages. (For each of the WDK's UMDF-based sample drivers, the Internal.h header file includes this macro.)

-   Include a [WPP\_INIT\_TRACING](https://docs.microsoft.com/previous-versions/windows/hardware/previsioning-framework/ff556191(v=vs.85)) macro in your driver's DllMain routine. This macro activates software tracing in your driver. (For each of the WDK's UMDF-based sample drivers, the DllSup.h header file includes this macro.)

-   Include a [WPP\_CLEANUP](https://docs.microsoft.com/previous-versions/windows/hardware/previsioning-framework/ff556179(v=vs.85)) macro in your driver's DllMain routine. This macro deactivates software tracing in your driver. (For each of the WDK's UMDF-based sample drivers, the DllSup.h header file includes this macro.)

-   Use the [**DoTraceMessage**](https://docs.microsoft.com/previous-versions/windows/hardware/previsioning-framework/ff544918(v=vs.85)) macro, or a [customized version](https://docs.microsoft.com/windows-hardware/drivers/devtest/can-i-customize-dotracemessage-) of the macro, in your driver to create trace messages. (For each of the WDK's UMDF-based sample drivers, the Internal.h header file includes a customized macro.)

-   Open the Property Pages for your driver project. Right-click the driver project in Solution Explorer and select **Properties**. In the Property Pages for the driver, click **Configuration Properties**, and then **Wpp**. Under the **General** menu, set **Run WPP Tracing** to Yes. Under the **File Options** menu, you should also specify the framework's WPP template file, for example:

    ```cpp
    {km-WdfDefault.tpl}*.tmh
    ```

For more information about adding tracing messages to your driver, see [Adding WPP Macros to a Driver](https://docs.microsoft.com/windows-hardware/drivers/devtest/adding-wpp-macros-to-a-trace-provider).

### Sample Drivers That Use WPP Software Tracing

All of the UMDF-based sample drivers in the WDK provide DllSup.h, Internal.h, and Sources files that enable WPP software tracing. Most of these sample drivers also use a customized macro to create trace messages.

### Viewing Your Driver's Trace Messages

If you have added trace messages to your driver, the driver is a [trace provider](https://docs.microsoft.com/windows-hardware/drivers/devtest/trace-provider). You can use a [trace controller](https://docs.microsoft.com/windows-hardware/drivers/devtest/trace-controller), such as [Tracelog](https://docs.microsoft.com/windows-hardware/drivers/devtest/tracelog), to control a [trace session](https://docs.microsoft.com/windows-hardware/drivers/devtest/trace-session) and create a [trace log](https://docs.microsoft.com/windows-hardware/drivers/devtest/trace-log). You can use a [trace consumer](https://docs.microsoft.com/windows-hardware/drivers/devtest/trace-consumer), such as [Tracefmt](https://docs.microsoft.com/windows-hardware/drivers/devtest/tracefmt), to view the messages.

For more information about how to use the software tracing tools, see [Survey of Software Tracing Tools](https://docs.microsoft.com/windows-hardware/drivers/devtest/survey-of-software-tracing-tools).

### Viewing the UMDF Trace Log

The UMDF log file is %windir%\\system32\\LogFiles\\WUDF\\WUDFTrace.etl.

**Note**  Starting in UMDF 2.15, the log directory is *%ProgramData%*\\Microsoft\\WDF.

 

You can view the UMDF log file by using either [TraceView](https://docs.microsoft.com/windows-hardware/drivers/devtest/traceview) or [Tracelog](https://docs.microsoft.com/windows-hardware/drivers/devtest/tracelog). Both tools require trace message format (TMF) files that format the trace log's messages. The TMF files are available in the WDK, under the \\tools\\tracing subdirectory. (In TraceView, UMDF appears as a named provider with the name of "UMDF-Framework Trace" or "Framework Trace", depending on the UMDF version.)

[WDF Verifier](https://docs.microsoft.com/windows-hardware/drivers/devtest/wdf-verifier-control-application) enables you to send trace messages to both the UMDF trace log and your kernel debugger. (You should not send trace messages to your kernel debugger by using the **-kd** option in [Tracelog](https://docs.microsoft.com/windows-hardware/drivers/devtest/tracelog), because **Tracelog** can disrupt trace logging within UMDF.)

You can also use the [**!wmitrace**](https://docs.microsoft.com/windows-hardware/drivers/debugger/wmi-tracing-extensions--wmitrace-dll-) debugger extension to [view the trace messages](https://docs.microsoft.com/windows-hardware/drivers/devtest/how-do-i-send-trace-messages-to-a-kernel-debugger-) in the debugger:

1.  In WinDbg, attach to the instance of WUDFHost that hosts the driver. For more information, see [How to Enable Debugging of a UMDF Driver](enabling-a-debugger.md).
2.  If your driver uses version 1.11 or later, and you are using the kernel debugger from Windows 8 or later, you can skip this step. If your driver uses a version of UMDF earlier than 1.11, use [**!wmitrace.tmffile**](https://docs.microsoft.com/windows-hardware/drivers/debugger/-wmitrace-tmffile) or [**!wmitrace.searchpath**](https://docs.microsoft.com/windows-hardware/drivers/debugger/-wmitrace-searchpath) to specify a platform-specific trace message format (.tmf) file, or a path to a .tmf file. The .tmf files are located in platform-specific subdirectories in the WDK.

3.  Use the [**!wmitrace.logdump**](https://docs.microsoft.com/windows-hardware/drivers/debugger/-wmitrace-logdump) command to display the contents of the trace buffers:

    ```cpp
    !wmitrace.logdump WudfTrace
    ```

### Controlling Trace Messages

You can control UMDF trace messages with the user interface that [WDF Verifier](https://docs.microsoft.com/windows-hardware/drivers/devtest/wdf-verifier-control-application) provides, or by modifying registry values. You should use the **WDF Verifier** interface when possible, because the registry values might change in future versions of UMDF. In addition, you should not access these values within INF files or your driver's code.

Currently, you can modify the following registry values, which are located under the **HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\WUDF** registry key:

-   The **LogEnable** value controls whether UMDF creates a trace log for your driver. If this value is set to 1, UMDF creates a trace log.

-   The **LogLevel** value controls the amount of information that UMDF trace messages contain. The default value for **LogLevel** is 3, which causes UMDF trace messages to contain error and warning messages. Set this value to 7 to include error and warning messages, plus non-error informational messages. Set it to 15 to include all of the trace information that UMDF is capable of providing.

-   The **LogKd** value controls whether UMDF sends trace messages to your kernel debugger. If **LogKd** is set to 1, UMDF sends its trace messages to your kernel debugger.

-   The **LogFlushPeriodSeconds** value specifies how often, in seconds, trace messages are written to the trace log.

-   The **LogMinidumpType** value contains flags that specify the type of information that a mini-dump file, if produced, will contain. For more information about these flags, see the [MINIDUMP\_TYPE](https://go.microsoft.com/fwlink/p/?linkid=160310) enumeration.

You might find additional registry values under the **HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\WUDF** registry key. You should not modify those values.

 

 





