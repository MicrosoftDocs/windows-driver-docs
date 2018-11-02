---
title: Remote Tool Examples
description: Remote Tool Examples
ms.assetid: 624f1a78-04da-45c2-8f8d-a593d557be7d
keywords: ["Remote Tool, examples"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Remote Tool Examples


## <span id="ddk_remote_tool_examples_dtools"></span><span id="DDK_REMOTE_TOOL_EXAMPLES_DTOOLS"></span>


The examples in this section demonstrate the use of the Remote tool and show sample input and output.

### <span id="basic_server_command"></span><span id="BASIC_SERVER_COMMAND"></span>Basic Server Command

The following command starts a remote session on the computer.

The command uses the **/s** parameter to indicate a server-side command. It uses the command, **cmd**, to start the Windows command shell (Cmd.exe), and names the session **test1**.

```console
remote /s cmd test1
```

In response, the Remote tool starts the session and displays the command that clients would use to connect to the session.

```console
**************************************
***********     REMOTE    ************
***********     SERVER    ************
**************************************
To Connect: Remote /C SERVER06 "test1"

Microsoft Windows XP [Version 5.1.2600]
(C) Copyright 1985-2001 Microsoft Corp.
```

### <span id="basic_client_command"></span><span id="BASIC_CLIENT_COMMAND"></span>Basic Client Command

The following command connects to a remote session on the Server01 computer. The command uses the **/c** parameter to indicate a client-side command. It specifies the name of the server computer, **Server01**, and the name of the session on that computer, **test1**.

```console
remote /c server01 test1
```

In response, the Remote tool displays a message reporting that the client computer is connected to the session on the server computer. The message displays the name of the server computer and local user (**Server04 user1**).

```console
**************************************
***********     REMOTE    ************
***********     CLIENT    ************
**************************************
Connected...

Microsoft Windows XP [Version 5.1.2600]
(C) Copyright 1985-2001 Microsoft Corp.

C:\Program Files\Debugging Tools for Windows>
**Remote: Connected to SERVER04 user1 [Tue 9:39 AM]
```

After the client connects to the server, the commands typed at the command prompt on the client and server computers appear on both displays..

For example, if you type **dir** at the command prompt of the client computer, the directory display appears in the Command Prompt window on both the client and server computers.

### <span id="using_server_options"></span><span id="USING_SERVER_OPTIONS"></span>Using Server Options

The following server-side command starts a remote session with the NTSD debugger.

The command uses the **/s** parameter to indicate a server-side command. The next parameter, **"ntsd -d -v"**, is the console command that starts the debugger, along with the debugger options. Because the console command includes spaces, it is enclosed in quotation marks. The command includes a name for the session, **debugit**.

The command uses the **/u** parameter to permit only administrators of the computer and a particular user, User03 in Domain01, to connect to the session. It uses the **/f** and **/b** options to specify black text (foreground) on a white background.

Finally, the command uses the **/-v** parameter to make the session invisible to user queries. Debugger sessions are visible by default.

```console
remote /s "ntsd -d -v" DebugIt /u Administrators /u Domain01\User03 
/f black /b white /-v
```

In response, the Remote tool creates a session named DebugIt and starts NTSD with the specified parameters. The message indicates that only the specified users have permission to connect. It also changes the command window to the specified colors.

```console
**************************************
***********     REMOTE    ************
***********     SERVER    ************
**************************************

Protected Server!  Only the following users or groups can connect:
    Administrators
    Domain01\User03
To Connect: Remote /C SERVER06 "debugit"

Microsoft Windows XP [Version 5.1.2600]
(C) Copyright 1985-2001 Microsoft Corp.
```

### <span id="using_client_options"></span><span id="USING_CLIENT_OPTIONS"></span>Using Client Options

The following command connects to the remote session with the NTSD debugger that was started in the previous example.

The command uses the **/c** parameter to indicate a client-side command. It specifies the name of the server computer, **server06**, and the name of the remote session, **debugit**.

The command also includes the **/k** parameter to specify the location of a keyword color file.

```console
remote /c server06 debugit /k c:\remote_client.txt
```

The color file includes the following text:

```console
Registry
white, blue
Token
red, white
```

This text instructs the Remote tool to display lines of output with the word "registry" (not case sensitive) in white text on a blue background and to display lines of output with the word "token" in red text on a white background.

In response, the Remote tool connects the client to the server session and displays the following message.

```console
**************************************
***********     REMOTE    ************
***********     CLIENT    ************
**************************************
Connected...

Microsoft Windows XP [Version 5.1.2600]
(C) Copyright 1985-2001 Microsoft Corp.
```

The client can now send commands to the NTSD debugger on the server computer. The output from the command appears on both the client and server computers.

Lines of output with the word "registry" are displayed on the client computer in white text on a blue background, and lines of output with the word "kernel" in red text on a white background.

### <span id="querying_a_session"></span><span id="QUERYING_A_SESSION"></span>Querying a Session

The Remote tool includes a query parameter (**/q**) that displays a list of remote sessions on a particular computer. The display includes only visible sessions (debugger sessions started without the **/-v** parameter and non-debugger sessions started with the **/v** parameter).

You can query for sessions from the server or client computers. You must specify the computer name, even when querying for sessions on the local computer.

The following command queries for sessions on the local computer, **Server04**.

```console
remote /q Server04
```

In response, the Remote tool reports that there are no remote sessions running on the local computer.

```console
Querying server \\Server04
No Remote servers running on \\Server04
```

In contrast, in response to a query about sessions on a different computer, **Server06**, the Remote tool lists the sessions running on that computer.

```console
Querying server \\Server06

Visible sessions on server Server06:

ntsd                            [Remote /C SERVER06 "debug"] visible
cmd                             [Remote /C SERVER06 "test"] visible
```

The display lists the visible sessions, the console programs running on those sessions (NTSD and the Command Prompt window), and the command that connects to the session. The session name appears in the command syntax in quotation marks.

The display does not show the permissions established for these sessions, if any. Therefore, the display might include sessions that you do not have permission to join.

### <span id="using_the_session_commands"></span><span id="USING_THE_SESSION_COMMANDS"></span>Using the Session Commands

You can use the remote session commands at any time during a remote session.

The following command sends a message to all computers connected to the session.

```console
@M I think I found the problem.
```

As a result, the message appears in the Command Prompt windows of all computers in the session. The message includes the computer name and the day and time of the message.

```console
@m I think I found the problem.     [SERVER01       Wed 11:53 AM]
```

When the message is sent from the server computer, "Local" appears in the label instead of the computer name.

```console
@m I think I found the problem.     [Local       Wed 11:52 AM]
```

The following command generates a pop-up message that appears on the server computer. On all client computers in the session, it writes a message to the Command Prompt window.

```console
@P Did you see that?
```

On client computers, the pop-up message appears in the command window.

```console
From SERVER02  [Wed 11:58 AM]

 Did you see that?
```

The time that appears in the message label is always the time on the server computer, even if the client computer that sent the message is in a different time zone.

### <span id="ending_a_remote_session"></span><span id="ENDING_A_REMOTE_SESSION"></span>Ending a Remote Session

The following examples demonstrate how to use the remote session commands to disconnect a client computer from a session and to end a remote session. Only the server computer that started the remote session can end it.

To disconnect a client computer from a remote session, on the client computer, type <strong>@q</strong>.

In response, the following message appears on the client computer that disconnected.

```console
*** SESSION OVER ***
```

On all other computers in the session, the Remote tool posts a message with the name of the computer and user who disconnected, and the day and time of the disconnect.

```console
**Remote:  Disconnected from SERVER04 User01  [Wed 12:01 PM]
```

To end a remote session, on the server computer, type <strong>@k</strong>. This command automatically disconnects the clients, and then ends the session.

 

 





