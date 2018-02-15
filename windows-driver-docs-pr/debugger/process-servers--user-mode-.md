---
title: Process Servers (User Mode)
description: Process Servers (User Mode)
ms.assetid: 9391fcd4-c64f-4c2b-89c2-da09be7646d1
keywords: ["remote debugging through a process server", "process server", "process server, overview", "smart client (user mode)", "DbgSrv", "DbgSrv, overview"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Process Servers (User Mode)


## <span id="ddk_process_servers_user_mode__dbg"></span><span id="DDK_PROCESS_SERVERS_USER_MODE__DBG"></span>


Remote debugging through a process server involves running a small application called a *process server* on the server computer. Then a user-mode debugger is started on the client computer. Since this debugger will be doing all of the actual processing, it is called the *smart client*.

The Debugging Tools for Windows package includes a process server called DbgSrv (dbgsrv.exe) for use in user mode.

The two computers do not have to be running the same version of Windows; they can be running any version of Windows. However, the debugger binaries used on the client and the DbgSrv binary used on the server must be from the same release of the Debugging Tools for Windows package. This method cannot be used for dump-file debugging.

To set up this remote session, the process server is set up first, and then the smart client is activated. Any number of smart clients can operate through a single process server -- these debugging sessions will remain separate and will not interfere with each other. If a debugging session is ended, the process server will continue to run and can be used for new debugging sessions.

## <span id="in_this_section"></span>In this section


-   [**Activating a Process Server**](activating-a-process-server.md)
-   [**Searching for Process Servers**](searching-for-process-servers.md)
-   [**Activating a Smart Client**](activating-a-smart-client.md)
-   [Process Server Examples](process-server-examples.md)
-   [Controlling a Process Server Session](controlling-a-process-server-session.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Process%20Servers%20%28User%20Mode%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




