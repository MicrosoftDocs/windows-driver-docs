---
title: Bug Check 0x116 VIDEO_TDR_FAILURE
description: The VIDEO_TDR_FAILURE bug check has a value of 0x00000116. This value indicates that an attempt to reset the display driver and recover from a timeout failed.
keywords: ["Bug Check 0x116 VIDEO_TDR_FAILURE","VIDEO_TDR_FAILURE", "VIDEO_TDR_ERROR"]
ms.date: 12/08/2022
topic_type:
- apiref
ms.topic: reference
api_name:
- VIDEO_TDR_FAILURE
api_type:
- NA
---

# Bug Check 0x116: VIDEO_TDR_FAILURE

The VIDEO_TDR_FAILURE bug check has a value of 0x00000116. This bug check indicates that an attempt to reset the display driver and recover from a timeout has failed.

> [!IMPORTANT]
> This article is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

## VIDEO_TDR_FAILURE parameters

|Parameter|Description|
|--- |--- |
|1|The pointer to the internal TDR recovery context, if available.|
|2|A pointer into the responsible device driver module (for example, the owner tag).|
|3|The error code of the last failed operation, if available.|
|4|Internal context dependent data, if available.|

## Cause

A common stability problem in graphics occurs when the system appears completely frozen or hung while processing an end-user command or operation. Usually the GPU is busy processing intensive graphics operations, typically during gameplay. No screen updates occur, and users assume that their system is frozen. Users usually wait a few seconds and then reboot the system by pressing the power button. Windows tries to detect these problematic hang situations and dynamically recover a responsive desktop.

This process of detection and recovery is known as Timeout Detection and Recovery (TDR). The default timeout is 2 seconds. In the TDR process for video cards, the operating system's GPU scheduler calls the display miniport driver's [DxgkDdiResetFromTimeout](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_resetfromtimeout) function to reinitialize the driver and reset the GPU.

During this process, the operating system tells the driver not to access the hardware or memory and gives it a short time for currently running threads to complete. If the threads don't complete within the timeout, the system bug checks with 0x116 VIDEO_TDR_FAILURE. For more information, see [Thread Synchronization and TDR](../display/thread-synchronization-and-tdr.md).

The system can also bug check with VIDEO_TDR_FAILURE if multiple TDR events occur in a short period of time. The default amount is more than five TDRs in one minute.

If the recovery process is successful, a message will be displayed, indicating that the "Display driver stopped responding and has recovered."

For more information, see [Timeout detection and recovery (TDR)](../display/timeout-detection-and-recovery.md), [TDR registry keys](../display/tdr-registry-keys.md), and [TDR changes in Windows 8 and later](../display/tdr-changes-in-windows-8.md).

## Resolution

The GPU is taking more time than permitted to display graphics to your monitor. This behavior can occur for one or more of the following reasons:

- You may need to install the latest updates for your display driver, so it properly supports the TDR process.
- Hardware issues that affect the ability of the video card to operate properly, including:
  - Over-clocked components, such as the motherboard
  - Incorrect component compatibility and settings (especially memory configuration and timings)
  - Insufficient system cooling
  - Insufficient system power
  - Defective parts (memory modules, motherboards, etc.)
- Visual effects, or too many programs running in the background may be slowing your PC down, so the video card can't respond as necessary.

The [!analyze](../debuggercmds/-analyze.md) debug extension displays information about the bug check and can be helpful in determining the root cause.

```dbgcmd
1: kd> !analyze -v
*******************************************************************************
*                                                                             *
*                        Bugcheck Analysis                                    *
*                                                                             *
*******************************************************************************

VIDEO_TDR_FAILURE (116)
Attempt to reset the display driver and recover from timeout failed.
Arguments:
Arg1: ffffe000c2c404c0, Optional pointer to internal TDR recovery context (TDR_RECOVERY_CONTEXT).
Arg2: fffff8016470c14c, The pointer into responsible device driver module (e.g. owner tag).
Arg3: ffffffffc000009a, Optional error code (NTSTATUS) of the last failed operation.
Arg4: 0000000000000004, Optional internal context dependent data.

...
```

The faulting module name is also shown.

