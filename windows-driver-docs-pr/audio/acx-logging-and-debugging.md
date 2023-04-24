---
title: ACX logging and debugging
description: This topic provides information on logging, tracing and debugging of the ACX Audio Class Extensions.
ms.date: 04/14/2023
ms.localizationpriority: medium
---

# ACX logging and debugging

>[!IMPORTANT]
> Some information relates to a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

This topic provides information on logging, tracing and debugging of the ACX Audio Class Extensions.

## ACX Driver Logging

Software tracing for drivers is usually based on Event Tracing for Windows (ETW), a kernel-level facility that logs trace messages for both kernel-mode and user-mode processes. As ACX drivers are WDF drivers, all of the WDF logging and eventing capabilities are available for ACX driver developers.

### WPP

Because ETW can be somewhat complicated to use, most driver developers use the Windows software trace preprocessor (WPP), which simplifies and enhances the process of instrumenting a driver for ETW tracing.

ACX uses WPP logs for tracing and debugging. For more information, see [Using WPP Software Tracing in KMDF Drivers](../wdf/using-wpp-software-tracing-in-kmdf-drivers.md) and [Adding WPP Software Tracing to a Windows Driver](../devtest/adding-wpp-software-tracing-to-a-windows-driver.md).

### In-Flight recorder (IFR)

In-Flight recorder (IFR) is supported and can be viewed via WDFKD, RCDRKD or with the ACXKD debugger extension when it is available. For general information working with IFR logs, see [Using Inflight Trace Recorder (IFR) in KMDF and UMDF 2 Drivers](../devtest/using-wpp-recorder.md) and [Video: Accessing driver IFR logs without a debugger](../wdf/video--accessing-driver-ifr-logs-without-a-debugger.md)

ACX logs key events using other ETW providers to simplify the visualization of these special events. 

### Adding logging to your driver

3rd party drivers are highly encouraged to use WPP and ETW events as well.  

This example code, shows checking a return value and logging an appropriate error.

```cpp

    //
    // The driver uses this DDI to delete the circuits from the current device. 
    //
    status = AcxDeviceRemoveCircuit(Device, devCtx->Speaker);
    if (!NT_SUCCESS(status)) { DrvLogError(g_AudioDspLog, FLAG_INIT, L"Failed to remove speaker circuit, continuing with ReleaseHardware, %!STATUS!", status); }
    status = AcxDeviceRemoveCircuit(Device, devCtx->MicArray);
    if (!NT_SUCCESS(status)) { DrvLogError(g_AudioDspLog, FLAG_INIT, L"Failed to remove micarray circuit, continuing with ReleaseHardware, %!STATUS!", status); }
    status = AcxDeviceRemoveCircuit(Device, devCtx->SpeakerHp);
    if (!NT_SUCCESS(status)) { DrvLogError(g_AudioDspLog, FLAG_INIT, L"Failed to remove speakerHp circuit, continuing with ReleaseHardware, %!STATUS!", status); }
    status = AcxDeviceRemoveCircuit(Device, devCtx->MicrophoneHp);
    if (!NT_SUCCESS(status)) { DrvLogError(g_AudioDspLog, FLAG_INIT, L"Failed to remove microphoneHp circuit, continuing with ReleaseHardware, %!STATUS!", status); }
    status = AcxDeviceRemoveCircuit(Device, devCtx->HDMI);
    if (!NT_SUCCESS(status)) { DrvLogError(g_AudioDspLog, FLAG_INIT, L"Failed to remove HDMI circuit, continuing with ReleaseHardware, %!STATUS!", status); }
```

The featured version of the Toaster driver sample code provides examples of WMI tracing as well as reusable tracing code. For more information about the Toaster sample, see [Toaster Sample Driver](/samples/microsoft/windows-driver-samples/toaster-sample-driver/).

### Recommendations for ACX Driver logging

To improve the reliability of your ACX driver consider the following behaviors for logging.

- Unexpected return values from stream buffer IO or other regular signal processing activity. 
- Unexpected power states or power state transitions.
- Errors related to calls made during updates or re-installation.
- Other behaviors that may lead to “no audio” could be considered for logging.

### Using the WMI Tracing debugger extensions

To view trace events in the debugger, use the WMI extension, Wmitrace.dll. It contains a library of functions designed to control and view WMI event tracing. For more information, see [WMI Tracing Extensions (Wmitrace.dll)](../debugger/wmi-tracing-extensions--wmitrace-dll-.md).

## ACX driver debugging

ACX drivers are WDF drivers, so the debugging techniques described for WDF drivers, apply to ACX drivers. See the following topics for information on debugging WDF drivers.

#### General information about the debugging tools

[Debugging Tools for Windows (WinDbg, KD, CDB, NTSD)](../debugger/index.md)

#### KMDF debugging

- [Summary of Debugger Extensions in Wdfkd.dll](../wdf/debugger-extensions-for-kmdf-drivers.md)

- This walk through uses the traditional Sysvad audio driver, but illustrates some techniques that may be help to ACX drivers.
[Debug Drivers - Step by Step Lab (Sysvad Kernel Mode)](../debugger/debug-universal-drivers--kernel-mode-.md)

#### Video Walkthroughs

- [Video: Debugging your driver with WDF source code](../wdf/video--debugging-your-driver-with-wdf-source-code.md)
- [Video Series: Debugging Kernel-Mode Driver Framework Drivers](../wdf/debugging-kernel-mode-driver-framework-drivers.md)

#### ACX kernel debugger extension library (AcxKd.dll)

To aid debugging, ACX has a companion kernel debugger extension library (AcxKd.dll). This library aids developers in tracking down issue on single and multi-stack audio paths. The kd extension allows developer to look inside ACX structures.

>[!NOTE]
> This debugger extension is under development and information will be provided here when it is available.

## See also

[ACX audio class extensions overview](acx-audio-class-extensions-overview.md)

[Summary of ACX objects](acx-summary-of-objects.md)
