---
title: Ending a Debugging Session in WinDbg
description: Ending a Debugging Session in WinDbg
ms.assetid: 9C19211B-38CC-482B-B69F-B83B29963B3F
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Ending a Debugging Session in WinDbg


## <span id="Exiting_WinDbg"></span><span id="exiting_windbg"></span><span id="EXITING_WINDBG"></span>Exiting WinDbg


You can exit WinDbg by choosing **Exit** from the **File** menu or by pressing ALT+F4.

If you are performing user-mode debugging, these commands close the application that you are debugging, unless you used the **-pd** command-line option when you started the debugger.

If you are performing kernel-mode debugging, the target computer remains in its current state. This situation enables you to leave the target running or frozen. (If you leave the target frozen, any future connection from a kernel debugger can resume debugging where you left it.)

## <span id="ending_a_user_mode_session_without_exiting"></span><span id="ENDING_A_USER_MODE_SESSION_WITHOUT_EXITING"></span>Ending a User-Mode Session Without Exiting


To end a user-mode debugging session, return the debugger to dormant mode, and close the target application, you can use the following methods:

-   Enter the [**.kill (Kill Process)**](-kill--kill-process-.md) command.

-   Enter the [**q (Quit)**](q--qq--quit-.md) command (unless you started the debugger with the **-pd** option).

-   Choose **Stop Debugging** from the **Debug** menu.
-   Press SHIFT+F5.

-   Click the **Stop Debugging** button (![screen shot of the stop debugging button ](images/tbstop.png)) on the toolbar

To end a user-mode debugging session, return the debugger to dormant mode, and set the target application running again, you can use the following methods:

-   Enter the [**.detach (Detach from Process)**](-detach--detach-from-process-.md) command. If you are debugging multiple targets, this command detaches from the current target and continues the debugging session with the remaining targets.

-   Choose **Detach Debugee** from the **Debug** menu. If you are debugging multiple targets, this command detaches from all current targets.

-   Enter the [**qd (Quit and Detach)**](qd--quit-and-detach-.md) command.

-   Enter the [**q (Quit)**](q--qq--quit-.md) command, if you started the debugger with the **-pd** option.

To end a user-mode debugging session, return the debugger to dormant mode, but leave the target application in the debugging state, you can use the following method:

-   Enter the [**.abandon (Abandon Process)**](-abandon--abandon-process-.md) command.

For information about reattaching to the target, see [Reattaching to the Target Application](reattaching-to-the-target-application.md).

## <span id="Ending_a_Kernel-Mode_Session_Without_Exiting"></span><span id="ending_a_kernel-mode_session_without_exiting"></span><span id="ENDING_A_KERNEL-MODE_SESSION_WITHOUT_EXITING"></span>Ending a Kernel-Mode Session Without Exiting


To end a kernel-mode debugging session, return the debugger to dormant mode, and leave the target computer frozen, you can use the following methods:

-   Enter the [**q (Quit)**](q--qq--quit-.md) command (unless you started the debugger with the **-pd** option)

-   Choose **Stop Debugging** from the **Debug** menu.
-   Press SHIFT+F5.

-   Click the **Stop debugging (Shift+F5)** button (![screen shot of the stop debugging button ](images/tbstop.png)) on the toolbar.

When a WinDbg session ends, you are prompted to save the workspace for the current session, and then WinDbg returns to dormant mode. At this point, you can use all starting options. That is, you can start to debug a running process, spawn a new process, attach to a target computer, open a crash dump, or connect to a remote debugging session.

 

 





