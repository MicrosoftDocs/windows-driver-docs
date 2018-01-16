---
title: Security During Remote Debugging
description: Security During Remote Debugging
ms.assetid: 55e570d2-b005-4c09-ac8f-0632233a64bd
keywords: ["security considerations, remote debugging", "remote debugging through remote.exe, security considerations", "remote debugging through the debugger, security considerations", "process server, security considerations"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Security%20During%20Remote%20Debugging%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