```dbgcmd
MODULE_NAME: nvlddmkm

IMAGE_NAME:  nvlddmkm.sys
```

You can use the [lm (List Loaded Modules)](../debuggercmds/lm--list-loaded-modules-.md) command to display information about the faulting driver, including the timestamp.

```dbgcmd
1: kd> lmvm nvlddmkm
Browse full module list
start             end                 module name
fffff801`63ec0000 fffff801`649a7000   nvlddmkm T (no symbols)           
    Loaded symbol image file: nvlddmkm.sys
    Image path: \SystemRoot\system32\DRIVERS\nvlddmkm.sys
    Image name: nvlddmkm.sys
    Browse all global symbols  functions  data
    Timestamp:        Wed Jul  8 15:43:44 2015 (559DA7A0)
    CheckSum:         00AA7491
    ImageSize:        00AE7000
    Translations:     0000.04b0 0000.04e4 0409.04b0 0409.04e4
```

Parameter 1 contains a pointer to the TDR_RECOVERY_CONTEXT. As shown in the !analyze output, if you have symbols for the associated code, you can use the `dt` command to display this data.

```dbgcmd
1: kd> dt dxgkrnl!_TDR_RECOVERY_CONTEXT ffffe000c2c404c0
   +0x000 Signature        : 0x52445476
   +0x008 pState           : 0xffffe000`c2b12a40 ??
   +0x010 TimeoutReason    : 9 ( TdrEngineTimeoutPromotedToAdapterReset )
   +0x018 Tick             : _ULARGE_INTEGER 0xb2
   +0x020 pAdapter         : 0xffffe000`c2a89010 DXGADAPTER
   +0x028 pVidSchContext   : (null) 
   +0x030 GPUTimeoutData   : _TDR_RECOVERY_GPU_DATA
   +0x048 CrtcTimeoutData  : _TDR_RECOVERY_CONTEXT::<unnamed-type-CrtcTimeoutData>
   +0x050 pProcessName     : (null) 
   +0x058 DbgOwnerTag      : 0xfffff801`6470c14c
   +0x060 PrivateDbgInfo   : _TDR_DEBUG_REPORT_PRIVATE_INFO
   +0xb00 pDbgReport       : 0xffffe000`c2c3f750 _WD_DEBUG_REPORT
   +0xb08 pDbgBuffer       : 0xffffc000`bd000000 Void
   +0xb10 DbgBufferSize    : 0x37515
   +0xb18 pDumpBufferHelper : (null) 
   +0xb20 pDbgInfoExtension : 0xffffc000`ba7e47a0 _DXGKARG_COLLECTDBGINFO_EXT
   +0xb28 pDbgBufferUpdatePrivateInfo : 0xffffc000`bd000140 Void
   +0xb30 ReferenceCount   : 0n1
   +0xb38 pResetCompletedEvent : (null) 
```

Parameter 2 contains a pointer into the responsible device driver module (for example, the owner tag).

```dbgcmd
1: kd> ub fffff8016470c14c
nvlddmkm+0x84c132:
fffff801`6470c132 cc              int     3
fffff801`6470c133 cc              int     3
fffff801`6470c134 48ff254d2deaff  jmp     qword ptr [nvlddmkm+0x6eee88 (fffff801`645aee88)]
fffff801`6470c13b cc              int     3
fffff801`6470c13c 48ff252d2eeaff  jmp     qword ptr [nvlddmkm+0x6eef70 (fffff801`645aef70)]
fffff801`6470c143 cc              int     3
fffff801`6470c144 48ff257d2deaff  jmp     qword ptr [nvlddmkm+0x6eeec8 (fffff801`645aeec8)]
fffff801`6470c14b cc              int     3
```

You may wish to examine the stack trace by using the [k, kb, kc, kd, kp, kP, kv (Display Stack Backtrace)](../debuggercmds/k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) command.

