---
title: Switching Modes
description: Switching Modes
ms.assetid: 167e5352-4ebc-423d-bf4f-ba1d459b394f
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Switching Modes


## <span id="ddk_opening_a_crash_dump_dbg"></span><span id="DDK_OPENING_A_CRASH_DUMP_DBG"></span>


When you [control user-mode debugging from the kernel debugger](controlling-the-user-mode-debugger-from-the-kernel-debugger.md), you encounter four different modes, and can switch between them in a variety of ways.

**Note**   In describing this scenario, *target application* refers to the user-mode application that is being debugged, *target computer* refers to the computer that contains the target application and the CDB or NTSD process, and *host computer* refers to the computer that contains the kernel debugger.

 

The following four modes will be encountered:

<span id="User-mode_debugging"></span><span id="user-mode_debugging"></span><span id="USER-MODE_DEBUGGING"></span>*User-mode debugging*  
The target computer and target application are frozen. The user-mode debugging prompt appears in the [Debugger Command window](debugger-command-window.md) of the kernel debugger. In WinDbg, the prompt in the lower panel of the WinDbg window displays Input&gt;. You can enter commands at this prompt, as if they are entered during user-mode debugging, to analyze the target application's state or cause it to run or step through its execution. Symbol files, extension DLLs, and other files that the debugger accesses will be those files on the target computer, not the host computer.

<span id="Target_application_execution"></span><span id="target_application_execution"></span><span id="TARGET_APPLICATION_EXECUTION"></span>*Target application execution*  
The target computer is running, the target application is running, and the debugger is waiting. This mode is the same as letting the target run in ordinary debugging.

<span id="Sleep_mode"></span><span id="sleep_mode"></span><span id="SLEEP_MODE"></span>*Sleep mode*  
The target computer is running, but the target application is frozen, and both debuggers are frozen. This mode is useful if you have to do something on the target computer but you do not want to change the state of the debugging session.

<span id="Kernel-mode_debugging"></span><span id="kernel-mode_debugging"></span><span id="KERNEL-MODE_DEBUGGING"></span>*Kernel-mode debugging*  
The target computer and the target application are frozen. The kernel-mode debugging prompt kd&gt; appears in the Debugger Command window of the kernel debugger. This mode is the typical kernel-mode debugging state.

The session begins in user-mode debugging mode. The following actions and events cause the mode to change:

-   To switch from user-mode debugging to target application execution, use the [**g (Go)**](g--go-.md) command at the `Input>` prompt.

-   To temporarily switch from user-mode debugging to target application execution and then return to user-mode debugging, use a step, trace, or other temporary execution command. For a list of such commands, see [Controlling the Target](controlling-the-target.md).

-   To switch from user-mode debugging to sleep mode, use the [**.sleep (Pause Debugger)**](-sleep--pause-debugger-.md) command. This command is timed. When the time expires, the system returns to user-mode debugging.

-   To switch from user-mode debugging to kernel-mode debugging, use the [**.breakin (Break to the Kernel Debugger)**](-breakin--break-to-the-kernel-debugger-.md) command. Note that **.breakin** might fail with an access denied error if the calling process does not have administrator rights. In this case, switch to KD by issuing a short **.sleep** command and pressing CTRL+C.

-   You can switch from target application execution to user-mode debugging only in certain environments. If the target computer is running Microsoft Windows XP or a later version of the Windows operating system, you can use the [**!bpid**](-bpid.md) extension command. If you are using CDB (not NTSD), you can activate the CDB window on the target computer and press CTRL+C.

-   If the target application hits a breakpoint, encounters an exception, encounters some other controlled event, or ends, the system switches from target application execution to user-mode debugging. You should plan such events in advance, especially when you are using NTSD. For more information about these events, see [Using Breakpoints](using-breakpoints2.md) and [Controlling Exceptions and Events](controlling-exceptions-and-events.md).

-   To switch from target application execution to kernel-mode debugging, press CTRL+C in the KD window, press CTRL+BREAK or click **Break** on the **Debug** menu in the WinDbg window, or press SYSRQ or ALT+SYSRQ on the target computer keyboard. (If your kernel debugger is KD and if you press CTRL+C at the same time that the kernel debugger is communicating with the user-mode debugger, the user-mode debugger might capture you pressing CTRL+C.)

-   If the debugger encounters a kernel error or if you use the Breakin.exe tool, the system switches from target application execution to kernel-mode debugging.

-   To switch from sleep mode to user-mode debugging, wait for the sleep time to expire, start a new CDB process on the target computer by using the -wake [**command-line option**](cdb-command-line-options.md), or use the [**.wake (Wake Debugger)**](-wake--wake-debugger-.md) command in a different copy of CDB or NTSD on the target computer.

-   To switch out of kernel-mode debugging, use the [**g (Go)**](g--go-.md) command at the `kd>` prompt. This command returns to user-mode debugging or target application execution (whichever of the two was the most recently-used state).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Switching%20Modes%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




