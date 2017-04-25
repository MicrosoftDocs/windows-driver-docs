---
title: Searching for KD Connection Servers
description: You can use KD or CDB with the -QR command-line option to obtain a list of available KD connection servers that are running on a network server.This list may include servers that no longer exist but which were not shut down properly -- connecting to one of these generates an error message. The list will also include debugging servers and user-mode process servers. The server type will be indicated in each case.The syntax for this is as follows
ms.assetid: 24ff0e2f-d40a-4f52-91ef-e766b9387a8a
keywords: ["Searching for KD Connection Servers Windows Debugging"]
topic_type:
- apiref
api_name:
- Searching for KD Connection Servers
api_type:
- NA
---

# Searching for KD Connection Servers


You can use KD or CDB with the **-QR** command-line option to obtain a list of available KD connection servers that are running on a network server.

This list may include servers that no longer exist but which were not shut down properly -- connecting to one of these generates an error message. The list will also include debugging servers and user-mode process servers. The server type will be indicated in each case.

The syntax for this is as follows:

``` syntax
Debugger -QR \\Server 
```

## <span id="ddk_searching_for_kd_connection_servers_dbg"></span><span id="DDK_SEARCHING_FOR_KD_CONNECTION_SERVERS_DBG"></span>


*Debugger* can be either KD or CDB -- the display will be the same in either case. The two backslashes (**\\\\**) preceding *Server* are optional.

In WinDbg, you can use the **Connect to Remote Stub Server** dialog box to browse a list of available KD connection servers. See [File | Connect to Remote Stub](https://msdn.microsoft.com/library/windows/hardware/ff545336) for more details.

**Note**  For a KD connection server to be discoverable, it must be activated with elevated privileges. For more information, see [Activating a KD Connection Server](activating-a-kd-connection-server.md).

 

**Note**  
If you are not logged on to the client computer with an account that has access to the server computer, you might need to provide a user name and password. On the client computer, in a Command Prompt window, enter the following command.

**net use \\\\***Server***\\ipc$ /user:***UserName*
where *Server* is the name of the server computer, and *UserName* is the name of an account that has access to the server computer.

When you are prompted, enter the password for *UserName*.

After this command succeeds, you can discover KD connection servers (running on the server computer) by using **-QR** or **Connect to Remote Stub**.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Searching%20for%20KD%20Connection%20Servers%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




