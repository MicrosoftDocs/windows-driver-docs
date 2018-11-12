---
title: Searching for Debugging Servers
description: You can use KD or CDB with the -QR command-line option to obtain a list of available debugging servers that are running on a network server.
ms.assetid: 510d5f9a-cde8-4dc8-8e2f-80f84ad44fce
keywords: ["Searching for Debugging Servers Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- Searching for Debugging Servers
api_type:
- NA
ms.localizationpriority: medium
---

# Searching for Debugging Servers


You can use KD or CDB with the **-QR** command-line option to obtain a list of available debugging servers that are running on a network server.

This list may include servers that no longer exist but which were not shut down properly -- connecting to one of these generates an error message. The list will also include process servers and KD connection servers. The server type will be indicated in each case.

The syntax for this is as follows:

```console
Debugger -QR \\Server 
```

## <span id="ddk_searching_for_debugging_servers_dbg"></span><span id="DDK_SEARCHING_FOR_DEBUGGING_SERVERS_DBG"></span>


*Debugger* can be either KD or CDB -- the display will be the same in either case. The two backslashes (**\\\\**) preceding *Server* are optional.

In WinDbg, you can use the **Connect to Remote Debugger Session** dialog box to browse a list of available servers. See [File | Connect to Remote Session](file---connect-to-remote-session.md) for details.

**Note**  For a debugging server to be discoverable, it must be activated with elevated privileges. For more information, see [Activating a Debugging Server](activating-a-debugging-server.md).

 

**Note**  
If you are not logged on to the client computer with an account that has access to the server computer, you might need to provide a user name and password. On the client computer, in a Command Prompt window, enter the following command.

**net use \\\\**<em>Server</em>**\\ipc$ /user:**<em>UserName</em>
where *Server* is the name of the server computer, and *UserName* is the name of an account that has access to the server computer.

When you are prompted, enter the password for *UserName*.

After this command succeeds, you can discover debugging servers (running on the server computer) by using **-QR** or **Connect to Remote Debugger Session**.

 

 

 





