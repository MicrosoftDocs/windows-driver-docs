---
title: Remote Debugging
description: This topic provides an overview of remote user-mode debugging. This involves two computers the client and the server.
keywords: remote debugging
ms.date: 05/23/2017
ms.topic: concept-article
---

# Remote Debugging

Remote user-mode debugging involves two computers: the *client* and the *server*. The server is the computer that runs the application to be debugged. The server also runs the user-mode debugger or a process server. The client is the computer that remotely controls the debugging session.

Remote kernel-mode debugging involves three computers: the *client*, the *server*, and the *target computer*. The target computer is the computer to be debugged. The server is a computer that runs the kernel debugger or a KD connection server. The client is the computer that remotely controls the debugging session.

> [!IMPORTANT]
> There are important security considerations when using remote debugging. For more information, including information on enabling secure mode, see [Security During Remote Debugging](security-during-remote-debugging.md) and [Security Considerations for Windows Debugging Tools](security-considerations.md).

[Choosing the Best Remote Debugging Method](choosing-the-best-remote-debugging-method.md)

[Remote Debugging Through the Debugger](remote-debugging-through-the-debugger.md)

[Controlling the User-Mode Debugger from the Kernel Debugger](controlling-the-user-mode-debugger-from-the-kernel-debugger.md)

[Remote Debugging Through Remote.exe](remote-debugging-through-remote-exe.md)

[Process Servers (User Mode)](process-servers--user-mode-.md)

[KD Connection Servers (Kernel Mode)](kd-connection-servers--kernel-mode-.md)

[Repeaters](repeaters.md)

[Advanced Remote Debugging Scenarios](advanced-remote-debugging-scenarios.md)


 

 