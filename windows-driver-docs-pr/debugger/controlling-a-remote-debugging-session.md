---
title: Controlling a Remote Debugging Session
description: Controlling a Remote Debugging Session
ms.assetid: dedd277d-1aa0-468c-919c-29b25b0b5c0d
keywords: ["remote debugging through the debugger, controlling a session"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Controlling a Remote Debugging Session


## <span id="ddk_controlling_a_remote_debugging_session_dbg"></span><span id="DDK_CONTROLLING_A_REMOTE_DEBUGGING_SESSION_DBG"></span>


Once the remote session has been started, commands can be entered into either the debugging server or the debugging client. If there are multiple clients, any of them can enter commands. Once ENTER is pressed, the command is transmitted to the debugging server and executed.

Whenever one user enters a command, all users will see the command itself and its output. If this command was issued from a debugging client, all other users will see an identification, preceding the command, of which user issued the command. Commands issued from the debugging server do not have this prefix.

After a command is executed by one user, other users who are connected through KD or CDB will not see a new command prompt. On the other hand, users of WinDbg will see the prompt in the bottom panel of the Debugger Command window continuously, even when the debugger engine is running. Neither of these should be a cause for alarm; any user can enter a command at any time, and the engine will execute these commands in the order they were received.

Actions made through the WinDbg interface will also be executed by the debugging server.

### <span id="communication_between_users"></span><span id="COMMUNICATION_BETWEEN_USERS"></span>Communication Between Users

Whenever a new debugging client connects to the session, all other users will see a message that this client has connected. No message is displayed when a client disconnects.

The [**.clients (List Debugging Clients)**](-clients--list-debugging-clients-.md) command will list all clients currently connected to the debugging session.

The [**.echo (Echo Comment)**](-echo--echo-comment-.md) command is useful for sending messages from one user to another.

### <span id="windbg_workspaces"></span><span id="WINDBG_WORKSPACES"></span>WinDbg Workspaces

When WinDbg is being used as a debugging client, its workspace will only save values set through the graphical interface. Changes made through the Debugger Command window will not be saved. (This guarantees that only changes made by the local client will be reflected, since the Debugger Command window will accept input from all clients as well as the debugging server.)

### <span id="file_paths"></span><span id="FILE_PATHS"></span>File Paths

The symbol path, executable image path, and extension DLL path are all interpreted as file paths relative to the Debugging Tools for Windows installation folder on the debugging server.

When WinDbg is used as a debugging client, it has its own *local source path* as well. All source-related commands will access the source files on the local computer. Therefore, the proper paths have to be set on any client or server that will use source commands.

This multiple-path system allows a debugging client to use source-related commands without actually sharing the source files with other clients or with the server. This is useful if there are private or confidential source files which one of the users has access to.

### <span id="canceling_the_debugging_server"></span><span id="CANCELING_THE_DEBUGGING_SERVER"></span>Canceling the Debugging Server

The [**.endsrv (End Debugging Server)**](-endsrv--end-debugging-server-.md) command can be used to terminate a debugging server. If the debugger has established multiple debugging servers, you can cancel some of them while leaving others running.

Terminating a server will prevent any future clients from attaching to it. It will not cut off any clients that are currently attached through the server.

### <span id="exiting_the_debugger_and_terminating_the_session"></span><span id="EXITING_THE_DEBUGGER_AND_TERMINATING_THE_SESSION"></span>Exiting the Debugger and Terminating the Session

To exit from one debugging client without terminating the server, you must issue a command from that specific client. If this client is KD or CDB, use the [**CTRL+B**](ctrl-b--quit-local-debugger-.md) key to exit. If you are using a script to run KD or CDB, use [**.remote\_exit (Exit Debugging Client)**](-remote-exit--exit-debugging-client-.md). If this client is WinDbg, choose **Exit** from the **File** menu to exit.

To terminate the entire session and exit the debugging server, use the [**q (Quit)**](q--qq--quit-.md) command. This command can be entered from any server or client, and it will terminate the entire session for all users.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Controlling%20a%20Remote%20Debugging%20Session%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




