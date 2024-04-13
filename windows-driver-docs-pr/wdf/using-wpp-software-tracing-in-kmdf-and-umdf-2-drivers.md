---
title: Using Inflight Trace Recorder (IFR) in KMDF and UMDF 2 Drivers
description: Starting in Windows 10, you can build your WDF driver so that it gets extra driver debugging information through the Windows software trace preprocessing.
ms.date: 02/07/2023
---

# Using Inflight Trace Recorder (IFR) in KMDF and UMDF 2 Drivers


Starting in Windows 10, you can build your KMDF or UMDF driver so that it gets extra driver debugging information through the Windows software trace preprocessing. This feature, called the Inflight Trace Recorder (IFR), is available starting in KMDF version 1.15 and UMDF version 2.15.

Inflight Trace Recorder is an extension of [WPP software tracing](../devtest/wpp-software-tracing.md). Unlike WPP tracing, the Inflight Trace Recorder continues to work without an attached trace consumer. The framework writes messages to a circular buffer, and your driver can also add its own messages. Each driver has its own log, so multiple devices associated with a driver share a single log.

If you turn on the IFR in your driver binary, the IFR is present and running during the lifetime of your driver. You don't need to start an explicit trace collection session.

The logs are stored in non-pageable memory, so they're recoverable after a system crash. In addition, Inflight Trace Recorder logs are included in minidump files except when the responsible driver is undetermined or if the crash was a host timeout.

**How to enable Inflight Trace Recorder and send messages from your driver**

1.  In Microsoft Visual Studio, do the following steps:

    -   Open the Property Pages for your driver project. Right-click the driver project in Solution Explorer and select **Properties**. In the Property Pages for the driver, select **Configuration Properties**, and then **Wpp Tracing**. On the **General** menu, set **Run WPP Tracing** to **Yes**.

    -   Navigate to **Properties-&gt;Wpp Tracing-&gt;Function and Macro Options** and choose **Enable WPP Recorder**.

    -   On the same menu, set **Scan Configuration Data** to the file containing your trace information, for example Trace.h.

2.  In each source file that calls a WPP macro, add an **\#include** directive that identifies a [trace message header (TMH) file](../devtest/trace-message-header-file.md). The file name must have a format of &lt;*driver-source-file-name*&gt;**.tmh**.

    For example, if your driver consists of two source files, called *MyDriver1.c* and *MyDriver2.c*, then *MyDriver1.c* must contain:

    **\#include "MyDriver1.tmh"**

    and *MyDriver2.c* must contain:

    **\#include "MyDriver2.tmh"**

    When you build your driver in Visual Studio, the WPP preprocessor generates the .*tmh* files.

3.  Define a [WPP\_CONTROL\_GUIDS](/previous-versions/windows/hardware/previsioning-framework/ff556186(v=vs.85)) macro in a header file. This macro defines a GUID and [trace flags](../devtest/trace-flags.md) for your driver's tracing messages.

    The Osrusbfx2 driver sample defines a single control GUID and seven trace flags in the Trace.h header file, as shown in the following example:

    ```cpp
    #define WPP_CONTROL_GUIDS \
    WPP_DEFINE_CONTROL_GUID(OsrUsbFxTraceGuid, \
      (d23a0c5a,d307,4f0e,ae8e,E2A355AD5DAB), \
      WPP_DEFINE_BIT(DBG_INIT)          /* bit  0 = 0x00000001 */ \
      WPP_DEFINE_BIT(DBG_PNP)           /* bit  1 = 0x00000002 */ \
      WPP_DEFINE_BIT(DBG_POWER)         /* bit  2 = 0x00000004 */ \
      WPP_DEFINE_BIT(DBG_WMI)           /* bit  3 = 0x00000008 */ \
      WPP_DEFINE_BIT(DBG_CREATE_CLOSE)  /* bit  4 = 0x00000010 */ \
      WPP_DEFINE_BIT(DBG_IOCTL)         /* bit  5 = 0x00000020 */ \
      WPP_DEFINE_BIT(DBG_WRITE)         /* bit  6 = 0x00000040 */ \
      WPP_DEFINE_BIT(DBG_READ)          /* bit  7 = 0x00000080 */ \
    )
    ```

    In this example:

    -   **OsrUsbFxTraceGuid** is the friendly name for the {d23a0c5a-d307-4f0e-ae8e-E2A355AD5DAB} GUID.
    -   The trace flags are used to differentiate between trace messages that are generated as the driver handles different types of I/O requests.

4.  Your driver (both KMDF and UMDF 2) must call [**WPP\_INIT\_TRACING for Kernel-Mode Drivers**](/previous-versions/windows/hardware/drivers/ff556193(v=vs.85)) with the driver object and a registry path, typically from [**DriverEntry**](./driverentry-for-kmdf-drivers.md):

    ```cpp
    WPP_INIT_TRACING( DriverObject, RegistryPath );
    ```

    To deactivate tracing, both KMDF and UMDF 2 drivers call [**WPP\_CLEANUP for Kernel-Mode Drivers**](/previous-versions/windows/hardware/drivers/ff556183(v=vs.85)) from [*EvtCleanupCallback*](/windows-hardware/drivers/ddi/wdfobject/nc-wdfobject-evt_wdf_object_context_cleanup) or [*EvtDriverUnload*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_unload):

    ```cpp
    WPP_CLEANUP( WdfDriverWdmGetDriverObject( Driver ));
    ```

    The [**WPP\_CLEANUP**](/previous-versions/windows/hardware/drivers/ff556183(v=vs.85)) macro takes a parameter of type PDRIVER\_OBJECT, so if your driver's [**DriverEntry**](./driverentry-for-kmdf-drivers.md) fails, you can skip calling [**WdfDriverWdmGetDriverObject**](/windows-hardware/drivers/ddi/wdfdriver/nf-wdfdriver-wdfdriverwdmgetdriverobject) and instead call **WPP\_CLEANUP** with a pointer to the WDM driver object.

    Because UMDF drivers use the kernel-mode signatures of these macros for initializing and cleaning up tracing, the calls look identical for KMDF and UMDF.

