---
title: Bug Check 0x117 VIDEO_TDR_TIMEOUT_DETECTED
description: The VIDEO_TDR_TIMEOUT_DETECTED bug check has a value of 0x00000117. This indicates that the display driver failed to respond in a timely fashion.
ms.assetid: 70e24a97-f695-4d35-b52f-69dfddecd9b5
keywords: ["Bug Check 0x117 VIDEO_TDR_TIMEOUT_DETECTED", "VIDEO_TDR_TIMEOUT_DETECTED"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- VIDEO_TDR_TIMEOUT_DETECTED
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x117: VIDEO\_TDR\_TIMEOUT\_DETECTED


The VIDEO\_TDR\_TIMEOUT\_DETECTED bug check has a value of 0x00000117. This indicates that the display driver failed to respond in a timely fashion.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## VIDEO\_TDR\_TIMEOUT\_DETECTED Parameters


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>1</p></td>
<td align="left"><p>The pointer to the internal TDR recovery context, if available.</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>A pointer into the responsible device driver module (for example, the owner tag).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>The secondary driver-specific bucketing key.</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Internal context dependent data, if available.</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

A common stability problem in graphics occurs when the system appears completely frozen or hung while processing an end-user command or operation. Usually the GPU is busy processing intensive graphics operations, typically during game-play. No screen updates occur, and users assume that their system is frozen. Users usually wait a few seconds and then reboot the system by pressing the power button. Windows tries to detect these problematic hang situations and dynamically recover a responsive desktop.

This process of detection and recovery is known as Timeout Detection and Recovery (TDR). The default timeout is 2 seconds. In the TDR process for video cards, the operating system's GPU scheduler calls the display miniport driver's [*DxgkDdiResetFromTimeout*](https://msdn.microsoft.com/library/windows/hardware/ff559815) function to reinitialize the driver and reset the GPU.

If the recovery process is successful, a message will be displayed, indicating that the "Display driver stopped responding and has recovered."

For more information, see Timeout Detection and Recovery (TDR), [TDR Registry Keys](https://msdn.microsoft.com/library/windows/hardware/ff569918) and [TDR changes in Windows 8](https://msdn.microsoft.com/library/windows/hardware/jj676805) which are located in [Debugging Tips for the Windows Display Driver Model (WDDM)](https://msdn.microsoft.com/library/windows/hardware/ff551790).

Resolution
----------

The GPU is taking more time than permitted to display graphics to your monitor. This behavior can occur for one or more of the following reasons:

-   You may need to install the latest updates for your display driver, so that it properly supports the TDR process.
-   Hardware issues that impact the ability of the video card to operate properly, including:
    -   Over-clocked components, such as the motherboard
    -   Incorrect component compatibility and settings (especially memory configuration and timings)
    -   Insufficient system cooling
    -   Insufficient system power
    -   Defective parts (memory modules, motherboards, etc.)
-   Visual effects, or too many programs running in the background may be slowing your PC down so that the video card can not respond as necessary.

The [**!analyze**](-analyze.md) debug extension displays information about the bug check and can be very helpful in determining the root cause.

```dbgcmd
3: kd> !analyze -v
*******************************************************************************
*                                                                             *
*                        Bugcheck Analysis                                    *
*                                                                             *
*******************************************************************************

VIDEO_TDR_TIMEOUT_DETECTED (117)
The display driver failed to respond in timely fashion.
(This code can never be used for a real bugcheck.)
Arguments:
Arg1: 8975d500, Optional pointer to internal TDR recovery context (TDR_RECOVERY_CONTEXT).
Arg2: 9a02381e, The pointer into responsible device driver module (e.g owner tag).
Arg3: 00000000, The secondary driver specific bucketing key.
Arg4: 00000000, Optional internal context dependent data.

...
```

Also displayed will be the faulting module name

```dbgcmd
MODULE_NAME: atikmpag

IMAGE_NAME:  atikmpag.sys
```

You can use the lmv command to display information about the faulting driver, including the timestamp.

```dbgcmd
3: kd> lmvm atikmpag
Browse full module list
start    end        module name
9a01a000 9a09a000   atikmpag T (no symbols)           
    Loaded symbol image file: atikmpag.sys
    Image path: atikmpag.sys
    Image name: atikmpag.sys
    Browse all global symbols  functions  data
    Timestamp:        Fri Dec  6 12:20:32 2013 (52A23190)
    CheckSum:         0007E58A
    ImageSize:        00080000
    Translations:     0000.04b0 0000.04e4 0409.04b0 0409.04e4
```

Parameter 1 contains a pointer to the TDR\_RECOVERY\_CONTEXT.

```dbgcmd
3: kd> dt dxgkrnl!_TDR_RECOVERY_CONTEXT fffffa8010041010
   +0x000 Signature        : ??
   +0x004 pState           : ???? 
   +0x008 TimeoutReason    : ??
   +0x010 Tick             : _ULARGE_INTEGER
   +0x018 pAdapter         : ???? 
   +0x01c pVidSchContext   : ???? 
   +0x020 GPUTimeoutData   : _TDR_RECOVERY_GPU_DATA
   +0x038 CrtcTimeoutData  : _TDR_RECOVERY_CONTEXT::<unnamed-type-CrtcTimeoutData>
   +0x040 DbgOwnerTag      : ??
   +0x048 PrivateDbgInfo   : _TDR_DEBUG_REPORT_PRIVATE_INFO
   +0xae0 pDbgReport       : ???? 
   +0xae4 pDbgBuffer       : ???? 
   +0xae8 DbgBufferSize    : ??
   +0xaec pDumpBufferHelper : ???? 
   +0xaf0 pDbgInfoExtension : ???? 
   +0xaf4 pDbgBufferUpdatePrivateInfo : ???? 
   +0xaf8 ReferenceCount   : ??
Memory read error 10041b08
```

Parameter 2 contains a pointer into the responsible device driver module (for example, the owner tag).

```dbgcmd
BUGCHECK_P2: ffffffff9a02381e
```

You may wish to examine the stack trace using the [**k, kb, kc, kd, kp, kP, kv (Display Stack Backtrace)**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) command.

```dbgcmd
3: kd> k
 # ChildEBP RetAddr  
00 81d9ace0 976e605e dxgkrnl!TdrUpdateDbgReport+0x93 [d:\blue_gdr\windows\core\dxkernel\dxgkrnl\core\dxgtdr.cxx @ 944]
01 81d9acfc 976ddead dxgkrnl!TdrCollectDbgInfoStage2+0x195 [d:\blue_gdr\windows\core\dxkernel\dxgkrnl\core\dxgtdr.cxx @ 1759]
02 81d9ad24 976e664f dxgkrnl!DXGADAPTER::Reset+0x23f [d:\blue_gdr\windows\core\dxkernel\dxgkrnl\core\adapter.cxx @ 14972]
03 81d9ad3c 977be9e0 dxgkrnl!TdrResetFromTimeout+0x16 [d:\blue_gdr\windows\core\dxkernel\dxgkrnl\core\dxgtdr.cxx @ 2465]
04 81d9ad50 977b7518 dxgmms1!VidSchiRecoverFromTDR+0x13 [d:\blue_gdr\windows\core\dxkernel\dxgkrnl\dxgmms1\vidsch\vidscher.cxx @ 1018]
05 (Inline) -------- dxgmms1!VidSchiRun_PriorityTable+0xfa71
06 81d9ad70 812c01d4 dxgmms1!VidSchiWorkerThread+0xfaf2 [d:\blue_gdr\windows\core\dxkernel\dxgkrnl\dxgmms1\vidsch\vidschi.cxx @ 424]
07 81d9adb0 81325fb1 nt!PspSystemThreadStartup+0x58 [d:\blue_gdr\minkernel\ntos\ps\psexec.c @ 5884]
08 81d9adbc 00000000 nt!KiThreadStartup+0x15 [d:\blue_gdr\minkernel\ntos\ke\i386\threadbg.asm @ 81]
```

You can also set a breakpoint in the code leading up to this stop code and attempt to single step forward into the faulting code, if you can consistently reproduce the stop code.

For more information see the following topics:

[Crash dump analysis using the Windows debuggers (WinDbg)](crash-dump-files.md)

If you are not equipped to use the Windows debugger to work on this problem, you can use some basic troubleshooting techniques.

-   Check the System Log in Event Viewer for additional error messages that might help identify the device or driver that is causing this bug check.

-   If a driver is identified in the bug check message, disable the driver or check with the manufacturer for driver updates.

-   Verify that all graphics related software such as DirectX and OpenGL are up to date, and any graphics intensive applications (such as games) are fully patched.
-   Confirm that any new hardware that is installed is compatible with the installed version of Windows. For example, you can get information about required hardware at [Windows 10 Specifications](https://www.microsoft.com/windows/windows-10-specifications).

-   **Using Safe Mode**

    Consider using Safe Mode to help isolate this issue. Using Safe Mode loads only the minimum required drivers and system services during the Windows startup. To enter Safe Mode, use **Update and Security** in Settings. Select **Recovery**-&gt;**Advanced startup** to boot to maintenance mode. At the resulting menu, choose **Troubleshoot**-&gt; **Advanced Options** -&gt; **Startup Settings** -&gt; **Restart**. After Windows restarts to the **Startup Settings** screen, select option, 4, 5 or 6 to boot to Safe Mode.

    Safe Mode may be available by pressing a function key on boot, for example F8. Refer to information from the manufacturer for specific startup options.

-   Run the Windows Memory Diagnostics tool, to test the memory. In the control panel search box, type Memory, and then click **Diagnose your computer's memory problems**.‌ After the test is run, use Event viewer to view the results under the System log. Look for the *MemoryDiagnostics-Results* entry to view the results.

-   You can try running the hardware diagnostics supplied by the system manufacturer.

-   For additional general troubleshooting information, see [**Blue Screen Data**](blue-screen-data.md).

Remarks
-------

**Hardware certification requirements**

For information on requirements that hardware devices must meet when they implement TDR, refer to the WHCK documentation on *Device.Graphics…TDRResiliency*.

 

 




