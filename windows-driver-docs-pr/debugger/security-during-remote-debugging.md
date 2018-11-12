---
title: Security During Remote Debugging
description: Security During Remote Debugging
ms.assetid: 55e570d2-b005-4c09-ac8f-0632233a64bd
keywords: ["security considerations, remote debugging", "remote debugging through remote.exe, security considerations", "remote debugging through the debugger, security considerations", "process server, security considerations"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Security During Remote Debugging


## <span id="ddk_security_during_remote_debugging_dbg"></span><span id="DDK_SECURITY_DURING_REMOTE_DEBUGGING_DBG"></span>


There are two ways to increase security during remote debugging: by restricting who can connect to your session and by restricting the powers of someone who does connect.

### <span id="controlling_access_to_the_debugging_session"></span><span id="CONTROLLING_ACCESS_TO_THE_DEBUGGING_SESSION"></span>Controlling Access to the Debugging Session

If you are performing [remote debugging through the debugger](remote-debugging-through-the-debugger.md), or using a [process server](process-servers--user-mode-.md) or [KD connection server](kd-connection-servers--kernel-mode-.md), any computer on your local network can attempt to attach to your debugging session.

If you are using the TCP, 1394, COM, or named pipe protocols, you can require the Debugging Client to supply a password. However, this password is not encrypted during transmission, and therefore these protocols are not secure.

If you want your Debugging Server to be secure, you must use secure sockets layer (SSL) or secure pipe (SPIPE) protocol.

If you are performing [remote debugging through remote.exe](remote-debugging-through-remote-exe.md), you can use the **/u** parameter to prohibit connections from unauthorized users.

### <span id="restricting_the_powers_of_the_client"></span><span id="RESTRICTING_THE_POWERS_OF_THE_CLIENT"></span>Restricting the Powers of the Client

If you are setting up a kernel-mode debugging session, you can restrict the debugger's ability to interfere with the host machine by using [Secure Mode](secure-mode.md).

In user mode, Secure Mode is not available. You can stop an intrusive client from issuing Microsoft MS-DOS commands and running external programs by issuing the [**.noshell (Prohibit Shell Commands)**](-noshell--prohibit-shell-commands-.md) command. However, there are many other ways for a client to interfere with your computer.

Note that both Secure Mode and **.noshell** will prevent both the Debugging Client and the Debugging Server from taking certain actions. There is no way to place a restriction on the client but not on the server.

### <span id="forgotten_process_servers"></span><span id="FORGOTTEN_PROCESS_SERVERS"></span>Forgotten Process Servers

When you start a process server on a remote machine, the process server runs silently.

If you perform remote debugging through this process server and then end the session, the process server continues to run.

A forgotten process server is a potential target for an attack. You should always shut down an unneeded process server. Use the Kill.exe utility or Task Manager to terminate the process server.

 

 





