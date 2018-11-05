---
title: KD Connection Servers (Kernel Mode)
description: KD Connection Servers (Kernel Mode)
ms.assetid: fe0c9110-8fbf-46ae-ae1d-75ab5231aef3
keywords: ["remote debugging through a KD connection server", "KD connection server", "KD connection server, overview", "smart client (kernel mode)", "KdSrv", "KdSrv, overview"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# KD Connection Servers (Kernel Mode)


## <span id="ddk_kd_connection_servers_kernel_mode__dbg"></span><span id="DDK_KD_CONNECTION_SERVERS_KERNEL_MODE__DBG"></span>


Kernel-mode remote debugging through a KD connection server involves running a small application called a *KD connection server* on the server. Then a kernel-mode debugger is started on the client. Since this debugger will be doing all of the actual processing, it is called the *smart client*.

The Debugging Tools for Windows package includes a KD connection server called KdSrv (kdsrv.exe).

The two computers do not have to be running the same version of Windows; they can be running any version of Windows. However, the debugger binaries used on the client and the KdSrv binary used on the server must be from the same release of the Debugging Tools for Windows package. This method cannot be used for dump-file debugging.

To set up this remote session, the KD connection server is set up first, and then the smart client is activated. Any number of smart clients can operate through a single KD connection server, but they must each be connected to a different kernel debugging session.

This section includes:

[Activating a KD Connection Server](activating-a-kd-connection-server.md)

[Searching for KD Connection Servers](searching-for-kd-connection-servers.md)

[Activating a Smart Client (Kernel Mode)](activating-a-smart-client--kernel-mode-.md)

[KD Connection Server Examples](kd-connection-server-examples.md)

[Controlling a KD Connection Server Session](controlling-a-kd-connection-server-session.md)

 

 





