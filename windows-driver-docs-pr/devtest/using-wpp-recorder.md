---
title: Inflight Trace Recorder (IFR) for logging traces
description: Inflight Trace Recorder (IFR) allows a trace provider, such as a kernel-mode driver, to record trace logs and store WPP log messages in buffers.
ms.date: 03/30/2020
---

# Inflight Trace Recorder (IFR) for logging traces


*Inflight Trace Recorder (IFR)* is a tracing feature that allows a trace provider, such as a kernel-mode driver or a UMDF driver, to create a set of in-memory circular buffer where the latest log messages are preserved. The log message can be viewed using a debugger.

IFR is built on top of [WPP software tracing](wpp-software-tracing.md). The primary benefit of IFR over WPP is that it is turned on automatically and you do not need to start trace sessions in advance.

**Applies to:**

-   Minimum OS: Windows 8 for KMDF and WDM driver developers
-   Minimum OS: Windows 10 for UMDF (2.15) driver developers

## How to enable Inflight Trace Recorder in Visual Studio

First, follow the steps in [Adding WPP Software Tracing to a Windows Driver](adding-wpp-software-tracing-to-a-windows-driver.md).

Next, in the Project property page, under **Configuration Properties->WPP Tracing->Function and Macro Options->Enable Inflight Trace Recorder**, select **Yes**.

Finally, for UMDF only, there is one additional step: under **WPP Tracing->Function and Macro Options->Preprocessor Definitions**, add `WPP_MACRO_USE_KM_VERSION_FOR_UM=1`.


## How to enable Inflight Trace Recorder from the command line

If you edit the .vcxproj file manually, set the following entries:

For a KMDF or WDM driver:

```xml
    <ClCompile Include=...>
        <WppEnabled>true</WppEnabled>
        <WppKernelMode>true</WppKernelMode>
        <WppRecorderEnabled>true</WppRecorderEnabled>
        ...
    </ClCompile>
```

For a UMDF driver:

```xml
    <ClCompile Include=...>
        <WppEnabled>true</WppEnabled>
        <WppRecorderEnabled>true</WppRecorderEnabled>
        <WppPreprocessorDefinitions>WPP_MACRO_USE_KM_VERSION_FOR_UM=1</WppPreprocessorDefinitions>
        ...
    </ClCompile>
```


## How to send trace messages to the default log

Follow the instructions in [Adding WPP Software Tracing to a Windows Driver](adding-wpp-software-tracing-to-a-windows-driver.md).  For example:

 - In [*DriverEntry*](../wdf/driverentry-for-kmdf-drivers.md), call `WPP_INIT_TRACING(DriverObject, RegistryPath)`.
 - In [*EvtDriverUnload*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_unload), call `WPP_CLEANUP(WdfDriverWdmGetDriverObject(Driver))`.

Now the driver is free to call the trace function as needed. For example: `TraceEvents(TRACE_LEVEL_ERROR, DBG_INIT, "WdfDriverCreate failed, %!STATUS!", ntStatus);`

For more info, see [WPP_INIT_TRACING](/previous-versions/windows/hardware/drivers/ff556193(v=vs.85)) and [WPP_CLEANUP](/previous-versions/windows/hardware/drivers/ff556183(v=vs.85)).

## How to add timestamp information to the default log

Starting in WDK Insider Preview build 22557, drivers can add timestamps to log entries that are then viewable using [**!rcdrkd.rcdrlogdump**](../debugger/-rcdrkd-rcdrlogdump.md) or [**!wdfkd.wdflogdump**](../debugger/-wdfkd-wdflogdump.md), for example:

```dbgcmd
0: kd> !rcdrlogdump SampleDriver
Sample Log 1: 02/03/2022-15:32:11.838 NativeMethodInterfaceRequest - interface successfully copied!
```

To add timestamps to log entries, add the lines between the comment markers below to the driver's INF file.
 
For a kernel-mode driver:

```inf
[IfrSample_Service_Inst] 
DisplayName    = %IfrSample.SvcDesc%
ServiceType    = 1               ; SERVICE_KERNEL_DRIVER
StartType      = 3               ; SERVICE_DEMAND_START
ErrorControl   = 1               ; SERVICE_ERROR_NORMAL
ServiceBinary  = %12%\IfrSample.sys
; =============== START TIMESTAMP ADDITION
AddReg = IfrSample_Service_Inst.AddReg
 
[IfrSample_Service_Inst.AddReg]
HKR, "Parameters", "WppRecorder_UseTimeStamp", %REG_DWORD%, 1
; =============== END TIMESTAMP ADDITION

[Strings]
REG_DWORD = 0x00010001
```

