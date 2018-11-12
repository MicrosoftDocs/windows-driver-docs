---
title: Remote Server Syntax
description: To start the server side of the Remote tool, use the following syntax at the command line.
ms.assetid: fecc9f43-6946-4d99-840b-a85c75ac397c
keywords: ["Remote Server Syntax Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- Remote Server Syntax
api_type:
- NA
ms.localizationpriority: medium
---

# Remote Server Syntax


To start the server side of the Remote tool, use the following syntax at the command line.

```console
remote /s Command SessionName [/f Color] [/b] [/u User [/u User...]] [/ud User [/ud User...]] [/v | /-v]
```

## <span id="ddk_remote_server_syntax_dtools"></span><span id="DDK_REMOTE_SERVER_SYNTAX_DTOOLS"></span>Parameters


<span id="________s______"></span><span id="________S______"></span> **/s**   
Starts a server session.

<span id="_______Command______"></span><span id="_______command______"></span><span id="_______COMMAND______"></span> *Command*   
Specifies the command that starts the console-based program. The command can include parameters. If the command includes spaces, enclose it in quotation marks.

<span id="_______SessionName______"></span><span id="_______sessionname______"></span><span id="_______SESSIONNAME______"></span> *SessionName*   
Assigns a name to the remote session. If the name includes spaces, enclose it in quotation marks. This parameter is not case-sensitive.

<span id="________f______"></span><span id="________F______"></span> **/f**   
Specifies the color of the text in the server command window.

<span id="________b______"></span><span id="________B______"></span> **/b**   
Specifies the background color of the server command window.

<span id="_______Color______"></span><span id="_______color______"></span><span id="_______COLOR______"></span> *Color*   
Specifies a color. Valid values are black, blue, green, cyan, red, purple, yellow, white, lblack, lblue, lgreen, lred, lpurple, lyellow, and lwhite.

<span id="________u______"></span><span id="________U______"></span> **/u**   
Specifies users or groups that are permitted to connect to the remote session; by default, everyone is permitted. When you use this parameter, everyone is denied permission, except for the users and groups specified by the *User* subparameter.

<span id="________ud______"></span><span id="________UD______"></span> **/ud**   
Specifies users or groups that are denied permission to connect to the remote session; by default, no one is denied permission.

<span id="_______User______"></span><span id="_______user______"></span><span id="_______USER______"></span> *User*   
Specifies the name of a user or group in \[*domain* | *computer*\]\\{*user* | *group*} format. When specifying users or groups on the local computer, omit the computer name.

<span id="________v______"></span><span id="________V______"></span> **/v**   
Makes a session visible. For more information, see [Visible Session](remote-tool-concepts.md#visible-session).

By default, only debugger sessions are visible, that is, sessions in which the value of the *Command* parameter include the words **kd**, **dbg**, **remoteds**, **ntsd**, or **cdb**; otherwise, the session is not visible.

<span id="_______-v______"></span><span id="_______-V______"></span> **-v**   
Makes a remote debugger session invisible. For more information, see [Visible Session](remote-tool-concepts.md#visible-session).

### <span id="comments"></span><span id="COMMENTS"></span>Comments

The *Command* and *SessionName* parameters must appear in the order shown on the syntax line.

To end a remote session, type <strong>@k</strong>. For more information, see [Remote Session Commands](remote-session-commands.md).

The Remote tool will not create a session that the current user does not have permission to join.

When starting more than one remote session on a single computer, open a new command window for each session. Also, use a different session name for each session. Because the session names are used to label the named pipes, they must be unique on the computer.

### <span id="sample_usage"></span><span id="SAMPLE_USAGE"></span>Sample Usage

```console
remote /s "i386kd -v" TestSession
remote /s "cmd" "My Remote Session" /f white /b black /u Server01\Administrators
remote /s "ntsd -d -g -x" DebugIt /-v
remote /q Server01
```

 

 





