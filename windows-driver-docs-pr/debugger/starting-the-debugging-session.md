---
title: Starting the Debugging Session
description: Starting the Debugging Session
ms.assetid: 789c61cf-edd2-4354-91a8-87a0a7af28a3
---

# Starting the Debugging Session


## <span id="ddk_opening_a_crash_dump_dbg"></span><span id="DDK_OPENING_A_CRASH_DUMP_DBG"></span>


In this documentation of how to [control user-mode debugging from the kernel debugger](controlling-the-user-mode-debugger-from-the-kernel-debugger.md), *target application* refers to the user-mode application that is being debugged, *target computer* refers to the computer that contains the target application and the NTSD or CDB process, and *host computer* refers to the computer that contains the kernel debugger.

To begin using this technique, you must do the following. You can do steps 1 and 2 in either order.

1.  Start NTSD or CDB on the target computer, with the -d command-line option.

    For example, you can attach to a running process by using the following syntax.

    **ntsd -d \[-y** *UserSymbolPath***\] -p** *PID*

    Or, you can start a new process as the target by using the following syntax.

    **ntsd -d \[-y** *UserSymbolPath***\]** *ApplicationName*

    If you are installing this as a postmortem debugger, you would use the following syntax.

    **ntsd -d \[-y** *UserSymbolPath***\]**

    For more information about this step, see [Debugging a User-Mode Process Using CDB](debugging-a-user-mode-process-using-cdb.md).

2.  Start WinDbg or KD on the host computer, as if you were going to debug the target computer, but do not actually break in to the target computer. To use WinDbg, use the following syntax.

    **windbg \[-y** *KernelSymbolPath***\] \[-k** *ConnectionOptions***\]**

    For more information about this step, see [Live Kernel-Mode Debugging Using WinDbg](performing-kernel-mode-debugging-using-windbg.md).

    **Note**  If you use WinDbg as the kernel debugger, many of the familiar features of WinDbg are not available in this scenario. For example, you cannot use the Locals window, the Disassembly window, or the Call Stack window, and you cannot step through source code. This is because WinDbg is only acting as a viewer for the debugger (NTSD or CDB) running on the target computer.

     

3.  If you have not set the user-mode symbol path, set it from the Input&gt; prompt. If you have not set the kernel-mode symbol path, set it from the kd&gt; prompt. For information on how to access these prompts and to switch between modes, see [Switching Modes](switching-modes.md).

If you use CDB, the Command Prompt window that is associated with CDB remains locked and unavailable while debugging continues. If you use NTSD, no additional window is created, even though NTSD has a process ID associated with it on the target computer.

If you want to run the user-mode debugger from the kernel debugger while also using it as a debugging server, see [Combining This Method with Remote Debugging](combining-this-method-with-remote-debugging.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Starting%20the%20Debugging%20Session%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




