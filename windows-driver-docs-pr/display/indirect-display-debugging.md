---
title: Debugging indirect display drivers
description: Describes debugging techniques for indirect display drivers
ms.date: 08/05/2022
keywords:
- Indirect display drivers, debugging
- IDDs, debuggingll
---

# Debugging indirect display drivers

Indirect Displays drivers (IDDs) are UMDF drivers so the UMDF debugging documentation, such as [Determining Why the UMDF Driver Fails to Load or the UMDF Device Fails to Start](../wdf/determining-why-the-umdf-driver-fails-to-load-or-the-umdf-device-fails.md), is a good starting point.  This page provides indirect display-specific debugging information.

## Registry control

The Indirect Display Driver Class eXtension (IccDx) has some registry settings that can be used to aid debugging IDDs. All registry values are located under the **HKLM\System\CurrentControlSet\Control\GraphicsDrivers** registry key.

| Value Name               | Details |
|--------------------------|---------|
| TerminateIndirectOnStall | A zero value will disable the watchdog that terminates the driver if it does not process a frame within 10 seconds of the frame being available. Any other value will leave the watchdog enabled. |
| IddCxDebugCtrl           | Bit-field that enabled different debug aspects of IddCx. See the table below. |

> [!NOTE]
>
> If the TerminateIndirectOnStall registry value is used to disable the watchdog, HLK tests will fail.

### IddCxDebugCtrl values

| Bit in IddCxDebugCtrl | Meaning  |
|:---------------------:|----------|
| 0x0001 | Break into the debugger when IddCx detects an error |
| 0x0002 | Break into the debugger when IddCx is loaded |
| 0x0004 | Break into the debugger when IddCx is unloaded |
| 0x0008 | Break into the debugger when IddCx DriverEntry is called |
| 0x0010 | Break into the debugger when driver bind is called |
| 0x0020 | Break into the debugger when driver start is called |
| 0x0040 | Break into the debugger when driver unbind is called |
| 0x0080 | Disables the DDI watchdog which terminates driver is takes too long in DDI call |
| 0x0100 | Unused |
| 0x0200 | Enable debug overlay, see below |
| 0x0400 | Overlay colored alpha box over dirty rects in frame; requires 0x0200 to be set |
| 0x0800 | Overlay pref stats into frame |
| 0x2000 | IddCx will query the capture frame registry values every frame; requires 0x0200 to be set |

> [!NOTE]
>
> For any of the overlay functions to work, the Direct3D device created by the driver and passed to [**IddCxSwapChainSetDevice**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxswapchainsetdevice) must be created with the **D3D11_CREATE_DEVICE_BGRA_SUPPORT** flag.

## IddCx WPP traces

Iddcx uses the [WPP infrastructure](../devtest/wpp-software-tracing.md) to log debug information. WPP information can be captured to a file, and while this capture is in progress it can be displayed in the kernel debugger.

### Capturing IddCx WPP tracing

There are several ways to enable WPP tracing. One convenient way is to use the build in [*logman.exe*](/windows-server/administration/windows-commands/logman) program. If you copy the following line to a batch file and run from an elevated command prompt it will collect IddCx WPP traces into the *IddCx.etl* file.

```console
@echo off  
echo Starting WPP tracing....
logman create trace IddCx -o IddCx.etl -ets -ow -mode sequential -p  {D92BCB52-FA78-406F-A9A5-2037509FADEA} 0x4f4 0xFF
echo Tracing enabled
pause
echo Stopping WPP tracing....
logman -stop IddCx -ets
```

#### Controlling what is captured

The Flags parameter of *logman.exe* (0x4f4 in this case) control what WPP messages IddCx logs.  The meaning value of this has change in Windows build 19041 and above.

##### Flags meaning for Windows build 19041 and above

The Flags is a bit-field, where each bit controls whether that type of message is captured.

