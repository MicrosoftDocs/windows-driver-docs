---
title: Searching for Process Servers
description: You can use KD or CDB with the -QR command-line option to obtain a list of available process servers that are running on a network server computer.
ms.assetid: 2f0cd4df-f18a-4222-ab90-7aba0f177eff
keywords: ["Searching for Process Servers Windows Debugging"]
ms.date: 02/28/2019
topic_type:
- apiref
api_name:
- Searching for Process Servers
api_type:
- NA
ms.localizationpriority: medium
---

# Searching for Process Servers


You can use KD or CDB with the **-QR** command-line option to obtain a list of available process servers that are running on a network server computer.

This list may include servers that no longer exist but which were not shut down properly -- connecting to one of these generates an error message. The list will also include debugging servers and KD connection servers. The server type will be indicated in each case.

The syntax for this is as follows:

```console
Debugger -QR \\Server
```

## <span id="ddk_searching_for_process_servers_dbg"></span><span id="DDK_SEARCHING_FOR_PROCESS_SERVERS_DBG"></span>


*Debugger* can be either KD or CDB -- the display will be the same in either case. The two backslashes (**\\\\**) preceding *Server* are optional.

In WinDbg, you can use the **Connect to Remote Stub Server** dialog box to browse a list of available process servers. See [File | Connect to Remote Stub](file---connect-to-remote-stub.md) for more details.

**Note**  For a process server to be discoverable, it must be activated with elevated privileges. For more information, see [Activating a Process Server](activating-a-process-server.md).

 

**Note**  
If you are not logged on to the client computer with an account that has access to the server computer, you might need to provide a user name and password. On the client computer, in a Command Prompt window, enter the following command.

**net use \\\\**<em>Server</em>**\\ipc$ /user:**<em>UserName</em>
where *Server* is the name of the server computer, and *UserName* is the name of an account that has access to the server computer.

When you are prompted, enter the password for *UserName*.

After this command succeeds, you can discover process servers (running on the server computer) by using **-QR** or **Connect to Remote Stub**.

 
## Troubleshooting

If you see this message : *The client is not using same version of remoting protocol as the server* this indicates that the version of DbgSrv that you are attempting to connect to is using a different protocol version than the version of WinDbg. 

It is uncommon that protocol changes are made. When this does happen, be sure you are using the matching versions of the latest available version of DbgSrv and WinDbg or WinDbg Preview. For information on downloading the latest version, see [Download Debugging Tools for Windows](debugger-download-tools.md).

 

 