5.  Use the [**DoTraceMessage**](/previous-versions/windows/hardware/previsioning-framework/ff544918(v=vs.85)) macro, or a [customized version](../devtest/can-i-customize-dotracemessage-.md) of the macro, in your driver to create trace messages.

    The following example shows how the Osrusbfx2 driver uses its **TraceEvents** function in a portion of the code devoted to handling read requests:

    ```cpp
    if (Length > TEST_BOARD_TRANSFER_BUFFER_SIZE) {
        TraceEvents(TRACE_LEVEL_ERROR,
                    DBG_READ,
                    "Transfer exceeds %d\n",
                    TEST_BOARD_TRANSFER_BUFFER_SIZE);
     
        status = STATUS_INVALID_PARAMETER;
    }
    ```

    The call to **TraceEvents** generates a trace message if the trace controller enables the **TRACE\_LEVEL\_ERROR** level and the **DBG\_READ** trace flag. The message includes the value of the driver-defined constant **TEST\_BOARD\_TRANSFER\_BUFFER\_SIZE**.

6.  To change the size of the circular buffer that the driver log uses, modify the **LogPages** registry value in the following registry location:

    <a href="" id="for-umdf-"></a>For UMDF:  

    **SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\WUDF\\Services\\&lt;YourDriver&gt;\\Parameters\\Wdf**

    <a href="" id="for-kmdf-"></a>For KMDF:  

    **HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Services\\&lt;YourDriver&gt;\\Parameters\\Wdf**

    This is a value of type **REG\_DWORD** that contains the size of the log buffer allocated, in pages. Valid values are between 0x1 and 0x10.

**For a KMDF driver**

1.  Load the RCDRKD commands by typing **.load rcdrkd.dll** in the debugger.
2.  Use the [**!wdfkd.wdfldr**](../debuggercmds/-wdfkd-wdfldr.md) extension to display information about the driver that are currently dynamically bound to Windows Driver Frameworks (WDF).
3.  Use [**!rcdrkd.rcdrlogdump**](../debuggercmds/-rcdrkd-rcdrlogdump.md) and [**!rcdrkd.rcdrcrashdump**](../debuggercmds/-rcdrkd-rcdrcrashdump.md) to view messages that the driver provides.
4.  Use [**!wdfkd.wdflogdump**](../debuggercmds/-wdfkd-wdflogdump.md) or [**!wdfkd.wdfcrashdump**](../debuggercmds/-wdfkd-wdfcrashdump.md) to see messages that the framework provides.

**Live debugging of a UMDF driver**

1.  Use the [**!wdfkd.wdfldr**](../debuggercmds/-wdfkd-wdfldr.md) extension to display information about the drivers that are currently dynamically bound to WDF. Find your user-mode driver. Enter the associated host process.
2.  Type **!wdfkd.wdflogdump** *&lt;YourDriverName.dll&gt; &lt;Flag&gt;* , where *&lt;Flag&gt;* is:

    -   0x1 – Merged framework and driver logs
    -   0x2 – Driver logs
    -   0x3 – Framework logs

    If there's no driver log for the specified driver, the extension displays only the framework log.

**Viewing Inflight Trace Recorder logs after a UMDF driver crash**

1. From WinDbg, select **File-&gt;Open Crash Dump**, and specify the minidump file you would like to debug.
2. Type [**!wdfkd.wdfcrashdump *&lt;YourDriverName.dll&gt; &lt;process ID of driver host&gt; &lt;Option&gt;***](../debuggercmds/-wdfkd-wdfcrashdump.md), where *&lt;Option&gt;* is:

   -   0x1 – Merged framework and driver logs
   -   0x2 – Driver logs
   -   0x3 – Framework logs

   If you don't specify a driver, [**!wdfcrashdump**](../debuggercmds/-wdfkd-wdfcrashdump.md) displays information for all drivers. If you don't specify a host process, and there's only one, the extension uses the single host process. If you don't specify a host process and there's more than one, the extension lists the active host processes.

   If the log information stored in the minidump doesn't match the entered name, the minidump doesn't contain the driver's logs.

If you don't have a debugger connected, you can still access the driver and framework logs.  To learn how, see [Video: Accessing driver IFR logs without a debugger](video--accessing-driver-ifr-logs-without-a-debugger.md).

For more information about adding tracing messages to your driver, see [Adding WPP Macros to a Driver](../devtest/adding-wpp-macros-to-a-trace-provider.md).

## Related articles


[How to Enable Debugging of a UMDF Driver](enabling-a-debugger.md)

[RCDRKD Extensions](../debuggercmds/rcdrkd-extensions.md)

[Using the Framework's Event Logger](using-the-framework-s-event-logger.md)

[Using WPP Software Tracing in UMDF Drivers](using-wpp-software-tracing-in-umdf-drivers.md)

 

