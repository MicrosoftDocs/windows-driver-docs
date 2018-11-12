---
title: Starting a Remote.exe Session
description: Starting a Remote.exe Session
ms.assetid: 2b70e54e-ab02-46f1-9af1-e7379c89cf3c
keywords: ["remote debugging through remote.exe, starting the session"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Starting a Remote.exe Session


## <span id="ddk_starting_a_remote_exe_session_dbg"></span><span id="DDK_STARTING_A_REMOTE_EXE_SESSION_DBG"></span>


There are two ways to start a remote.exe session with KD or CDB. Only the second of these methods works with NTSD.

### <span id="customizing_your_command_prompt_window"></span><span id="CUSTOMIZING_YOUR_COMMAND_PROMPT_WINDOW"></span>Customizing Your Command Prompt Window

The Remote.exe Client and Remote.exe Server run in Command Prompt windows.

To prepare for the remote session, you should customize this window to increase its usability. Open a Command Prompt window. Right-click the title bar and select **Properties**. Select the **Layout** tab. Go to the section titled "Screen Buffer Size" and type **90** in the **Width** box and a value between **4000** and **9999** in the **Height** box. This enables scroll bars in the remote session on the kernel debugger.

Change the values for the height and width of the "Windows Size" section if you want to alter the shape of the command prompt. Select the **Options** tab. Enable the **Edit Options** quickedit mode and insert mode. This allows you to cut and paste information in the command prompt session. Click **OK** to apply the changes. Select the option to apply the changes to all future sessions when prompted.

### <span id="starting_the_remote_exe_server__first_method"></span><span id="STARTING_THE_REMOTE_EXE_SERVER__FIRST_METHOD"></span>Starting the Remote.exe Server: First Method

The general syntax for starting a Remote.exe Server is as follows:

```console
remote /s "Command_Line" Unique_Id [/f Foreground_Color] [/b Background_Color] 
```

This can be used to start KD or CDB on the remote computer, as in the following examples:

```console
remote /s "KD [options]" MyBrokenBox 

remote /s "CDB [options]" MyBrokenApp 
```

This starts the Remote.exe Server in the Command Prompt window, and starts the debugger.

You cannot use this method to start NTSD directly, because the NTSD process runs in a different window than the one in which it was invoked.

### <span id="starting_the_remote_exe_server__second_method"></span><span id="STARTING_THE_REMOTE_EXE_SERVER__SECOND_METHOD"></span>Starting the Remote.exe Server: Second Method

There is an alternate method that can start a Remote.exe Server. This method involves first starting the debugger, and then using the [**.remote (Create Remote.exe Server)**](-remote--create-remote-exe-server-.md) command to start the server.

Since the **.remote** command is issued after the debugger has started, this method works equally well with KD, CDB, and NTSD.

Here is an example. First, start the debugger in the normal fashion:

```console
KD [options] 
```

Once the debugger is running, use the **.remote** command:

```dbgcmd
.remote MyBrokenBox 
```

This results in a KD process that is also a Remote.exe Server with an ID of "MyBrokenBox", exactly as in the first method.

One advantage of this method is that you do not have to decide in advance if you intend to use remote debugging. If you are debugging with one of the console debuggers and then decide that you would prefer someone in a remote location to take over, you can use the **.remote** command and then they can connect to your session.

### <span id="starting_the_remote_exe_client"></span><span id="STARTING_THE_REMOTE_EXE_CLIENT"></span>Starting the Remote.exe Client

The general syntax for starting a Remote.exe Client is as follows:

```console
remote /c ServerNetBIOSName Unique_ID [/l Lines_to_Get] [/f Foreground_Color] [/b Background_Color] 
```dbgcmd

For example, if the "MyBrokenBox" session, described above, was started on a local host computer whose network name was "Server2", you can connect to it with the command:

```console
remote /c server2 MyBrokenBox 
```

Anyone on the network with appropriate permission can connect to this debug session, as long as they know your machine name and the session ID.

### <span id="issuing_commands"></span><span id="ISSUING_COMMANDS"></span>Issuing Commands

Commands are issued through the Remote.exe Client and are sent to the Remote.exe Server. You can enter any command into the client as if you were directly entering it into the debugger.

To exit from the remote.exe session on the Remote.exe Client, enter the <strong>@Q</strong> command. This leaves the Remote.exe Server and the debugger running.

To end the server session, enter the <strong>@K</strong> command on the Remote.exe Server.

 

 