| Flags bit | Message type captured  |
|:---------:|------------------------|
| 0x001     | Unused  |
| 0x002     | Unused  |
| 0x004     | Errors  |
| 0x008     | Benign errors, eg when debug overlay are enabled without D3D11_CREATE_DEVICE_BGRA_SUPPORT set |
| 0x010     | IddCx objects  |
| 0x020     | UMDF framework calls into IddCx |
| 0x040     | DDI calls from IddCx to the driver |
| 0x080     | Low frequency calls from driver to IddCx |
| 0x100     | High frequency frame related calls from driver to IddCx |
| 0x200     | High frequency cursor related calls from driver to IddCx |
| 0x400     | Calls from kernel to IddCx |
| 0x800     | Calls from IddCx to kernel |

A normal logging scenario of 0x0f4 is a good starting point. If you want to view per frame info then 0x1f4 is a good starting point.

##### Flags meaning prior to Windows build 19041

Flags was treated as a level, each increasing level added a new type of message along with all the messages from the previous levels.

| Flags level value  | Message type captured |
|:------------------:|-----------------------|
| 1                  | Not used              |
| 2                  | Errors                |
| 3                  | Warnings              |
| 4                  | Information           |
| 5                  | Verbose               |

### Decoding IddCx WPP tracing

Like all WPP traces, the WPP information is stored in *pdb* files and hence access to *pdb*s with that information are necessary to decode. Starting with Windows build 19560, the *IddCx.pdb* on the public symbol server contains the WPP information necessary to decode WPP messages. Before Windows build 19560, the *IddCx.pdb* on the public symbol server does *not* contain the necessary WPP information to enable WPP decode.

Any of the standard WPP decode tools can be used to decode and display the messages.

## Debugging IddCx errors

While developing an Indirect Display driver it is often useful to get additional information when IddCx detects an error. As described above, you can configure IddCx to break into the debugger when IddCx detects an error, but it is also useful to display the IddCx error message in the last few trace messages to understand the context of the error.

Using the above section, you can enable WPP tracing using *logman.exe* and with the following information display the in-memory WPP buffer in the kernel debugger at the point of the failure.

> [!NOTE]
>
> For this to work you need to be using a kernel debugger (not user mode debugger) and Windows build 19560 or above in order for the debugger to get the *IddCx.pdb* that contain the WPP decode info.

In the example below, a Indirect Display driver calls [**IddCxMonitorArrival**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxmonitorarrival). As a part of the processing, IddCx calls the driver's [**EvtIddCxMonitorQueryTargetModes**](/windows-hardware/drivers/ddi/iddcx/nc-iddcx-evt_idd_cx_monitor_query_target_modes) DDI. In this example, the driver returned a mode with DISPLAYCONFIG_VIDEO_SIGNAL_INFO.AdditionalSignalInfo.vSyncFreqDivider set to zero which is invalid and causes an error.

Here is a list of the debugger commands used:

| Command                             | Meaning  |
|-------------------------------------|----------|
| !wmitrace.bufdump                   | List all the logging buffer along with the name, IddCx is the name of ours, comes from the logman.exe command line |
| !wmitrace.logdump *LogBufferName*   | Decodes and displays the content of the specified logging buffer, which is IddCx in the example below |

Here is the debugger output for this example:

