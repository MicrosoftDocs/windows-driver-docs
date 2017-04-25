---
title: KD Connection Server Examples
description: KD Connection Server Examples
ms.assetid: 5e54dda7-4f79-40e3-bcc5-248a3a047e31
keywords: ["KD connection server, examples"]
---

# KD Connection Server Examples


## <span id="ddk_kd_connection_server_examples_dbg"></span><span id="DDK_KD_CONNECTION_SERVER_EXAMPLES_DBG"></span>


Suppose a debugging technician is not present at the site where the computer to be debugged is located. The debugging technician asks someone at this site to connect this target computer to some other computer with a debug cable.

Let this other computer be at IP address 127.0.0.42. The debug cable connects COM1 on this computer to whichever port has been debug-enabled on the target computer. The KD connection server is started with this command:

```
E:\Debugging Tools for Windows> kdsrv -t tcp:port=1027 
```

Then at the other location, the technician starts WinDbg as a smart client with this command:

```
G:\Debugging Tools> windbg -k kdsrv:server=@{tcp:server=127.0.0.42,port=1027},trans=@{com:port=com1,baud=57600} -y SymbolPath 
```

The symbol path will be relative to the computer where the smart client is running.

Here is another example. In this case, NPIPE protocol is chosen, and KD is used instead of WinDbg. The first user chooses a pipe name. This can be any alphanumeric string -- in this example, "KernelPipe". The first user opens an elevated Command Prompt window (Run as Administrator) and starts a debugging server by entering these commands:

```
E:\Debugging Tools for Windows> set _NT_DEBUG_PORT=com1 
E:\Debugging Tools for Windows> kdsrv -t npipe:pipe=KernelPipe 
```

The technician is logged on to the client computer with an account that does not have access to the server computer. But the technician knows the username and password for an account that does have access to the server computer. The username for that account is Contoso. The technician enters the following command:

```
net use \\BOX17\ipc$ /user:Contoso
```

When prompted, the technician enters the password for the Contoso account.

The technician is not sure what name was used for the named pipe, so she queries 127.0.0.42 for KD connection servers:

```
G:\Debugging Tools> cdb -QR 127.0.0.42 
Servers on 127.0.0.42:
Debugger Server - npipe:Pipe=MainPipe
Remote Process Server - npipe:Pipe=AnotherPipe
Remote Kernel Debugger Server - npipe:Pipe=KernelPipe
```

Three pipes are shown. However, only one is a KD connection server -- the others are a debugging server and a user-mode process server. The technician enters the following command can to start the smart client:

```
G:\Debugging Tools> kd -k kdsrv:server=@{npipe:server=127.0.0.42,pipe=KernelPipe},trans=@{com:baud=57600} -y SymbolPath 
```

Notice that although the baud rate is specified, the port is not. This causes the debugger to default to the port specified by \_NT\_DEBUG\_PORT on the computer where KdSrv is running.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20KD%20Connection%20Server%20Examples%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




