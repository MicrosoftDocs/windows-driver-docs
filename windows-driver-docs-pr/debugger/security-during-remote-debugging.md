---
title: Security During Remote Debugging
description: Security During Remote Debugging
keywords: ["security considerations, remote debugging", "remote debugging through remote.exe, security considerations", "remote debugging through the debugger, security considerations", "process server, security considerations"]
ms.date: 11/26/2024
---

# Security During Remote Debugging

This topic describes different techniques to increase security during remote debugging. 

## Control access to the debugging session

If you are performing [remote debugging through the debugger](remote-debugging-through-the-debugger.md), or using a [process server](process-servers--user-mode-.md) or [KD connection server](kd-connection-servers--kernel-mode-.md), any computer on your local network can attempt to attach to your debugging session.

If you are using the TCP, COM, or named pipe protocols, you can require the debugging client to supply a password. However, this password is not encrypted during transmission, and therefore these protocols are not secure.

If you want your debugging server to be more secure, you must use secure sockets layer (SSL) or secure pipe (SPIPE) protocol.

## Prohibit connections from unauthorized users

If you are performing [remote debugging through remote.exe](remote-debugging-through-remote-exe.md), you can use the **/u** parameter to prohibit connections from unauthorized users.

## Network segment isolation

To avoid protocol wire attacks, consider isolating the network segment that the client and server are running on. For instance, you can use a local network switch to connect the two systems, ensuring it is not connected to the internet or the rest of the LAN

## Use the most secure transport available

Use the most secure and the latest available version of the transport. For more information on secure transport protocols available in Windows, see [Protocols in TLS/SSL (Schannel SSP)](/windows/win32/secauthn/protocols-in-tls-ssl--schannel-ssp-).

## Use Secure Mode in kernel mode

When you are performing kernel-mode debugging, you can run the debugger in *Secure Mode*. This helps to prevent the debugger from affecting the host computer, yet does not significantly decrease its freedom to debug the target computer. Secure Mode is recommended if you are going to allow remote clients to join your debugging session. For more information see, [Features of Secure Mode](features-of-secure-mode.md) and [Activating Secure Mode](activating-secure-mode.md).

## Restrict the powers of the client in user mode

In user mode, Secure Mode is not available. You can stop an intrusive client from issuing Microsoft MS-DOS commands and running external programs by issuing the [**.noshell (Prohibit Shell Commands)**](../debuggercmds/-noshell--prohibit-shell-commands-.md) command. However, there are many other ways for a client to interfere with your computer.

Note that both Secure Mode and **.noshell** will prevent both the debugging client and the debugging server from taking certain actions. There is no way to place a restriction on the client but not on the server.

## Kill forgotten Process Servers

When you start a process server on a remote machine, the process server runs silently. If you perform remote debugging through this process server and then end the session, the process server continues to run. A forgotten process server is a potential target for an attack. You should always shut down an unneeded process server. Use Task Manager or the [Kill.exe tool](kill-tool.md) to terminate the process server.

## See also

[Security During Kernel-Mode Debugging](security-during-kernel-mode-debugging.md)

[Security During User-Mode Debugging](security-during-user-mode-debugging.md)