```dbgcmd
1: kd> k
 # Child-SP          RetAddr           Call Site
00 ffffd001`7d53d918 fffff801`61ba2b4c nt!KeBugCheckEx [d:\th\minkernel\ntos\ke\amd64\procstat.asm @ 122]
01 ffffd001`7d53d920 fffff801`61b8da0e dxgkrnl!TdrBugcheckOnTimeout+0xec [d:\th\windows\core\dxkernel\dxgkrnl\core\dxgtdr.cxx @ 2731]
02 ffffd001`7d53d960 fffff801`61b8dd7f dxgkrnl!ADAPTER_RENDER::Reset+0x15e [d:\th\windows\core\dxkernel\dxgkrnl\core\adapter.cxx @ 19443]
03 ffffd001`7d53d990 fffff801`61ba2385 dxgkrnl!DXGADAPTER::Reset+0x177 [d:\th\windows\core\dxkernel\dxgkrnl\core\adapter.cxx @ 19316]
04 ffffd001`7d53d9e0 fffff801`63c5fba7 dxgkrnl!TdrResetFromTimeout+0x15 [d:\th\windows\core\dxkernel\dxgkrnl\core\dxgtdr.cxx @ 2554]
05 ffffd001`7d53da10 fffff801`63c47e5d dxgmms1!VidSchiRecoverFromTDR+0x11b [d:\th\windows\core\dxkernel\dxgkrnl\dxgmms1\vidsch\vidscher.cxx @ 1055]
06 ffffd001`7d53dbc0 fffff801`aa55c698 dxgmms1!VidSchiWorkerThread+0x8d [d:\th\windows\core\dxkernel\dxgkrnl\dxgmms1\vidsch\vidschi.cxx @ 426]
07 ffffd001`7d53dc00 fffff801`aa5c9306 nt!PspSystemThreadStartup+0x58 [d:\th\minkernel\ntos\ps\psexec.c @ 6845]
08 ffffd001`7d53dc60 00000000`00000000 nt!KxStartSystemThread+0x16 [d:\th\minkernel\ntos\ke\amd64\threadbg.asm @ 80]
```

You can also set a breakpoint in the code leading up to this stop code and attempt to single step forward into the faulting code, if you can consistently reproduce the stop code.

For more information, see [Analyze crash dump files by using WinDbg](crash-dump-files.md).

If you aren't equipped to use the Windows debugger to work on this problem, you can use some basic troubleshooting techniques.

- Check the System Log in Event Viewer for other error messages that might help identify the device or driver that is causing this bug check.

- If a driver is identified in the bug check message, disable the driver or check with the manufacturer for driver updates.

- Verify that all graphics related software, such as DirectX and OpenGL, are up to date, and any graphics intensive applications (such as games) are fully patched.

- Confirm that any new hardware that's installed is compatible with the installed version of Windows. For example, you can get information about required hardware at [Windows 10 Specifications](https://www.microsoft.com/windows/windows-10-specifications).

- Run the Windows Memory Diagnostics tool to test the memory. In the control panel search box, enter **Memory**, and then select **Diagnose your computer's memory problems**.‌ After the test is run, use Event viewer to view the results under the System log. Look for the *MemoryDiagnostics-Results* entry to view the results.

- You can try running the hardware diagnostics supplied by the system manufacturer.

- Use Safe Mode

    Consider using Safe Mode to help isolate this issue. Using Safe Mode loads only the minimum required drivers and system services during the Windows startup.  
    1. To enter Safe Mode, go to **Update and Security** in Settings.  
    2. Select **Recovery** &gt; **Advanced startup** to boot to maintenance mode.  
    3. At the resulting menu, choose **Troubleshoot** &gt; **Advanced Options** &gt; **Startup Settings** &gt; **Restart**.  
    4. After Windows restarts to the **Startup Settings** screen, select option, 4, 5 or 6 to boot to Safe Mode.

    Safe Mode may be available by pressing a function key on boot, for example F8. Refer to information from the manufacturer for specific startup options.

For general troubleshooting information, see [Blue Screen Data](blue-screen-data.md).

## Remarks

For information about requirements that hardware devices must meet when they implement TDR, see [Windows Hardware Lab Kit](/windows-hardware/test/hlk/) documentation. For example, [TDR2 - Standard Two Device Test Graphics](/windows-hardware/test/hlk/testref/575d868d-b89a-48f7-b356-1c9f8c371a6f).

## See also

[Bug Check Code Reference](bug-check-code-reference2.md)
