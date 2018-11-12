---
title: Combining This Method with Remote Debugging
description: Combining This Method with Remote Debugging
ms.assetid: 4f9a60ab-b221-4a60-b3d5-cd907e33ec19
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Combining This Method with Remote Debugging


## <span id="ddk_opening_a_crash_dump_dbg"></span><span id="DDK_OPENING_A_CRASH_DUMP_DBG"></span>


It is sometimes useful to [control the user-mode debugger from the kernel debugger](controlling-the-user-mode-debugger-from-the-kernel-debugger.md)and use the user-mode debugger as a [debugging server](remote-debugging-through-the-debugger.md) at the same time.

For example, this configuration is useful when your user-mode symbols are located on a symbol server. In the standard configuration for controlling the user-mode debugger from a kernel debugger, the interaction of the two debuggers can lead to tiny lapses in synchronization, and these lapses can prevent symbol server authentication. The more complex configuration described here can avoid this problem.

**Note**   In describing this scenario, *target application* refers to the user-mode application that is being debugged, *target computer* refers to the computer that contains the target application and the CDB or NTSD process, and *host computer* refers to the computer that contains the kernel debugger.

 

To use this technique, you must do the following:

1.  Start NTSD or CDB on the target computer, with the -ddefer and -server command-line options, specifying the desired transport options. The -server option must be the first parameter on the command line.

    For example, you can attach to a running process by using the following syntax.

    ```console
    ntsd -server ServerTransport -ddefer [-y UserSymbolPath] -p PID 
    ```

    Or, you can start a new process as the target by using the following syntax.

    ```console
    ntsd -server ServerTransport -ddefer [-y UserSymbolPath] ApplicationName 
    ```

    If you are installing this as a postmortem debugger, you would use the following syntax. Note that you must manually edit the registry to install a postmortem debugger that includes the -server parameter; for details, see [Enabling Postmortem Debugging](enabling-postmortem-debugging.md).

    ```console
    ntsd -server ServerTransport -ddefer [-y UserSymbolPath] 
    ```

    For information about the available transport options, see [**Activating a Debugging Server**](activating-a-debugging-server.md).

2.  Start WinDbg or KD on the host computer, as if you were going to debug the target computer, but do not actually break in to the target computer. To use WinDbg, use the following syntax.

    ```console
    windbg [-y KernelSymbolPath] [-k ConnectionOptions] 
    ```

    For more information about this step, see [Live Kernel-Mode Debugging Using WinDbg](performing-kernel-mode-debugging-using-windbg.md)

    .

3.  Start WinDbg or CDB as a debugging client, with the same transport options used to start the server. This debugging client can be run on either the host computer or on a third computer.

    ```console
    cdb -remote ClientTransport 
    ```

    For more information about this step, see [**Activating a Debugging Client**](activating-a-debugging-client.md).

4.  Once the debuggers are running and the `Input>` prompt appears in the kernel debugger, use the [**.sleep (Pause Debugger)**](-sleep--pause-debugger-.md) command to pause the debuggers and let the target computer run for a few seconds. This gives the target computer time to process the remote transport protocol, establishing the connection between the user-mode remote server and the remote client.

If you use CDB as the user-mode debugger, the Command Prompt window that is associated with CDB remains locked and unavailable while debugging continues. If you use NTSD, no additional window is created, even though NTSD has a process ID associated with it on the target computer.

The four modes and the methods of switching between them described in the topic [Switching Modes](switching-modes.md) apply in this combination scenario, with the following differences:

-   There are two different user-mode debugging modes. When the target computer is running, the debugging server is controlled by the debugging client as in any other remote debugging session; this is called *remote-controlled user-mode debugging*. When the kernel-mode debugger is broken in to the target computer and the `Input>` prompt is showing, the user-mode debugger is controlled by the kernel debugger; this is called *kernel-controlled user-mode debugging*.

-   These two modes are never available at the same time. When the kernel debugger is broken in to the target computer, even though the user-mode debugger may be active, the target computer is unable to process the remote transport protocol, and therefore the user-mode debugger will not be able to receive remote input across this connection.

-   If your user-mode symbols are located on a symbol server, any debugger commands that require symbol access should be issued while in remote-controlled user-mode debugging mode.

-   To switch from kernel-controlled user-mode debugging to remote-controlled user-mode debugging, use the [**.sleep (Pause Debugger)**](-sleep--pause-debugger-.md) command. When the user-mode debugger wakes from the sleep command, it will be in remote-controlled user-mode debugging mode.

-   To switch from remote-controlled user-mode debugging to kernel-mode debugging, enter any command from the `Input>` prompt. If this prompt is not visible, switch to kernel-mode debugging, and then use the [**g (Go)**](g--go-.md) command at the `kd>` prompt.

Internally, a user-mode debugger started with -ddefer gives first priority to input from the debugging client, and second priority to input from the kernel debugger. However, there can never be a conflict between simultaneous inputs, because when the kernel debugger has broken in to the target computer, the remote connection is unavailable.

 

 





