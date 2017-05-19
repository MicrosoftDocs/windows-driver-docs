---
title: Remote Debugging
description: This topic provides an overview of remote user-mode debugging. This involves two computers: the client and the server.
ms.assetid: fa87b55c-c339-4b8c-8614-c7355d203a6e
keywords: ["remote debugging"]
---

# Remote Debugging


## <span id="ddk_remote_debugging_dbg"></span><span id="DDK_REMOTE_DEBUGGING_DBG"></span>


Remote user-mode debugging involves two computers: the *client* and the *server*. The server is the computer that runs the application to be debugged. The server also runs the user-mode debugger or a process server. The client is the computer that remotely controls the debugging session.

Remote kernel-mode debugging involves three computers: the *client*, the *server*, and the *target computer*. The target computer is the computer to be debugged. The server is a computer that runs the kernel debugger or a KD connection server. The client is the computer that remotely controls the debugging session.

[Choosing the Best Remote Debugging Method](choosing-the-best-remote-debugging-method.md)

[Remote Debugging Through the Debugger](remote-debugging-through-the-debugger.md)

[Controlling the User-Mode Debugger from the Kernel Debugger](controlling-the-user-mode-debugger-from-the-kernel-debugger.md)

[Remote Debugging Through Remote.exe](remote-debugging-through-remote-exe.md)

[Process Servers (User Mode)](process-servers--user-mode-.md)

[KD Connection Servers (Kernel Mode)](kd-connection-servers--kernel-mode-.md)

[Repeaters](repeaters.md)

[Advanced Remote Debugging Scenarios](advanced-remote-debugging-scenarios.md)

[Remote Debugging on Workgroup Computers](remote-debugging-on-workgroup-computers.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Remote%20Debugging%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




