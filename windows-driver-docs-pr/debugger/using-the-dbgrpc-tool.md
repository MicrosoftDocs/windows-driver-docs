---
title: Using the DbgRpc Tool
description: Using the DbgRpc Tool
ms.assetid: a98b9141-72e1-4957-a65c-36e677d159a6
keywords: ["DbgRpc", "DbgRpc, basic use"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using the DbgRpc Tool


## <span id="ddk_using_the_dbgrpc_tool_dbg"></span><span id="DDK_USING_THE_DBGRPC_TOOL_DBG"></span>


The DbgRpc tool (Dbgrpc.exe) is located in the root directory of the Debugging Tools for Windows installation and must be started in a Command Prompt window. Double-clicking the icon will not start this tool.

The Command Prompt window must be running under an account with administrative privileges on the local computer, or with domain administrative privileges.

DbgRpc makes no calls to any system services (such as LSASS). This makes it useful for debugging even if a system service has crashed, as long as the kernel is still running.

### <span id="using_dbgrpc_on_a_remote_computer"></span><span id="USING_DBGRPC_ON_A_REMOTE_COMPUTER"></span>Using DbgRpc on a Remote Computer

DbgRpc can also be used to examine information from a remote machine. For this to work, the remote machine must be able to accept remote connections and authenticate remote users. If the remote machine's RPCSS (RPC Endpoint Mapper) service has crashed, DbgRpc will not be able to work. Administrative or domain administrative privileges on the remote machine are required.

The **-s** command-line option is used to specify the server name, and the **-p** parameter is used to specify the transport protocol. Both TCP and named pipe protocols are available. TCP is the recommended protocol; it should work in almost every situation.

Here is an example:

```
G:\>dbgrpc -s MyServer -p ncacn_ip_tcp -l -P 1e8 -L 0.1
Getting remote cell info ...
Endpoint
Status: Active
Protocol Sequence: LRPC
Endpoint name: OLE18
```

### <span id="dbgrpc_command_line"></span><span id="DBGRPC_COMMAND_LINE"></span>DbgRpc Command Line

For a description of the full command syntax, see [**DbgRpc Command-Line Options**](dbgrpc-command-line-options.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Using%20the%20DbgRpc%20Tool%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