```dbgcmd
0: kd> !wmitrace.bufdump
(WmiTrace) BufDump
    LoggerContext Array @ 0xFFFFE6055EB0AC40 [64 Elements]

 Logger Context  Number Available   Size    NPP Usage   PP Usage
================ ====== ========= ======== =========== ==========
ffffe6055ee6c800      4         2     4096       16384             Circular Kernel Context Logger
ffffe6055eaa8640      2         2    65536      131072             Eventlog-Security
ffffe6055eb83a00      2         1    65536      131072             DefenderApiLogger
ffffe6055ebb6a00      2         2    65536      131072             DefenderAuditLogger
ffffe6055eb74040      2         1    16384       32768             DiagLog
ffffe6055eb74640      4         2    65536      262144             Diagtrack-Listener
ffffe6055eaa8040      2         2    65536                 131072  EventLog-Application
ffffe6055eb7c040      2         1    65536      131072             EventLog-System
ffffe6055eb7c640      5         3    65536      327680             LwtNetLog
ffffe6055eb85040      4         2    65536      262144             Microsoft-Windows-Rdp-Graphics-RdpIdd-Trace
ffffe6055eb85680      8         6   131072     1048576             NetCore
ffffe6055eb89040      4         4     4096       16384             NtfsLog
ffffe6055eb89640      8         6   131072     1048576             RadioMgr
ffffe605683ef040      3         2     4096                  12288  WindowsUpdate_trace_log
ffffe6055eb8f640      2         2     2048        4096             UBPM
ffffe6055eb108c0      4         2    16384       65536             WdiContextLog
ffffe6055eb968c0      4         2    81920      327680             WiFiSession
ffffe60567e8a6c0      5         3     8192       40960             IddCx
ffffe605658379c0     10         9     3072       30720             umstartup
ffffe605659d4840     10         9   131072     1310720             SCM
ffffe605655af9c0      2         1    65536      131072             UserNotPresentTraceSession
ffffe605659d6840      2         1     4096        8192             COM
ffffe60565925080     10         8    20480      204800             Terminal-Services-LSM
ffffe60565956080     10         9    20480      204800             Terminal-Services-RCM
ffffe6055eba39c0     50        49     3072      153600             UserMgr
ffffe60567388280      2         2    32768       65536             WFP-IPsec Diagnostics
ffffe605678a3040      5         3     4096       20480             MpWppTracing-20200424-092923-00000003-ffffffff
ffffe60567e35080      2         1    65536      131072             ScreenOnPowerStudyTraceSession
ffffe605655e0a00      5         3     4096       20480             SHS-04242020-092951-7-7f
ffffe605692054c0      4         4     8192       32768             RdpIdd
ffffe60567f597c0      4         3    65536      262144             SgrmEtwSession
ffffe605678a9a00      4         4     8192       32768             DispBrok-DeskSrv
ffffe60569286680      4         4     8192       32768             DispBrok-Desk
ffffe605668026c0      4         4     8192       32768             DispBrok
================ ====== ========= ======== =========== ==========
                    195       159             6651904     143360

0: kd> !wmitrace.logdump IddCx
(WmiTrace) LogDump for Logger Id 0x13
Found Buffers: 5 Messages: 537, sorting entries
[1]0EF8.0CF0::04/24/2020-09:43:36.894 [cx][IddCx]DriverEntry: Enter
[1]0EF8.0CF0::04/24/2020-09:43:36.897 [cx][IddCx]?IddCxLibraryInitialize@@YAJXZ: Enter
[1]0EF8.0CF0::04/24/2020-09:43:36.897 [cx][IddCx]?IddCxLibraryInitialize@@YAJXZ: Exit
[1]0EF8.0CF0::04/24/2020-09:43:36.897 [cx][IddCx]DriverEntry: Exit, status=STATUS_SUCCESS
[0]0EF8.0CF0::04/24/2020-09:43:36.904 [cx][IddCx]?IddCxLibraryBindClient@@YAJPEAU_WDF_CLASS_BIND_INFO@@PEAPEAX@Z: Enter
[0]0EF8.0CF0::04/24/2020-09:43:36.904 [cx][IddCx]?IddCxLibraryBindClient@@YAJPEAU_WDF_CLASS_BIND_INFO@@PEAPEAX@Z: Exit, status=STATUS_SUCCESS
[0]0EF8.0CF0::04/24/2020-09:43:36.910 [cx][IddCx]IddCxImplDeviceInitConfig: Enter
[0]0EF8.0CF0::04/24/2020-09:43:36.910 [cx][IddCx]IddCxImplDeviceInitConfig: Exit, status=STATUS_SUCCESS
[0]0EF8.0CF0::04/24/2020-09:43:36.910 [cx][IddCx]IddCxImplGetVersion: Enter
[0]0EF8.0CF0::04/24/2020-09:43:36.910 [cx][IddCx]IddCxImplGetVersion: Exit, status=STATUS_SUCCESS
[0]0EF8.0CF0::04/24/2020-09:43:36.911 [cx][IddCx]IddCxImplDeviceInitialize: Enter
[0]0EF8.0CF0::04/24/2020-09:43:36.912 [cx][IddCx]IddCxImplDeviceInitialize: New IddDevice 0x000001642F5E0770 created
[0]0EF8.0CF0::04/24/2020-09:43:36.912 [cx][IddCx]IddCxImplDeviceInitialize: Exit, status=STATUS_SUCCESS
[0]0EF8.0CF0::04/24/2020-09:43:36.917 [cx][IddCx]IddCxImplAdapterInitAsync: Enter
[0]0EF8.0CF0::04/24/2020-09:43:36.917 [cx][IddCx]?Init@IddAdapter@@QEAAXPEAUIDDCX_ADAPTER__@@PEAVIddDevice@@PEAUIDDCX_ADAPTER_CAPS@@@Z: New IddAdapter 0x000001642F5E77D0 created, API object 0xFFFFFE9BD0A18978, IddDevice 0x000001642F5E0770
[0]0EF8.0CF0::04/24/2020-09:43:36.917 [cx][IddCx]?SendUserModeMessage@IddAdapter@@QEAAJIPEAXI0W4DXGK_IDD_ESCAPE_CODE@@PEAI@Z: Sending escape 0x0 to kernel
Unknown( 76): GUID=ac5ec775-ccdb-3c2c-6150-28b4eacacbc4 (No Format Information found).
[0]0EF8.0CF0::04/24/2020-09:43:36.917 [cx][IddCx]IddCxImplAdapterInitAsync: Exit, status=STATUS_SUCCESS
[0]0EF8.0558::04/24/2020-09:43:36.935 [cx][IddCx]?HandleKernelModeMessage@IddAdapter@@QEAAXIPEAXI0PEAI@Z: IddAdapter 0x000001642F5E77D0, processing command START_ADAPTER_COMPLETE from KMD
[0]0EF8.0558::04/24/2020-09:43:36.935 [cx][IddCx]?HandleKernelModeMessage@IddAdapter@@QEAAXIPEAXI0PEAI@Z: IddAdapter 0x000001642F5E77D0, Successful adapter start, Wddm Luid = 0xe6e90, Adapter caps 0x0, Session Id 0, Terminal Luid 0x0
[0]0EF8.0558::04/24/2020-09:43:36.935 [cx][IddCx]?HandleKernelModeMessage@IddAdapter@@QEAAXIPEAXI0PEAI@Z: Exit
[0]0EF8.1588::04/24/2020-09:43:36.936 [cx][IddCx]<lambda_e42696d61f3ea0fd0d39fdb90d856b7b>::operator(): DDI: Calling EvtIddCxAdapterInitFinished DDI, IddAdapter 0xFFFFFE9BD0A18978
[0]0EF8.1588::04/24/2020-09:43:36.936 [cx][IddCx]IddCxImplMonitorCreate: Enter
[0]0EF8.1588::04/24/2020-09:43:36.936 [cx][IddCx]IddCxImplMonitorCreate: New IddMonitor 0x000001642F5EF720 created, API object 0xFFFFFE9BD0A11A38, IddAdapter 0x000001642F5E77D0
[0]0EF8.1588::04/24/2020-09:43:36.936 [cx][IddCx]IddCxImplMonitorCreate: Exit, status=STATUS_SUCCESS
[0]0EF8.1588::04/24/2020-09:43:36.936 [cx][IddCx]IddCxImplMonitorArrival: Enter
[0]0EF8.1588::04/24/2020-09:43:36.936 [cx][IddCx]?StartWatchInternal@IddWatchdog@@AEAAXK@Z: IddWatchdog 0x000001642F5E77F0, still has pending watch not started by watchdog thread.
[0]0EF8.1588::04/24/2020-09:43:36.936 [cx][IddCx]?ParseMonitorDescription@IddDevice@@QEAAXUIDDCX_MONITOR_DESCRIPTION@@AEAV?$vector@UIDDCX_MONITOR_MODE@@V?$allocator@UIDDCX_MONITOR_MODE@@@std@@@std@@AEAI@Z: DDI: Calling EvtIddCxParseMonitorDescriptio DDI to get mode count, Device 0x000001642F5E0770
[0]0EF8.1588::04/24/2020-09:43:36.936 [cx][IddCx]?ParseMonitorDescription@IddDevice@@QEAAXUIDDCX_MONITOR_DESCRIPTION@@AEAV?$vector@UIDDCX_MONITOR_MODE@@V?$allocator@UIDDCX_MONITOR_MODE@@@std@@@std@@AEAI@Z: DDI: Return successfully from EvtIddCxParseMonitorDescriptio DDI to get mode count, mode count 23
[0]0EF8.1588::04/24/2020-09:43:36.936 [cx][IddCx]?StartWatchInternal@IddWatchdog@@AEAAXK@Z: IddWatchdog 0x000001642F5E77F0, still has pending watch not started by watchdog thread.
[0]0EF8.1588::04/24/2020-09:43:36.936 [cx][IddCx]?StartWatchInternal@IddWatchdog@@AEAAXK@Z: IddWatchdog 0x000001642F5E77F0, still has pending watch not started by watchdog thread.
[0]0EF8.1588::04/24/2020-09:43:36.936 [cx][IddCx]?ParseMonitorDescription@IddDevice@@QEAAXUIDDCX_MONITOR_DESCRIPTION@@AEAV?$vector@UIDDCX_MONITOR_MODE@@V?$allocator@UIDDCX_MONITOR_MODE@@@std@@@std@@AEAI@Z: DDI: Calling EvtIddCxParseMonitorDescriptio DDI to get modes, Device 0x000001642F5E0770
[0]0EF8.1588::04/24/2020-09:43:36.936 [cx][IddCx]?ParseMonitorDescription@IddDevice@@QEAAXUIDDCX_MONITOR_DESCRIPTION@@AEAV?$vector@UIDDCX_MONITOR_MODE@@V?$allocator@UIDDCX_MONITOR_MODE@@@std@@@std@@AEAI@Z: DDI: Return successfully from EvtIddCxParseMonitorDescriptio DDI to get modes
[0]0EF8.1588::04/24/2020-09:43:36.936 [cx][IddCx]?StartWatchInternal@IddWatchdog@@AEAAXK@Z: IddWatchdog 0x000001642F5E77F0, still has pending watch not started by watchdog thread.
[0]0EF8.1588::04/24/2020-09:43:36.936 [cx][IddCx]?AddMonitorModes@IddMonitor@@AEAAXAEAV?$vector@UTARGET_MONITOR_MODE@@V?$allocator@UTARGET_MONITOR_MODE@@@std@@@std@@@Z: IddMonitor 0x000001642F5EF720, parseMonitorDescription returned 23 modes.
[0]0EF8.1588::04/24/2020-09:43:36.936 [cx][IddCx]?StartWatchInternal@IddWatchdog@@AEAAXK@Z: IddWatchdog 0x000001642F5E77F0, still has pending watch not started by watchdog thread.
[0]0EF8.1588::04/24/2020-09:43:36.936 [cx][IddCx]?QueryModes@IddMonitor@@AEAAXAEAV?$vector@UIDDCX_TARGET_MODE@@V?$allocator@UIDDCX_TARGET_MODE@@@std@@@std@@@Z: DDI: Calling EvtIddCxMonitorQueryTargetModes DDI for mode count, IddMonitor 0x000001642F5EF720
[0]0EF8.1588::04/24/2020-09:43:36.936 [cx][IddCx]?QueryModes@IddMonitor@@AEAAXAEAV?$vector@UIDDCX_TARGET_MODE@@V?$allocator@UIDDCX_TARGET_MODE@@@std@@@std@@@Z: DDI: Return successfully from EvtIddCxMonitorQueryTargetModes DDI, mode count = 0x23
[0]0EF8.1588::04/24/2020-09:43:36.936 [cx][IddCx]?StartWatchInternal@IddWatchdog@@AEAAXK@Z: IddWatchdog 0x000001642F5E77F0, still has pending watch not started by watchdog thread.
[0]0EF8.1588::04/24/2020-09:43:36.936 [cx][IddCx]?StartWatchInternal@IddWatchdog@@AEAAXK@Z: IddWatchdog 0x000001642F5E77F0, still has pending watch not started by watchdog thread.
[0]0EF8.1588::04/24/2020-09:43:36.936 [cx][IddCx]?QueryModes@IddMonitor@@AEAAXAEAV?$vector@UIDDCX_TARGET_MODE@@V?$allocator@UIDDCX_TARGET_MODE@@@std@@@std@@@Z: DDI: Calling EvtIddCxMonitorQueryTargetModes DDI to get modes, IddMonitor 0x000001642F5EF720
[0]0EF8.1588::04/24/2020-09:43:36.936 [cx][IddCx]?QueryModes@IddMonitor@@AEAAXAEAV?$vector@UIDDCX_TARGET_MODE@@V?$allocator@UIDDCX_TARGET_MODE@@@std@@@std@@@Z: DDI: Return successfully from EvtIddCxMonitorQueryTargetModes DDI
[0]0EF8.1588::04/24/2020-09:43:36.936 [cx][IddCx]?StartWatchInternal@IddWatchdog@@AEAAXK@Z: IddWatchdog 0x000001642F5E77F0, still has pending watch not started by watchdog thread.
[0]0EF8.1588::04/24/2020-09:43:36.936 [cx][IddCx]?AddTargetModes@IddMonitor@@AEAAXAEAV?$vector@UTARGET_MONITOR_MODE@@V?$allocator@UTARGET_MONITOR_MODE@@@std@@@std@@@Z: IddMonitor 0x000001642F5EF720, queryTargetModes returned 23 modes.
[0]0EF8.1588::04/24/2020-09:43:55.341 [cx][IddCx] Throwing error (Status 0xc000000d(STATUS_INVALID_PARAMETER)) from function Validate in onecoreuap\windows\core\dxkernel\indirectdisplays\classext\cx\ddivalidation.cpp:412, Msg DISPLAYCONFIG_VIDEO_SIGNAL_INFO.AdditionalSignalInfo.vSyncFreqDivider cannot be zero for target mode
Total of 537 Messages from 5 Buffers

```