For a UMDF driver:

```inf 
[IfrSampleUm_Install] 
UmdfLibraryVersion=$UMDFVERSION$
ServiceBinary=%13%\IfrSampleUm.dll
; =============== START TIMESTAMP ADDITION
AddReg=IfrSampleUm_Install.AddReg
 
[IfrSampleUm_Install.AddReg]
HKR, "Parameters", "WppRecorder_UseTimeStamp", %REG_DWORD%,
; =============== END TIMESTAMP ADDITION
```

If you would like more precise timestamps, in addition to **WppRecorder_UseTimeStamp**, add **WppRecorder_PreciseTimeStamp** using the same syntax shown above.

Precise timestamps look like this:

```dbgcmd
1: kd> !rcdrlogdump IfrSample 
DriverLog 1: 02/03/2022-16:16:25.9571373 DriverEntry - Reg path = \REGISTRY\MACHINE\SYSTEM\ControlSet001\Services\IfrSample
DriverLog 2: 02/03/2022-16:16:25.9571377 DriverEntry - Demonstrate usage of NTSTATUS: 0xc000000d(STATUS_INVALID_PARAMETER)
```

## How to send trace messages to a custom log

This only applies to kernel-mode drivers (KMDF or WDM).

For the majority of drivers, the single default log is good enough. However, in some scenarios, it's helpful to have separate log buffers for distinct entities.

For example, when writing a bus driver, you might want each child device to have its own buffer. Then you can use the debugger to dump only the log for a specific child device.

To set up custom logs, the driver must include `<WppRecorder.h>`. Then call the following APIs:

 - [**WppRecorderLogCreate**](/windows-hardware/drivers/ddi/wpprecorder/nf-wpprecorder-wpprecorderlogcreate) to create more than one log buffer
 - [**WppRecorderLogDelete**](/windows-hardware/drivers/ddi/wpprecorder/nf-wpprecorder-wpprecorderlogdelete) before calling **WPP_CLEANUP**.
 - [**WppRecorderLogSetIdentifier**](/windows-hardware/drivers/ddi/wpprecorder/nf-wpprecorder-wpprecorderlogsetidentifier) to set a string identifier for a given recorder log (optional)
 - [**WppRecorderConfigure**](/windows-hardware/drivers/ddi/wpprecorder/nf-wpprecorder-wpprecorderconfigure) to disable the default log (optional)

The driver also needs to define a new trace macro that takes the log handle as the first parameter. For an example, see the [Toaster Sample Driver](https://github.com/microsoft/Windows-driver-samples/tree/master/general/toaster/toastDrv/kmdf/func/featured/trace.h).

## How to add timestamp information to a custom log

If your driver calls [**WppRecorderLogCreate**](/windows-hardware/drivers/ddi/wpprecorder/nf-wpprecorder-wpprecorderlogcreate) to create additional log handles, it is possible to enable timestamps for some log handles but not others.

Then you need to add a single line to the driver code for each log handle that should use timestamps.
For a code example, see [**WppRecorderLogCreate**](/windows-hardware/drivers/ddi/wpprecorder/nf-wpprecorder-wpprecorderlogcreate).

> [!NOTE]
> This functionality is only available starting in WDK Insider Preview build 22557. For info on targeting a specific release, see [Building Drivers for Different Versions of Windows](/windows-hardware/drivers/develop/building-drivers-for-different-versions-of-windows).

## How to view trace messages in the debugger

For KMDF and UMDF drivers, use [**!wdfkd.wdflogdump**](../debugger/-wdfkd-wdflogdump.md) as usual. It will print out both the framework IFR log and the driver IFR log.

For WDM drivers, use [**!rcdrkd.rcdrloglist**](../debugger/-rcdrkd-rcdrloglist.md) and [**!rcdrkd.rcdrlogdump**](../debugger/-rcdrkd-rcdrlogdump.md).


## Configure Inflight Trace Recorder parameters

The IFR can be configured under the driver's [Parameter key](../wdf/introduction-to-registry-keys-for-drivers.md).

Use the following registry values:

**LogPages:  REG_DWORD**

Set to the number of pages to store the default log. The default is one.

**VerboseOn: REG_DWORD**

The default setting of zero causes the IFR to log errors, warnings, and informational events. Set to one to add verbose output to the log.
