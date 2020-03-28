---
title: Inflight Trace Recorder (IFR) for logging traces
description: Inflight Trace Recorder (IFR) allows a trace provider, such as a kernel-mode driver, to record trace logs and store WPP log messages in buffers.
ms.assetid: D11FA28E-3B0C-4D9D-AEDA-8A80DE58091C
ms.date: 03/27/2020
ms.localizationpriority: medium
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


## How to send trace messages to the WPP default log

Follow the instructions in [Adding WPP Software Tracing to a Windows Driver](adding-wpp-software-tracing-to-a-windows-driver.md).  For example, in *DriverEntry*, call `WPP_INIT_TRACING(DriverObject, RegistryPath)`; in *EvtDriverUnload*, call `WPP_CLEANUP(WdfDriverWdmGetDriverObject(Driver))`.

Once that is done, you're free to call the trace function as you like.


## How to send trace messages to a custom log

This only applies to kernel-mode drivers (KMDF or WDM).

For the majority of drivers, the single default log is good enough. However, in some scenarios, it's helpful to have separate log buffers for distinct entities.

For example, when writing a bus driver, you might want each child device to have its own buffer. Then you can use the debugger to dump only the log for a specific child device.

To set up custom logs, the driver must include `<WppRecorder.h>`. Then call the following APIs:

 - **WppRecorderLogCreate** to create more than one log buffer
 - **WppRecorderLogDelete** before calling **WPP_CLEANUP**.
 - **WppRecorderLogSetIdentifier** to set a string identifier for a given recorder log (optional)
 - **WppRecorderConfigure** to disable the default log

The driver also needs to define a new trace macro that takes the log handle as the first parameter. For an example, see the [Toaster Sample Driver](https://github.com/microsoft/Windows-driver-samples/tree/master/general/toaster/toastDrv).


## How to view trace messages in the debugger

For KMDF and UMDF drivers, use **!wdfkd.wdflogdump** as usual. It will print out both the framework IFR log and the driver IFR log.

For WDM drivers, use **!rcdrkd.rcdrloglist** and **!rcdrkd.rcdrlogdump**.


## Configure Inflight Trace Recorder parameters

The IFR can be configured under the driver's [Parameter key](https://docs.microsoft.com/windows-hardware/drivers/wdf/introduction-to-registry-keys-for-drivers).

Use the following registry values:

**LogPages:  REG_DWORD**

Set to the number of pages to store the default log. The default is one.

**VerboseOn: REG_DWORD**

The default setting of zero causes the IFR to log errors, warnings, and informational events. Set to one to add verbose output to the log. 
