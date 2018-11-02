---
title: Debugging the Service Application Automatically
description: Debugging the Service Application Automatically
ms.assetid: 3168b5c1-30fa-4ff5-b871-736dcdeb8f31
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Debugging the Service Application Automatically


A debugger can be launched automatically when the service application starts up. Alternatively, it can be launched automatically when the service application encounters an exception or executes a **DebugBreak** command. If you have chosen one of these methods, this topic explains how to proceed. If you are not sure which method to choose, see [Choosing the Best Method](choosing-the-best-method.md).

Then use the following procedure:

1.  Do one of the following preparatory steps:
    -   If you plan to debug the service application from the very beginning, including its initialization code, follow the procedure described in Enabling the Debugging of the Initialization Code. Alternatively, if you want the service application to break into the debugger when it crashes or encounters an exception, follow the procedure described in Enabling the Service Application to Break Into the Debugger.
    -   To assure that the service application will allow the debugger to run properly, perform the procedure described in [Adjusting the Service Application Timeout](preparing-to-debug-the-service-application.md#adjusting-the-service-application-timeout).
    -   If the service is combined with other services in a single SvcHost process, perform the procedure described in Isolating the Service.

2.  If the service is already running, you must restart it for these changes to take effect. We recommend that you restart Windows itself, in order to remove any effects of the running service. If you do not want to restart Windows, use the following commands, where *ServiceName* is the name of the service:

    ```console
    net stop ServiceName 
    net start ServiceName 
    ```

3.  If you have chosen to debug the service application's initialization code, when the service starts, the debugger is launched and attaches to the service application.

    If you have chosen to let the debugger be triggered by an exception, the service application executes normally until it encounters an exception or executes a **DebugBreak** function. At this point, the debugger is launched and attaches to the service application.

4.  The next step depends on the debugger command line you specified during step 1:
    -   If you specified a debugger without any remoting options, this debugger is launched and its window becomes visible.
    -   If you specified NTSD with the -server and -noio options, NTSD is launched without a console window. You can then connect to the debugging session from another computer by starting any user-mode debugger with the -remote parameter. For instructions, see [**Activating a Debugging Client**](activating-a-debugging-client.md).
    -   If you specified NTSD with the -d option, NTSD is launched without a console window. You can then connect to the debugging session by using kernel debugger running on another computer. For instructions, see [Controlling the User-Mode Debugger from the Kernel Debugger](controlling-the-user-mode-debugger-from-the-kernel-debugger.md).
    -   If you specified NTSD with the -ddefer and -server options, NTSD is launched without a console window. You can then connect to the debugging session by using both a kernel debugger and a user-mode remote debugger, running on a different computer than the service (but possibly the same computer as each other). For instructions, see [Combining This Method with Remote Debugging](combining-this-method-with-remote-debugging.md).

5.  When the debugger starts, the service pauses at the initial process breakpoint, the exception, or the **DebugBreak** command. This enables you to examine the current state of the service application, set breakpoints, and make any other desired configuration choices.

6.  Use [**g (Go)**](g--go-.md) or another execution command to resume the execution of the service application.

## <span id="related_topics"></span>Related topics


[DebugBreak function](https://go.microsoft.com/fwlink/p/?linkid=124229)

 

 






