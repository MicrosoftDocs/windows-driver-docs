---
title: KD Connection Servers (Kernel Mode)
description: KD Connection Servers (Kernel Mode)
ms.assetid: fe0c9110-8fbf-46ae-ae1d-75ab5231aef3
keywords: ["remote debugging through a KD connection server", "KD connection server", "KD connection server, overview", "smart client (kernel mode)", "KdSrv", "KdSrv, overview"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20KD%20Connection%20Servers%20%28Kernel%20Mode%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




