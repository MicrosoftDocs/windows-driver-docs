---
title: Ending a Debugging Session in WinDbg
description: Ending a Debugging Session in WinDbg
ms.assetid: 9C19211B-38CC-482B-B69F-B83B29963B3F
---

# Ending a Debugging Session in WinDbg


## <span id="Exiting_WinDbg"></span><span id="exiting_windbg"></span><span id="EXITING_WINDBG"></span>Exiting WinDbg


You can exit WinDbg by choosing **Exit** from the **File** menu or by pressing ALT+F4.

If you are performing user-mode debugging, these commands close the application that you are debugging, unless you used the **-pd** command-line option when you started the debugger.

If you are performing kernel-mode debugging, the target computer remains in its current state. This situation enables you to leave the target running or frozen. (If you leave the target frozen, any future connection from a kernel debugger can resume debugging where you left it.)

## <span id="ending_a_user_mode_session_without_exiting"></span><span id="ENDING_A_USER_MODE_SESSION_WITHOUT_EXITING"></span>Ending a User-Mode Session Without Exiting


To end a user-mode debugging session, return the debugger to dormant mode, and close the target application, you can use the following methods:

-   Enter the [**.kill (Kill Process)**](https://msdn.microsoft.com/library/windows/hardware/ff563855) command.

-   Enter the [**q (Quit)**](https://msdn.microsoft.com/library/windows/hardware/ff553507) command (unless you started the debugger with the **-pd** option).

-   Choose **Stop Debugging** from the **Debug** menu.
-   Press SHIFT+F5.

-   Click the **Stop Debugging** button (![screen shot of the stop debugging button ](images/tbstop.png)) on the toolbar

To end a user-mode debugging session, return the debugger to dormant mode, and set the target application running again, you can use the following methods:

-   Enter the [**.detach (Detach from Process)**](https://msdn.microsoft.com/library/windows/hardware/ff562334) command. If you are debugging multiple targets, this command detaches from the current target and continues the debugging session with the remaining targets.

-   Choose **Detach Debugee** from the **Debug** menu. If you are debugging multiple targets, this command detaches from all current targets.

-   Enter the [**qd (Quit and Detach)**](https://msdn.microsoft.com/library/windows/hardware/ff553498) command.

-   Enter the [**q (Quit)**](https://msdn.microsoft.com/library/windows/hardware/ff553507) command, if you started the debugger with the **-pd** option.

To end a user-mode debugging session, return the debugger to dormant mode, but leave the target application in the debugging state, you can use the following method:

-   Enter the [**.abandon (Abandon Process)**](https://msdn.microsoft.com/library/windows/hardware/ff561508) command.

For information about reattaching to the target, see [Reattaching to the Target Application](reattaching-to-the-target-application.md).

## <span id="Ending_a_Kernel-Mode_Session_Without_Exiting"></span><span id="ending_a_kernel-mode_session_without_exiting"></span><span id="ENDING_A_KERNEL-MODE_SESSION_WITHOUT_EXITING"></span>Ending a Kernel-Mode Session Without Exiting


To end a kernel-mode debugging session, return the debugger to dormant mode, and leave the target computer frozen, you can use the following methods:

-   Enter the [**q (Quit)**](https://msdn.microsoft.com/library/windows/hardware/ff553507) command (unless you started the debugger with the **-pd** option)

-   Choose **Stop Debugging** from the **Debug** menu.
-   Press SHIFT+F5.

-   Click the **Stop debugging (Shift+F5)** button (![screen shot of the stop debugging button ](images/tbstop.png)) on the toolbar.

When a WinDbg session ends, you are prompted to save the workspace for the current session, and then WinDbg returns to dormant mode. At this point, you can use all starting options. That is, you can start to debug a running process, spawn a new process, attach to a target computer, open a crash dump, or connect to a remote debugging session.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Ending%20a%20Debugging%20Session%20in%20WinDbg%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