The last line gives the reason for the failure.

## Indirect display screen capture debug functionality

Starting in [Windows build 25164](/windows-insider/flight-hub/), IddCx has the ability to dump the desktop frame that IddCx passes to the driver. This functionality can be used to debug visual issues. It can be combined with the debug overlays like shading dirty regions of a frame.

As IddCx will look for changes in the debug registry setting for frame capture on every frame, there is a master control value in [IddCxDebugCtrl](#iddcxdebugctrl-values) that controls whether IddCx will check the capture registry value each frame. This ensures there is no performance penalty when disabled.

> [!NOTE]
> This functionality is disabled when the OPM interface is active to the driver.

### Registry values that control the capture

The following registry values are located in **HKLM\System\CurrentControlSet\Control\GraphicsDrivers\IddCxFrameCapture**. This registry folder should be created before the IddCxDebugCtrl value is set.

| Name | Default if missing | Meaning |
| ---- | ------------------ | ------- |
| **TriggerUniqueness**  | 0      | When each IddCx swapchain is called to acquire a new frame it will read this value. If **TriggerUniqueness** is non-zero and different from the previously read value then the below values will be read and frame capture will be enabled. |
| **TargetMask**         | 0xffff | Bitmask, one bit for each target index on the adapter that controls whether the swapchain for that target should be part of this capture sequence. |
| **CaptureCount**       | 10     | Number of frames that each enabled-for-capture IddCx swapchain should capture. |
| **SkipFrames**         | 0      | Number of frames to skip between each captured frame. |
| **CaptureSessionID**   | 0      | The session in which frame capture will be enabled. A value of zero always means the console session. |
| **ScaleFactor**        | 100    | Controls the scale factor used to decide what the dimensions of the captured file, valid values 1-100
| **CaptureFolder**      | *c:\IddCxImages* | Folder where capture files will be written. A *c:\IddCxImages* folder will be created if it doesn't exist. |

The capture parameters are stored per target which allows a capture session to span a mode change on a given target.

If a new non-zero **TriggerUniqueness** value is detected while a monitor object is still capturing frames from a previous capture it will stop the current capture and start the newly triggered one.

### Using REG files to control frame capture

REG files are a good way to control the frame captures. One file can set the initial values and another can update **TriggerUniqueness**.

#### REG file to set initial values

``` Registry
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers]
"IddCxDebugCtrl"=dword:2200

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers\IddCxFrameCapture]
"TriggerUniqueness"=dword:0
```

#### REG file to update TriggerUniqueness

``` Registry
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers\IddCxFrameCapture]
"TriggerUniqueness"=dword:1
```

### File name and format

The captured frames will be in PNG file format with the following file name format:

S<*Session Id, zero for console*>\_Ad<*Hex value of ID adapter LUID*>\_T<*Hex Value of ID target Idx*>\_Frame<*Frame number from IDDCX_METADATA.PresentationFrameNumber*>\_<*Date in mmddyy format*>\_<*Time in hhmmss*>.png

The following are some example file names:

* S0_Ad8ade_T3_Frame2343_020422_173434.png
* S0_Ad8ade_T3_Frame2344_020422_173434.png
* S0_Ad8ade_T3_Frame2345_020422_173435.png

### WPP logging

For each *new* capture session that is started, WPP messages will be logged for each value read in from the registry or set by default.

Each time a frame is captured and written to file, IddCx will add a WPP message that contains the full filename of the image file.

### Example capture setting

#### Capture frames from when a monitor is first connected

The following are the registry values needed in order to capture the first 20 frames of when any monitor is first plugged in, followed by the REG file.

| Registry entry    | Value | Notes |
| --------------    | ----- | ----- |
| CaptureCount      | 20    | Set 20 frames rather than the default 10
| TriggerUniqueness | 1     | Any non-zero value will work as target object starts with zero as store uniqueness

``` Registry
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers\IddCxFrameCapture]
"CaptureCount"=dword:00000014
"TriggerUniqueness"=dword:00000001
```

#### Start capture while monitor is active

Given that the swapchains check for a new uniqueness value when the driver acquires each frame, you should set the **TriggerUniqueness** entry last to ensure all the parameters are read as expected. The following example also halves the file resolution in order to save space and writes the capture files in the *c:\frames* folder.

| Registry entry    | Value | Notes |
| --------------    | ----- | ----- |
| CaptureCount      | 100   | Set 100 frames rather than the default 10 |
| ScaleFactor       | 50    | Set 50% resolution to save space |
| CaptureFolder     | *c:\frames* | Set output folder |
| TriggerUniqueness | 1     | Any non-zero value will work as the target object starts with zero as store uniqueness |

``` Registry
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers\IddCxFrameCapture]
"CaptureCount"=dword:00000014
"CaptureFolder"="c:\\frames"
"ScaleFactor"=dword:00000032
"TriggerUniqueness"=dword:00000001
```

#### Capture 10 frames from second target in remote session 3 with 5 frames between each capture

This capture also uses debug overlay to highlight the dirty regions for each of the frames.

| Registry entry    | Value | Notes |
| --------------    | ----- | ----- |
| IddCxDebugCtrl    | Bit 0x0400 also set | 0x0400 enables dirty region highlighting, 0x2200 bits also required |
| CaptureSessionID  | 3     | Enables capture in remote session 3  |
| TargetMask        | 0x2   | Bit 1 corresponds to target Idx 1 |
| SkipFrames        | 5     | Skip capturing 5 frames between each capture |
| TriggerUniqueness | 1     | Any non-zero value will work as target object starts with zero as store uniqueness |

``` Registry
Windows Registry Editor Version 5.00  

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers]  
"IddCxDebugCtrl"=dword:2600

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers\IddCxFrameCapture]
"CaptureSessionID"=dword:00000003
"TargetMask"=dword:00000002
"SkipFrames"=dword:00000005    
"TriggerUniqueness"=dword:00000001
```
