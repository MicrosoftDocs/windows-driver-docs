---
title: Debugging the Service Application Automatically
description: Debugging the Service Application Automatically
ms.assetid: 3168b5c1-30fa-4ff5-b871-736dcdeb8f31
---

# Debugging the Service Application Automatically


A debugger can be launched automatically when the service application starts up. Alternatively, it can be launched automatically when the service application encounters an exception or executes a **DebugBreak** command. If you have chosen one of these methods, this topic explains how to proceed. If you are not sure which method to choose, see [Choosing the Best Method](choosing-the-best-method.md).

Then use the following procedure:

1.  Do one of the following preparatory steps:
    -   If you plan to debug the service application from the very beginning, including its initialization code, follow the procedure described in Enabling the Debugging of the Initialization Code. Alternatively, if you want the service application to break into the debugger when it crashes or encounters an exception, follow the procedure described in Enabling the Service Application to Break Into the Debugger.
    -   To assure that the service application will allow the debugger to run properly, perform the procedure described in [Adjusting the Service Application Timeout](preparing-to-debug-the-service-application.md#adjusting-the-service-application-timeout).
    -   If the service is combined with other services in a single SvcHost process, perform the procedure described in Isolating the Service.

2.  If the service is already running, you must restart it for these changes to take effect. We recommend that you restart Windows itself, in order to remove any effects of the running service. If you do not want to restart Windows, use the following commands, where *ServiceName* is the name of the service:
    ```
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


[DebugBreak function](http://go.microsoft.com/fwlink/p/?linkid=124229)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugging%20the%20Service%20Application%20Automatically%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





