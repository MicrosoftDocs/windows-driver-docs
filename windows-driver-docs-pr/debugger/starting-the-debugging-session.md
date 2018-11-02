---
title: Starting the Debugging Session
description: Starting the Debugging Session
ms.assetid: 789c61cf-edd2-4354-91a8-87a0a7af28a3
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Starting the Debugging Session


## <span id="ddk_opening_a_crash_dump_dbg"></span><span id="DDK_OPENING_A_CRASH_DUMP_DBG"></span>


In this documentation of how to [control user-mode debugging from the kernel debugger](controlling-the-user-mode-debugger-from-the-kernel-debugger.md), *target application* refers to the user-mode application that is being debugged, *target computer* refers to the computer that contains the target application and the NTSD or CDB process, and *host computer* refers to the computer that contains the kernel debugger.

To begin using this technique, you must do the following. You can do steps 1 and 2 in either order.

1. Start NTSD or CDB on the target computer, with the -d command-line option.

   For example, you can attach to a running process by using the following syntax.

   **ntsd -d \[-y** <em>UserSymbolPath</em>**\] -p** *PID*

   Or, you can start a new process as the target by using the following syntax.

   **ntsd -d \[-y** <em>UserSymbolPath</em>**\]** *ApplicationName*

   If you are installing this as a postmortem debugger, you would use the following syntax.

   **ntsd -d \[-y** <em>UserSymbolPath</em>**\]**

   For more information about this step, see [Debugging a User-Mode Process Using CDB](debugging-a-user-mode-process-using-cdb.md).

2. Start WinDbg or KD on the host computer, as if you were going to debug the target computer, but do not actually break in to the target computer. To use WinDbg, use the following syntax.

   **windbg \[-y** <em>KernelSymbolPath</em>**\] \[-k** <em>ConnectionOptions</em>**\]**

   For more information about this step, see [Live Kernel-Mode Debugging Using WinDbg](performing-kernel-mode-debugging-using-windbg.md).

   **Note**  If you use WinDbg as the kernel debugger, many of the familiar features of WinDbg are not available in this scenario. For example, you cannot use the Locals window, the Disassembly window, or the Call Stack window, and you cannot step through source code. This is because WinDbg is only acting as a viewer for the debugger (NTSD or CDB) running on the target computer.

     

3. If you have not set the user-mode symbol path, set it from the Input&gt; prompt. If you have not set the kernel-mode symbol path, set it from the kd&gt; prompt. For information on how to access these prompts and to switch between modes, see [Switching Modes](switching-modes.md).

If you use CDB, the Command Prompt window that is associated with CDB remains locked and unavailable while debugging continues. If you use NTSD, no additional window is created, even though NTSD has a process ID associated with it on the target computer.

If you want to run the user-mode debugger from the kernel debugger while also using it as a debugging server, see [Combining This Method with Remote Debugging](combining-this-method-with-remote-debugging.md).

 

 





