---
title: Using the DbgRpc Tool
description: Using the DbgRpc Tool
ms.assetid: a98b9141-72e1-4957-a65c-36e677d159a6
keywords: ["DbgRpc", "DbgRpc, basic use"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
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

```console
G:\>dbgrpc -s MyServer -p ncacn_ip_tcp -l -P 1e8 -L 0.1
Getting remote cell info ...
Endpoint
Status: Active
Protocol Sequence: LRPC
Endpoint name: OLE18
```

### <span id="dbgrpc_command_line"></span><span id="DBGRPC_COMMAND_LINE"></span>DbgRpc Command Line

For a description of the full command syntax, see [**DbgRpc Command-Line Options**](dbgrpc-command-line-options.md).

 

 





